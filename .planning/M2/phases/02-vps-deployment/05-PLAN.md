---
phase: M2-02-vps-deployment
plan: 05
type: execute
wave: 1
depends_on: [01, 02, 03, 04]
files_modified:
  - .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md
  - .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md
autonomous: true
decisions: [D-17, D-18]
success_criteria_addressed: [4]
requirements: [D-17, D-18]
must_haves:
  truths:
    - "Cloudflare runbook is a step-by-step markdown document the IAM dev executes click-by-click without consulting a second source"
    - "Every step names the exact Cloudflare UI panel, the exact setting name, and the exact value"
    - "The runbook covers: domain add, nameserver swap, SSL mode Full(strict) (D-17), Always Use HTTPS, Bot Fight Mode, Rate Limit Rule for /api/chat, optional cache rules"
    - "HANDOFF-CHECKLIST.md enumerates every placeholder value in the repo that IAM dev must fill before running bootstrap.sh"
  artifacts:
    - path: ".planning/M2/phases/02-vps-deployment/cloudflare-runbook.md"
      contains: "Full (strict)"
    - path: ".planning/M2/phases/02-vps-deployment/cloudflare-runbook.md"
      contains: "interactivemove.nl"
    - path: ".planning/M2/phases/02-vps-deployment/cloudflare-runbook.md"
      contains: "Rate Limit"
    - path: ".planning/M2/phases/02-vps-deployment/cloudflare-runbook.md"
      contains: "/api/chat"
    - path: ".planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md"
      contains: "REPLACE_ME"
    - path: ".planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md"
      contains: "OPENROUTER_API_KEY"
    - path: ".planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md"
      contains: "LETSENCRYPT_EMAIL"
  key_links:
    - from: "cloudflare-runbook.md"
      to: "IAM dev"
      via: "markdown instruction executed click-by-click in Cloudflare dashboard"
    - from: "HANDOFF-CHECKLIST.md"
      to: "tools/env-template, tools/env-staging-template, bootstrap.sh"
      via: "explicit gap list per placeholder protocol"
---

<objective>
Deliver the two human-facing docs that complete this phase: the Cloudflare runbook (D-18) and the handoff checklist (placeholder protocol). Without these, the code in Plans 01-04 cannot be safely executed by the IAM dev on the real VPS.

Purpose: Close phase success criterion #4 ("Cloudflare runbook delivered to IAM dev") and fulfill the placeholder protocol imposed on this autonomous run — every `REPLACE_ME_*` in the codebase must have an entry explaining what it is, where it goes, and what breaks if it's wrong.

Output: `cloudflare-runbook.md` and `HANDOFF-CHECKLIST.md`, both under `.planning/M2/phases/02-vps-deployment/`.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
</execution_context>

<context>
@.planning/M2/phases/02-vps-deployment/CONTEXT.md
@.planning/M2/phases/02-vps-deployment/01-PLAN.md
@.planning/M2/phases/02-vps-deployment/02-PLAN.md
@.planning/M2/phases/02-vps-deployment/03-PLAN.md
@.planning/M2/phases/02-vps-deployment/04-PLAN.md
</context>

<tasks>

