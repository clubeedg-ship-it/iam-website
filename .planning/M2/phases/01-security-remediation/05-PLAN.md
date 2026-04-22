---
phase: M2-01-security-remediation
plan: 05
type: execute
wave: 3
depends_on: [03, 04]
files_modified:
  - api/test/smoke.test.js
  - api/test/mock-openrouter.js
  - api/test/README.md
  - api/package.json
autonomous: true
decisions: [D-13]
success_criteria_addressed: [3, 4]
requirements: [M2-01-SC-3, M2-01-SC-4]
must_haves:
  truths:
    - "A smoke test harness exists under api/test/ that exercises the hardened proxy without hitting live OpenRouter"
    - "Test case (a): a valid request from an allowed origin returns HTTP 200 with streamed SSE body"
    - "Test case (b): a request from a disallowed origin returns HTTP 403"
    - "Test case (c): a request body greater than 32KB returns HTTP 413"
    - "Test case (d): more than 10 requests/min from a single client return HTTP 429"
    - "The test harness uses a local HTTP stub for OpenRouter, selected via env var OPENROUTER_URL"
    - "No test path reaches openrouter.ai over the network"
  artifacts:
    - path: api/test/smoke.test.js
      provides: "four smoke tests (allowed, disallowed, oversized, flood)"
      contains: "OPENROUTER_URL"
    - path: api/test/mock-openrouter.js
      provides: "local http server mocking OpenRouter /api/v1/chat/completions with a canned SSE stream"
      contains: "data: "
    - path: api/test/README.md
      provides: "how to run tests locally and how the mock server works"
    - path: api/package.json
      provides: "test script wired to run the smoke suite"
      contains: "\"test\""
  key_links:
    - from: api/test/smoke.test.js
      to: api/chat-proxy.js
      via: "spawn proxy process with OPENROUTER_URL pointing at the mock, CHAT_ALLOWED_ORIGINS set, CHAT_PORT set"
      pattern: "OPENROUTER_URL"
    - from: api/test/smoke.test.js
      to: api/test/mock-openrouter.js
      via: "start mock http server on a free local port before spawning proxy"
      pattern: "mock-openrouter"
    - from: api/chat-proxy.js
      to: process.env.OPENROUTER_URL
      via: "use OPENROUTER_URL env override (fallback to https://openrouter.ai) so tests can redirect upstream"
      pattern: "OPENROUTER_URL"
---

<objective>
Create a self-contained smoke test harness under `api/test/` that proves the hardened proxy from Plan 03 and the budget module from Plan 04 enforce the four guarantees of success criteria 3 and 4 (origin lock, rate limit, size cap, validation) — without ever calling live OpenRouter.

Purpose: Give the Phase 03 CI pipeline and any future reviewer a deterministic, runnable check of the security boundaries. Satisfies D-13.

Output: `api/test/smoke.test.js`, `api/test/mock-openrouter.js`, `api/test/README.md`, `api/package.json` test script. Four test cases, all green against the local stub.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
@$HOME/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@.planning/M2/GUARDRAILS.md
@.planning/M2/ROADMAP.md
@.planning/M2/phases/01-security-remediation/CONTEXT.md
@api/chat-proxy.js
@api/package.json
</context>

<tasks>

<task type="auto">
  <name>Task 1: Build a local OpenRouter mock server</name>
  <files>api/test/mock-openrouter.js</files>
  <read_first>
    - api/chat-proxy.js (to know exactly what upstream shape the proxy forwards + how it consumes the SSE body)
    - api/test/ directory does not yet exist — create it
  </read_first>
  <action>
    Create a CommonJS module exporting `startMockOpenRouter(port)` that returns a promise resolving to `{ server, port, receivedRequests }`.

    Behavior:
    - Listens on `127.0.0.1` on the provided port (or 0 = OS-chosen, report back actual port).
    - Responds to `POST /api/v1/chat/completions` with:
      - HTTP 200
      - `Content-Type: text/event-stream`
      - Body: two SSE frames then `[DONE]`:
        `data: {"choices":[{"delta":{"content":"hello"}}]}\n\n`
        `data: {"choices":[{"delta":{"content":" world"}}]}\n\n`
        `data: [DONE]\n\n`
    - Captures each incoming request body into `receivedRequests[]` as `{ headers, body }` so the test can assert server-side prepend of system prompt + KB (per D-09).
    - Every other path returns 404.
    - Exports a `stop()` helper that closes the server cleanly.

    Use only Node stdlib `http` (no extra deps). Do NOT call openrouter.ai from this file.
  </action>
  <verify>
    <automated>node -e "const m=require('./api/test/mock-openrouter'); m.startMockOpenRouter(0).then(({port,stop})=>{console.log('ok',port);stop();})"</automated>
  </verify>
  <acceptance_criteria>
    - File `api/test/mock-openrouter.js` exists
    - `grep -q "startMockOpenRouter" api/test/mock-openrouter.js` succeeds
    - `grep -q "data: \[DONE\]" api/test/mock-openrouter.js` succeeds
    - `grep -q "openrouter.ai" api/test/mock-openrouter.js` returns NOTHING (mock must not reach live host)
    - Module exports `startMockOpenRouter` and `stop` (verified by `node -e "require('./api/test/mock-openrouter').startMockOpenRouter"` not being `undefined`)
  </acceptance_criteria>
  <done>Mock server starts, serves a canned SSE stream for `POST /api/v1/chat/completions`, records request bodies, and can be stopped from a test.</done>
</task>

