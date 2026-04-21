---
phase: M2-02-vps-deployment
plan: 03
type: execute
wave: 1
depends_on: [01, 02]
files_modified:
  - bootstrap.sh
autonomous: true
decisions: [D-01, D-02, D-03, D-04, D-16]
success_criteria_addressed: [1, 2, 3, 5]
requirements: [D-01, D-02, D-03, D-04, D-16]
must_haves:
  truths:
    - "bootstrap.sh is a single file at repo root, idempotent, runs as root on a fresh Ubuntu 22.04/24.04 VPS"
    - "It creates the iam system user and deploy SSH-only user (D-04)"
    - "It pins Node 20 LTS via NodeSource and installs nginx, certbot+plugin, fail2ban, ufw, git (D-01, D-16)"
    - "It copies config/systemd/*.service to /etc/systemd/system/ and enables both units"
    - "It renders tools/env-template → /etc/iam-api/env (chmod 600, owner iam:iam) using env vars or prompts (D-02, D-03)"
    - "It copies config/nginx/*.conf to /etc/nginx/sites-available/ and symlinks into sites-enabled"
    - "It requests Let's Encrypt certs via certbot --nginx for both domains (D-16)"
    - "It wires gitleaks pre-commit hook via `git config --system core.hooksPath` reference (Phase 01 D-04)"
    - "It supports non-interactive mode via BOOTSTRAP_NONINTERACTIVE=1 for CI use"
    - "It never echoes secret values to stdout or logs"
  artifacts:
    - path: "bootstrap.sh"
      contains: "#!/bin/bash"
    - path: "bootstrap.sh"
      contains: "set -euo pipefail"
    - path: "bootstrap.sh"
      contains: "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -"
    - path: "bootstrap.sh"
      contains: "useradd --system"
    - path: "bootstrap.sh"
      contains: "chmod 600"
    - path: "bootstrap.sh"
      contains: "systemctl enable"
    - path: "bootstrap.sh"
      contains: "certbot --nginx"
    - path: "bootstrap.sh"
      contains: "BOOTSTRAP_NONINTERACTIVE"
  key_links:
    - from: "bootstrap.sh"
      to: "config/systemd/iam-api.service"
      via: "install -m 644 to /etc/systemd/system/"
    - from: "bootstrap.sh"
      to: "config/nginx/interactivemove.nl.conf"
      via: "install to /etc/nginx/sites-available + ln -sf to sites-enabled"
    - from: "bootstrap.sh"
      to: "tools/env-template"
      via: "render to /etc/iam-api/env with envsubst or sed"
---

<objective>
Write a single idempotent `bootstrap.sh` at the repo root that stands up the VPS from a fresh Ubuntu 22.04/24.04 image to a running, TLS-terminated `interactivemove.nl` + `iam.abbamarkt.nl` in one invocation.

Purpose: Closes phase success criterion #1 ("bootstrap.sh installs all deps + configs + brings site online on fresh Ubuntu in one run"). Operators run it with `sudo bash bootstrap.sh` after SSHing as a human user; CI can run it non-interactively. The script is authored here but is NOT executed by this planning session — it is committed to the repo for the IAM dev to run on the actual VPS.

Output: `bootstrap.sh` at repo root, ~300-400 lines, shellcheck-clean.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
</execution_context>

<context>
@.planning/M2/GUARDRAILS.md
@.planning/M2/phases/02-vps-deployment/CONTEXT.md
@.planning/M2/phases/02-vps-deployment/01-PLAN.md
@.planning/M2/phases/02-vps-deployment/02-PLAN.md
@deploy.sh
@.githooks/pre-commit

<interfaces>
<!-- Env vars bootstrap reads (D-02) -->
DOMAIN=interactivemove.nl                 # prod domain (default)
STAGING_DOMAIN=iam.abbamarkt.nl           # staging subdomain (default)
LETSENCRYPT_EMAIL=<required>              # for certbot
OPENROUTER_API_KEY=<required for prod>
OPENROUTER_API_KEY_STAGING=<required for staging>
REPO_URL=https://github.com/oopuo-ship/iam-website.git  # or current
BOOTSTRAP_NONINTERACTIVE=0|1              # 1 = fail if inputs missing instead of prompt

