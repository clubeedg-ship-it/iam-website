# M2-01 History Scan — Secret Exposure Report

**Generated:** 2026-04-21
**Branch:** `m2/phase-01` (worktree)
**Decisions:** D-01 (credential rotation), D-02 (history-scrub gate)
**Status:** REPORT ONLY — **no history rewrite performed**, per GUARDRAILS.md.

This file records the output of four scans run against the full repo history. Any destructive follow-up (e.g. `git filter-repo`) is a **HUMAN ACTION** and MUST be explicitly authorized by the IAM dev before execution.

---

## Commits touching `.env` / `.env.docker`

Command: `git log --all --oneline -- .env .env.docker`

```
b5e61c4 Security fixes: CSP header, gitignore .env.docker, Ghost mail config, nginx rate limit
f33ea1f Add Google Tag Manager (GTM-KPX78C22) to all pages
90558f9 Security fixes: CSP header, gitignore .env.docker, Ghost mail config, nginx rate limit
99dfb4e Add Google Tag Manager (GTM-KPX78C22) to all pages
```

Four commits touch `.env.docker`. Pairs `(f33ea1f, 99dfb4e)` and `(b5e61c4, 90558f9)` appear to be the same change set reachable from two different tip branches (likely a force-push/rebase remnant) — this is relevant because `git filter-repo`, if chosen, must cover **all** reachable refs, not just the current branch tip.

### Patch findings (from `git log --all -p -- .env .env.docker | head -500`)

`.env.docker` was **added in `f33ea1f` / `99dfb4e`** containing two credential-shaped values:

- `GHOST_DB_PASSWORD=<REDACTED-BASE64-44CHAR>`
- `MYSQL_ROOT_PASSWORD=<REDACTED-BASE64-44CHAR>`

`.env.docker` was **deleted in `b5e61c4` / `90558f9`**, but the blob remains reachable in history and both values are fully disclosed in the patch. The current working tree no longer contains `.env.docker` (already in `.gitignore`). **Per D-01 both values must be treated as leaked and rotated.**

No `.env` (without `.docker` suffix) additions were found. `api/.env` has never been committed.

Truncation note: `| head -500` was applied; the above is the full relevant content (patch is well under 500 lines).

---

## Commits referencing OpenRouter key patterns

Command: `git log --all --oneline -S OPENROUTER_API_KEY`

```
8224c4b feat: production-ready chatbot setup, remove all dev artifacts
54c1dd0 refactor: replace Docker with pure Node.js static server
30ee8b2 refactor: strip Ghost CMS, static shell with secure chat proxy
7699a60 fix: secure chatbot proxy (API key server-side), use Qwen 3.5, port 3860
b1e8b82 feat: add AI support chatbot widget with Qwen 3.5 via OpenRouter
98d9d52 fix: secure chatbot proxy (API key server-side), use Qwen 3.5, port 3860
c387ad7 feat: add AI support chatbot widget with Qwen 3.5 via OpenRouter
```

These commits add/remove the **symbol name** `OPENROUTER_API_KEY` (e.g. in `process.env.OPENROUTER_API_KEY` references in `api/chat-proxy.js`). The symbol itself is not a secret. The scan does not by itself prove a live key was committed.

Command: `git log --all --oneline -S 'sk-or-'`

```
8224c4b feat: production-ready chatbot setup, remove all dev artifacts
```

One commit surfaces the `sk-or-` prefix (OpenRouter keys begin with `sk-or-v1-…`). The commit subject is "remove all dev artifacts", suggesting a scrub, but an `-S` hit on either an add or a delete still means the literal string is reachable in history via that blob. **This is sufficient grounds under D-01 to treat the current OpenRouter key as exposed and rotate it.** Further inspection (and reproduction of the literal string in any artifact) is deliberately avoided per GUARDRAILS — echoing secrets to verify them is prohibited.

---

## Recommendation

**HUMAN APPROVAL REQUIRED before any history rewrite.**

