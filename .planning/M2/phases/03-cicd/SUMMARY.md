# M2 Phase 03: CI/CD — Summary

**Branch:** `m2/phase-03` (branched from `m2/phase-02`)
**Completed:** 2026-04-21
**Commits:** see below
**Status:** Code-complete; not executed (GitHub Environments + Secrets are human-only configuration).

## What shipped

All five phase success criteria from ROADMAP.md are addressed:

| SC | Description | Status |
|----|-------------|--------|
| 1 | Push to `main` triggers Actions, atomic symlink swap, reloads services, health check, under 2 min | `deploy-prod` job written, invokes `iam-deploy prod` over SSH |
| 2 | Push to `staging` performs equivalent against `iam.abbamarkt.nl` | `deploy-staging` job written, invokes `iam-deploy staging` |
| 3 | Rollback via Actions re-run OR VPS-side symlink flip | Both documented in HANDOFF-CHECKLIST §6 |
| 4 | Deploy user SSH-only, no sudo, scoped to release dir | `config/sudoers.d/iam-deploy` with narrow NOPASSWD only for `iam-deploy` + `systemctl reload|restart` of the three managed services |
| 5 | Zero hardcoded secrets — all via Actions Secrets | Workflow uses only `${{ secrets.* }}`; no literals. HANDOFF-CHECKLIST enumerates every secret name |

## Decisions honored (D-01..D-13)

- **D-01:** Single workflow `.github/workflows/deploy.yml` with two jobs, shared job logic.
- **D-02:** `ubuntu-latest`; checkout → install SSH key from secret → scp tarball → SSH exec `iam-deploy`.
- **D-03:** Secrets: `SSH_PRIVATE_KEY`, `VPS_HOST`, `VPS_USER`. GitHub Environments `production` / `staging` for per-env scoping.
- **D-04:** Prod environment will require reviewer approval (configured via GitHub UI — documented in HANDOFF-CHECKLIST §1).
- **D-05:** Post-deploy health check: `curl -fsS --max-time 5 https://$DOMAIN/` with 5 retries at 3s each. Note: CONTEXT suggested also a POST to `/api/chat` — deferred to HANDOFF-CHECKLIST Open Questions because chat POSTs would hit the rate limiter during rapid deploys.
- **D-06:** `tools/iam-deploy.sh` written in Phase 02; `bootstrap.sh` copies to `/usr/local/bin/iam-deploy`.
- **D-07:** atomic flow preserved — the workflow's tarball path `/tmp/iam-deploy-<sha>.tar.gz` matches `iam-deploy`'s expected tarball contract.
- **D-08:** Rollback via re-run (Actions UI) or manual symlink flip — documented.
- **D-09:** `config/sudoers.d/iam-deploy` — narrow NOPASSWD for `deploy` user; `bootstrap.sh` installs with mode 440 + `visudo -cf` validation. (Added as a minor extension of Phase 02's bootstrap.sh — noted below.)
- **D-10:** `iam-deploy` already idempotent (Phase 02 Plan 04).
- **D-11, D-12:** Atomic symlink swap + `systemctl restart` — implemented in `iam-deploy` (Phase 02).
- **D-13:** No Slack/email notifications; Actions UI only.

## Cross-phase amendment

The workflow requires `deploy ALL=(iam) NOPASSWD: /usr/local/bin/iam-deploy *` and reload-only systemctl entries (D-09). The cleanest place for that is bootstrap.sh. So this phase:

1. Added `config/sudoers.d/iam-deploy` (new file).
2. Added `install_sudoers_deploy()` function to `bootstrap.sh` and wired it into `main()`.

This is a forward-only addition to `bootstrap.sh`. No behavior change when the drop-in file is absent (function warns and returns). Recorded as part of this phase's commit series.

## Files delivered

**In repo:**
- `.github/workflows/deploy.yml` — 143 lines, YAML-valid
- `config/sudoers.d/iam-deploy` — sudoers drop-in (mode-sensitive; installed at 440)
- `bootstrap.sh` — amended with `install_sudoers_deploy()` + call in `main()`

**In planning:**
- `.planning/M2/phases/03-cicd/HANDOFF-CHECKLIST.md`
- `SUMMARY.md` (this file)

## Verification

- `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/deploy.yml'))"` → OK
- `bash -n bootstrap.sh` → OK
- Both jobs gate on an `if:` matching their ref; `workflow_dispatch` input routes manual runs
- No hardcoded secrets: `grep -rE '(sk-or-|ghp_|ghs_)[A-Za-z0-9]{16,}' .github/ config/ bootstrap.sh tools/ api/` → empty
- `concurrency:` group prevents overlapping deploys on the same ref

## Deferred / reviewer attention

1. **GitHub Environments + Secrets are human-set** (scope-of-this-run limit — Actions Secrets are out of reach for this worker). HANDOFF-CHECKLIST §2 enumerates the exact names and values.
2. **SSH key pairing** between Actions and the VPS `deploy` user is human-only. HANDOFF-CHECKLIST §3 has the recipe.
3. **Post-deploy chat POST** in the health check was deferred to avoid rate-limit interactions during rapid deploys; currently health check hits `/` only.

## STOP-AND-ASK triggers hit

None (excluding items resolved under the session override).

## Guardrail Overrides in force

Same as Phase 02: STOP-AND-ASK #1 replaced with PLACEHOLDER PROTOCOL; stop-after-phase replaced with chained-phase protocol; PR-opening deferred.

All other guardrails still enforced: no credential rotation, no filter-repo, no live API calls, no `/etc` writes from the worker, no direct push to `main`.

---

*Phase: M2-03-cicd*
*Chained autonomous run: 2026-04-21*
*Next: Phase 04 (HubSpot backend routing) branches from this branch.*
