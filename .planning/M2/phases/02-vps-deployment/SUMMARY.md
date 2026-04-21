# M2 Phase 02: VPS Deployment — Summary

**Branch:** `m2/phase-02` (branched from `m2/phase-01`)
**Completed:** 2026-04-21
**Commits:** 8 code/config + 1 docs
**Status:** Code-complete; not executed on a real VPS (by design — GUARDRAILS prohibit running bootstrap against prod infra from this worker).

## What shipped

All five phase success criteria from ROADMAP.md are addressed; two have "executes on VPS" completion outside this run's scope.

| SC | Description | Status |
|----|-------------|--------|
| 1 | `bootstrap.sh` installs deps + configs + brings site online in one run on fresh Ubuntu | Script written; executes on VPS (HUMAN) |
| 2 | `iam-api` under systemd (auto-restart, journald, resource limits) | Unit files delivered; enabled on first bootstrap run |
| 3 | Both domains over TLS with HSTS + CSP + security headers | Nginx vhosts + Certbot command delivered; TLS issuance happens on VPS |
| 4 | Cloudflare runbook delivered to IAM dev | `cloudflare-runbook.md` complete |
| 5 | Staging and prod separation (users, ports, env files, units) | Independent staging unit + vhost + env template |

## Decisions honored (D-01 … D-20)

- **Bootstrap (D-01..D-04):** `bootstrap.sh` idempotent, single-file, root-required, env-var-or-prompt input, deploy/iam users, `useradd --system`, `chmod 600` + owner `iam` on env files, non-interactive mode via `BOOTSTRAP_NONINTERACTIVE=1`.
- **systemd (D-05..D-08):** `iam-api.service` + `iam-api-staging.service`, `EnvironmentFile=`, `Restart=on-failure`, 3-strike-60s throttle, `MemoryMax=256M`, `CPUQuota=50%`, `TasksMax=50`, journald logging (no log files), runs as `iam` user, `After=network-online.target`. PM2 replaced.
- **Nginx (D-09..D-15):** separate vhost files for each domain, HTTP→HTTPS redirect, `/api/chat` proxy to `localhost:3860` (prod) / `3861` (staging), `/api/contact` reserved for Phase 04, `limit_req_zone` at `10r/m` with burst 5 nodelay (`chat` prod / `chat_staging`), strict CSP, HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, `Cache-Control: public, max-age=31536000, immutable` for `/media` and `/js/*.min.js`, `no-cache` for HTML.
- **TLS + Cloudflare (D-16..D-18):** Certbot with Nginx plugin, systemd timer for renewal; runbook delivered with "Full (strict)" instruction and Rate Limit Rule for `/api/chat`.
- **Staging split (D-19, D-20):** separate user, port, systemd unit, env template, release root, state dir, and a distinct staging OpenRouter key (`REPLACE_ME_OPENROUTER_STAGING_KEY`) per D-20.

## Files delivered

**In repo (executable code/config):**
- `bootstrap.sh` — 275 lines, `bash -n` clean, `shellcheck` deferred to VPS install
- `tools/iam-deploy.sh` — atomic release/rollback template
- `tools/env-template`, `tools/env-staging-template`
- `config/systemd/iam-api.service`, `config/systemd/iam-api-staging.service`
- `config/nginx/interactivemove.nl.conf`, `config/nginx/iam.abbamarkt.nl.conf`

**In planning (force-added for reviewer audit):**
- `.planning/M2/phases/02-vps-deployment/cloudflare-runbook.md`
- `.planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md`
- 5 × `NN-PLAN.md`
- `SUMMARY.md` (this file)

## Commits (phase branch only)

```
47d6b55 docs(M2-02): cloudflare runbook and handoff checklist per D-17/D-18
988b299 feat(M2-02): tools/iam-deploy.sh atomic release script per D-06,D-07,D-08,D-10
6516516 feat(M2-02): bootstrap.sh full idempotent installer per D-01..D-04,D-16
471e044 feat(M2-02): add iam.abbamarkt.nl nginx staging vhost per D-19
228375d feat(M2-02): add interactivemove.nl nginx vhost per D-09..D-15
b5dc841 feat(M2-02): add env templates for prod and staging per D-03/D-20
cbbcf9f feat(M2-02): add iam-api-staging.service unit per D-19/D-20
4a7e199 feat(M2-02): add iam-api.service unit per D-05..D-08
```

## Verification (static only — no VPS)

- `bash -n bootstrap.sh` → OK
- `bash -n tools/iam-deploy.sh` → OK
- `bash tools/iam-deploy.sh` (no args) → exits 2 with usage message
- 20+ grep acceptance criteria across systemd units, Nginx vhosts, env templates, bootstrap.sh, iam-deploy.sh → all pass
- Cross-check loop: every `REPLACE_ME_*` token in repo code is enumerated in HANDOFF-CHECKLIST.md → clean (no MISSING entries)
- No real-looking secrets anywhere: `grep -rE 'sk-or-[A-Za-z0-9]{16,}'` returns empty across all phase-02 files

## Placeholders & IAM dev actions

See HANDOFF-CHECKLIST.md for the full table. Summary of blocking items for the IAM dev before first deploy:

1. Provide `LETSENCRYPT_EMAIL`, `OPENROUTER_API_KEY`, `OPENROUTER_API_KEY_STAGING` (interactive prompt or env vars when running `sudo bash bootstrap.sh` on the VPS).
2. Rotate OpenRouter key(s) per Phase 01's `HISTORY-SCAN.md`.
3. Set `REPO_URL` in `bootstrap.sh` (or as env var) once the target repo for Phase 03/05 is confirmed.
4. Fill `REPLACE_ME_VPS_IP` in `cloudflare-runbook.md` when handing off.
5. Leave the three HubSpot `REPLACE_ME_HUBSPOT_*` placeholders alone for now — Phase 04 handles them.

## STOP-AND-ASK triggers hit

1. Guardrail-ambiguous moment (resolved under the override): Plan 03 executor (gsd-executor subagent) hit a stream-idle timeout after 484s with zero progress. The orchestrator (me) took over and wrote `bootstrap.sh` directly rather than retry a subagent and risk another timeout + partial-state mess. All static acceptance-criterion greps pass; the file is committed as one coherent feat commit.

## Guardrail Overrides

Session-wide override in effect (user-authorized):
- **STOP-AND-ASK #1 (missing CONTEXT input)** replaced with PLACEHOLDER PROTOCOL.
- **"Stop after each phase"** replaced with chained-phase protocol.
- **"Open PR at phase boundary"** deferred — a separate reviewer agent will open PRs in a batch pass.

Rules still in force and honored: no autonomous credential rotation, no `git filter-repo`, no `sudo`/writes under `/etc|/usr|/var` on any real machine (only inside the repo here), no live third-party API calls, no direct push to `main`, no force push to shared branches.

---

*Phase: M2-02-vps-deployment*
*Chained autonomous run: 2026-04-21*
*Next: Phase 03 (CI/CD) branches from this branch.*
