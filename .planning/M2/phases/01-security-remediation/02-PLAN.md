---
phase: M2-01-security-remediation
plan: 02
type: execute
wave: 1
depends_on: []
files_modified:
  - api/knowledge-base.js
  - api/system-prompt.js
  - js/iam-knowledge-base.js
  - js/chat-widget.js
  - js/chat-config.js
autonomous: true
decisions: [D-09]
success_criteria_addressed: [5]
requirements: [M2-01-SC-5]
must_haves:
  truths:
    - "The IAM knowledge base text is no longer present in any file under js/"
    - "The chat system prompt is no longer present in js/chat-widget.js"
    - "api/knowledge-base.js exports IAM_KNOWLEDGE_BASE for server consumption"
    - "api/system-prompt.js exports the system prompt string"
    - "Client payload to /api/chat contains only user-authored turns (no role:'system', no KB)"
  artifacts:
    - path: api/knowledge-base.js
      provides: "server-side IAM knowledge base, exports IAM_KNOWLEDGE_BASE"
    - path: api/system-prompt.js
      provides: "server-side system prompt, exports SYSTEM_PROMPT"
    - path: js/iam-knowledge-base.js
      provides: "either deleted or reduced to a <10 line stub that does NOT contain KB text"
  key_links:
    - from: js/chat-widget.js
      to: /api/chat
      via: "fetch POST with body { messages: [{role:'user',content:...}, ...] } — no system role, no KB"
      pattern: "messages:\\s*\\["
---

<objective>
Move the IAM knowledge base and system prompt server-side so neither is visible in browser source. Tighten the client payload contract to user turns only — the rewritten proxy (Plan 03) prepends the system prompt + KB.

Purpose: closes SC-5 (prompt and KB server-side). Must land before Plan 03 so the proxy rewrite can rely on the server-side modules existing and the client payload shape being stable.
Output: two new `api/` modules, stripped client files, updated payload contract.
</objective>

<context>
@.planning/M2/GUARDRAILS.md
@.planning/M2/phases/01-security-remediation/CONTEXT.md
@js/iam-knowledge-base.js
@js/chat-widget.js
@js/chat-config.js
</context>

<interfaces>
New server-side contract (Plan 03 will consume these):

```js
// api/knowledge-base.js
module.exports = { IAM_KNOWLEDGE_BASE: `...` };

// api/system-prompt.js
module.exports = { SYSTEM_PROMPT: `...` };
```

New client payload contract (Plan 03 will validate against this with zod):
```js
// POST /api/chat
{ messages: [ { role: 'user'|'assistant', content: string }, ... ] }
```
Note: CommonJS `module.exports` chosen because `api/package.json` has `"type": "commonjs"`. If Plan 03 migrates to ESM, update both modules in that same commit.
</interfaces>

<tasks>

<task type="auto">
  <name>Task 1: Create server-side api/knowledge-base.js and api/system-prompt.js (D-09)</name>
  <files>api/knowledge-base.js, api/system-prompt.js</files>
  <read_first>
    - js/iam-knowledge-base.js (full file — this is the source of truth to copy verbatim)
    - js/chat-widget.js lines 150-200 (contains the `systemPrompt = \`...\`` template literal — this is the source of truth for the system prompt)
    - api/package.json (confirm "type": "commonjs" — determines export style)
  </read_first>
  <action>
    1. Copy the complete `IAM_KNOWLEDGE_BASE` template literal body (everything between the backticks in js/iam-knowledge-base.js) into a new file `api/knowledge-base.js`:
       ```js
       // Server-side IAM knowledge base — moved from js/iam-knowledge-base.js per M2-01 D-09.
       // Never ship to client.
       const IAM_KNOWLEDGE_BASE = `
       <paste exact body here>
       `;

       module.exports = { IAM_KNOWLEDGE_BASE };
       ```
    2. Locate the `const systemPrompt = \`...\`;` declaration in js/chat-widget.js (around line 153). Copy the full template literal body into `api/system-prompt.js`:
       ```js
       // Server-side system prompt — moved from js/chat-widget.js per M2-01 D-09.
       // Never ship to client.
       const SYSTEM_PROMPT = `
       <paste exact body here>
       `;

       module.exports = { SYSTEM_PROMPT };
       ```
    3. Verify both files load without syntax errors: `node -e "console.log(require('./api/knowledge-base').IAM_KNOWLEDGE_BASE.length, require('./api/system-prompt').SYSTEM_PROMPT.length)"` should print two positive integers.
    4. Commit: `feat(M2-01): extract KB and system prompt server-side per D-09`
  </action>
  <verify>
    <automated>node -e "const {IAM_KNOWLEDGE_BASE}=require('./api/knowledge-base'); const {SYSTEM_PROMPT}=require('./api/system-prompt'); if(IAM_KNOWLEDGE_BASE.length<500||SYSTEM_PROMPT.length<200) process.exit(1)"</automated>
  </verify>
  <acceptance_criteria>
    - `api/knowledge-base.js` exists
    - `api/system-prompt.js` exists
    - Both files export via `module.exports` (CommonJS)
    - `require('./api/knowledge-base').IAM_KNOWLEDGE_BASE` returns a string of length > 500
    - `require('./api/system-prompt').SYSTEM_PROMPT` returns a string of length > 200
    - `grep -q "Inter Active Move" api/knowledge-base.js` matches (verifies real content copied, not a stub)
  </acceptance_criteria>
  <done>Both server-side modules created, require without error, contain the full content.</done>
