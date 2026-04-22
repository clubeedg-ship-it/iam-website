# M2 Master Review Brief

> Single document to drive end-to-end review of Milestone M2 (Production-Ready IAM Website). Generated at the close of the chained autonomous run, 2026-04-21. The reviewer agent / human auditor uses this alongside each phase's `CONTEXT.md` and `SUMMARY.md`.

---

## Phase-by-phase summary

### Phase 01 — Security Remediation (branch `m2/phase-01`)

Rewrote the vulnerable 76-line chat proxy into a hardened Express app: CORS allowlist (`CHAT_ALLOWED_ORIGINS`), 10-req/min per-IP rate limit, zod validation (32KB body, 4000-char message, 20-turn history), pino logging, monthly token budget counter (flat-JSON), and server-side prepend of the IAM knowledge base + system prompt (the two formerly client-side files are deleted; client payload is now user turns only). Pre-commit gitleaks hook installed under `.githooks/`. `CLAUDE.md` untracked and added to `.gitignore`. History scan produced `HISTORY-SCAN.md` flagging `.env.docker` additions in commits `f33ea1f`/`99dfb4e` and an `sk-or-` literal in `8224c4b` — rotation is a human action per GUARDRAILS. Smoke tests: **5/5 pass** against a local OpenRouter mock (D-13 affordance introduced mid-flight as the `OPENROUTER_URL` env override).

### Phase 02 — VPS Deployment (branch `m2/phase-02`)

Fresh-Ubuntu bootstrap delivered end-to-end: `bootstrap.sh` (idempotent, interactive-or-env-driven, Node 20 via NodeSource, Nginx + Certbot + fail2ban + UFW + gitleaks), two systemd units (`iam-api.service` + `iam-api-staging.service`) with resource limits, two Nginx vhosts with HSTS/CSP/security-headers/per-location rate limiting, prod + staging env templates with `REPLACE_ME_*` placeholders, and `tools/iam-deploy.sh` — the atomic-symlink release/rollback script. Cloudflare click-by-click runbook delivered at `.planning/M2/phases/02-vps-deployment/cloudflare-runbook.md`. No VPS was touched; all verification is static (`bash -n`, grep sweeps).

### Phase 03 — CI/CD (branch `m2/phase-03`, local-only — PAT scope blocks push)

`.github/workflows/deploy.yml`: two jobs gated by `if:` on ref (`deploy-prod` on main, `deploy-staging` on staging) with `workflow_dispatch` override, production environment requires reviewer approval per D-04, Actions Secrets `SSH_PRIVATE_KEY` / `VPS_HOST` / `VPS_USER` scoped per-environment. Workflow builds a tarball (excluding `.git`, `.planning`, `.github`, `.claude`, `.kiro`, `node_modules`), scp to VPS `/tmp/`, invokes `sudo -u iam /usr/local/bin/iam-deploy <env> <sha>`, retries `curl https://$DOMAIN/` 5× before failing. `config/sudoers.d/iam-deploy` drop-in — narrow NOPASSWD for the deploy user; `bootstrap.sh` gained `install_sudoers_deploy()` with `visudo -cf` validation.

### Phase 04 — HubSpot Integrations (branch `m2/phase-04`, local-only)

