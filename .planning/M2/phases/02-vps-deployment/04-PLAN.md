---
phase: M2-02-vps-deployment
plan: 04
type: execute
wave: 1
depends_on: [03]
files_modified:
  - tools/iam-deploy.sh
autonomous: true
decisions: [D-06, D-07, D-08, D-10]
success_criteria_addressed: [1, 2]
requirements: [D-06, D-07, D-08, D-10]
must_haves:
  truths:
    - "tools/iam-deploy.sh is a template committed to the repo, copied by bootstrap.sh to /usr/local/bin/iam-deploy, and invoked over SSH by Phase 03's GitHub Actions workflow"
    - "It performs an atomic release: creates /var/www/iam/releases/<ts>-<sha>/, runs npm ci --omit=dev under api/, flips the current symlink, reloads systemd"
    - "It accepts ENV=prod or ENV=staging on the CLI and routes to the matching paths/units"
    - "It retains the last 5 release directories and garbage-collects older ones"
    - "It exits non-zero if the health check after symlink flip fails, leaving the old symlink in place"
  artifacts:
    - path: "tools/iam-deploy.sh"
      contains: "#!/bin/bash"
    - path: "tools/iam-deploy.sh"
      contains: "set -euo pipefail"
    - path: "tools/iam-deploy.sh"
      contains: "npm ci --omit=dev"
    - path: "tools/iam-deploy.sh"
      contains: "ln -sfn"
    - path: "tools/iam-deploy.sh"
      contains: "systemctl restart iam-api"
  key_links:
    - from: "tools/iam-deploy.sh"
      to: "systemd units (iam-api.service / iam-api-staging.service)"
      via: "systemctl restart"
    - from: "tools/iam-deploy.sh"
      to: "/var/www/iam/current (symlink)"
      via: "ln -sfn <release_dir> <current>"
---

<objective>
Author `tools/iam-deploy.sh` — the release/rollback script that Phase 03's GitHub Actions workflow will invoke over SSH after Plan 02 of this phase already lays the groundwork. bootstrap.sh (Plan 03) copies this file to `/usr/local/bin/iam-deploy` on the VPS.

Purpose: Capture the atomic-release-via-symlink pattern (CONTEXT "Patterns") in one reviewable script so that Phase 03 wiring is trivial (`ssh deploy@prod iam-deploy prod <sha>`). This script runs AS the deploy user (or iam user), so it must not require sudo for any operation — the release tree is already owned correctly by bootstrap.sh.

Output: `tools/iam-deploy.sh` committed to the repo; executable; shellcheck-clean.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
</execution_context>

<context>
@.planning/M2/phases/02-vps-deployment/CONTEXT.md
@.planning/M2/phases/02-vps-deployment/03-PLAN.md
@deploy.sh
@api/package.json

<interfaces>
<!-- Invocation contract (Phase 03 workflow will use this) -->
iam-deploy <env> <git_sha> [<tarball_path>]
  env         = prod | staging
  git_sha     = 7+ char short SHA of the commit being deployed
  tarball_path = optional local tarball path; if absent, script expects /tmp/iam-deploy-<sha>.tar.gz

<!-- Paths (must match bootstrap.sh) -->
prod:
  release_root = /var/www/iam
  current      = /var/www/iam/current
  releases     = /var/www/iam/releases/<ts>-<sha>/
  unit         = iam-api.service
  port         = 3860
staging:
  release_root = /var/www/iam-staging
  current      = /var/www/iam-staging/current
  releases     = /var/www/iam-staging/releases/<ts>-<sha>/
  unit         = iam-api-staging.service
  port         = 3861