<!-- Files bootstrap consumes (all relative to the repo clone) -->
config/systemd/iam-api.service
config/systemd/iam-api-staging.service
config/nginx/interactivemove.nl.conf
config/nginx/iam.abbamarkt.nl.conf
tools/env-template
tools/env-staging-template
tools/iam-deploy.sh         (from Plan 04, installed to /usr/local/bin/iam-deploy)
.githooks/pre-commit        (from Phase 01)

<!-- Files bootstrap creates on the VPS -->
/etc/systemd/system/iam-api.service
/etc/systemd/system/iam-api-staging.service
/etc/nginx/sites-available/interactivemove.nl.conf
/etc/nginx/sites-available/iam.abbamarkt.nl.conf
/etc/nginx/sites-enabled/interactivemove.nl.conf (symlink)
/etc/nginx/sites-enabled/iam.abbamarkt.nl.conf   (symlink)
/etc/iam-api/env                              chmod 600 owner iam:iam
/etc/iam-api-staging/env                      chmod 600 owner iam:iam
/var/www/iam/releases/<ts>-<sha>/             owner iam:iam
/var/www/iam/current                          symlink → release
/var/www/iam-staging/releases/<ts>-<sha>/
/var/www/iam-staging/current                  symlink → release
/var/lib/iam-api/                             owner iam:iam (token budget)
/var/lib/iam-api-staging/                     owner iam:iam
/var/www/letsencrypt/                         for ACME challenge
/usr/local/bin/iam-deploy                     copied from tools/iam-deploy.sh
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Write bootstrap.sh — preflight, users, packages, Node 20</name>
  <files>bootstrap.sh</files>
  <read_first>
    - deploy.sh (reference for Node install flow)
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (D-01..D-04, D-16)
    - .githooks/pre-commit (confirm gitleaks invocation shape)
  </read_first>
  <action>
    Create `bootstrap.sh` at repo root with the structure below. The file is long (~300-400 lines); write it end-to-end in this single task. All steps must be idempotent — re-running must not create duplicate users, duplicate systemd units, or clobber env files that already exist.

    Required top-of-file shape:
    ```bash
    #!/bin/bash
    # IAM VPS bootstrap — Phase M2-02
    # Idempotent installer for Ubuntu 22.04 / 24.04 LTS.
    # Usage (interactive):    sudo bash bootstrap.sh
    # Usage (non-interactive): sudo BOOTSTRAP_NONINTERACTIVE=1 LETSENCRYPT_EMAIL=... OPENROUTER_API_KEY=... OPENROUTER_API_KEY_STAGING=... bash bootstrap.sh
    set -euo pipefail

    # --- Constants (match D-XX in .planning/M2/phases/02-vps-deployment/CONTEXT.md) ---
    DOMAIN="${DOMAIN:-interactivemove.nl}"
    STAGING_DOMAIN="${STAGING_DOMAIN:-iam.abbamarkt.nl}"
    REPO_URL="${REPO_URL:-REPLACE_ME_REPO_URL}"
    IAM_USER="iam"
    DEPLOY_USER="deploy"
    PROD_RELEASE_ROOT="/var/www/iam"
    STAGING_RELEASE_ROOT="/var/www/iam-staging"
    PROD_ENV_DIR="/etc/iam-api"
    STAGING_ENV_DIR="/etc/iam-api-staging"
    PROD_STATE_DIR="/var/lib/iam-api"
    STAGING_STATE_DIR="/var/lib/iam-api-staging"
    NODE_MAJOR="20"
    NONINTERACTIVE="${BOOTSTRAP_NONINTERACTIVE:-0}"

    log()  { printf '[bootstrap] %s\n' "$*"; }
    die()  { printf '[bootstrap] ERROR: %s\n' "$*" >&2; exit 1; }
    # Never echoes values — only lengths/hashes
    redact_len() { printf '%d' "${#1}"; }

    require_root() { [[ $EUID -eq 0 ]] || die "run as root (sudo bash bootstrap.sh)"; }
    ```

    Implement these steps as functions, invoked from a `main()` at the bottom. Each step must be idempotent. Steps for Task 1:

    **preflight_check()** — verify Ubuntu 22.04 or 24.04 via `/etc/os-release` (check `ID=ubuntu` and `VERSION_ID` in `22.04|24.04`). `die` if not. Verify repo root contains `config/systemd/iam-api.service`, `config/nginx/interactivemove.nl.conf`, `tools/env-template` — die if missing.

    **gather_inputs()** — read env vars. If any required var is missing:
      - if `NONINTERACTIVE=1`: die listing the missing vars
      - else: prompt with `read -r` for plain vars, `read -rs` for secrets (OPENROUTER_API_KEY*), echo newline after read
      Required: `LETSENCRYPT_EMAIL`, `OPENROUTER_API_KEY`, `OPENROUTER_API_KEY_STAGING`.
      Validate: email matches `^[^@]+@[^@]+\.[^@]+$`; api keys non-empty. Never echo values — only `log "got openrouter key (len=$(redact_len "$OPENROUTER_API_KEY"))"`.

    **create_users()** — create `iam` as `useradd --system --user-group --no-create-home --shell /usr/sbin/nologin iam` if `id iam` fails. Create `deploy` as `useradd --create-home --shell /bin/bash deploy` if `id deploy` fails. Add `deploy` to the `iam` group via `usermod -aG iam deploy` (for release-dir write access). Both creations wrapped in `id <user> &>/dev/null || useradd ...`.

    **install_packages()** — run `apt-get update`, then `DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates curl gnupg nginx certbot python3-certbot-nginx fail2ban ufw git`. Use `--no-install-recommends` to keep the footprint lean.

    **install_node20()** — if `node -v` does NOT start with `v20.`, run (EXACT command string required):
    ```
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
    apt-get install -y nodejs
    ```
    After install: `node -v | grep -q '^v20\.' || die "node 20 not active"`.

    End Task 1 with a commit. Later tasks extend the same file.
  </action>
  <acceptance_criteria>
    - `grep -Fxc '#!/bin/bash' bootstrap.sh` returns 1 (first line)
    - `head -1 bootstrap.sh` equals `#!/bin/bash`
    - `grep -c 'set -euo pipefail' bootstrap.sh` returns 1
    - `grep -c 'BOOTSTRAP_NONINTERACTIVE' bootstrap.sh` returns at least 1
    - `grep -Fc 'curl -fsSL https://deb.nodesource.com/setup_20.x | bash -' bootstrap.sh` returns 1
    - `grep -c 'useradd --system' bootstrap.sh` returns at least 1 (iam user)
    - `grep -c 'usermod -aG iam deploy' bootstrap.sh` returns 1
    - `grep -c 'apt-get install -y' bootstrap.sh` returns at least 1 and that line mentions `nginx certbot python3-certbot-nginx fail2ban ufw`
    - File does not echo secret values: `grep -cE '(echo|printf).*\$OPENROUTER_API_KEY' bootstrap.sh` returns 0
    - `shellcheck bootstrap.sh` returns 0 (install via `apt-get install -y shellcheck` if missing locally; if install not possible, record in commit body)
    - `bash -n bootstrap.sh` returns 0 (syntax check)
  </acceptance_criteria>
  <verify>
    <automated>bash -n bootstrap.sh && head -1 bootstrap.sh | grep -Fxq '#!/bin/bash' && grep -Fq 'curl -fsSL https://deb.nodesource.com/setup_20.x | bash -' bootstrap.sh && grep -q 'set -euo pipefail' bootstrap.sh && ! grep -qE '(echo|printf).*\$OPENROUTER_API_KEY' bootstrap.sh</automated>
  </verify>
  <done>Skeleton + preflight/users/packages/Node-install functions land; `bash -n` clean; commit `feat(M2-02): bootstrap.sh skeleton (preflight, users, packages, node 20) per D-01..D-04`.</done>
