---
phase: M2-02-vps-deployment
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - config/systemd/iam-api.service
  - config/systemd/iam-api-staging.service
  - tools/env-template
  - tools/env-staging-template
autonomous: true
decisions: [D-03, D-05, D-06, D-07, D-08, D-19, D-20]
success_criteria_addressed: [2, 5]
requirements: [D-03, D-05, D-06, D-07, D-08, D-19, D-20]
must_haves:
  truths:
    - "systemctl start iam-api launches chat-proxy.js as the iam user with prod env file loaded"
    - "systemctl start iam-api-staging launches the staging instance on port 3861 with staging env file"
    - "systemd kills the process if memory exceeds 256M, CPU exceeds 50%, or tasks exceed 50"
    - "Env templates render to /etc/iam-api/env and /etc/iam-api-staging/env with chmod 600 at bootstrap time"
  artifacts:
    - path: "config/systemd/iam-api.service"
      contains: "EnvironmentFile=/etc/iam-api/env"
    - path: "config/systemd/iam-api.service"
      contains: "MemoryMax=256M"
    - path: "config/systemd/iam-api.service"
      contains: "CPUQuota=50%"
    - path: "config/systemd/iam-api.service"
      contains: "TasksMax=50"
    - path: "config/systemd/iam-api.service"
      contains: "User=iam"
    - path: "config/systemd/iam-api.service"
      contains: "ExecStart=/usr/bin/node chat-proxy.js"
    - path: "config/systemd/iam-api.service"
      contains: "After=network-online.target"
    - path: "config/systemd/iam-api.service"
      contains: "Restart=on-failure"
    - path: "config/systemd/iam-api-staging.service"
      contains: "EnvironmentFile=/etc/iam-api-staging/env"
    - path: "tools/env-template"
      contains: "OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_PROD_KEY"
    - path: "tools/env-staging-template"
      contains: "OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_STAGING_KEY"
    - path: "tools/env-template"
      contains: "CHAT_PORT=3860"
    - path: "tools/env-staging-template"
      contains: "CHAT_PORT=3861"
  key_links:
    - from: "config/systemd/iam-api.service"
      to: "/etc/iam-api/env"
      via: "EnvironmentFile directive"
    - from: "config/systemd/iam-api.service"
      to: "/var/www/iam/current/api/chat-proxy.js"
      via: "WorkingDirectory + ExecStart"
---

<objective>
Produce the two systemd unit files and the two env file templates that Plan 03's `bootstrap.sh` will install on the VPS. This plan writes local files in the repo only — nothing is installed on any VPS.

Purpose: Establish the process-supervision contract (D-05..D-08) and the secrets-file shape (D-03, D-19, D-20) for the IAM chat proxy, separately for prod and staging, with exact resource caps and env-file references that bootstrap and downstream plans rely on.

Output: `config/systemd/iam-api.service`, `config/systemd/iam-api-staging.service`, `tools/env-template`, `tools/env-staging-template`.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
</execution_context>

<context>
@.planning/M2/GUARDRAILS.md
@.planning/M2/phases/02-vps-deployment/CONTEXT.md
@.planning/M2/phases/01-security-remediation/SUMMARY.md
@api/chat-proxy.js
@api/package.json

<interfaces>
<!-- From api/chat-proxy.js — env vars the service consumes -->
Required env:
  OPENROUTER_API_KEY             (Bearer for OpenRouter)
Optional env (defaults shown):
  CHAT_PORT=3860                 (prod) / 3861 (staging)
  CHAT_MODEL=google/gemini-2.0-flash-001
  CHAT_ALLOWED_ORIGINS=https://interactivemove.nl,https://iam.abbamarkt.nl
  CHAT_RATE_LIMIT_MAX=10
  CHAT_RATE_LIMIT_WINDOW_MS=60000
  LOG_LEVEL=info
  TOKEN_BUDGET_PATH=/var/lib/iam-api/token-budget.json
  OPENROUTER_URL=https://openrouter.ai    (leave default in prod)

