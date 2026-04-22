---
phase: M2-01-security-remediation
plan: 04
type: execute
wave: 2
depends_on: [02]
files_modified:
  - api/token-budget.js
  - api/chat-proxy.js
autonomous: true
decisions: [D-10, D-12]
success_criteria_addressed: [4]
requirements: [M2-01-SC-4]
must_haves:
  truths:
    - "A token counter persists across proxy restarts to a flat JSON file"
    - "When the monthly budget is exceeded, /api/chat returns a friendly error (HTTP 429 with error:'budget_exhausted')"
    - "The counter resets at the start of each new calendar month"
    - "No database is introduced (flat JSON only, per D-12)"
  artifacts:
    - path: api/token-budget.js
      provides: "loadBudget(), recordUsage(tokens), isExhausted() helpers"
      contains: "module.exports"
    - path: api/chat-proxy.js
      provides: "budget check middleware on /api/chat and usage recording after upstream completion"
  key_links:
    - from: api/chat-proxy.js
      to: api/token-budget.js
      via: "require('./token-budget') and middleware call before forwarding"
      pattern: "require\\(['\"]\\./token-budget['\"]\\)"
    - from: api/token-budget.js
      to: TOKEN_BUDGET_PATH env (default ./var/token-budget.json locally, /var/lib/iam-api/token-budget.json prod)
      via: "fs.readFileSync/writeFileSync on configurable path"
      pattern: "TOKEN_BUDGET_PATH"
---

<objective>
Add a monthly token-budget counter persisted as flat JSON, consulted before forwarding requests and updated after upstream responses. Prevents runaway drain even if rate limits are bypassed.

Purpose: closes the remaining gap in SC-4 (input validation + abuse protection). Complements rate limit (short-term) with budget (long-term).
Output: `api/token-budget.js` module + integration in `api/chat-proxy.js`.
</objective>

<context>
@.planning/M2/GUARDRAILS.md
@.planning/M2/phases/01-security-remediation/CONTEXT.md
@.planning/M2/phases/01-security-remediation/03-PLAN.md
@api/chat-proxy.js
</context>

<interfaces>
```js
// api/token-budget.js
module.exports = {
  isExhausted(): boolean,
  recordUsage(tokens: number): void, // persists to disk
  currentPeriodKey(): string,        // 'YYYY-MM' calendar month
  _stateFile(): string,              // for tests
};
```

Env:
- `TOKEN_BUDGET_PATH` — absolute path; default `./var/token-budget.json` in dev, `/var/lib/iam-api/token-budget.json` in prod
- `TOKEN_BUDGET_MONTHLY` — integer token cap; default `2000000` (2M tokens/month)

Reset policy: **calendar month** (agent-discretion item; chosen for simpler reasoning and predictable reset — see CONTEXT "agent discretion"). When `currentPeriodKey()` differs from persisted key, counter resets to 0.

Accounting source: OpenRouter streams include `usage: { total_tokens }` in final SSE chunk. Parse final event and record. If parsing fails (network error mid-stream), skip recording rather than double-count.
</interfaces>

<tasks>

<task type="auto">
  <name>Task 1: Create api/token-budget.js module (D-10, D-12)</name>
  <files>api/token-budget.js</files>
  <read_first>
    - .planning/M2/phases/01-security-remediation/CONTEXT.md (D-10, D-12)
    - api/chat-proxy.js (to know the pino logger convention)
  </read_first>
  <action>
    Create `api/token-budget.js`:

    ```js
    // M2-01 D-10/D-12: monthly token budget, persisted as flat JSON.
    const fs = require('fs');
    const path = require('path');

    const DEFAULT_PATH = process.env.NODE_ENV === 'production'
      ? '/var/lib/iam-api/token-budget.json'
      : path.resolve(__dirname, '..', 'var', 'token-budget.json');

    const FILE = process.env.TOKEN_BUDGET_PATH || DEFAULT_PATH;
    const CAP = Number(process.env.TOKEN_BUDGET_MONTHLY || 2_000_000);

    function currentPeriodKey() {
      const d = new Date();
      return `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, '0')}`;
    }

    function ensureDir() {
      const dir = path.dirname(FILE);
      try { fs.mkdirSync(dir, { recursive: true }); } catch { /* ignore */ }
    }

    function readState() {
      try {
        const raw = fs.readFileSync(FILE, 'utf8');
        const s = JSON.parse(raw);
        if (s.period !== currentPeriodKey()) return { period: currentPeriodKey(), tokens: 0 };
        return s;
      } catch {
        return { period: currentPeriodKey(), tokens: 0 };
      }
    }

    function writeState(s) {
      ensureDir();
      fs.writeFileSync(FILE, JSON.stringify(s), 'utf8');
    }

    function isExhausted() {
      return readState().tokens >= CAP;
    }

    function recordUsage(tokens) {
      if (!Number.isFinite(tokens) || tokens <= 0) return;
      const s = readState();
      s.tokens += Math.floor(tokens);
      writeState(s);
    }

    module.exports = {
      isExhausted,
      recordUsage,
      currentPeriodKey,
      _stateFile: () => FILE,
      _cap: () => CAP,
    };
    ```

    Also add `var/` to the repo-level `.gitignore` (local dev state file) — append a single line `var/` under the existing D-03 block.

    Commit: `feat(M2-01): add monthly token budget module per D-10/D-12`
  </action>
  <verify>
    <automated>node -e "const b=require('./api/token-budget'); b.recordUsage(1); if(!b.currentPeriodKey().match(/^\\d{4}-\\d{2}$/)) process.exit(1); if(typeof b.isExhausted()!=='boolean') process.exit(1)" && grep -q "^var/$" .gitignore</automated>
  </verify>
  <acceptance_criteria>
    - `api/token-budget.js` exists
    - Exports `isExhausted`, `recordUsage`, `currentPeriodKey`
    - `currentPeriodKey()` returns `YYYY-MM` string
    - After calling `recordUsage(100)`, reading the state file shows `tokens >= 100`
    - `.gitignore` contains `var/`
    - No database dependency introduced (`grep -q "mongoose\|pg\|sqlite\|redis" api/package.json` returns empty — D-12)
  </acceptance_criteria>
  <done>Budget module works, persists to disk, resets on month boundary, no DB added.</done>
