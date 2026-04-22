# M2 Phase 01: Security Remediation — Summary

**Branch:** `m2/phase-01`
**Completed:** 2026-04-21
**Commits:** 10 (see below)
**Status:** Ready for reviewer-session audit

## What shipped

All six phase success criteria from `.planning/M2/ROADMAP.md` are addressed:

| SC | Description | How closed |
|----|-------------|------------|
| 1 | No secrets in `git log -p` output | `HISTORY-SCAN.md` produced; rotation checklist in same doc (D-01 is human action, not executed). `git filter-repo` deliberately deferred per GUARDRAILS — the Phase 05 repo migration is the cleaner seam. |
| 2 | `CLAUDE.md` not tracked | `git ls-files CLAUDE.md` returns empty; `.gitignore` covers `CLAUDE.md`, `.claude/`, `.kiro/`. |
| 3 | `/api/chat` rejects origins other than `interactivemove.nl` / `iam.abbamarkt.nl` | Express CORS allowlist + explicit 403 middleware. Verified by smoke test (b). |
| 4 | Per-IP rate limit + input validation | `express-rate-limit` (10/min, 429) + zod (32KB body, 4000-char msg, 20-turn history, 400/413 on breach). Verified by smoke tests (c) and (d). |
| 5 | System prompt + KB server-side only | `api/knowledge-base.js` + `api/system-prompt.js` created; `js/iam-knowledge-base.js` deleted; widget payload shrunk to user-authored turns only; `<script src=…iam-knowledge-base.js>` removed from all 19 HTML pages. |
| 6 | Pre-commit secret scanner blocks reintroduction | `.githooks/pre-commit` (executable, runs `gitleaks protect --staged --redact --verbose`) + `.githooks/README.md` with activation command. Global `core.hooksPath` wiring deferred to Phase 02 `bootstrap.sh` per D-04. |

## Decisions honored

| ID | Decision | Status |
|----|----------|--------|
| D-01 | Rotate OpenRouter / DB creds that ever hit history | **HUMAN action** — documented in `HISTORY-SCAN.md`, NOT executed (per GUARDRAILS) |
| D-02 | `git filter-repo` if history shows secret additions | **REPORT ONLY** — scan findings recorded; actual rewrite deferred (GUARDRAILS: no history rewrite without explicit human approval) |
| D-03 | Untrack `CLAUDE.md`, `.gitignore` entry | Done |
| D-04 | gitleaks pre-commit hook via `.githooks/` | Hook files in repo; `core.hooksPath` wiring is Phase 02's bootstrap.sh |
| D-05 | Minimal Express app (express + express-rate-limit + zod) | Done; `api/chat-proxy.js` fully rewritten |
| D-06 | CORS allowlist from env, 403 on miss | Done; env var `CHAT_ALLOWED_ORIGINS`, default `https://interactivemove.nl,https://iam.abbamarkt.nl` |
| D-07 | 10 req/min per IP, 429 | Done; env-configurable via `CHAT_RATE_LIMIT_MAX` / `CHAT_RATE_LIMIT_WINDOW_MS` |
| D-08 | 32KB body, 4000-char msg, 20-turn history | Done; zod validation + body-parser cap; 413/400 responses |
| D-09 | Move KB + system prompt server-side | Done across Plan 02 (create) and Plan 03 (prepend on every request) |
| D-10 | Monthly token budget counter to flat JSON | Done; calendar-month reset; env-configurable `TOKEN_BUDGET_PATH` (default `./var/token-budget.json` dev, `/var/lib/iam-api/token-budget.json` prod); friendly 429 on exhaustion |
| D-11 | pino → stdout | Done (no `console.log` in request handlers) |
| D-12 | No DB — flat JSON + in-memory | Done; no DB dependencies added |
| D-13 | Smoke tests for 200/403/413/429 | Done; 5/5 tests pass against a local OpenRouter mock |

## Mid-flight amendment

Before execution, `03-PLAN.md` was amended (no new D-XX) to introduce `const UPSTREAM_URL = new URL(process.env.OPENROUTER_URL || 'https://openrouter.ai')` and protocol-aware transport, replacing the hardcoded `hostname: 'openrouter.ai'`. Rationale: testability affordance for D-13 so smoke tests exercise the proxy without ever touching live OpenRouter. Prod behavior unchanged when env var is unset.