</task>

<task type="auto">
  <name>Task 2: bootstrap.sh — config install, env rendering, systemd, nginx, certbot</name>
  <files>bootstrap.sh</files>
  <read_first>
    - bootstrap.sh (from Task 1)
    - config/systemd/iam-api.service, config/systemd/iam-api-staging.service
    - config/nginx/interactivemove.nl.conf, config/nginx/iam.abbamarkt.nl.conf
    - tools/env-template, tools/env-staging-template
  </read_first>
  <action>
    Extend `bootstrap.sh` (append to the file before `main()` wires the call order) with these additional functions:

    **create_dirs()** — `install -d -o iam -g iam -m 755` for each:
      `$PROD_RELEASE_ROOT/releases`, `$STAGING_RELEASE_ROOT/releases`,
      `$PROD_STATE_DIR`, `$STAGING_STATE_DIR`,
      `/var/www/letsencrypt` (owned by root:www-data, mode 755).
    `$PROD_ENV_DIR` and `$STAGING_ENV_DIR` must be `root:iam` mode `750` (iam can read, nobody else).

    **render_env()** — for prod: if `$PROD_ENV_DIR/env` does NOT exist, render `tools/env-template` by substituting only the two placeholders this script knows:
      `REPLACE_ME_OPENROUTER_PROD_KEY` → `$OPENROUTER_API_KEY`
      (HubSpot placeholders deliberately left in place — Phase 04's concern; bootstrap logs a warning listing remaining placeholders)
    Write to a temp file via `mktemp`, `chmod 600`, `chown iam:iam`, then `mv` atomically into place. Never `cat` the temp file to stdout. After render: `grep -v '^OPENROUTER_API_KEY=' "$PROD_ENV_DIR/env" | ...` if you need to confirm — do not print the key line.
    If the file already exists, log `env file already present, skipping (edit manually if needed)` and move on. Same logic for staging.
    Use `awk` or `sed` with a delimiter that cannot appear in a key (`sed -i "s#REPLACE_ME_OPENROUTER_PROD_KEY#$OPENROUTER_API_KEY#"` — `#` chosen because OpenRouter keys don't contain `#`).

    **install_systemd_units()** — `install -m 644 config/systemd/iam-api.service /etc/systemd/system/iam-api.service` (same for staging). Then:
    ```
    systemctl daemon-reload
    systemctl enable iam-api.service iam-api-staging.service
    ```
    Do NOT start the services yet — release dirs may be empty (Phase 03 CI fills them later). Log: "systemd units installed and enabled; will start after first deploy."

    **install_nginx_vhosts()** — `install -m 644 config/nginx/interactivemove.nl.conf /etc/nginx/sites-available/interactivemove.nl.conf` (same for staging). Then:
    ```
    ln -sf /etc/nginx/sites-available/interactivemove.nl.conf /etc/nginx/sites-enabled/interactivemove.nl.conf
    ln -sf /etc/nginx/sites-available/iam.abbamarkt.nl.conf   /etc/nginx/sites-enabled/iam.abbamarkt.nl.conf
    nginx -t
    systemctl reload nginx
    ```

    **request_certs()** — D-16. Run `certbot --nginx --non-interactive --agree-tos --email "$LETSENCRYPT_EMAIL" --domains "$DOMAIN,www.$DOMAIN" --redirect --keep-until-expiring`. Repeat for `$STAGING_DOMAIN` (no www variant). Wrap in `if` that checks `/etc/letsencrypt/live/$DOMAIN/fullchain.pem` existence first — skip if present and `--keep-until-expiring` handles renewal. certbot's systemd timer already runs — no additional cron needed.

    **install_deploy_tool()** — copy `tools/iam-deploy.sh` (Plan 04 writes it) to `/usr/local/bin/iam-deploy`, `chmod 755`, `chown root:root`. This is what Phase 03's GitHub Actions workflow invokes over SSH.

    **install_git_hooks()** — set `git config --system core.hooksPath /etc/iam-githooks` and copy `.githooks/pre-commit` there. This ensures contributors checking out the repo on the VPS (rare) still get gitleaks. (Primary hook wiring is dev-machine-side; system-wide is a safety net.)

    **configure_firewall()** — `ufw allow OpenSSH`, `ufw allow 'Nginx Full'`, `ufw --force enable`. Idempotent: `ufw status | grep -q 'Status: active'` → skip re-enable.

    **print_next_steps()** — print the one-liner "Now do the Cloudflare runbook at .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md" plus a reminder that env files at `$PROD_ENV_DIR/env` still contain `REPLACE_ME_HUBSPOT_*` placeholders to fill in before Phase 04.

    Finally, the **main()** at the bottom must call, in order:
    ```
    require_root
    preflight_check
    gather_inputs
    create_users
    install_packages
    install_node20
    create_dirs
    render_env
    install_systemd_units
    install_nginx_vhosts
    request_certs
    install_deploy_tool
    install_git_hooks
    configure_firewall
    print_next_steps
    ```
    Wrap `main "$@"` at the very end. Keep the file executable: `chmod +x bootstrap.sh`.
  </action>
  <acceptance_criteria>
    - `grep -c '^install_systemd_units()' bootstrap.sh` returns 1
    - `grep -c '^install_nginx_vhosts()' bootstrap.sh` returns 1
    - `grep -c '^request_certs()' bootstrap.sh` returns 1
    - `grep -c '^render_env()' bootstrap.sh` returns 1
    - `grep -c '^create_dirs()' bootstrap.sh` returns 1
    - `grep -c '^install_deploy_tool()' bootstrap.sh` returns 1
    - `grep -c 'systemctl daemon-reload' bootstrap.sh` returns at least 1
    - `grep -c 'systemctl enable iam-api.service iam-api-staging.service' bootstrap.sh` returns 1
    - `grep -c 'ln -sf /etc/nginx/sites-available/' bootstrap.sh` returns 2
    - `grep -c 'certbot --nginx' bootstrap.sh` returns at least 1
    - `grep -c 'chmod 600' bootstrap.sh` returns at least 1
    - `grep -Fc '/etc/iam-api/env' bootstrap.sh` returns at least 1
    - `grep -Fc '/etc/iam-api-staging/env' bootstrap.sh` returns at least 1
    - `grep -c '^main "\$@"$' bootstrap.sh` returns 1 (actual invocation at the end)
    - `test -x bootstrap.sh` succeeds (executable bit set)
    - `bash -n bootstrap.sh` returns 0
    - `shellcheck bootstrap.sh` returns 0 (skip with note if shellcheck unavailable)
    - File does not contain any real-looking secret: `grep -E 'sk-or-[a-zA-Z0-9]{16,}' bootstrap.sh` returns empty (exit 1)
    - File does not call `sudo` internally (bootstrap is already run as root): `grep -c '^[^#]*\bsudo\b' bootstrap.sh` returns 0
  </acceptance_criteria>
  <verify>
    <automated>bash -n bootstrap.sh && test -x bootstrap.sh && grep -q '^main "\$@"$' bootstrap.sh && grep -q 'certbot --nginx' bootstrap.sh && grep -q 'systemctl enable iam-api.service iam-api-staging.service' bootstrap.sh && ! grep -qE 'sk-or-[a-zA-Z0-9]{16,}' bootstrap.sh && ! grep -qE '^[^#]*\bsudo\b' bootstrap.sh</automated>
  </verify>
  <done>Complete bootstrap.sh end-to-end passes `bash -n` and `shellcheck`; commit `feat(M2-02): bootstrap.sh configs/env/systemd/nginx/certbot/firewall per D-01..D-04,D-16`.</done>
</task>

</tasks>

<verification>
Final checks on bootstrap.sh:
```
bash -n bootstrap.sh
shellcheck bootstrap.sh     # skip if shellcheck not installed locally, record in SUMMARY
grep -c 'systemctl\|nginx\|certbot\|useradd\|NodeSource\|setup_20\.x' bootstrap.sh   # expect >= 6
```
</verification>

<success_criteria>
- `bootstrap.sh` exists at repo root, executable, shellcheck/bash-n clean
- Re-running the script on a VPS where everything is already set up does not break state (idempotency preserved by `id user &>/dev/null ||`, `[[ -e file ]] ||`, `ln -sf`, `--keep-until-expiring`, `mktemp + mv`)
- Secrets are read with `read -rs`, written with `chmod 600`, never echoed
- Operator only needs to know four inputs (DOMAIN, LETSENCRYPT_EMAIL, OPENROUTER_API_KEY, OPENROUTER_API_KEY_STAGING) — everything else has sane defaults
</success_criteria>

<output>
After completion: create `.planning/M2/phases/02-vps-deployment/03-SUMMARY.md` with the bootstrap.sh line count, `bash -n` result, `shellcheck` result (or "not available"), and a short explanation of idempotency patterns used.
</output>