<task type="auto">
  <name>Task 2: Write the four smoke tests and wire the npm script</name>
  <files>api/test/smoke.test.js, api/test/README.md, api/package.json</files>
  <read_first>
    - api/chat-proxy.js (confirm it honors `OPENROUTER_URL` env — if Plan 03 did not add this override, Plan 03 must be amended; flag to human per GUARDRAILS STOP-AND-ASK trigger 5)
    - api/test/mock-openrouter.js (built in Task 1)
    - api/package.json (to wire the test script without breaking existing fields)
  </read_first>
  <action>
    Create `api/test/smoke.test.js` as a single Node script (no test framework needed; plain asserts + process exit code) that:

    1. Starts the mock OpenRouter server on a free port (e.g. 4860).
    2. Spawns the proxy via `child_process.spawn('node', ['chat-proxy.js'], { cwd: 'api', env })` with env:
       - `CHAT_PORT=3861` (not 3860, to avoid colliding with any running dev instance)
       - `CHAT_ALLOWED_ORIGINS=https://interactivemove.nl,https://iam.abbamarkt.nl`
       - `OPENROUTER_URL=http://127.0.0.1:${mockPort}`
       - `OPENROUTER_API_KEY=test-key-not-real`
       - `CHAT_RATE_LIMIT_MAX=10`
       - `CHAT_RATE_LIMIT_WINDOW_MS=60000`
       - `TOKEN_BUDGET_PATH=/tmp/iam-test-budget.json` (wipe before test)
    3. Waits for the proxy to be listening (poll `GET /health` or a TCP connect to the port, up to 5s; fail fast if not).
    4. Runs the four cases using `fetch` (Node 18+):
       - (a) ALLOWED: `POST http://127.0.0.1:3861/api/chat` with header `Origin: https://interactivemove.nl`, body `{"messages":[{"role":"user","content":"hi"}]}`. Expect HTTP 200 and a body containing `hello world` (from the mock SSE). Assert the mock received a request whose body contains the IAM knowledge base sentinel string (e.g. `"Inter Active Move"` or `"IAM_KNOWLEDGE_BASE"` marker) — proves D-09 server-side prepend.
       - (b) DISALLOWED: same POST but `Origin: https://evil.example.com`. Expect HTTP 403.
       - (c) OVERSIZED: POST body > 32KB (e.g. a single message of 40000 chars) with allowed origin. Expect HTTP 413.
       - (d) FLOOD: 12 POSTs from the same allowed origin within the window. Expect at least one HTTP 429 in the last two responses.
    5. Kills the proxy process and stops the mock.
    6. Prints a PASS/FAIL summary and exits 0 on all green, 1 otherwise.

    Also create `api/test/README.md` with:
    - How to run: `cd api && npm test`
    - What the four cases prove, mapped to decisions D-06, D-07, D-08, D-09.
    - Reminder: the suite MUST NOT ever reach `openrouter.ai`. If it does, something is wrong with `OPENROUTER_URL` plumbing.

    Update `api/package.json`:
    - `scripts.test` → `"node test/smoke.test.js"`
    - Keep existing fields untouched.

    If during verification Task 2 reveals `api/chat-proxy.js` hardcodes `openrouter.ai` without an `OPENROUTER_URL` env override, STOP-AND-ASK per GUARDRAILS rule 5 (CONTEXT says D-13 "MUST NOT hit live OpenRouter"; the only clean way is an env override). Document the gap and halt; do not patch Plan 03 from this plan.
  </action>
  <verify>
    <automated>cd api && npm test</automated>
  </verify>
  <acceptance_criteria>
    - File `api/test/smoke.test.js` exists
    - File `api/test/README.md` exists
    - `grep -q "OPENROUTER_URL" api/test/smoke.test.js` succeeds
    - `grep -q "https://evil.example.com" api/test/smoke.test.js` succeeds (disallowed origin case present)
    - `grep -q "413" api/test/smoke.test.js` succeeds (oversized case asserts 413)
    - `grep -q "429" api/test/smoke.test.js` succeeds (flood case asserts 429)
    - `grep -q "openrouter.ai" api/test/smoke.test.js` returns NOTHING
    - `node -e "console.log(require('./api/package.json').scripts.test)"` prints `node test/smoke.test.js`
    - `cd api && npm test` exits 0 with all four cases reporting PASS
  </acceptance_criteria>
  <done>Running `npm test` from `api/` spawns the proxy against a local mock, exercises the four abuse paths, and exits 0 when origin lock (403), size cap (413), rate limit (429), and valid allowed-origin (200 + server-side KB prepend) all behave correctly. No network call to `openrouter.ai`.</done>
</task>

</tasks>

<verification>
- `cd api && npm test` exits 0
- `grep -r "openrouter.ai" api/test/` returns nothing
- Disallowed-origin case returns 403 (manual sanity: `curl -i -H 'Origin: https://evil.example.com' -X POST http://127.0.0.1:3861/api/chat -d '{"messages":[]}'` while proxy is running under test env)
- Mock server records at least one request whose body contains the KB sentinel string (proves D-09 server-side prepend, not client-supplied)
</verification>

<success_criteria>
- Four smoke tests pass against the local mock
- Zero live OpenRouter calls during any test run
- Test script wired into `npm test` so Phase 03 CI can invoke it unchanged
- D-13 satisfied; success criteria 3 and 4 have an automated regression gate
</success_criteria>

<output>
After completion, the Phase 01 executor (or human at end of phase) creates `.planning/M2/phases/01-security-remediation/SUMMARY.md` per GUARDRAILS end-of-phase contract. This plan does not write SUMMARY itself.
</output>
