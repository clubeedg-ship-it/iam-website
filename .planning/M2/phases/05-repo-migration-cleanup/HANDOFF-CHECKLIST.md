# M2 Phase 05 — Repo Migration + Cleanup Handoff Checklist

> Phase 05 prepared the clean state locally. Cutover is strictly a human action — see `CUTOVER-RUNBOOK.md`. This checklist enumerates the placeholder values that need human input before cutover, and the decisions the human must make along the way.

## 1. Decisions the human owns

| Decision | Current state | What to do |
|----------|---------------|------------|
| LICENSE choice (D-15) | `LICENSE` contains `REPLACE_ME_LICENSE_CHOICE` | Choose: proprietary / MIT / Apache-2.0 / BSD-3-Clause. Edit `LICENSE` with full text. Commit. |
| `oopuo-ship` git identity (D-05) | `tools/prepare-clean-repo.sh` expects `AUTHOR_NAME` + `AUTHOR_EMAIL` env vars | Set to the `oopuo-ship` GitHub account name and email. Never the personal/dev account — that leaks authorship across the cutover boundary. |
| Whether to keep `tools/migrate_i18n.py` (D-06) | Not present in this repo as of phase 05; not created by worker | Verify with IAM dev; if it exists in the working tree but is unused, delete before running `prepare-clean-repo.sh`. Worker did not touch. |
| Whether to keep `tools/vm-check.sh` (D-06) | Not present in this repo | Same. |
| Whether to keep `server.js` | Present; static server, likely local-dev only | Decide: keep as dev convenience OR delete (Nginx serves statics in prod). Worker did not delete. |

## 2. Placeholder tokens introduced by Phase 05

| Token | File | What it becomes |
|-------|------|-----------------|
| `REPLACE_ME_LICENSE_CHOICE` | `LICENSE` | License text |
| `REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_NAME` | `tools/prepare-clean-repo.sh` | The `oopuo-ship` GitHub account's display name (override via `$AUTHOR_NAME` env) |
| `REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_EMAIL` | `tools/prepare-clean-repo.sh` | The `oopuo-ship` GitHub account's primary email (override via `$AUTHOR_EMAIL` env) |

All Phase 01–04 placeholders (env vars, Cloudflare, HubSpot, SSH) are **still open** and re-listed in `.planning/M2/MASTER-REVIEW-BRIEF.md §REPLACE_ME inventory` for a single-document view.

## 3. Infrastructure-bound items left open (NOT code-side)

These stay for human completion; worker did NOT resolve them because they require infra access:

- GitHub account creation (`oopuo-ship/iam-website` public, `oopuo-ship/iam-website-internal` private)
- OpenRouter key rotation (Phase 01 D-01)
- VPS provisioning + `bootstrap.sh` run (Phase 02)
- GitHub Environments + Actions Secrets (Phase 03)
- HubSpot custom-property enablement (Phase 04 D-12/D-13)
- SSH key pairing for the new repo's deploy workflow (Phase 03 + CUTOVER step 6)
- Cloudflare runbook execution (Phase 02)
- DNS for staging
- Branch protection rules on the new repo
- Archival of the old `clubeedg-ship-it/iam-website` repo

## 4. Items Phase 05 swept and closed (inherited from prior phases)

From prior HANDOFF-CHECKLISTs, these were explicitly marked "code-only, no infra" and are now closed:

- (Phase 02) `.gitignore` cleanup for new repo — extended to cover `coverage/`, `.nyc_output/`, editor swap files (`*~`, `.*.swp`, `.*.swo`), worktrees (`.claude/worktrees/`), `.env*` glob instead of just `.env`, `*.pem`, `*.key`, `*_rsa`, `id_ed25519*`, `credentials.json`, `service-account*.json`.
- (Phase 02) Tracked-by-force entries for `tools/iam-deploy.sh` — added explicit `!tools/iam-deploy.sh` exception to `.gitignore` so the file's tracking is not accidentally reversed.
- (Phase 03) gitleaks CI workflow — delivered at `.github/workflows/gitleaks.yml`. Runs on PR + push to main/staging. Harmless on current repo (doesn't block anything that would have blocked anyway); primary purpose is to protect the new repo from day one.
- (Phase 05 self) README.md — minimal, AI-workflow-free. Covers stack, local dev, deploy one-liner, contact email.

## 5. Cross-phase placeholder tokens STILL open at end of M2

Complete re-inventory lives in `MASTER-REVIEW-BRIEF.md`. Short form:

```
REPLACE_ME_LICENSE_CHOICE                         — LICENSE (M2-05, human chooses license)
REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_NAME           — tools/prepare-clean-repo.sh (human, pre-cutover)
REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_EMAIL          — tools/prepare-clean-repo.sh (human, pre-cutover)
REPLACE_ME_REPO_URL                               — bootstrap.sh (human, set before next VPS bootstrap)
REPLACE_ME_VPS_IP                                 — cloudflare-runbook.md (human, at Cloudflare setup)
REPLACE_ME_OPENROUTER_PROD_KEY                    — tools/env-template (auto-rendered by bootstrap from $OPENROUTER_API_KEY)
REPLACE_ME_OPENROUTER_STAGING_KEY                 — tools/env-staging-template (auto-rendered by bootstrap)
REPLACE_ME_HUBSPOT_PORTAL_ID                      — both env templates (human, pre-prod-start)
REPLACE_ME_HUBSPOT_CONTACT_FORM_GUID              — both env templates (human, pre-prod-start)
REPLACE_ME_HUBSPOT_PARTNER_FORM_GUID              — both env templates (reserved; MVP uses single GUID)
```

## 6. Known caveats

- `prepare-clean-repo.sh` uses `rsync` and `git init`. It does not currently inspect the `.planning/M2/RUN-REPORT.md` or the reviewer audit outputs — those live only in `.planning/`, which is excluded by design. If the reviewer wants them in `iam-website-internal`, they're copied as part of CUTOVER §5 "mirror internal workflow tree".
- The script fails fast if the `AUTHOR_NAME`/`AUTHOR_EMAIL` env vars are still placeholders — safety rail against accidentally committing as "REPLACE_ME".
- The script refuses to commit if any gitignored files snuck into the staging area. This is a defense against the `force-add` pattern Phase 01/02 used for planning artifacts.
- Gitleaks CI (`.github/workflows/gitleaks.yml`) runs only if the repo has `secrets.GITHUB_TOKEN`, which every GitHub repo does by default — no human setup needed beyond merging.