<task type="auto">
  <name>Task 1: Write cloudflare-runbook.md</name>
  <files>.planning/M2/phases/02-vps-deployment/cloudflare-runbook.md</files>
  <read_first>
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (D-17, D-18)
  </read_first>
  <action>
    Create the runbook with the structure below. Screenshots are marked as placeholders (`![Cloudflare SSL settings panel](./screenshots/cf-ssl.png)`) because we can't take real screenshots in this run — the IAM dev can add them later if desired. The text alone must be precise enough to execute without them.

    Required top-level sections (H2 headings, exact text):

    1. `## 0. Prerequisites` — IAM dev has: a Cloudflare account (free tier works); domain registrar access for `interactivemove.nl`; the VPS running `bootstrap.sh` has completed successfully and `certbot` has valid certs for both `interactivemove.nl` and `iam.abbamarkt.nl`.

    2. `## 1. Add interactivemove.nl to Cloudflare`
       - Log in → **Add a Site** (top-right) → enter `interactivemove.nl` → **Continue**.
       - Select the **Free** plan → **Continue**.
       - Cloudflare imports existing DNS records. Verify the **A** record for `@` points to the VPS public IP (placeholder: `REPLACE_ME_VPS_IP` — the IP you ran bootstrap.sh against). Keep proxy status **Proxied (orange cloud)** for `@` and `www`.

    3. `## 2. Update nameservers at your domain registrar`
       - Cloudflare shows two NS records (e.g. `xxx.ns.cloudflare.com`).
       - Log in at the registrar that holds `interactivemove.nl`, replace the current nameservers with the two Cloudflare values.
       - Click **Done, check nameservers** in Cloudflare. Propagation can take up to a few hours; the dashboard will email when active.

    4. `## 3. SSL/TLS mode — Full (strict)` (D-17)
       - Cloudflare sidebar → **SSL/TLS** → **Overview**.
       - Set **Encryption mode** to **Full (strict)**. This requires the origin cert; bootstrap.sh installed one via Let's Encrypt, so this will validate.
       - **Edge Certificates** tab → enable **Always Use HTTPS** (toggle on). Enable **Automatic HTTPS Rewrites**. Min TLS Version → **TLS 1.2**.

    5. `## 4. Bot Fight Mode`
       - **Security** → **Bots** → enable **Bot Fight Mode** (free tier). No other bot settings.

    6. `## 5. Rate Limit Rule for /api/chat`
       - **Security** → **WAF** → **Rate limiting rules** → **Create rule**.
       - Rule name: `chat-endpoint-limit`.
       - If expression: `(http.request.uri.path eq "/api/chat")`.
       - When rate exceeds: **10 requests per 1 minute** per IP.
       - Action: **Block**. Duration: **1 minute**.
       - Deploy.

    7. `## 6. (Optional) Cache Rules for static assets`
       - **Caching** → **Cache Rules** → create rule.
       - Rule: `(http.request.uri.path matches "^/(media|js|css|fonts)/")` → **Edge TTL: 1 year**.
       - Origin already sends `Cache-Control: public, max-age=31536000, immutable` for those paths (Nginx vhost from Plan 02), so Cloudflare respects it.

    8. `## 7. Do NOT add iam.abbamarkt.nl to Cloudflare (staging)`
       - Staging must remain reachable directly so internal tests hit the origin, not the edge.
       - Keep staging DNS at whatever registrar it lives at (abbamarkt.nl's DNS).
       - Point an A record `iam.abbamarkt.nl` → VPS IP with no Cloudflare proxy.

    9. `## 8. Verification checklist`
       - `curl -I https://interactivemove.nl` returns `server: cloudflare` and `strict-transport-security: max-age=...`
       - `curl -X POST https://interactivemove.nl/api/chat -H "Origin: https://interactivemove.nl" -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"hi"}]}'` returns 200 (or 503 if prod OpenRouter key not yet set, which is expected until handoff checklist is complete)
       - 11 rapid requests to `/api/chat` produce a 429 (Cloudflare block or Nginx limit_req — either is fine)

    10. `## 9. Rollback (if Cloudflare breaks prod)`
        - DNS → change A record proxy status from orange to grey (DNS only, no proxy).
        - This removes Cloudflare from the path; TLS terminates directly at Nginx with the Let's Encrypt cert.
        - Investigate, fix, re-enable proxy.

    Use clear markdown, short sentences, exact panel names. Include a header yaml block with `doc: cloudflare-runbook`, `phase: M2-02`, `decision: D-18`, `author_note: delivered to IAM dev as a hand-off artifact`.
  </action>
  <acceptance_criteria>
    - `test -f .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` succeeds
    - `grep -Fc 'Full (strict)' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns at least 1
    - `grep -Fc '/api/chat' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns at least 2
    - `grep -Fc '10 requests per 1 minute' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns 1
    - `grep -Fc 'Always Use HTTPS' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns 1
    - `grep -Fc 'Bot Fight Mode' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns at least 1
    - `grep -Fc 'iam.abbamarkt.nl' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns at least 1
    - `grep -Fc 'REPLACE_ME_VPS_IP' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns at least 1
    - Document has at least 9 H2 sections: `grep -c '^## ' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` returns at least 9
  </acceptance_criteria>
  <verify>
    <automated>test -f .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md && grep -Fq 'Full (strict)' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md && grep -Fq '10 requests per 1 minute' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md && [ "$(grep -c '^## ' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md)" -ge 9 ]</automated>
  </verify>
  <done>Runbook present with all 10 sections; commit `docs(M2-02): cloudflare runbook for prod edge per D-18/D-17`.</done>
</task>

<task type="auto">
  <name>Task 2: Write HANDOFF-CHECKLIST.md</name>
  <files>.planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md</files>
  <read_first>
    - tools/env-template, tools/env-staging-template (from Plan 01)
    - bootstrap.sh (from Plan 03)
    - .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md (Task 1 above)
  </read_first>
  <action>
    Create the handoff checklist. The doc MUST enumerate every placeholder in the repo under one table and every runtime input the IAM dev must supply to `bootstrap.sh`. Structure:

    ```
    # M2-02 Handoff Checklist

    > Autonomous run produced code and configs with clearly-marked placeholders. This doc lists every placeholder, every runtime input, and what breaks if any of them is wrong.

    ## 1. Runtime inputs bootstrap.sh will ask for

    | Input | Where it's asked | What it is | What breaks if wrong |
    |-------|------------------|------------|----------------------|
    | `LETSENCRYPT_EMAIL` | env var or prompt | Email address Let's Encrypt associates with the cert, used for expiration warnings | No certs issued → Nginx reload fails → prod offline |
    | `OPENROUTER_API_KEY` | env var or prompt (no echo) | Prod OpenRouter API key | Prod chat returns 503 until corrected |
    | `OPENROUTER_API_KEY_STAGING` | env var or prompt (no echo) | Staging OpenRouter API key (separate billing/budget per D-20) | Staging chat returns 503 until corrected |
    | `DOMAIN` | defaults to `interactivemove.nl` | Prod domain | Wrong cert SAN → Cloudflare "Full (strict)" fails |
    | `STAGING_DOMAIN` | defaults to `iam.abbamarkt.nl` | Staging subdomain | Wrong cert → TLS error on staging |
    | `REPO_URL` | env var or prompt | Git URL the deploy tarball originates from | Bootstrap itself doesn't clone; only Phase 03 workflow uses this. Currently `REPLACE_ME_REPO_URL` in bootstrap.sh — must be set before first deploy. |

    ## 2. Placeholders in repo files

    Every `REPLACE_ME_*` token. Listed here so IAM dev can grep-and-verify none are missed before running bootstrap.sh or the first deploy.

    | Token | File | What value to provide | Impact if left unfilled |
    |-------|------|----------------------|-------------------------|
    | `REPLACE_ME_OPENROUTER_PROD_KEY` | `tools/env-template` → `/etc/iam-api/env` (rendered by bootstrap.sh) | Prod OpenRouter API key (starts `sk-or-`) | bootstrap.sh substitutes this from `$OPENROUTER_API_KEY` automatically; only an issue if you write the env file by hand |
    | `REPLACE_ME_OPENROUTER_STAGING_KEY` | `tools/env-staging-template` → `/etc/iam-api-staging/env` | Staging OpenRouter API key | Same — substituted by bootstrap |
    | `REPLACE_ME_HUBSPOT_PORTAL_ID` | both env templates | HubSpot portal id (numeric) | Phase 04 `/api/contact` returns 500; contact form stops working |
    | `REPLACE_ME_HUBSPOT_CONTACT_FORM_GUID` | both env templates | Contact form GUID (UUID) | Same |
    | `REPLACE_ME_HUBSPOT_PARTNER_FORM_GUID` | both env templates | Partner form GUID (UUID) | Same |
    | `REPLACE_ME_REPO_URL` | `bootstrap.sh` constant | Public git URL of the iam-website repo | bootstrap.sh logs it and Phase 03 workflow uses it; must be set before Phase 03 runs |
    | `REPLACE_ME_VPS_IP` | `.planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` | VPS public IPv4 | Runbook step 1 won't be executable until filled |

    ## 3. Actions IAM dev takes outside the repo

    1. **Rotate OpenRouter keys** — per Phase 01 handoff (`HISTORY-SCAN.md`), the key(s) that ever hit git history MUST be rotated. Do this on the OpenRouter dashboard before running bootstrap.sh.
    2. **Provide a dedicated staging key** — per D-20, staging should use a lower-budget key, not the prod key.
    3. **Cloudflare** — follow `cloudflare-runbook.md` after bootstrap.sh completes on the VPS.
    4. **SSH hardening** — ensure the VPS accepts SSH key auth only (no passwords) and the `deploy` user has an authorized_keys file with the GitHub Actions deploy key (Phase 03 delivers the workflow; key provisioning is an IAM dev action).
    5. **DNS for staging** — add `iam.abbamarkt.nl` A record → VPS IP, un-proxied (no Cloudflare).

    ## 4. Verification after handoff

    Run on the VPS once the above is done:
    ```
    sudo systemctl status iam-api iam-api-staging
    curl -sI https://interactivemove.nl   | grep -i strict-transport-security
    curl -sI https://iam.abbamarkt.nl     | grep -i strict-transport-security
    sudo journalctl -u iam-api -n 50 --no-pager
    ```
    Expected: both services active, HSTS headers present, journald shows `chat_proxy_listening` pino log line.

    ## 5. Open questions to surface back to the planning sessions

    - Confirm VPS OS version (22.04 vs 24.04) — bootstrap.sh supports both.
    - Confirm WordPress Nginx vhost path — bootstrap.sh does not touch it, but IAM dev should verify `nginx -t` after bootstrap still lists the WordPress vhost.
    - Confirm GitHub repo slug for Phase 03 workflow (`oopuo-ship/iam-website` or the current repo).
    ```

    No actual secrets in this file. All placeholders identifiable by the literal string `REPLACE_ME`.
  </action>
  <acceptance_criteria>
    - `test -f .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` succeeds
    - `grep -c 'REPLACE_ME' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns at least 7
    - `grep -Fc 'OPENROUTER_API_KEY' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns at least 2
    - `grep -Fc 'LETSENCRYPT_EMAIL' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns at least 1
    - `grep -Fc 'HUBSPOT' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns at least 3
    - `grep -Fc 'REPO_URL' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns at least 1
    - `grep -Fc 'VPS_IP' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns at least 1
    - Has at least 5 H2 sections: `grep -c '^## ' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns at least 5
    - No real-looking secrets: `grep -E 'sk-or-[a-zA-Z0-9]{16,}' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md` returns empty (exit 1)
  </acceptance_criteria>
  <verify>
    <automated>test -f .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md && [ "$(grep -c 'REPLACE_ME' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md)" -ge 7 ] && [ "$(grep -c '^## ' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md)" -ge 5 ] && ! grep -qE 'sk-or-[a-zA-Z0-9]{16,}' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md</automated>
  </verify>
  <done>Checklist enumerates every placeholder, every runtime input, every external action; commit `docs(M2-02): handoff checklist enumerating placeholders and IAM dev actions`.</done>
</task>

</tasks>

<verification>
```
grep -c 'REPLACE_ME' .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md   # expect >= 7
grep -c '^## ' .planning/M2/phases/02-vps-deployment/cloudflare-runbook.md        # expect >= 9
# Cross-check: every REPLACE_ME in repo code is mentioned in the checklist
for tok in $(grep -rhoE 'REPLACE_ME_[A-Z_]+' tools/ bootstrap.sh config/ 2>/dev/null | sort -u); do
  grep -Fq "$tok" .planning/M2/phases/02-vps-deployment/HANDOFF-CHECKLIST.md || echo "MISSING: $tok"
done
```
The cross-check loop should print nothing.
</verification>

<success_criteria>
- cloudflare-runbook.md is click-by-click executable by IAM dev, covers D-17 "Full (strict)" and the rate-limit rule
- HANDOFF-CHECKLIST.md covers every REPLACE_ME token in the repo and every bootstrap.sh input
- No real secrets anywhere in either file
</success_criteria>

<output>
After completion: create `.planning/M2/phases/02-vps-deployment/05-SUMMARY.md` with the cross-check loop output (expected empty) and file paths.

Additionally (phase-level): after Plan 05 commits, the executor should prepare a phase-level `SUMMARY.md` per the GUARDRAILS "end of phase" contract and open a PR. That is orchestrator work, not this plan's — noting here for the chain.
</output>