Two independent findings (Ghost/MySQL DB creds in `.env.docker` blobs, and `sk-or-` literal reachable via commit `8224c4b`) satisfy the D-02 precondition "additions exist in history". The worker MUST NOT run `git filter-repo` autonomously; GUARDRAILS.md prohibits history rewrites without explicit approval for a specific commit range.

For the human reviewer to consider after credential rotation (D-01) is complete:

```bash
# REVIEW ONLY — do not run until D-01 rotations are confirmed complete.
# Back up the repo (or run in a fresh clone) before attempting this.
git filter-repo \
  --invert-paths \
  --path .env \
  --path .env.docker
```

Additional considerations for the human:

- `git filter-repo` rewrites **all** commit SHAs on touched branches. The M2 Phase 05 plan is to migrate to a fresh repo anyway — the pragmatic option is often to skip the rewrite on the current repo and start clean in the new one.
- If the rewrite is performed in place, all open PRs, forks, and clones must be coordinated; mirrors and backups should be purged separately.
- The `sk-or-` hit in commit `8224c4b` is **not** covered by a path-based filter-repo (it's not in `.env.docker`). Scrubbing that blob would require a content-based filter and is a separate decision.
- Once D-01 rotations are done, the exposed values are neutralized even if the blobs remain — this is the normal "rotate, don't scrub" stance. Scrubbing becomes a belt-and-suspenders nicety, not a security necessity.

Recommended path forward: **rotate now (D-01), defer/skip filter-repo per D-02 if Phase 05 repo migration is on track.** Decision belongs to the IAM dev.

---

## D-01 credential rotation checklist

All items below are **HUMAN ACTION** per GUARDRAILS.md ("No rotation of the OpenRouter key, HubSpot portal secrets, Cloudflare API tokens, or any live credential ... Rotation is a human action."). The worker session will not and cannot execute any of these.

- [ ] **HUMAN ACTION — Rotate OpenRouter API key.** Visit https://openrouter.ai/keys, revoke the current key, generate a replacement, update the value stored in the deployment secret store (Phase 02 will wire `systemd-creds` / VPS `.env` per D-04 + D-11). The current key must be considered compromised due to the `sk-or-` hit in history.
- [ ] **HUMAN ACTION — Rotate `GHOST_DB_PASSWORD`.** The value disclosed in `.env.docker` blobs `f33ea1f` / `99dfb4e` must be rotated at the database and the new value written only to the server-side `.env.docker` (or the replacement config introduced in Phase 02). Note: Ghost has been removed in a later commit (`30ee8b2 refactor: strip Ghost CMS`), so this credential may now be unused; confirm and either rotate or formally decommission.
- [ ] **HUMAN ACTION — Rotate `MYSQL_ROOT_PASSWORD`.** Same disclosure path as above. If the MySQL instance associated with the old Docker stack is still live, rotate; if the stack was torn down with the Ghost removal, confirm the DB is destroyed so the leaked value is moot.
- [ ] **HUMAN ACTION — Confirm no other credentials were in the removed `.env.docker`.** The patch shows only the two above, but any auxiliary services (SMTP, backups, etc.) referenced in contemporaneous configs should be spot-checked.
- [ ] **HUMAN ACTION — Update server-side `.env` files in Phase 02.** Once new values are generated, Phase 02's `bootstrap.sh` and VPS provisioning plan consume them. Do not email or paste rotated values; transfer via `systemd-creds`, `op inject`, or equivalent.
- [ ] **HUMAN ACTION — Decide on `git filter-repo` per D-02.** See Recommendation above. Default recommendation: skip, rely on rotation + Phase 05 repo migration.

---

## Evidence of non-destructive execution

- No `filter-repo` was invoked by this plan. `git reflog --all | head -20` should show only the three M2-01 plan commits plus whatever preceded them; no `filter-repo` entries.
- This file is the only artifact committed by Task 3.
- Verification per plan: `git diff HEAD~1 --stat` after Task 3's commit shows only `HISTORY-SCAN.md`.
