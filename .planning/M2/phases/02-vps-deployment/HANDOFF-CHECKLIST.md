# M2 Phase 02 — Handoff Checklist

> Autonomous run produced code and configs with clearly-marked placeholders. This doc lists every placeholder, every runtime input, and what breaks if any of them is wrong. Reviewer surfaces to IAM dev at merge time.

## 1. Runtime inputs bootstrap.sh will ask for

| Input | Where it's asked | What it is | What breaks if wrong |
|-------|------------------|------------|----------------------|
| `LETSENCRYPT_EMAIL` | env var or interactive prompt | Email Let's Encrypt associates with the cert; used for expiration warnings | No cert issued → Nginx reload fails → prod offline |
| `OPENROUTER_API_KEY` | env var or prompt (input hidden) | Prod OpenRouter API key | Prod chat returns 503 until corrected |
| `OPENROUTER_API_KEY_STAGING` | env var or prompt (input hidden) | Staging OpenRouter API key (separate billing/budget per D-20) | Staging chat returns 503 until corrected |
| `DOMAIN` | defaults to `interactivemove.nl` | Prod domain | Wrong cert SAN → Cloudflare "Full (strict)" fails |
| `STAGING_DOMAIN` | defaults to `iam.abbamarkt.nl` | Staging subdomain | Wrong cert → TLS error on staging |
| `REPO_URL` | env var | Git URL the deploy tarball originates from | bootstrap.sh itself does not clone; Phase 03 uses this. Currently `REPLACE_ME_REPO_URL` in `bootstrap.sh` — set before first deploy. |

## 2. Placeholders in repo files

Every `REPLACE_ME_*` token. Listed here so IAM dev can grep-and-verify none are missed.

| Token | File | What value to provide | Impact if unfilled |
|-------|------|----------------------|--------------------|
| `REPLACE_ME_OPENROUTER_PROD_KEY` | `tools/env-template` → `/etc/iam-api/env` (rendered by bootstrap.sh) | Prod OpenRouter API key (starts `sk-or-`) | bootstrap.sh substitutes from `$OPENROUTER_API_KEY` automatically; only an issue if you hand-edit the env file. |
| `REPLACE_ME_OPENROUTER_STAGING_KEY` | `tools/env-staging-template` → `/etc/iam-api-staging/env` | Staging OpenRouter API key | Same — substituted by bootstrap. |
| `REPLACE_ME_HUBSPOT_PORTAL_ID` | both env templates | HubSpot portal id (numeric) | Phase 04 `/api/contact` returns 500; contact form stops working. |
| `REPLACE_ME_HUBSPOT_CONTACT_FORM_GUID` | both env templates | Contact form GUID (UUID) | Same. |
| `REPLACE_ME_HUBSPOT_PARTNER_FORM_GUID` | both env templates | Partner form GUID (UUID) | Same. |
| `REPLACE_ME_REPO_URL` | `bootstrap.sh` constant | Public git URL of the iam-website repo | Logged by bootstrap; Phase 03 workflow uses it. Must be set before Phase 03 runs. |
| `REPLACE_ME_VPS_IP` | `.planning/M2/phases/02-vps-deployment/cloudflare-runbook.md` | VPS public IPv4 | Runbook step 1 is not executable until filled. |

## 3. Actions IAM dev takes outside the repo

1. **Rotate OpenRouter keys** — per Phase 01 handoff (`HISTORY-SCAN.md`), any key that ever hit git history MUST be rotated. Do this on the OpenRouter dashboard before running bootstrap.sh.
2. **Provide a dedicated staging key** — per D-20, staging should use a lower-budget key, not the prod key.
3. **Cloudflare** — follow `cloudflare-runbook.md` after bootstrap.sh completes on the VPS.
4. **SSH hardening** — ensure the VPS accepts SSH key auth only (no passwords). Give the `deploy` user an `~/.ssh/authorized_keys` file with the GitHub Actions deploy key (Phase 03 delivers the workflow; key provisioning is an IAM dev action).
5. **DNS for staging** — add an A record `iam.abbamarkt.nl` → VPS IP, un-proxied (no Cloudflare).

## 4. Verification after handoff

Run on the VPS once the above is done:

```
sudo systemctl status iam-api iam-api-staging
curl -sI https://interactivemove.nl   | grep -i strict-transport-security
curl -sI https://iam.abbamarkt.nl     | grep -i strict-transport-security
sudo journalctl -u iam-api -n 50 --no-pager
```

Expected: both services active, HSTS headers present, journald shows `chat_proxy_listening` pino log line.

Pre-start env check:

```
sudo grep REPLACE_ME /etc/iam-api/env /etc/iam-api-staging/env && echo "FILL PLACEHOLDERS BEFORE STARTING SERVICE"
```

Must return empty before `systemctl start iam-api` / `iam-api-staging`.

## 5. Open questions to surface back to the planning sessions

- Confirm VPS OS version (22.04 vs 24.04) — bootstrap.sh supports both.
- Confirm WordPress Nginx vhost path — bootstrap.sh does not touch it, but IAM dev should verify `nginx -t` after bootstrap still lists the WordPress vhost.
- Confirm GitHub repo slug for Phase 03 workflow (`oopuo-ship/iam-website` or the current repo).

## 6. Tooling gaps noted in autonomous run

- `systemd-analyze` not available in worker environment; unit files were verified by `grep` only. Reviewer or VPS bootstrap should run `systemd-analyze verify` on the installed unit files.
- `shellcheck` not available in worker environment; `bootstrap.sh` and `tools/iam-deploy.sh` were verified with `bash -n` only. `bootstrap.sh` installs `shellcheck` via apt — run it on the VPS against these files before first deploy.