New `api/contact-route.js` mounted into the Phase-01 Express app: zod schema, rate limit 5/10min, origin allowlist (reuses chat's), honeypot checked BEFORE zod so bots get silent 200 (not 400 tell), server-to-server fetch to HubSpot v3 with 10s AbortController timeout, `{ok:true}` / `{ok:false, reason:...}` wire format. Client `js/contact-form.js` rewritten to POST same-origin `/api/contact` — portal ID and form GUID removed from the client entirely. Mailto fallback logic preserved. New smoke suite `api/test/contact.smoke.test.js` (5 cases + 2 assertion passes) against `api/test/mock-hubspot.js` — **7/7 pass**; never hits `api.hsforms.com`.

### Phase 05 — Repo Migration + Cleanup (branch `m2/phase-05`, local-only)

Cosmetic HTML cleanup: 9 files, 9 stray AI-placeholder comments deleted (`<!-- Testimonials placeholder -->`, `<!-- Video placeholder -->`, `<!-- Contact privacy notice removed -->`). Repo-migration prep delivered without touching any remote: `LICENSE` placeholder, new minimal AI-fingerprint-free `README.md`, extended `.gitignore` (coverage, editor swap, `.env*` glob, keys, worktrees), `.github/workflows/gitleaks.yml`, and `tools/prepare-clean-repo.sh` — read-only against current repo; when invoked later against a fresh target it rsyncs a clean tree, does a single oopuo-ship-authored `initial import` commit, and safety-scans for leaked artifacts. `CUTOVER-RUNBOOK.md` spells out the human-only procedure (11 sections, 5 gates). No remotes touched, no DNS changes, no GitHub settings changes.

---

## Branches

| Branch | Based on | Commit count | Pushed to origin? | Blocker if not pushed |
|--------|----------|--------------|-------------------|-----------------------|
| `m2/phase-01` | `main` | 11 | ✓ | — |
| `m2/phase-02` | `m2/phase-01` | 9 | ✓ | — |
| `m2/phase-03` | `m2/phase-02` | 2 | ✗ local only | PAT lacks `workflow` scope (adds `.github/workflows/deploy.yml`) |
| `m2/phase-04` | `m2/phase-03` | 2 | ✗ local only | inherits workflow file from phase-03 — same block |
| `m2/phase-05` | `m2/phase-04` | 3 | ✗ local only | inherits workflow files from phase-03 — same block |

**To unblock:** grant the PAT the GitHub `workflow` scope (fine-grained token: Repository permissions → Workflows → Read and write). Then from this worktree:

```
git push -u origin m2/phase-03
git push -u origin m2/phase-04
git push -u origin m2/phase-05
```

---

## REPLACE_ME inventory (consolidated across all phases)

| Token | Where it lives | Meaning | Who resolves |
|-------|----------------|---------|--------------|
| `REPLACE_ME_LICENSE_CHOICE` | `LICENSE` | License text (proprietary / MIT / Apache-2.0 / BSD-3-Clause) | IAM dev / OOPUO owner |
| `REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_NAME` | `tools/prepare-clean-repo.sh` | `oopuo-ship` GitHub account display name | OOPUO sysadmin (script fails fast otherwise) |
| `REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_EMAIL` | `tools/prepare-clean-repo.sh` | `oopuo-ship` GitHub account email | OOPUO sysadmin |
| `REPLACE_ME_REPO_URL` | `bootstrap.sh` | Public git URL of the repo | OOPUO sysadmin at next bootstrap |
| `REPLACE_ME_VPS_IP` | `.planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` | VPS public IPv4 | IAM dev at Cloudflare step 1 |
| `REPLACE_ME_OPENROUTER_PROD_KEY` | `tools/env-template` | OpenRouter API key for prod | IAM dev — but bootstrap auto-substitutes from `$OPENROUTER_API_KEY` |
| `REPLACE_ME_OPENROUTER_STAGING_KEY` | `tools/env-staging-template` | Separate staging OpenRouter key per D-20 | IAM dev — bootstrap auto-substitutes |
| `REPLACE_ME_HUBSPOT_PORTAL_ID` | both env templates | HubSpot portal id (numeric) — known-good `49291889` from hotfix `e01514c` | IAM dev before prod start |
| `REPLACE_ME_HUBSPOT_CONTACT_FORM_GUID` | both env templates | Contact form GUID — known-good `82e91e6d-7a36-47a4-8171-9f213e17fcb5` | IAM dev before prod start |
| `REPLACE_ME_HUBSPOT_PARTNER_FORM_GUID` | both env templates | Reserved; MVP uses single GUID | IAM dev (can leave equal to contact GUID) |

A negative grep for real-looking secrets across all tracked files at HEAD:
```
grep -rE 'sk-or-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|ghs_[A-Za-z0-9]{20,}|[A-Za-z0-9_-]{20,}@serviceaccount\.com' \
  --exclude-dir=.git --exclude-dir=node_modules .
```
returns empty (verified 2026-04-21).

---

## HANDOFF items by actor

### IAM dev owns (most items)

- **Credential rotation** (Phase 01 D-01 / `HISTORY-SCAN.md`): rotate any OpenRouter / DB password that ever landed in git history. Do this on the OpenRouter dashboard before running `bootstrap.sh`.
- **VPS provisioning**: fresh Ubuntu 22.04 or 24.04 LTS box with SSH access. Phase 02 `bootstrap.sh` does everything else.
- **`bootstrap.sh` inputs**: `LETSENCRYPT_EMAIL`, `OPENROUTER_API_KEY`, `OPENROUTER_API_KEY_STAGING` — env vars or interactive prompts.
- **HubSpot env values**: set `HUBSPOT_PORTAL_ID`, `HUBSPOT_CONTACT_FORM_GUID` in `/etc/iam-api/env` + staging equivalent. Reload with `sudo systemctl reload iam-api iam-api-staging`.
- **HubSpot custom properties** (Phase 04 D-12/D-13): confirm `page_source` and `language` exist on form `82e91e6d-…`; if they do, extend `toHubSpotFields()` in `api/contact-route.js` per HANDOFF §2 and redeploy.
- **Cloudflare setup** (Phase 02 D-18): follow `cloudflare-runbook.md` click-by-click after `bootstrap.sh` finishes and certs are issued.
- **DNS for staging**: add A record `iam.abbamarkt.nl` → VPS IP, un-proxied (no Cloudflare).
- **End-to-end QA** (Phase 04 D-14): three form submissions from prod with `CLAUDE-TEST` marker; confirm HubSpot record + email at `klantcontact@interactivemove.nl`; delete test records.
- **Network-failure smoke** (Phase 04 D-15): stop `iam-api`, submit form, confirm mailto fallback, restart.

### Autonomous worker owns (this run closed these)

- All code-side, config-side, and documentation deliverables across all five phases.
- Placeholder inventory + HANDOFF-CHECKLIST per phase + consolidated in this doc.
- Smoke-test suites: chat (5 cases) and contact (7 cases), 12/12 passing against local mocks.
- `prepare-clean-repo.sh` that enables the migration without needing worker hands on any remote.
- No live credential rotation, no git history rewrite, no remote changes.

### OOPUO sysadmin owns (Phase 05 cutover)

- Create `oopuo-ship/iam-website` (public, empty) and `oopuo-ship/iam-website-internal` (private, empty).
- Run `tools/prepare-clean-repo.sh` with `AUTHOR_NAME` / `AUTHOR_EMAIL` env vars set.
- Push to the new public repo (`CUTOVER §4`).
- Mirror internal tree to the private repo (`CUTOVER §5`).
- Configure branch protection, environments, secrets on the new repo (`CUTOVER §6`).
- Run staging smoke from the new repo (`CUTOVER §7`).
- Switch prod to the new repo (`CUTOVER §8`).
- Archive the old `clubeedg-ship-it/iam-website` (+30 days delete) (`CUTOVER §9`).

### Reviewer agent (separate session) owns

- Audit each phase branch against its `CONTEXT.md` / `SUMMARY.md`.
- Raise PAT permission issue to unblock push of `m2/phase-03..05`.
- Open four PRs in order: 01 → 02 → 03 → 04 → 05. Each based on the prior.
- Approve or comment. Merge cascade only after all five pass.

---

## Cross-phase D-XX audit

For each decision in every phase's CONTEXT.md, the commit that implements it. "NOT IMPLEMENTED" rows are deferred on purpose (human action or cutover gate).

### Phase 01 (`m2/phase-01`)

| D-XX | Topic | Commit |
|------|-------|--------|
| D-01 | Treat ever-committed creds as leaked, rotate | `7bb0e38` documents; ROTATION is HUMAN |
| D-02 | filter-repo if history shows additions | `7bb0e38` REPORT only (gated human) |
| D-03 | `git rm --cached CLAUDE.md` + gitignore | `222cd37` |
| D-04 | gitleaks pre-commit via `.githooks/` | `bd61eb1` |
| D-05 | Express app rewrite | `0eaadc4` |
| D-06 | CORS allowlist from env, 403 | `0eaadc4` |
| D-07 | Rate limit 10/min, 429 | `0eaadc4` |
| D-08 | 32KB / 4000-char / 20-turn limits | `0eaadc4` |
| D-09 | Server-side KB + system prompt | `55c7a27` (create) + `3893116` (strip client) + `0eaadc4` (prepend) |
| D-10 | Monthly token budget | `1844af9` (module) + `9394b34` (integration) |
| D-11 | pino logging | `0eaadc4` |
| D-12 | No DB, flat JSON + in-memory | implicit across `1844af9` + `0eaadc4` |
| D-13 | Smoke tests | `555b1d5` (mock) + `b15302a` (suite) |

### Phase 02 (`m2/phase-02`)

| D-XX | Topic | Commit |
|------|-------|--------|
| D-01 | `bootstrap.sh` single idempotent script | `6516516` |
| D-02 | Env-var-or-prompt inputs | `6516516` |
| D-03 | Env files `/etc/iam-api/env` chmod 600 owner iam | `6516516` + `b5dc841` (templates) |
| D-04 | Non-privileged `iam` user + `deploy` user | `6516516` |
| D-05 | systemd units (prod + staging) | `4a7e199` + `cbbcf9f` |
| D-06 | Resource limits | `4a7e199` |
| D-07 | journald only | `4a7e199` |
| D-08 | Replaces PM2 | `4a7e199` |
| D-09 | Two Nginx vhosts | `228375d` + `471e044` |
| D-10 | Static from release dir + `current` symlink | `228375d` + `988b299` |
| D-11 | `/api/chat` proxy headers | `228375d` |
| D-12 | `/api/contact` reserved location | `228375d` + `471e044` |
| D-13 | Nginx rate limit | `228375d` + `471e044` |
| D-14 | Security headers | `228375d` + `471e044` |
| D-15 | Cache headers | `228375d` + `471e044` |
| D-16 | Certbot + systemd timer | `6516516` |
| D-17 | Cloudflare Full (strict) | `47d6b55` (runbook) |
| D-18 | Cloudflare runbook deliverable | `47d6b55` |
| D-19 | Staging split | `cbbcf9f` + `471e044` + `b5dc841` |
| D-20 | Separate staging OpenRouter key | `b5dc841` (staging env template) |

### Phase 03 (`m2/phase-03`)

| D-XX | Topic | Commit |
|------|-------|--------|
| D-01 | Single workflow file | `5927cec` |
| D-02 | ubuntu-latest + checkout + SSH + iam-deploy | `5927cec` |
| D-03 | Secrets via Actions Secrets + Environments | `5927cec` + HUMAN (repo settings) |
| D-04 | Prod reviewer approval | `5927cec` (env name) + HUMAN (settings) |
| D-05 | Health check + rollback on fail | `5927cec` (health) + `988b299` (iam-deploy rollback) |
| D-06 | `iam-deploy` at `/usr/local/bin` installed by bootstrap | `6516516` (install) + `988b299` (source) |
| D-07 | Atomic release flow | `988b299` |
| D-08 | Rollback via symlink flip | `988b299` + HANDOFF §6 |
| D-09 | Narrow NOPASSWD sudoers | `5927cec` (drop-in + bootstrap amend) |
| D-10 | iam-deploy idempotent | `988b299` |
| D-11 | Static file symlink swap atomic | `988b299` |
| D-12 | Node service reload/restart | `988b299` |
| D-13 | No Slack/email notifications | implemented by absence |

### Phase 04 (`m2/phase-04`)

| D-XX | Topic | Commit |
|------|-------|--------|
| D-01 | Rationale (server-side) | `4427b52` documents |
| D-02 | `POST /api/contact` on Express app | `4427b52` |
| D-03 | Zod schema | `4427b52` |
| D-04 | 5/10min rate limit | `4427b52` |
| D-05 | Honeypot silent 200 | `4427b52` |
| D-06 | Origin allowlist (reused) | `4427b52` |
| D-07 | Server-to-server fetch | `4427b52` |
| D-08 | `{ok:true}` / `{ok:false, reason:'hubspot_unavailable'}` | `4427b52` |
| D-09 | Portal + GUID off client | `4427b52` |
| D-10 | Backend shapes fields array | `4427b52` |
| D-11 | Mailto fallback preserved | `4427b52` |
| **D-12** | **page_source + language fields** | **NOT IMPLEMENTED** — deferred until IAM dev confirms custom properties (HANDOFF §2) |
| **D-13** | **Same (fallback path)** | **NOT IMPLEMENTED** — same gate |
| **D-14** | **End-to-end QA pass** | **HUMAN action** — HANDOFF §3 |
| **D-15** | **Network-failure smoke on prod** | **HUMAN action** — HANDOFF §4 |

### Phase 05 (`m2/phase-05`)

| D-XX | Topic | Commit |
|------|-------|--------|
| D-01, D-02 | Create repos | **HUMAN, CUTOVER §1** |
| D-03, D-04 | History squash | `3262eb7` (tool) — `prepare-clean-repo.sh` — executes at CUTOVER §3 |
| D-05 | oopuo-ship identity | `3262eb7` (env-var contract) |
| D-06 | File exclusions | `3262eb7` (exclude list) |
| D-07 | Testimonials placeholder | `6ed3602` |
| D-08 | Video placeholder | `6ed3602` |
| D-09 | Contact privacy notice comment | `6ed3602` |
| D-10 | HubSpot placeholder comment | `6ed3602` (verified empty — no-op) |
| D-11 | TODO/FIXME/HACK sweep | `6ed3602` (confirmed clean) |
| D-12 | Branch protection | **HUMAN, CUTOVER §6** |
| D-13 | gitleaks CI | `3262eb7` |
| D-14 | `.gitignore` | `3262eb7` |
| D-15 | LICENSE | `3262eb7` (placeholder) |
| D-16 | README | `3262eb7` |
| D-17, D-18, D-19 | Cutover procedure | `3159eaf` (runbook) — HUMAN executes |

**NOT IMPLEMENTED count:** 2 in Phase 04 (D-12, D-13 custom properties — deferred until IAM dev confirms HubSpot form fields). All other "NOT IMPLEMENTED" rows are human/cutover actions by design, not oversights.

---

## Smoke test results

Ran at end of Phase 04 against branch `m2/phase-04` (still green on `m2/phase-05` — no code path touched).

**Chat suite** (`api/test/smoke.test.js` against `api/test/mock-openrouter.js`): 5/5 pass.
```
PASS: (a) allowed origin returns 200 with streamed content
PASS: (a) mock received server-side KB prepend (D-09)
PASS: (b) disallowed origin returns 403
PASS: (c) oversized (>32KB) body returns 413
PASS: (d) flood (12 requests) yields 429 in last two responses
=== SUMMARY === 5/5 passed
```

**Contact suite** (`api/test/contact.smoke.test.js` against `api/test/mock-hubspot.js`): 7/7 pass.
```
PASS: (a) valid submission returns 200 {ok:true}
PASS: (a) mock received correct v3 path
PASS: (a) mock received fields array with firstname+email
PASS: (b) disallowed origin returns 403
PASS: (c) missing required field returns 400
PASS: (d) honeypot trip returns silent 200 (mock not called)
PASS: (e) flood yields 429 once limit is exceeded
=== CONTACT SUMMARY === 7/7 passed
```

**What was mocked:**
- OpenRouter upstream (via `OPENROUTER_URL=http://127.0.0.1:<port>`)
- HubSpot Forms v3 (via `HUBSPOT_FORMS_API_URL=http://127.0.0.1:<port>`)

**What was NOT tested (deferred to human):**
- Real OpenRouter streaming against live account
- Real HubSpot form submissions
- VPS-side `bootstrap.sh` / `iam-deploy.sh` execution (static `bash -n` only)
- Cloudflare edge behavior
- GitHub Actions workflow live run

---

## Known risks + ambiguities

1. **Phase 01 Wave 1 parallel-executor race left a non-linear commit history on `m2/phase-01`.** Content is correct (all acceptance criteria + 5/5 smoke), but the Plan 02 Task 2 work landed in a single atomic replay commit `3893116` instead of two clean commits. Reviewer should confirm the diff matches intent, not just linearity.

2. **`gh pr create` + `git push` blocked by PAT scope.** `workflow` scope needed for `.github/workflows/*` pushes; `pull_requests:write` needed for `gh pr create`. Neither is in the active PAT. Phases 03–05 are committed locally but not on origin.

3. **D-01 credential rotation pending.** `HISTORY-SCAN.md` confirms a `sk-or-` literal and `.env.docker` passwords leaked into git history. Nothing will be safe until the IAM dev rotates and retires the exposed keys. Worker deliberately did not rotate.

4. **D-02 history rewrite NOT executed.** Per GUARDRAILS, `git filter-repo` requires explicit human approval. Phase 05 cutover supersedes this concern (new repo starts with a squashed single commit) — but the old repo's history remains dirty until archival + deletion.

5. **Phase 04 D-12/D-13 (page_source + language custom properties) is "NOT IMPLEMENTED" by design.** Deploying the 2-line extension without first confirming the custom properties exist on the HubSpot form will break submissions. HANDOFF §2 has the gated procedure.

6. **`bootstrap.sh` installs shellcheck but is itself not shellcheck-validated** in this run (shellcheck not available in the worker env). `bash -n` only. Recommend running `shellcheck bootstrap.sh tools/iam-deploy.sh tools/prepare-clean-repo.sh` on the VPS before first invocation.

7. **`prepare-clean-repo.sh` has not been dry-run.** Static syntax check passes; actual behavior against a fresh target will be exercised only during cutover. Reviewer may want to run it locally against `/tmp/dry-run-target/` with dummy identity env vars — the script fails fast on placeholder identity, so invoke with real values BUT do not push the resulting clean tree anywhere.

8. **No UAT on the Cloudflare or GitHub Actions paths.** Both are documented in runbooks; neither has a green-light stamp. First prod deploy from the new repo IS the smoke test — that's why CUTOVER Gate D exists (stop if staging doesn't deploy green).

