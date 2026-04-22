---
doc: cloudflare-runbook
phase: M2-02
decision: D-18
author_note: delivered to IAM dev as a hand-off artifact
---

# Cloudflare Setup Runbook — interactivemove.nl

Step-by-step. Execute click-by-click in the Cloudflare dashboard. Exact panel and setting names match the Cloudflare UI as of April 2026; minor layout drift is possible.

## 0. Prerequisites

- A Cloudflare account (Free tier is sufficient).
- Registrar access for `interactivemove.nl` (ability to change nameservers).
- The VPS is running — `bootstrap.sh` has completed successfully, and `certbot` has issued valid Let's Encrypt certificates for both `interactivemove.nl` and `iam.abbamarkt.nl`. Verify with `sudo certbot certificates` on the VPS.

## 1. Add interactivemove.nl to Cloudflare

- Log in → **Add a Site** (top-right) → enter `interactivemove.nl` → **Continue**.
- Select the **Free** plan → **Continue**.
- Cloudflare imports existing DNS records. Verify the **A** record for `@` points to the VPS public IP (placeholder: `REPLACE_ME_VPS_IP` — the IP you ran `bootstrap.sh` against). Keep proxy status **Proxied (orange cloud)** for both `@` and `www`.

## 2. Update nameservers at your domain registrar

- Cloudflare shows two NS records (for example `amy.ns.cloudflare.com` and `dave.ns.cloudflare.com`).
- Log in at the registrar that holds `interactivemove.nl`. Replace the current nameservers with the two Cloudflare values.
- Click **Done, check nameservers** in Cloudflare. Propagation can take up to a few hours; the dashboard will email you when activation completes.

## 3. SSL/TLS mode — Full (strict)

- Cloudflare sidebar → **SSL/TLS** → **Overview**.
- Set **Encryption mode** to **Full (strict)**. This requires the origin cert — `bootstrap.sh` installed one via Let's Encrypt, so validation will succeed.
- **Edge Certificates** tab:
  - Enable **Always Use HTTPS** (toggle on).
  - Enable **Automatic HTTPS Rewrites**.
  - **Minimum TLS Version** → **TLS 1.2**.

## 4. Bot Fight Mode

- Sidebar → **Security** → **Bots** → enable **Bot Fight Mode** (available on the Free tier). Leave other bot settings untouched.

## 5. Rate Limit Rule for /api/chat

- Sidebar → **Security** → **WAF** → **Rate limiting rules** → **Create rule**.
- **Rule name**: `chat-endpoint-limit`.
- **If expression**: `(http.request.uri.path eq "/api/chat")`.
- **When rate exceeds**: **10 requests per 1 minute** per IP.
- **Action**: **Block**. **Duration**: **1 minute**.
- **Deploy**.

This is belt-and-suspenders with the Nginx-level `limit_req` and the Express `express-rate-limit` from Phase 01. All three can safely coexist.

## 6. (Optional) Cache Rules for static assets

- Sidebar → **Caching** → **Cache Rules** → **Create rule**.
- **If expression**: `(http.request.uri.path matches "^/(media|js|css|fonts)/")`.
- **Edge TTL**: **1 year**.
- Origin already sends `Cache-Control: public, max-age=31536000, immutable` for those paths (Nginx vhost from Plan 02), so Cloudflare respects it.

## 7. Do NOT add iam.abbamarkt.nl to Cloudflare (staging)

- Staging must remain reachable directly so internal tests hit the origin, not the edge.
- Keep staging DNS at whatever registrar hosts `abbamarkt.nl`.
- Create an A record `iam.abbamarkt.nl` → VPS IP with **no Cloudflare proxy**.

## 8. Verification checklist

After propagation completes:

- `curl -I https://interactivemove.nl` returns a response with `server: cloudflare` and `strict-transport-security: max-age=...`.
- `curl -X POST https://interactivemove.nl/api/chat -H "Origin: https://interactivemove.nl" -H "Content-Type: application/json" -d '{"messages":[{"role":"user","content":"hi"}]}'` returns **200** (or **503** if the prod OpenRouter key is not yet installed — expected until the handoff checklist is complete).
- 11 rapid requests to `/api/chat` from a single IP return **429** (from Cloudflare's rule OR from Nginx `limit_req` — either is acceptable).

## 9. Rollback (if Cloudflare breaks prod)

- DNS → change the A record **proxy status** from orange (Proxied) to grey (DNS only).
- This removes Cloudflare from the path entirely. TLS terminates directly at Nginx using the Let's Encrypt cert.
- Investigate the specific Cloudflare setting that caused the break, fix it, then re-enable proxy.