Entrypoint: `node chat-proxy.js` (cwd must be the `api/` subdir of the release)
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Write prod systemd unit</name>
  <files>config/systemd/iam-api.service</files>
  <read_first>
    - api/chat-proxy.js (confirm entrypoint is chat-proxy.js and that PORT env is CHAT_PORT)
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (D-05..D-08, D-19)
  </read_first>
  <action>
    Create `config/systemd/iam-api.service` with this exact content (no extra keys, no reordering of the [Unit]/[Service]/[Install] sections). Per D-05, D-06, D-07, D-08, D-19:

    ```
    [Unit]
    Description=IAM chat proxy (prod)
    After=network-online.target
    Wants=network-online.target

    [Service]
    Type=simple
    User=iam
    Group=iam
    WorkingDirectory=/var/www/iam/current/api
    EnvironmentFile=/etc/iam-api/env
    ExecStart=/usr/bin/node chat-proxy.js
    Restart=on-failure
    RestartSec=5s
    StartLimitBurst=3
    StartLimitIntervalSec=60
    StandardOutput=journal
    StandardError=journal
    SyslogIdentifier=iam-api

    # Resource limits per D-06
    MemoryMax=256M
    CPUQuota=50%
    TasksMax=50

    # Basic hardening (no sudo needed at runtime)
    NoNewPrivileges=true
    ProtectSystem=strict
    ProtectHome=true
    PrivateTmp=true
    ReadWritePaths=/var/lib/iam-api

    [Install]
    WantedBy=multi-user.target
    ```

    Reference D-05..D-08 in the commit message.
  </action>
  <acceptance_criteria>
    - `grep -c '^MemoryMax=256M$' config/systemd/iam-api.service` returns 1
    - `grep -c '^CPUQuota=50%$' config/systemd/iam-api.service` returns 1
    - `grep -c '^TasksMax=50$' config/systemd/iam-api.service` returns 1
    - `grep -c '^User=iam$' config/systemd/iam-api.service` returns 1
    - `grep -c '^Group=iam$' config/systemd/iam-api.service` returns 1
    - `grep -c '^EnvironmentFile=/etc/iam-api/env$' config/systemd/iam-api.service` returns 1
    - `grep -c '^WorkingDirectory=/var/www/iam/current/api$' config/systemd/iam-api.service` returns 1
    - `grep -c '^ExecStart=/usr/bin/node chat-proxy.js$' config/systemd/iam-api.service` returns 1
    - `grep -c '^After=network-online.target$' config/systemd/iam-api.service` returns 1
    - `grep -c '^Restart=on-failure$' config/systemd/iam-api.service` returns 1
    - `grep -c '^StandardOutput=journal$' config/systemd/iam-api.service` returns 1
    - `grep -cE '^StartLimit(Burst=3|IntervalSec=60)$' config/systemd/iam-api.service` returns 2
    - `systemd-analyze verify config/systemd/iam-api.service` returns 0 IF systemd-analyze is available locally; otherwise this check is skipped and recorded as "systemd-analyze not available" in the commit message.
  </acceptance_criteria>
  <verify>
    <automated>grep -c '^MemoryMax=256M$\|^CPUQuota=50%$\|^TasksMax=50$\|^User=iam$\|^EnvironmentFile=/etc/iam-api/env$\|^WorkingDirectory=/var/www/iam/current/api$\|^ExecStart=/usr/bin/node chat-proxy.js$\|^After=network-online.target$\|^Restart=on-failure$' config/systemd/iam-api.service | grep -qx 9</automated>
  </verify>
  <done>All acceptance greps return exactly the expected counts; commit `feat(M2-02): add iam-api.service unit per D-05..D-08`.</done>
</task>

