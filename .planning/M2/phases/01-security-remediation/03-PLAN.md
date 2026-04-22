---
phase: M2-01-security-remediation
plan: 03
type: execute
wave: 2
depends_on: [02]
files_modified:
  - api/chat-proxy.js
  - api/package.json
autonomous: true
decisions: [D-05, D-06, D-07, D-08, D-09, D-11]
success_criteria_addressed: [3, 4, 5]
requirements: [M2-01-SC-3, M2-01-SC-4, M2-01-SC-5]
must_haves:
  truths:
    - "Requests from allowed origins (interactivemove.nl, iam.abbamarkt.nl) pass CORS; others receive 403"
    - "More than 10 requests per minute from one IP result in HTTP 429"
    - "Bodies > 32KB are rejected with 413"
    - "Messages > 4000 chars or history > 20 turns are rejected with 400"
    - "The proxy prepends server-side SYSTEM_PROMPT + IAM_KNOWLEDGE_BASE before forwarding to OpenRouter"
    - "Upstream streaming (SSE) pass-through is preserved"
    - "All logs are JSON via pino on stdout"
  artifacts:
    - path: api/chat-proxy.js
      provides: "hardened Express chat proxy"
      contains: "require('express')"
    - path: api/package.json
      provides: "zod + pino dependencies added"
  key_links:
    - from: api/chat-proxy.js
      to: api/knowledge-base.js
      via: "require('./knowledge-base')"
      pattern: "require\\(['\"]\\./knowledge-base['\"]\\)"
    - from: api/chat-proxy.js
      to: api/system-prompt.js
      via: "require('./system-prompt')"
      pattern: "require\\(['\"]\\./system-prompt['\"]\\)"
    - from: api/chat-proxy.js
      to: https://openrouter.ai/api/v1/chat/completions
      via: "forward with stream:true, pipe upstream response to res"
      pattern: "openrouter\\.ai"
---

<objective>
Rewrite `api/chat-proxy.js` as a hardened Express application implementing CORS allowlist, per-IP rate limiting, request validation, body-size cap, server-side prompt/KB prepend, and structured logging.

Purpose: closes SC-3 (origin restriction), SC-4 (rate limit + input validation), completes SC-5 (server prepends prompt/KB).
Output: new `api/chat-proxy.js`; `api/package.json` gains `zod` and `pino`.
</objective>

<context>
@.planning/M2/GUARDRAILS.md
@.planning/M2/phases/01-security-remediation/CONTEXT.md
@.planning/M2/phases/01-security-remediation/02-PLAN.md
@api/chat-proxy.js
@api/package.json
@api/knowledge-base.js
@api/system-prompt.js
</context>

<interfaces>
Route: `POST /api/chat`
Request body (validated by zod):
```
{
  messages: Array<{ role: 'user'|'assistant', content: string }> // 1..20 items, content 1..4000 chars
}
```
Response: streamed SSE passed through from OpenRouter (content-type preserved).

Server prepends before forwarding:
```
[
  { role: 'system', content: SYSTEM_PROMPT + '\n\n' + IAM_KNOWLEDGE_BASE },
  ...clientMessages
]
```

Env vars consumed:
- `OPENROUTER_API_KEY` (required at startup; log warning if absent, 503 on request)
- `CHAT_MODEL` (default `google/gemini-2.0-flash-001`)
- `CHAT_PORT` (default 3860)
- `CHAT_ALLOWED_ORIGINS` (default `https://interactivemove.nl,https://iam.abbamarkt.nl`)
- `CHAT_RATE_LIMIT_MAX` (default 10), `CHAT_RATE_LIMIT_WINDOW_MS` (default 60000)
- `OPENROUTER_URL` (default `https://openrouter.ai`) — upstream base URL; exists as a testability affordance for D-13 smoke tests (Plan 05) to redirect to a local mock. Prod-unaffected when unset.
</interfaces>

<tasks>

<task type="auto">
  <name>Task 1: Add zod and pino deps; install</name>
  <files>api/package.json</files>
  <read_first>
    - api/package.json (already has express ^5.2.1, express-rate-limit ^8.3.1, cors ^2.8.6, dotenv)
  </read_first>
  <action>
    Add to `dependencies` in `api/package.json` (keep alphabetical):
    - `"pino": "^9.5.0"`
    - `"zod": "^3.23.8"`
    Then from `api/` run `npm install` (local node_modules only — this is the worktree, not prod).
    Do NOT lock specific dev versions beyond these ranges. Do NOT add helmet unless Task 2 decides to use it (agent discretion per CONTEXT).
    Commit AFTER Task 2 (single commit for the rewrite + deps).
  </action>
  <verify>
    <automated>node -e "const p=require('./api/package.json'); if(!p.dependencies.zod||!p.dependencies.pino) process.exit(1)"</automated>
  </verify>
  <acceptance_criteria>
    - `api/package.json` dependencies contains `zod` and `pino`
    - `api/node_modules/zod/package.json` exists after install
    - `api/node_modules/pino/package.json` exists after install
  </acceptance_criteria>
  <done>zod + pino installed locally; package.json updated.</done>