</task>

<task type="auto">
  <name>Task 2: Integrate budget check and usage accounting into api/chat-proxy.js (D-10)</name>
  <files>api/chat-proxy.js</files>
  <read_first>
    - api/chat-proxy.js (from Plan 03)
    - api/token-budget.js (just created)
  </read_first>
  <action>
    Modify `api/chat-proxy.js`:

    1. Add `const budget = require('./token-budget');` near the other requires.
    2. Add a middleware BEFORE the zod validation step in `app.post('/api/chat', ...)`:
       ```js
       if (budget.isExhausted()) {
         log.warn({ period: budget.currentPeriodKey() }, 'budget_exhausted');
         return res.status(429).json({
           error: 'budget_exhausted',
           message: 'Monthly chat budget reached. Please contact klantcontact@interactivemove.nl or retry next month.',
         });
       }
       ```
       Place this check AFTER the 503 api_key_missing check and BEFORE `BodySchema.safeParse`.
    3. In the upstream streaming handler, tap the stream to capture `usage.total_tokens`. Because we pass-through pipe the response, sniff the bytes with a PassThrough:
       ```js
       const { PassThrough } = require('stream');
       // ... inside the https.request callback, replace `up.pipe(res)` with:
       const tap = new PassThrough();
       let buf = '';
       tap.on('data', (chunk) => {
         buf += chunk.toString('utf8');
         // Keep only the tail — usage lands at end
         if (buf.length > 16_384) buf = buf.slice(-16_384);
       });
       tap.on('end', () => {
         try {
           // OpenRouter SSE: last data event contains the usage. Find the last "total_tokens" occurrence.
           const match = buf.match(/"total_tokens"\s*:\s*(\d+)/g);
           if (match && match.length) {
             const last = match[match.length - 1];
             const n = Number(last.match(/(\d+)/)[1]);
             if (n > 0) budget.recordUsage(n);
           }
         } catch (e) {
           log.warn({ err: e.message }, 'usage_parse_failed');
         }
       });
       up.pipe(tap).pipe(res);
       ```
    4. Keep the existing error path intact.
    5. Commit: `feat(M2-01): wire token budget check and usage tap into chat proxy per D-10`
  </action>
  <verify>
    <automated>grep -q "require('./token-budget')" api/chat-proxy.js && grep -q "budget.isExhausted" api/chat-proxy.js && grep -q "budget.recordUsage" api/chat-proxy.js && grep -q "budget_exhausted" api/chat-proxy.js && node -e "require('./api/chat-proxy')"</automated>
  </verify>
  <acceptance_criteria>
    - `api/chat-proxy.js` contains `require('./token-budget')`
    - `api/chat-proxy.js` contains `budget.isExhausted()` check returning 429 with `error: 'budget_exhausted'`
    - `api/chat-proxy.js` contains `budget.recordUsage(` in the tap stream's end handler
    - `api/chat-proxy.js` references `total_tokens` for parsing
    - Module still loads: `node -e "require('./api/chat-proxy')"` exits 0
    - Smoke test (Plan 05) will cover behavior end-to-end
  </acceptance_criteria>
  <done>Budget consulted on every request and updated after each streamed response; friendly 429 on exhaustion.</done>
</task>

</tasks>

<verification>
- `node -e "const b=require('./api/token-budget'); b.recordUsage(5); console.log(JSON.stringify(require('fs').readFileSync(b._stateFile(),'utf8')))"` shows `tokens` >=5 and current `period`
- Setting `TOKEN_BUDGET_MONTHLY=1` and making a request against a mock upstream returns 429 budget_exhausted on the second request (verified in Plan 05)
</verification>

<success_criteria>
Fills the long-horizon abuse-protection gap of SC-4. Works alongside rate limit (minute granularity) + budget (month granularity).
</success_criteria>

<output>
Contributes to phase SUMMARY.md.
</output>