</task>

<task type="auto">
  <name>Task 2: Strip client-side KB/prompt and update payload shape (D-09)</name>
  <files>js/iam-knowledge-base.js, js/chat-widget.js, js/chat-config.js</files>
  <read_first>
    - js/chat-widget.js (full file — need to find every reference to systemPrompt and IAM_KNOWLEDGE_BASE)
    - js/chat-config.js (confirm it has no KB reference to remove; currently 5 lines)
    - js/iam-knowledge-base.js
    - api/knowledge-base.js and api/system-prompt.js from Task 1 (source of truth now server-side — client MUST NOT duplicate)
  </read_first>
  <action>
    1. Delete `js/iam-knowledge-base.js` entirely (`git rm js/iam-knowledge-base.js`). Rationale: D-09 says move server-side; leaving a stub invites drift.
    2. In `js/chat-widget.js`:
       - Remove the entire `const systemPrompt = \`...\`;` declaration block.
       - Locate the `fetch(apiUrl, { ... body: JSON.stringify({ messages: [ { role: 'system', content: systemPrompt }, ... ] }) })` call.
       - Replace the `messages` array construction so it contains ONLY user/assistant turns from the widget's conversation state. Remove the `{ role: 'system', content: systemPrompt }` prepend.
       - New shape: `body: JSON.stringify({ messages: conversationHistory })` where `conversationHistory` is the array of `{role: 'user'|'assistant', content}` objects the widget already maintains.
    3. In any HTML file that loads `js/iam-knowledge-base.js` via `<script src="...">`, remove the script tag. Find them with: `grep -rn "iam-knowledge-base" --include="*.html"` and remove each match. Do NOT modify unrelated HTML.
    4. Leave `js/chat-config.js` unchanged if it contains no KB reference (confirmed: current file is 5 lines with only apiUrl). Otherwise remove any `window.IAM_KNOWLEDGE_BASE` reference.
    5. Sanity check: `grep -rn "IAM_KNOWLEDGE_BASE\|systemPrompt" js/` should return empty.
    6. Commit: `refactor(M2-01): strip KB and system prompt from client per D-09`
  </action>
  <verify>
    <automated>test ! -f js/iam-knowledge-base.js && ! grep -rq "IAM_KNOWLEDGE_BASE" js/ && ! grep -rq "systemPrompt" js/ && ! grep -rq "iam-knowledge-base" --include="*.html" .</automated>
  </verify>
  <acceptance_criteria>
    - `js/iam-knowledge-base.js` does not exist
    - `grep -rn "IAM_KNOWLEDGE_BASE" js/` returns empty
    - `grep -rn "systemPrompt" js/chat-widget.js` returns empty
    - `grep -rn "role: 'system'" js/chat-widget.js` returns empty (no client-side system-role injection)
    - No HTML file contains a `<script src=".*iam-knowledge-base.*">` tag
    - `js/chat-widget.js` still contains a `fetch(` call to `/api/chat` and still sends a `messages:` array
  </acceptance_criteria>
  <done>KB text nowhere in client bundle; widget sends user-only turns to /api/chat.</done>
</task>

</tasks>

<verification>
- View-source of any HTML page loading the widget shows no IAM_KNOWLEDGE_BASE content
- `curl -s https://interactivemove.nl/js/chat-widget.js 2>/dev/null | grep -c systemPrompt` would return 0 (local equivalent: `grep -c systemPrompt js/chat-widget.js` == 0)
- Both `require('./api/knowledge-base')` and `require('./api/system-prompt')` return populated strings
</verification>

<success_criteria>
Closes SC-5 (prompt and KB server-side). Enables Plan 03 to prepend server-owned prompt without client payload ambiguity.
</success_criteria>

<output>
Contributes to phase SUMMARY.md.
</output>
