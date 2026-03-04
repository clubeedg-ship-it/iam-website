# IAM Website — QA Audit Report

**Date:** 2026-03-04  
**Environment:** Docker on localhost:3007 (iam.zenithcred.com)  
**Auditor:** Kira (automated)

---

## 1. Ghost Blog

| Check | Status |
|-------|--------|
| Ghost container running | ✅ `iam-ghost` up 4 days |
| Ghost admin accessible (`/ghost/`) | ✅ HTTP 200 |
| Ghost Content API (`/ghost/api/content/`) | ⚠️ HTTP 404 — no content API key configured or no published posts |
| MySQL healthy | ✅ healthy |

**Issues:**
- **WARN: Missing `mail.from` config** — Ghost logs show repeated warnings every 5 min. Configure `mail__from` env var in docker-compose.yml (e.g., `mail__from: noreply@interactivemove.nl`).
- **Rate limiting too aggressive for Ghost Admin** — nginx logs show many 503s on `/ghost/api/admin/` with `burst=5`. Ghost admin makes ~10+ parallel requests on page load. **Recommendation:** Increase `burst=15` for `ghost_admin` zone.
- **Ghost `url` set to `http://localhost:3007`** — This means Ghost generates localhost URLs in API responses. For production, set to `https://iam.zenithcred.com`.

---

## 2. Bug Check / Recent Changes

### Git Log (last 20 commits)
Key fixes verified:
- ✅ GTM added to all pages (commit `99dfb4e`)
- ✅ Broken links fixed, WhatsApp→email migration (commit `7599673`)
- ✅ Navigation standardized across all pages (commit `67d24eb`)
- ✅ Scroll animations fixed after HTMX swap (commit `a2811f8`)
- ✅ GDPR compliance implemented (commit `2f3f717`)
- ✅ Accessibility statement added (commit `98f3f9a`)

### Nginx Error Logs
- Rate limiting errors on Ghost admin (Feb 28) — see section 1
- No 404s for static assets — all CSS/JS/fonts/media loading correctly
- Recent traffic (Mar 3) shows clean 200 responses for all assets

**No broken asset issues detected.**

---

## 3. HubSpot Form

| File | Status |
|------|--------|
| `word-partner.html` | Has `<div id="hubspot-partner-form">` placeholder |
| `partials/word-partner-nl.html` | Same placeholder |
| `partials/word-partner-en.html` | Same placeholder |

**🔴 CRITICAL: HubSpot form is NOT implemented.** The divs contain only a comment `<!-- HubSpot form will be embedded here -->` with no actual HubSpot embed script. Visitors to the partner page see an empty form area.

**`js/contact-form.js`:** Uses a `mailto:` link (not HubSpot). This is the main contact form — works correctly, opens email client with pre-filled data to `klantcontact@interactivemove.nl`.

**Recommendation:** Either:
1. Add HubSpot embed script (`<script>hbspt.forms.create({...})</script>`) to the partner pages, OR
2. Replace with a mailto-based form like the contact form, OR  
3. Remove the empty placeholder to avoid broken UX

---

## 4. Security

### Cookie Banner
✅ **Present and GDPR-compliant.** `js/cookie-consent.js` loaded on all HTML pages. Features:
- Equal Accept/Reject buttons (Dutch law requirement)
- Consent stored with timestamp
- No cookies set before consent

### CSP Headers
🔴 **Missing.** No `Content-Security-Policy` header in nginx config. Only these headers are set:
- ✅ `X-Frame-Options: SAMEORIGIN`
- ✅ `X-Content-Type-Options: nosniff`
- ✅ `X-XSS-Protection: 1; mode=block`
- ✅ `Referrer-Policy: strict-origin-when-cross-origin`
- ✅ `Permissions-Policy: camera=(), microphone=(), geolocation=()`

**Recommendation:** Add a CSP header. Suggested starter:
```
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; frame-src https://www.googletagmanager.com; connect-src 'self'" always;
```

### External Font Loading (GDPR)
✅ **No external fonts detected.** Fonts are self-hosted at `/media/fonts/` (Inter-Regular, Inter-SemiBold, Inter-ExtraBold as .woff2). No Google Fonts or CDN font references found.

### GTM Script
✅ **Correctly placed** in `index.html` (and per git log, all pages):
- Script tag in `<head>` (line 20)
- `<noscript>` fallback in `<body>` (line 26)
- Correct ID: `GTM-KPX78C22`

---

## 5. General

### Docker Compose
✅ Well-structured. Services: nginx, ghost, mysql with proper dependencies and healthchecks.

**Minor issues:**
- Ghost `url` should be production URL, not `http://localhost:3007`
- Missing `mail__from` configuration

### Service Health
| Service | Status |
|---------|--------|
| iam-nginx | ✅ Up 20 min (recently restarted) |
| iam-ghost | ✅ Up 4 days |
| iam-mysql | ✅ Up 4 days (healthy) |

### Environment Files
🔴 **`.env.docker` is tracked in git** (`git ls-files` confirms it). Contains database passwords.  
✅ `.env` is properly gitignored.

**Recommendation:** Add `.env.docker` to `.gitignore` and remove from git tracking:
```bash
echo ".env.docker" >> .gitignore
git rm --cached .env.docker
```

### Nginx Config
- ✅ Blocks access to dotfiles, docker-compose, .env, /tools/, /reference/
- ✅ Static asset caching (30d with immutable)
- ✅ Clean URL support (`try_files $uri $uri.html`)

---

## Summary

### 🔴 Critical (3)
1. **HubSpot partner form not implemented** — empty placeholder on word-partner pages
2. **No CSP header** — leaves site vulnerable to XSS/injection
3. **`.env.docker` with passwords tracked in git**

### 🟡 Warning (3)
4. Ghost `mail.from` not configured (repeated warnings)
5. Ghost admin rate limit too aggressive (`burst=5` → recommend `burst=15`)
6. Ghost `url` set to localhost instead of production domain

### ✅ Good
- All services healthy and running
- GDPR compliance: cookie consent, self-hosted fonts, privacy/cookie policies
- GTM correctly placed on all pages
- Security headers present (except CSP)
- Contact form working (mailto-based)
- No broken assets or 404s on static content
- Sensitive files blocked by nginx
- Accessibility statement present
