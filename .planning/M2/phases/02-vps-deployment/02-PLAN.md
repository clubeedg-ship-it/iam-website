---
phase: M2-02-vps-deployment
plan: 02
type: execute
wave: 1
depends_on: [01]
files_modified:
  - config/nginx/interactivemove.nl.conf
  - config/nginx/iam.abbamarkt.nl.conf
autonomous: true
decisions: [D-09, D-10, D-11, D-12, D-13, D-14, D-15, D-17]
success_criteria_addressed: [3]
requirements: [D-09, D-10, D-11, D-12, D-13, D-14, D-15, D-17]
must_haves:
  truths:
    - "Prod vhost serves static files from /var/www/iam/current and reverse-proxies /api/chat to localhost:3860"
    - "Staging vhost serves from /var/www/iam-staging/current and reverse-proxies /api/chat to localhost:3861"
    - "Both vhosts force HTTPS, set HSTS, CSP, security headers, and apply chat rate limit before the proxy_pass"
    - "/api/contact returns 404 today but is wired as a reverse-proxy location reserved for Phase 04"
    - "Static assets under /media/ and /js/*.min.js are cached 1 year; *.html is no-cache"
  artifacts:
    - path: "config/nginx/interactivemove.nl.conf"
      contains: "server_name interactivemove.nl"
    - path: "config/nginx/interactivemove.nl.conf"
      contains: "limit_req_zone $binary_remote_addr zone=chat:10m rate=10r/m"
    - path: "config/nginx/interactivemove.nl.conf"
      contains: "limit_req zone=chat burst=5 nodelay"
    - path: "config/nginx/interactivemove.nl.conf"
      contains: "proxy_pass http://127.0.0.1:3860"
    - path: "config/nginx/interactivemove.nl.conf"
      contains: "Strict-Transport-Security"
    - path: "config/nginx/interactivemove.nl.conf"
      contains: "Content-Security-Policy"
    - path: "config/nginx/interactivemove.nl.conf"
      contains: "root /var/www/iam/current"
    - path: "config/nginx/iam.abbamarkt.nl.conf"
      contains: "server_name iam.abbamarkt.nl"
    - path: "config/nginx/iam.abbamarkt.nl.conf"
      contains: "proxy_pass http://127.0.0.1:3861"
    - path: "config/nginx/iam.abbamarkt.nl.conf"
      contains: "root /var/www/iam-staging/current"
  key_links:
    - from: "config/nginx/interactivemove.nl.conf"
      to: "localhost:3860 (iam-api.service)"
      via: "location /api/chat { proxy_pass ... }"
    - from: "config/nginx/iam.abbamarkt.nl.conf"
      to: "localhost:3861 (iam-api-staging.service)"
      via: "location /api/chat { proxy_pass ... }"
---

<objective>
Produce two Nginx vhost files — one for prod (`interactivemove.nl`) and one for staging (`iam.abbamarkt.nl`) — that serve static files, reverse-proxy `/api/chat` and `/api/contact` to the Node service on the correct port, apply TLS/HSTS/CSP/security headers per D-14, and apply the Nginx-level rate limit per D-13.

Purpose: Define the edge contract between the public internet (eventually via Cloudflare) and the systemd-supervised Node services from Plan 01. Separate vhosts keep prod and staging fully isolated (D-19) and coexist with the existing WordPress vhost on the same Nginx (D-09).

Output: `config/nginx/interactivemove.nl.conf`, `config/nginx/iam.abbamarkt.nl.conf`. Phase 03's `bootstrap.sh` symlinks these into `/etc/nginx/sites-enabled/`.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
</execution_context>

<context>
@.planning/M2/phases/02-vps-deployment/CONTEXT.md
@.planning/M2/phases/02-vps-deployment/01-PLAN.md
@api/chat-proxy.js

<interfaces>
<!-- Upstream services (from Plan 01) -->
Prod:    iam-api.service          → 127.0.0.1:3860   (POST /api/chat)
Staging: iam-api-staging.service  → 127.0.0.1:3861   (POST /api/chat)