<task type="auto">
  <name>Task 2: Write staging systemd unit</name>
  <files>config/systemd/iam-api-staging.service</files>
  <read_first>
    - config/systemd/iam-api.service (just created — mirror its structure)
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (D-19, D-20)
  </read_first>
  <action>
    Copy the structure from Task 1's unit. Change every prod-specific value:

    ```
    [Unit]
    Description=IAM chat proxy (staging)
    After=network-online.target
    Wants=network-online.target

    [Service]
    Type=simple
    User=iam
    Group=iam
    WorkingDirectory=/var/www/iam-staging/current/api
    EnvironmentFile=/etc/iam-api-staging/env
    ExecStart=/usr/bin/node chat-proxy.js
    Restart=on-failure
    RestartSec=5s
    StartLimitBurst=3
    StartLimitIntervalSec=60
    StandardOutput=journal
    StandardError=journal
    SyslogIdentifier=iam-api-staging

    MemoryMax=256M
    CPUQuota=50%
    TasksMax=50

    NoNewPrivileges=true
    ProtectSystem=strict
    ProtectHome=true
    PrivateTmp=true
    ReadWritePaths=/var/lib/iam-api-staging

    [Install]
    WantedBy=multi-user.target
    ```

    Note: same User=iam (D-04 says one service user; staging is isolated by env file, paths, and port — not a second user).
  </action>
  <acceptance_criteria>
    - `grep -c '^EnvironmentFile=/etc/iam-api-staging/env$' config/systemd/iam-api-staging.service` returns 1
    - `grep -c '^WorkingDirectory=/var/www/iam-staging/current/api$' config/systemd/iam-api-staging.service` returns 1
    - `grep -c '^SyslogIdentifier=iam-api-staging$' config/systemd/iam-api-staging.service` returns 1
    - `grep -c '^ReadWritePaths=/var/lib/iam-api-staging$' config/systemd/iam-api-staging.service` returns 1
    - `grep -c '^MemoryMax=256M$' config/systemd/iam-api-staging.service` returns 1
    - File MUST NOT contain the prod path: `grep -c '/var/www/iam/current' config/systemd/iam-api-staging.service` returns 0
    - File MUST NOT contain `/etc/iam-api/env` (prod): use `grep -x 'EnvironmentFile=/etc/iam-api/env' config/systemd/iam-api-staging.service` returns empty (exit 1)
  </acceptance_criteria>
  <verify>
    <automated>grep -q '^EnvironmentFile=/etc/iam-api-staging/env$' config/systemd/iam-api-staging.service && grep -q '^WorkingDirectory=/var/www/iam-staging/current/api$' config/systemd/iam-api-staging.service && ! grep -q '/var/www/iam/current' config/systemd/iam-api-staging.service</automated>
  </verify>
  <done>Staging unit parallels prod unit with only paths, port-via-env, and identifier differing; commit `feat(M2-02): add iam-api-staging.service unit per D-19/D-20`.</done>
</task>