## Commits

```
b15302a test(M2-01): add chat-proxy smoke tests per D-13
555b1d5 test(M2-01): add local OpenRouter mock server per D-13
9394b34 feat(M2-01): wire token budget check and usage tap into chat proxy per D-10
1844af9 feat(M2-01): add monthly token budget module per D-10/D-12
0eaadc4 feat(M2-01): rewrite chat proxy as hardened Express app per D-05..D-11
3893116 refactor(M2-01): strip KB and system prompt from client per D-09
7bb0e38 docs(M2-01): record history scan and rotation checklist per D-01/D-02
55c7a27 feat(M2-01): extract KB and system prompt server-side per D-09
bd61eb1 feat(M2-01): add gitleaks pre-commit hook files per D-04
222cd37 chore(M2-01): untrack CLAUDE.md and ignore AI artifacts per D-03
```

## Verification evidence

**Smoke tests** (`npm --prefix api test` — runs against local mock on random port):
```
PASS: (a) allowed origin returns 200 with streamed content — status=200 bodyLen=179
PASS: (a) mock received server-side KB prepend (D-09) — receivedRequests=1
PASS: (b) disallowed origin returns 403 — status=403
PASS: (c) oversized (>32KB) body returns 413 — status=413
PASS: (d) flood (12 requests) yields 429 in last two responses — statuses=200,200,200,200,200,200,200,200,200,429,429,429
5/5 passed
```

**Grep checks (negative):**
- `grep -rn "Access-Control-Allow-Origin.*\*" api/` — empty
- `grep -rn "IAM_KNOWLEDGE_BASE" js/` — empty
- `grep -rn "iam-knowledge-base" --include="*.html" .` — empty
- `grep -rn "openrouter.ai" api/test/` — empty
- `git ls-files CLAUDE.md` — empty

**Grep checks (positive):**
- `api/chat-proxy.js` contains `require('express')`, `require('express-rate-limit')`, `require('./knowledge-base')`, `require('./system-prompt')`, `express.json({ limit: '32kb' })`, `z.array(MessageSchema).min(1).max(20)`, `.max(4000)`, `res.status(403)`, `res.status(413)`, `process.env.OPENROUTER_URL`.

## Deferred / unresolved items for reviewer attention

1. **D-01 credential rotation (human action).** `HISTORY-SCAN.md` records that `.env.docker` was committed in `f33ea1f` / `99dfb4e` (removed in `b5e61c4` / `90558f9`) with real-looking `GHOST_DB_PASSWORD` and `MYSQL_ROOT_PASSWORD` values; `sk-or-` prefix hit in `8224c4b`. These credentials must be rotated by whoever holds them. This phase deliberately did NOT rotate per GUARDRAILS.
2. **D-02 history rewrite (gated).** Scan is positive — history DOES contain secret additions. A future session with explicit human approval should run `git filter-repo` OR, more likely, the Phase 05 repo migration (fresh `oopuo-ship/iam-website` repo with squashed initial commit) will supersede the need.
3. **gitleaks `core.hooksPath` wiring.** Hook files are in `.githooks/` but the per-repo `core.hooksPath` is not set. `bootstrap.sh` in Phase 02 is the intended mechanism; contributors today must run `git config core.hooksPath .githooks` manually — noted in `.githooks/README.md`.
4. **Stray `core.hooksPath` in the worker's worktree.** During execution we observed `git config --get core.hooksPath` returning `/Users/ottogen/Projects/IAM/iam-website/.git/hooks` (the sibling worktree's internal hook dir). This is local environment state set outside the repo — not touched by this phase. Reviewer may want to clean it up.
5. **Wave 1 parallel-executor race.** The orchestrator initially ran Plan 01 and Plan 02 in parallel; they raced on `git add`/`git commit` and the recovery left Plan 02 Task 2 to be re-committed in a single atomic replay (`3893116`). Content is correct; audit trail has one more commit than a perfectly clean run would. Wave 2 switched to serial execution, no further races.

## Guardrail Overrides

None.

---

*Phase: M2-01-security-remediation*
*Orchestrator session: 2026-04-21*
*Executor agents: 5 (Plan 01, Plan 02, Plan 03, Plan 04, Plan 05)*