---

## Cutover order — hard sequence with gates

```
┌─────────────────────────────────────────────────────────────────┐
│ PRE-CUTOVER (work must already be done)                         │
├─────────────────────────────────────────────────────────────────┤
│ 1. Reviewer merges m2/phase-01..05 to main                      │
│ 2. Prod live on old repo (clubeedg-ship-it/iam-website)         │
│ 3. IAM dev rotated OpenRouter key per HISTORY-SCAN.md           │
│ 4. Phase 02 bootstrap ran on VPS; certs issued; services live   │
│ 5. Phase 04 HubSpot env vars set; QA pass green                 │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼  Gate A — old-repo prod green end-to-end
┌─────────────────────────────────────────────────────────────────┐
│ CUTOVER                                                          │
├─────────────────────────────────────────────────────────────────┤
│ 1. Create oopuo-ship account + two repos       (HUMAN)          │
│ 2. Resolve LICENSE placeholder                  (HUMAN)          │
│ 3. Run tools/prepare-clean-repo.sh              (HUMAN, local)   │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼  Gate B — clean tree passes all sanity greps
┌─────────────────────────────────────────────────────────────────┐
│ 4. Push clean state to oopuo-ship/iam-website   (HUMAN)          │
│ 5. Mirror internal tree                         (HUMAN)          │
│ 6. Branch protection + environments + secrets   (HUMAN)          │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼  Gate C — new repo configured + Actions visible
┌─────────────────────────────────────────────────────────────────┐
│ 7. Staging deploy smoke from new repo           (HUMAN)          │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼  Gate D — staging green from new repo (LAST CHANCE TO ABORT)
┌─────────────────────────────────────────────────────────────────┐
│ 8. Prod deploy from new repo                     (HUMAN, Actions)│
└─────────────────────────────────────────────────────────────────┘
         │
         ▼  Gate E — prod green, chat + contact live-verified
┌─────────────────────────────────────────────────────────────────┐
│ 9.a Archive old repo — SAME DAY                  (HUMAN)          │
│ 9.b Delete old repo — +30 DAYS                    (HUMAN)          │
└─────────────────────────────────────────────────────────────────┘
```

**Any gate failure → rollback per CUTOVER §10.** Option 1 (roll the `current` symlink back on the VPS) is always preferred over flipping the remote back.

---

*Brief generated at the close of the M2 autonomous build, 2026-04-21.*
*Next: reviewer agent audits each branch; OOPUO sysadmin executes cutover; Phase 05 is the last build-side phase of M2.*