<task type="auto">
  <name>Task 3: Write env file templates for prod and staging</name>
  <files>tools/env-template, tools/env-staging-template</files>
  <read_first>
    - api/chat-proxy.js lines 13-25 (env vars consumed)
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (D-03, D-20)
    - .planning/M2/phases/01-security-remediation/CONTEXT.md (for HubSpot / Phase 04 env vars — include placeholders now)
  </read_first>
  <action>
    Create `tools/env-template` with this exact content. Placeholders MUST be the literal strings `REPLACE_ME_<NAME>` so handoff-checklist.md can grep them:

    ```
    # IAM chat proxy — PRODUCTION env file
    # Rendered to /etc/iam-api/env by bootstrap.sh (chmod 600, owner iam:iam)
    # DO NOT commit real values. DO NOT echo this file to logs.

    # --- OpenRouter (chat proxy) ---
    OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_PROD_KEY
    CHAT_MODEL=google/gemini-2.0-flash-001

    # --- Listener ---
    CHAT_PORT=3860

    # --- CORS allowlist (D-06) ---
    CHAT_ALLOWED_ORIGINS=https://interactivemove.nl

    # --- Rate limit (D-07) ---
    CHAT_RATE_LIMIT_MAX=10
    CHAT_RATE_LIMIT_WINDOW_MS=60000

    # --- Token budget (D-10) ---
    TOKEN_BUDGET_PATH=/var/lib/iam-api/token-budget.json

    # --- Logging ---
    LOG_LEVEL=info

    # --- HubSpot (reserved for Phase 04; keep placeholders so env file is stable across phases) ---
    HUBSPOT_PORTAL_ID=REPLACE_ME_HUBSPOT_PORTAL_ID
    HUBSPOT_CONTACT_FORM_GUID=REPLACE_ME_HUBSPOT_CONTACT_FORM_GUID
    HUBSPOT_PARTNER_FORM_GUID=REPLACE_ME_HUBSPOT_PARTNER_FORM_GUID
    ```

    Create `tools/env-staging-template` with the same shape, but port 3861, staging origin, a distinct OpenRouter key placeholder (D-20), and staging token-budget path:

    ```
    # IAM chat proxy — STAGING env file
    # Rendered to /etc/iam-api-staging/env by bootstrap.sh (chmod 600, owner iam:iam)

    OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_STAGING_KEY
    CHAT_MODEL=google/gemini-2.0-flash-001

    CHAT_PORT=3861

    CHAT_ALLOWED_ORIGINS=https://iam.abbamarkt.nl

    CHAT_RATE_LIMIT_MAX=10
    CHAT_RATE_LIMIT_WINDOW_MS=60000

    TOKEN_BUDGET_PATH=/var/lib/iam-api-staging/token-budget.json

    LOG_LEVEL=info

    HUBSPOT_PORTAL_ID=REPLACE_ME_HUBSPOT_PORTAL_ID
    HUBSPOT_CONTACT_FORM_GUID=REPLACE_ME_HUBSPOT_CONTACT_FORM_GUID
    HUBSPOT_PARTNER_FORM_GUID=REPLACE_ME_HUBSPOT_PARTNER_FORM_GUID
    ```
  </action>
  <acceptance_criteria>
    - `grep -c '^OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_PROD_KEY$' tools/env-template` returns 1
    - `grep -c '^OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_STAGING_KEY$' tools/env-staging-template` returns 1
    - `grep -c '^CHAT_PORT=3860$' tools/env-template` returns 1
    - `grep -c '^CHAT_PORT=3861$' tools/env-staging-template` returns 1
    - `grep -c '^CHAT_ALLOWED_ORIGINS=https://interactivemove.nl$' tools/env-template` returns 1
    - `grep -c '^CHAT_ALLOWED_ORIGINS=https://iam.abbamarkt.nl$' tools/env-staging-template` returns 1
    - `grep -c '^TOKEN_BUDGET_PATH=/var/lib/iam-api/token-budget.json$' tools/env-template` returns 1
    - `grep -c '^TOKEN_BUDGET_PATH=/var/lib/iam-api-staging/token-budget.json$' tools/env-staging-template` returns 1
    - `grep -c 'REPLACE_ME_HUBSPOT' tools/env-template` returns 3
    - `grep -c 'REPLACE_ME_HUBSPOT' tools/env-staging-template` returns 3
    - Neither file contains a real-looking API key: `grep -E 'sk-or-[a-zA-Z0-9]{16,}' tools/env-template tools/env-staging-template` returns empty (exit 1)
  </acceptance_criteria>
  <verify>
    <automated>grep -q '^OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_PROD_KEY$' tools/env-template && grep -q '^OPENROUTER_API_KEY=REPLACE_ME_OPENROUTER_STAGING_KEY$' tools/env-staging-template && ! grep -qE 'sk-or-[a-zA-Z0-9]{16,}' tools/env-template tools/env-staging-template</automated>
  </verify>
  <done>Both templates present with exact required lines, all placeholders use `REPLACE_ME_` prefix, no real-looking keys. Commit `feat(M2-02): add env templates for prod and staging per D-03/D-20`.</done>
</task>

</tasks>

<verification>
Combined final check:
```
grep -l 'MemoryMax=256M' config/systemd/iam-api.service config/systemd/iam-api-staging.service
grep -l 'REPLACE_ME_OPENROUTER' tools/env-template tools/env-staging-template
```
Both commands must list all four files.
</verification>

<success_criteria>
- Two systemd unit files exist and parse (if systemd-analyze available)
- Two env templates exist with `REPLACE_ME_*` placeholders for every secret
- Prod and staging differ in: env-file path, working directory, syslog identifier, port (via env), origin (via env), OpenRouter key (via env), token-budget path (via env)
- No real credentials anywhere in the diff
</success_criteria>

<output>
After completion: create `.planning/M2/phases/02-vps-deployment/01-SUMMARY.md` with the file list and the grep evidence from Task 1-3 verify commands.
</output>