<!-- Health check target -->
curl -fsS --max-time 5 http://127.0.0.1:<port>/api/chat -X OPTIONS
  - OPTIONS request is CORS preflight — service responds without needing a real payload
  - any 2xx/3xx/4xx means the process is listening
  - connection refused / timeout means the service is down → roll back
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Write tools/iam-deploy.sh</name>
  <files>tools/iam-deploy.sh</files>
  <read_first>
    - deploy.sh (reference for PM2-based flow being replaced)
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (atomic release pattern, D-06..D-10)
    - api/package.json (confirm `npm ci --omit=dev` is the correct install command)
  </read_first>
  <action>
    Create `tools/iam-deploy.sh` with this exact structure (inline verbatim — all commands below are required):

    ```bash
    #!/bin/bash
    # IAM atomic deploy — installed as /usr/local/bin/iam-deploy by bootstrap.sh (Plan 03).
    # Invoked over SSH by Phase 03 GitHub Actions workflow.
    # Runs as the `deploy` user (member of `iam` group); no sudo required.
    set -euo pipefail

    ENV="${1:-}"
    SHA="${2:-}"
    TARBALL="${3:-/tmp/iam-deploy-${SHA}.tar.gz}"

    [[ -n "$ENV" && -n "$SHA" ]] || {
      echo "usage: iam-deploy <prod|staging> <git_sha> [tarball]" >&2
      exit 2
    }

    case "$ENV" in
      prod)
        RELEASE_ROOT="/var/www/iam"
        UNIT="iam-api.service"
        PORT="3860"
        ;;
      staging)
        RELEASE_ROOT="/var/www/iam-staging"
        UNIT="iam-api-staging.service"
        PORT="3861"
        ;;
      *)
        echo "unknown env: $ENV (expected prod|staging)" >&2
        exit 2
        ;;
    esac

    RELEASES_DIR="${RELEASE_ROOT}/releases"
    CURRENT_LINK="${RELEASE_ROOT}/current"
    TS="$(date -u +%Y%m%d-%H%M%S)"
    NEW_DIR="${RELEASES_DIR}/${TS}-${SHA}"
    KEEP=5

    log() { printf '[iam-deploy %s] %s\n' "$ENV" "$*"; }
    die() { printf '[iam-deploy %s] ERROR: %s\n' "$ENV" "$*" >&2; exit 1; }

    [[ -d "$RELEASES_DIR" ]] || die "releases dir missing: $RELEASES_DIR (run bootstrap.sh first)"
    [[ -f "$TARBALL" ]]      || die "tarball missing: $TARBALL"

    # 1. Extract new release
    log "extracting $TARBALL → $NEW_DIR"
    mkdir -p "$NEW_DIR"
    tar -xzf "$TARBALL" -C "$NEW_DIR"

    # 2. Install prod deps under api/
    if [[ -f "$NEW_DIR/api/package.json" ]]; then
      log "installing prod deps (npm ci --omit=dev)"
      (cd "$NEW_DIR/api" && npm ci --omit=dev --no-audit --no-fund)
    else
      die "new release is missing api/package.json"
    fi

    # 3. Capture previous target for rollback
    PREV_TARGET=""
    if [[ -L "$CURRENT_LINK" ]]; then
      PREV_TARGET="$(readlink -f "$CURRENT_LINK" || true)"
      log "previous release: ${PREV_TARGET:-<none>}"
    fi

    # 4. Atomic symlink flip
    log "flipping $CURRENT_LINK → $NEW_DIR"
    ln -sfn "$NEW_DIR" "$CURRENT_LINK"

    # 5. Restart the unit
    log "restarting $UNIT"
    systemctl restart "$UNIT"
    # small settle window for Node to bind the port
    sleep 2

    # 6. Health check — if it fails, roll back
    log "health check on 127.0.0.1:${PORT}"
    if ! curl -fsS --max-time 5 -o /dev/null -X OPTIONS "http://127.0.0.1:${PORT}/api/chat"; then
      log "health check FAILED — rolling back"
      if [[ -n "$PREV_TARGET" && -d "$PREV_TARGET" ]]; then
        ln -sfn "$PREV_TARGET" "$CURRENT_LINK"
        systemctl restart "$UNIT"
        die "rolled back to $PREV_TARGET"
      else
        die "no previous release to roll back to"
      fi
    fi
    log "health check OK"

    # 7. Prune old releases (keep last $KEEP)
    log "pruning old releases (keeping $KEEP)"
    # shellcheck disable=SC2012  # ls -t is fine here; filenames are timestamped, no spaces
    ls -1t "$RELEASES_DIR" | tail -n +$((KEEP + 1)) | while read -r old; do
      [[ -n "$old" ]] || continue
      log "removing $RELEASES_DIR/$old"
      rm -rf "${RELEASES_DIR:?}/${old}"
    done

    log "deploy complete: $NEW_DIR"
    ```

    Make executable: `chmod +x tools/iam-deploy.sh`.
  </action>
  <acceptance_criteria>
    - `head -1 tools/iam-deploy.sh | grep -Fxq '#!/bin/bash'` succeeds
    - `test -x tools/iam-deploy.sh` succeeds
    - `bash -n tools/iam-deploy.sh` returns 0
    - `grep -c 'set -euo pipefail' tools/iam-deploy.sh` returns 1
    - `grep -c 'npm ci --omit=dev' tools/iam-deploy.sh` returns 1
    - `grep -c 'ln -sfn' tools/iam-deploy.sh` returns at least 2 (flip + potential rollback)
    - `grep -c 'systemctl restart' tools/iam-deploy.sh` returns at least 2 (normal + rollback)
    - `grep -c 'curl -fsS' tools/iam-deploy.sh` returns 1
    - `grep -c '127.0.0.1:3860\|127.0.0.1:3861\|127.0.0.1:\${PORT}' tools/iam-deploy.sh` returns at least 1 (port usage)
    - `grep -c 'readlink -f' tools/iam-deploy.sh` returns 1 (rollback target capture)
    - `grep -c 'KEEP=5' tools/iam-deploy.sh` returns 1
    - `shellcheck tools/iam-deploy.sh` returns 0 (skip with note if unavailable)
    - No sudo usage: `grep -c '^[^#]*\bsudo\b' tools/iam-deploy.sh` returns 0
    - Invoking with bad args exits 2: `bash tools/iam-deploy.sh; [ $? = 2 ]` returns true (test locally via a dry-run subshell that captures exit code)
  </acceptance_criteria>
  <verify>
    <automated>bash -n tools/iam-deploy.sh && test -x tools/iam-deploy.sh && grep -q 'npm ci --omit=dev' tools/iam-deploy.sh && grep -q 'ln -sfn' tools/iam-deploy.sh && grep -q 'systemctl restart' tools/iam-deploy.sh && grep -q 'curl -fsS' tools/iam-deploy.sh && ! grep -qE '^[^#]*\bsudo\b' tools/iam-deploy.sh && ( bash tools/iam-deploy.sh > /dev/null 2>&1; [ $? = 2 ] )</automated>
  </verify>
  <done>iam-deploy.sh present, executable, shellcheck-clean, rejects missing args with exit 2; commit `feat(M2-02): tools/iam-deploy.sh atomic release script per D-06,D-07,D-08,D-10`.</done>
</task>

</tasks>

<verification>
```
bash -n tools/iam-deploy.sh
shellcheck tools/iam-deploy.sh           # or record "shellcheck not available"
grep -Fq 'npm ci --omit=dev' tools/iam-deploy.sh
grep -Fq 'ln -sfn' tools/iam-deploy.sh
```
</verification>

<success_criteria>
- tools/iam-deploy.sh implements the atomic-symlink release pattern from CONTEXT
- Health check gates the deploy; failure rolls the symlink back
- Keeps last 5 releases, GCs older ones
- No sudo; runs as the deploy user (member of iam group)
- bootstrap.sh Plan 03 already copies this file to /usr/local/bin/iam-deploy
</success_criteria>

<output>
After completion: create `.planning/M2/phases/02-vps-deployment/04-SUMMARY.md` with bash -n and shellcheck output and a short summary of the atomic-release mechanism.
</output>