<!-- Static content layout -->
Prod web root:    /var/www/iam/current/          (symlink managed in Phase 03)
Staging web root: /var/www/iam-staging/current/  (symlink managed in Phase 03)

<!-- Certbot will write (after `certbot --nginx` in Plan 03): -->
Prod certs:    /etc/letsencrypt/live/interactivemove.nl/fullchain.pem, privkey.pem
Staging certs: /etc/letsencrypt/live/iam.abbamarkt.nl/fullchain.pem,   privkey.pem

<!-- CSP scope (per D-14 + what the site actually uses) -->
The site uses:
  - self-hosted assets under /media/ and /js/
  - inline <script> init blocks
  - HTMX (self-hosted in /js/)
  - HubSpot Forms API v3 at api.hsforms.com / forms.hubspot.com (Phase 04 / already live hotfix)
  - Cloudflare (prod) as proxy (TLS terminates at Cloudflare too, origin is still TLS)
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Write prod vhost interactivemove.nl.conf</name>
  <files>config/nginx/interactivemove.nl.conf</files>
  <read_first>
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (D-09..D-15, D-17)
    - api/chat-proxy.js (confirm port 3860, path /api/chat)
  </read_first>
  <action>
    Create `config/nginx/interactivemove.nl.conf` with the exact content below. Put the `limit_req_zone` at the top (outside any server block — it's a `http{}`-context directive but Nginx tolerates it in an included site file when included from `http{}`). We mark it with a comment explaining that bootstrap.sh will either rely on Nginx's include order or relocate the zone into `nginx.conf`.

    ```nginx
    # IAM prod vhost — interactivemove.nl
    # Managed by Phase M2-02 bootstrap.sh. Coexists with the WordPress vhost (untouched).
    # Decisions: D-09..D-15, D-17.

    # Rate limit zone for /api/chat (D-13). Belt-and-suspenders with the Express limit from Phase 01.
    # NOTE: limit_req_zone is an http{}-context directive. bootstrap.sh ensures this file is
    # included from http{} (default Ubuntu Nginx does `include /etc/nginx/sites-enabled/*;`
    # inside http{}, so this works without modification).
    limit_req_zone $binary_remote_addr zone=chat:10m rate=10r/m;

    # HTTP → HTTPS redirect
    server {
        listen 80;
        listen [::]:80;
        server_name interactivemove.nl www.interactivemove.nl;

        # ACME challenge (Certbot)
        location /.well-known/acme-challenge/ {
            root /var/www/letsencrypt;
        }

        location / {
            return 301 https://interactivemove.nl$request_uri;
        }
    }

    # HTTPS main server
    server {
        listen 443 ssl;
        listen [::]:443 ssl;
        http2 on;
        server_name interactivemove.nl;

        ssl_certificate     /etc/letsencrypt/live/interactivemove.nl/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/interactivemove.nl/privkey.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 1d;

        root /var/www/iam/current;
        index index.html;

        # --- Security headers (D-14) ---
        add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-Frame-Options "DENY" always;
        add_header Referrer-Policy "strict-origin-when-cross-origin" always;
        add_header Permissions-Policy "camera=(), microphone=(), geolocation=(), interest-cohort=()" always;
        # CSP allows: self, self-hosted fonts/scripts (including HTMX and inline init blocks used by the site),
        # HubSpot Forms API v3 endpoints (live hotfix + Phase 04), and Cloudflare-served assets if any.
        add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://js.hsforms.net https://js.hs-scripts.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self' https://api.hsforms.com https://forms.hubspot.com; frame-src https://forms.hubspot.com; form-action 'self' https://forms.hubspot.com; base-uri 'self'; object-src 'none'; frame-ancestors 'none'" always;

        # --- WWW redirect ---
        if ($host = www.interactivemove.nl) {
            return 301 https://interactivemove.nl$request_uri;
        }

        # --- Static cache (D-15) ---
        location /media/ {
            add_header Cache-Control "public, max-age=31536000, immutable" always;
            try_files $uri =404;
        }
        location ~* \.min\.(js|css)$ {
            add_header Cache-Control "public, max-age=31536000, immutable" always;
            try_files $uri =404;
        }
        location ~* \.html$ {
            add_header Cache-Control "no-cache" always;
            try_files $uri =404;
        }

        # --- /api/chat reverse proxy (D-11, D-13) ---
        location = /api/chat {
            limit_req zone=chat burst=5 nodelay;
            limit_req_status 429;

            proxy_pass http://127.0.0.1:3860;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Connection "";

            # Streaming (SSE) support — chat proxy streams upstream tokens
            proxy_buffering off;
            proxy_cache off;
            proxy_read_timeout 120s;
            proxy_send_timeout 120s;
        }

        # --- /api/contact reserved for Phase 04 (D-12) ---
        location = /api/contact {
            proxy_pass http://127.0.0.1:3860;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            # Until Phase 04 implements the handler, upstream returns 404 — surface it as-is.
        }

        # --- Default location: static file serving ---
        location / {
            try_files $uri $uri/ $uri.html =404;
        }

        # Deny hidden files except ACME
        location ~ /\.(?!well-known) {
            deny all;
        }
    }
    ```
  </action>
  <acceptance_criteria>
    - `grep -c 'server_name interactivemove.nl' config/nginx/interactivemove.nl.conf` returns at least 2 (http + https blocks)
    - `grep -Fc 'limit_req_zone $binary_remote_addr zone=chat:10m rate=10r/m;' config/nginx/interactivemove.nl.conf` returns 1
    - `grep -Fc 'limit_req zone=chat burst=5 nodelay;' config/nginx/interactivemove.nl.conf` returns 1
    - `grep -c 'proxy_pass http://127.0.0.1:3860' config/nginx/interactivemove.nl.conf` returns 2 (one /api/chat, one /api/contact)
    - `grep -c 'Strict-Transport-Security' config/nginx/interactivemove.nl.conf` returns 1
    - `grep -c 'Content-Security-Policy' config/nginx/interactivemove.nl.conf` returns 1
    - `grep -c 'root /var/www/iam/current' config/nginx/interactivemove.nl.conf` returns 1
    - `grep -c 'return 301 https://interactivemove.nl' config/nginx/interactivemove.nl.conf` returns at least 1
    - `grep -c 'X-Forwarded-Proto \$scheme' config/nginx/interactivemove.nl.conf` returns 2
    - `grep -c 'max-age=31536000, immutable' config/nginx/interactivemove.nl.conf` returns 2
    - `grep -c 'Cache-Control "no-cache"' config/nginx/interactivemove.nl.conf` returns 1
    - `grep -c 'proxy_buffering off' config/nginx/interactivemove.nl.conf` returns 1
    - If `nginx` is installed locally: `nginx -t -c /dev/stdin < config/nginx/interactivemove.nl.conf` parses without syntax errors. If nginx is not installed: record "nginx not available locally" in the commit body and rely on grep checks.
  </acceptance_criteria>
  <verify>
    <automated>grep -Fq 'limit_req_zone $binary_remote_addr zone=chat:10m rate=10r/m;' config/nginx/interactivemove.nl.conf && grep -Fq 'limit_req zone=chat burst=5 nodelay;' config/nginx/interactivemove.nl.conf && [ "$(grep -c 'proxy_pass http://127.0.0.1:3860' config/nginx/interactivemove.nl.conf)" = "2" ] && grep -q 'Strict-Transport-Security' config/nginx/interactivemove.nl.conf && grep -q 'Content-Security-Policy' config/nginx/interactivemove.nl.conf</automated>
  </verify>
  <done>All acceptance greps pass. Commit `feat(M2-02): add interactivemove.nl nginx vhost per D-09..D-15`.</done>
</task>

<task type="auto">
  <name>Task 2: Write staging vhost iam.abbamarkt.nl.conf</name>
  <files>config/nginx/iam.abbamarkt.nl.conf</files>
  <read_first>
    - config/nginx/interactivemove.nl.conf (just created)
    - .planning/M2/phases/02-vps-deployment/CONTEXT.md (D-19)
  </read_first>
  <action>
    Mirror the prod vhost with these changes:
    - `server_name iam.abbamarkt.nl;` (no www variant for staging)
    - Certs under `/etc/letsencrypt/live/iam.abbamarkt.nl/`
    - `root /var/www/iam-staging/current;`
    - `proxy_pass http://127.0.0.1:3861;` (both `/api/chat` and `/api/contact`)
    - Separate rate-limit zone name to avoid collision: `limit_req_zone $binary_remote_addr zone=chat_staging:10m rate=10r/m;` and `limit_req zone=chat_staging burst=5 nodelay;`
    - Keep HSTS but use a shorter `max-age=3600` so staging can be toggled without painting browsers into a corner (agent discretion within D-14 spirit)
    - Same CSP as prod (staging must exercise the same policy)
    - Drop the `www.` redirect line entirely

    Use the same structure otherwise — HTTP→HTTPS redirect server, HTTPS server with static/cache/proxy locations.
  </action>
  <acceptance_criteria>
    - `grep -c 'server_name iam.abbamarkt.nl' config/nginx/iam.abbamarkt.nl.conf` returns at least 2
    - `grep -Fc 'limit_req_zone $binary_remote_addr zone=chat_staging:10m rate=10r/m;' config/nginx/iam.abbamarkt.nl.conf` returns 1
    - `grep -Fc 'limit_req zone=chat_staging burst=5 nodelay;' config/nginx/iam.abbamarkt.nl.conf` returns 1
    - `grep -c 'proxy_pass http://127.0.0.1:3861' config/nginx/iam.abbamarkt.nl.conf` returns 2
    - `grep -c 'root /var/www/iam-staging/current' config/nginx/iam.abbamarkt.nl.conf` returns 1
    - `grep -c '/etc/letsencrypt/live/iam.abbamarkt.nl/' config/nginx/iam.abbamarkt.nl.conf` returns 2 (fullchain + privkey)
    - File MUST NOT reference the prod port: `grep -c '127.0.0.1:3860' config/nginx/iam.abbamarkt.nl.conf` returns 0
    - File MUST NOT reference the prod root: `grep -c '/var/www/iam/current' config/nginx/iam.abbamarkt.nl.conf` returns 0
    - `grep -c 'max-age=3600' config/nginx/iam.abbamarkt.nl.conf` returns 1 (staging HSTS)
  </acceptance_criteria>
  <verify>
    <automated>grep -Fq 'limit_req_zone $binary_remote_addr zone=chat_staging:10m rate=10r/m;' config/nginx/iam.abbamarkt.nl.conf && [ "$(grep -c 'proxy_pass http://127.0.0.1:3861' config/nginx/iam.abbamarkt.nl.conf)" = "2" ] && ! grep -q '127.0.0.1:3860' config/nginx/iam.abbamarkt.nl.conf && ! grep -q '/var/www/iam/current[^-]' config/nginx/iam.abbamarkt.nl.conf</automated>
  </verify>
  <done>All acceptance greps pass; no prod port or root leaked into staging; commit `feat(M2-02): add iam.abbamarkt.nl nginx staging vhost per D-19`.</done>
</task>

</tasks>

<verification>
Final combined check:
```
grep -l 'proxy_pass http://127.0.0.1:3860' config/nginx/interactivemove.nl.conf
grep -l 'proxy_pass http://127.0.0.1:3861' config/nginx/iam.abbamarkt.nl.conf
# Cross-contamination check
! grep -l '127.0.0.1:3860' config/nginx/iam.abbamarkt.nl.conf
! grep -l '127.0.0.1:3861' config/nginx/interactivemove.nl.conf
```
</verification>

<success_criteria>
- Prod vhost routes /api/chat → 3860, /api/contact → 3860, serves /var/www/iam/current, TLS + full security header set, Nginx-level chat rate limit
- Staging vhost routes /api/chat → 3861, /api/contact → 3861, serves /var/www/iam-staging/current, same structure with a distinct rate-limit zone name
- Neither file contains the other environment's port or root
</success_criteria>

<output>
After completion: create `.planning/M2/phases/02-vps-deployment/02-SUMMARY.md` with the file list and the grep evidence.
</output>