</task>

<task type="auto">
  <name>Task 2: Rewrite api/chat-proxy.js as Express app (D-05, D-06, D-07, D-08, D-09, D-11)</name>
  <files>api/chat-proxy.js</files>
  <read_first>
    - api/chat-proxy.js (current http.createServer version — note the `proxyRes.pipe(res)` pattern to preserve)
    - api/knowledge-base.js (D-09: module exporting IAM_KNOWLEDGE_BASE)
    - api/system-prompt.js (D-09: module exporting SYSTEM_PROMPT)
    - .planning/M2/phases/01-security-remediation/CONTEXT.md (D-05..D-11 exact values)
    - .planning/M2/GUARDRAILS.md ("No calls to live OpenRouter API in retry loops")
  </read_first>
  <action>
    Replace `api/chat-proxy.js` entirely with an Express app. Required structure (CommonJS, matches `"type": "commonjs"`):

    ```js
    // M2-01 hardened chat proxy — per D-05..D-11.
    const express = require('express');
    const rateLimit = require('express-rate-limit');
    const cors = require('cors');
    const { z } = require('zod');
    const pino = require('pino');
    const https = require('https');
    const { IAM_KNOWLEDGE_BASE } = require('./knowledge-base');
    const { SYSTEM_PROMPT } = require('./system-prompt');

    const log = pino({ level: process.env.LOG_LEVEL || 'info' });

    const PORT = Number(process.env.CHAT_PORT || 3860);
    const API_KEY = process.env.OPENROUTER_API_KEY;
    const MODEL = process.env.CHAT_MODEL || 'google/gemini-2.0-flash-001';
    const ALLOWED_ORIGINS = (process.env.CHAT_ALLOWED_ORIGINS
      || 'https://interactivemove.nl,https://iam.abbamarkt.nl')
      .split(',').map(s => s.trim()).filter(Boolean);
    const RL_MAX = Number(process.env.CHAT_RATE_LIMIT_MAX || 10);
    const RL_WINDOW = Number(process.env.CHAT_RATE_LIMIT_WINDOW_MS || 60_000);
    const UPSTREAM_URL = new URL(process.env.OPENROUTER_URL || 'https://openrouter.ai');

    if (!API_KEY) log.warn('OPENROUTER_API_KEY not set — /api/chat will 503');

    const app = express();
    app.set('trust proxy', 1); // behind nginx in prod (Phase 02)

    // Middleware order (agent discretion, per CONTEXT):
    //  1. security headers (hand-rolled — avoid extra dep)
    //  2. cors allowlist
    //  3. json body parser with 32KB cap
    //  4. per-IP rate limit on /api/chat
    //  5. zod payload validation
    //  6. upstream forward

    app.use((req, res, next) => {
      res.setHeader('X-Content-Type-Options', 'nosniff');
      res.setHeader('X-Frame-Options', 'DENY');
      res.setHeader('Referrer-Policy', 'no-referrer');
      next();
    });

    app.use(cors({
      origin(origin, cb) {
        if (!origin) return cb(null, false); // block no-origin (curl without -H) for /api/chat
        if (ALLOWED_ORIGINS.includes(origin)) return cb(null, true);
        return cb(null, false);
      },
      methods: ['POST', 'OPTIONS'],
      credentials: false,
    }));

    // Explicit 403 for disallowed origins (cors() silently strips headers; we want an error status)
    app.use('/api/chat', (req, res, next) => {
      const origin = req.get('origin');
      if (req.method === 'OPTIONS') return next();
      if (!origin || !ALLOWED_ORIGINS.includes(origin)) {
        log.warn({ origin, ip: req.ip }, 'origin_rejected');
        return res.status(403).json({ error: 'origin_not_allowed' });
      }
      next();
    });

    app.use('/api/chat', express.json({ limit: '32kb' })); // 413 on overflow

    const chatLimiter = rateLimit({
      windowMs: RL_WINDOW,
      max: RL_MAX,
      standardHeaders: true,
      legacyHeaders: false,
      message: { error: 'rate_limited' },
    });

    const MessageSchema = z.object({
      role: z.enum(['user', 'assistant']),
      content: z.string().min(1).max(4000),
    });
    const BodySchema = z.object({
      messages: z.array(MessageSchema).min(1).max(20),
    });

    app.post('/api/chat', chatLimiter, (req, res) => {
      if (!API_KEY) return res.status(503).json({ error: 'api_key_missing' });

      const parsed = BodySchema.safeParse(req.body);
      if (!parsed.success) {
        log.warn({ issues: parsed.error.issues, ip: req.ip }, 'validation_failed');
        return res.status(400).json({ error: 'invalid_payload' });
      }

      const upstreamMessages = [
        { role: 'system', content: `${SYSTEM_PROMPT}\n\n${IAM_KNOWLEDGE_BASE}` },
        ...parsed.data.messages,
      ];

      const postData = JSON.stringify({ model: MODEL, messages: upstreamMessages, stream: true });

      const transport = UPSTREAM_URL.protocol === 'http:' ? require('http') : https;
      const upstream = transport.request({
        hostname: UPSTREAM_URL.hostname,
        port: UPSTREAM_URL.port || (UPSTREAM_URL.protocol === 'http:' ? 80 : 443),
        path: '/api/v1/chat/completions',
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${API_KEY}`,
          'Content-Type': 'application/json',
          'X-Title': 'IAM Support Chat',
          'Content-Length': Buffer.byteLength(postData),
        },
      }, (up) => {
        res.writeHead(up.statusCode || 502, up.headers);
        up.pipe(res);
      });

      upstream.on('error', (err) => {
        log.error({ err: err.message }, 'upstream_error');
        if (!res.headersSent) res.status(502).json({ error: 'upstream_error' });
      });

      upstream.write(postData);
      upstream.end();
    });

    // 413 handler for body-parser overflow
    app.use((err, req, res, next) => {
      if (err && err.type === 'entity.too.large') {
        log.warn({ ip: req.ip }, 'body_too_large');
        return res.status(413).json({ error: 'payload_too_large' });
      }
      next(err);
    });

    if (require.main === module) {
      app.listen(PORT, () => log.info({ port: PORT, model: MODEL, allowed: ALLOWED_ORIGINS }, 'chat_proxy_listening'));
    }

    module.exports = app; // exported for smoke tests (Plan 05)
    ```

    NOTE: route path changed from `/chat` (old) to `/api/chat` (per CONTEXT integration point — "nginx currently routes /api/chat to localhost:3860"). Confirm by checking any local scripts that reference `/chat`; none should exist outside this file.

    Commit (together with Task 1 deps): `feat(M2-01): rewrite chat proxy as hardened Express app per D-05..D-11`
  </action>
  <verify>
    <automated>node -e "const app=require('./api/chat-proxy'); if(typeof app!=='function') process.exit(1)" && grep -q "require('express')" api/chat-proxy.js && grep -q "require('express-rate-limit')" api/chat-proxy.js && ! grep -q "Access-Control-Allow-Origin.*\\*" api/chat-proxy.js</automated>
  </verify>
  <acceptance_criteria>
    - `api/chat-proxy.js` contains `require('express')` and `require('express-rate-limit')`
    - `api/chat-proxy.js` contains `require('./knowledge-base')` and `require('./system-prompt')`
    - `api/chat-proxy.js` does NOT contain the string `Access-Control-Allow-Origin: *` nor `Access-Control-Allow-Origin', '*'`
    - `api/chat-proxy.js` contains `express.json({ limit: '32kb' })` (exact string)
    - `api/chat-proxy.js` contains `z.array(MessageSchema).min(1).max(20)`
    - `api/chat-proxy.js` contains `.max(4000)` for message content
    - `api/chat-proxy.js` contains `res.status(403)` and `res.status(413)` and the rate-limit 429 behavior comes from `express-rate-limit` defaults
    - `api/chat-proxy.js` contains `pino` and NOT raw `console.log` in request handlers
    - `node -e "require('./api/chat-proxy')"` exits 0 (module loads without error)
    - Route is `POST /api/chat` (grep `app.post\\('/api/chat'`)
    - `api/chat-proxy.js` contains `process.env.OPENROUTER_URL` and does NOT contain the string literal `hostname: 'openrouter.ai'` (testability affordance for D-13; prod behavior unchanged when env var is unset)
  </acceptance_criteria>
  <done>Proxy rewritten; loads without error; all required strings present; app exported for tests.</done>
</task>

</tasks>

<verification>
- `node -e "require('./api/chat-proxy')"` succeeds
- Starting the app locally (`OPENROUTER_API_KEY=dummy node api/chat-proxy.js &`) and calling:
  - `curl -i -X POST -H 'Origin: https://example.com' -H 'Content-Type: application/json' -d '{"messages":[{"role":"user","content":"hi"}]}' http://localhost:3860/api/chat` returns 403
  - `curl -i -X POST -H 'Origin: https://interactivemove.nl' -H 'Content-Type: application/json' --data-binary "@/tmp/big.json" http://localhost:3860/api/chat` (where big.json is >32KB) returns 413
  (Full automation of these checks is in Plan 05.)
</verification>

<success_criteria>
Closes SC-3, SC-4, and finishes SC-5 by prepending server-side prompt+KB.
</success_criteria>

<output>
Contributes to phase SUMMARY.md.
</output>
