# IAM Website — Full Review Report
Generated: 2026-03-10

## Critical Issues (blocks launch)

- [ ] **Instagram icon uses Twitter SVG path** — `index.html:752`, all shell pages, all partials with footer — The `<a href="https://www.instagram.com/interactivemove">` link uses the Twitter bird SVG path (`M23 3a10.9...`), not an Instagram icon. Visitors clicking what looks like Twitter will go to Instagram. **Fix:** Replace SVG path with proper Instagram icon (rounded rectangle + circle + dot).

- [ ] **blog.html has broken HTML structure — duplicate `</main>` tags** — `blog.html:493` and `blog.html:554` — Two `</main>` closing tags, causing malformed DOM. The footer and scripts appear outside the intended structure. **Fix:** Remove the extra `</main>` at line 493 and restructure so there's one `<main id="content-area">` wrapping all content.

- [ ] **blog.html loads scripts twice** — `blog.html:557-564` and `blog.html:765-779` — `projector.js`, `cookie-consent.js`, `iam-knowledge-base.js`, `chat-config.js`, `chat-widget.js` all loaded twice. Causes duplicate chat bubbles, double event listeners, and potential errors. **Fix:** Remove the duplicate script block (lines 565-582 approximately).

- [ ] **blog.html references non-existent `js/reveal.js`** — `blog.html` loads `js/reveal.js` which returns 404. **Fix:** Remove the `<script src="js/reveal.js"></script>` line; reveal functionality is already in `site.js`.

- [ ] **GTM loads before cookie consent — GDPR violation** — All shell pages (`index.html:12`, etc.) — Google Tag Manager script loads unconditionally in `<head>` before any cookie consent is obtained. The cookie-consent.js banner is cosmetic only — it doesn't gate GTM loading. **Fix:** Wrap GTM loading in a function that only fires after consent is granted (`choice === 'all'`).

- [ ] **Chat proxy is down** — `curl http://172.17.0.1:3860/health` returns connection refused (000). The chat widget at `/api/chat` will fail silently for users. **Fix:** Ensure the chat proxy service is running, or add a visible fallback message.

- [ ] **`/contact` URL returns 404** — `docker/nginx/default.conf:33` — The rewrite `rewrite ^ /index.html#contact last;` doesn't work because nginx can't handle fragment identifiers (`#contact`) in rewrites — the `#` is stripped. The nav links to `index.html#contact` directly which works, but anyone typing `/contact` in the browser gets a 404. **Fix:** Rewrite to `/index.html` and handle the scroll client-side, or use a proper redirect: `return 302 /#contact;`.

- [ ] **Dutch typo in privacy consent** — `index.html:722`, `partials/index-nl.html:613` — "gegevens" is misspelled as "gegevens" (actually "gegevens" → checking again... it says "gegevens" which is correct, wait: `mijn gegevens` — the correct Dutch is `mijn gegevens`. Let me recheck... The text says "gegevens" which IS correct.) — **RETRACTED, not an issue.**

## Visual/Design Issues

- [ ] **Instagram social link uses Twitter bird icon** — All pages (footer) — Users see a bird icon next to the Instagram link. Visually confusing and unprofessional. Affects all 22 shell pages + 26 partials with footers.

- [ ] **Homepage flagship 2-in-1 product card: 2-column grid breaks on mobile** — `index.html` inline styles: `grid-template-columns: 1fr 1fr` — No responsive override. On mobile (<768px) the two columns will be too narrow. **Fix:** Add `@media (max-width: 768px) { grid-template-columns: 1fr; }` or use a class instead of inline styles.

- [ ] **Excessive inline styles throughout index.html** — `index.html` lines 343-420 (flagship card), lines 499+ (product cards) — Heavy use of `style="..."` instead of CSS classes. Makes the design inconsistent and hard to maintain. At least 50+ inline style attributes on the homepage alone.

- [ ] **logo-final.png is 235KB** — `media/logo-final.png` — Very large for a logo that appears on every page. Should be <20KB. **Fix:** Convert to SVG or compress PNG aggressively / use WebP.

## Code Quality Issues

- [ ] **Ghost API key exposed in client-side JS** — `js/blog-carousel.js:3` — `const GHOST_KEY = 'b8903092a7c9a8b54d7378f5a1';` — Content API keys are technically public/read-only, but best practice is to proxy through your backend. Low risk but worth noting.

- [ ] **blog-carousel.js uses hardcoded `blog.html?post=` URL** — `js/blog-carousel.js:29` — `'<a href="blog.html?post=' + post.slug + '"...'` — This relative URL breaks when the carousel is loaded on product pages (where base is `../`). On product pages the link would go to `products/blog.html?post=...` (404). **Fix:** Use absolute path: `/blog?post=`.

- [ ] **blog-carousel "Lees meer" not translated** — `js/blog-carousel.js:34` — The "Lees meer →" text is hardcoded Dutch even when `lang=en`. **Fix:** Check `isEn` variable and use "Read more →" when English.

- [ ] **blog-carousel date format hardcoded Dutch** — `js/blog-carousel.js:22` — `toLocaleDateString('nl-NL', ...)` — Should use `'en-GB'` or similar when `isEn` is true.

- [ ] **Inconsistent JS path references** — Some pages use `/js/site.js` (absolute) while chat/knowledge scripts use `js/chat-widget.js` (relative) or `../js/chat-widget.js`. Product pages use `../js/` for chat but `/js/` for site.js. This works but is inconsistent. **Fix:** Use absolute paths (`/js/...`) everywhere.

- [ ] **`projector.js` loaded as relative path** — All shell pages use `src="projector.js"` (relative), product pages use `src="../projector.js"`. **Fix:** Use `/projector.js` everywhere for consistency.

- [ ] **Cookie consent uses `localStorage` not cookies** — `js/cookie-consent.js:15-18` — Consent stored in `localStorage` which is not accessible server-side. If GTM/analytics decisions need to be made server-side, this won't work. Minor issue for a static site.

- [ ] **`switchLang()` called on DOMContentLoaded when not NL** — `js/site.js:109-111` — When `lang=en`, `switchLang('en')` fires which does an HTMX fetch. But the page already has NL content loaded as server-rendered HTML, causing a visible flash of Dutch → English. **Fix:** Server-side render the correct language partial, or hide `#content-area` until swap completes.

- [ ] **No `blog-carousel.js` loaded on blog.html** — `blog.html` doesn't load `blog-carousel.js` — only `index.html` does. The blog page has its own inline blog loading logic. This is fine but means blog-carousel is index-only. Consistent but worth documenting.

## SEO & Accessibility Gaps

- [ ] **No Open Graph meta tags on any page** — All 22 pages — No `og:title`, `og:description`, `og:image`, or `og:url` tags. Social sharing will show generic or no previews. **Fix:** Add OG tags to every shell page `<head>`.

- [ ] **No canonical URLs on any page** — All 22 pages — No `<link rel="canonical" ...>` tag. Risk of duplicate content issues (with/without `.html`, with/without `?lang=`). **Fix:** Add canonical tags pointing to the clean URL.

- [ ] **No `hreflang` tags for language alternates** — All pages — Since the site is bilingual (NL/EN via query param), there should be `<link rel="alternate" hreflang="nl" ...>` and `<link rel="alternate" hreflang="en" ...>` tags for proper SEO.

- [ ] **SVG icons lack proper alt text** — Homepage and all pages — Inline SVGs in spec cards, practical icons, footer social links, etc. use `fill="currentColor"` but many lack `aria-label` or `role="img"`. Screen readers may announce path data. **Fix:** Add `role="img" aria-hidden="true"` to decorative SVGs, proper `aria-label` to meaningful ones.

- [ ] **Heading hierarchy issues on homepage** — `index.html` — Trust bar section uses `<p class="trust-label">` where an `<h2>` might be more semantic. Client logos section uses `<p class="logos-label">` instead of heading. FAQ section has `<h2>` after product section `<h2>` which is correct, but `<summary>` elements act as implicit headings without heading semantics.

- [ ] **`skip-link` target `#main-content` doesn't exist** — All shell pages have `<a href="#main-content" class="skip-link">` but the main element has `id="content-area"`, not `id="main-content"`. **Fix:** Change skip link to `#content-area` or add `id="main-content"` to the `<main>` element.

- [ ] **Contact form validation has no visible error messages** — `js/contact-form.js:72-82` — Validation silently returns without telling the user what's wrong (empty name, invalid email, unchecked consent). **Fix:** Add visible inline error messages.

## Performance Issues

- [ ] **26MB video file** — `media/video/2-in-1-floor-wall.mp4` (26MB) — Extremely large. Will cause slow page loads on product pages that use it. **Fix:** Compress to <5MB, use adaptive bitrate, or host on a CDN/YouTube.

- [ ] **Hero video served as two formats (9MB total)** — `media/hero-video.mp4` (3.8MB) + `media/hero-video.webm` (5.2MB) — Both are loaded in the `<video>` tag. Browser only uses one, but total served could be optimized. WebM should be smaller than MP4, not larger. **Fix:** Re-encode WebM with better compression.

- [ ] **styles.css is 116KB (5863 lines) — unminified** — `styles.css` — No minification, no gzip evident at nginx config level (check if gzip module is enabled). **Fix:** Minify CSS for production. Enable gzip in nginx if not already.

- [ ] **8+ JS files loaded per page** — Every page loads: htmx.min.js, projector.js, site.js, cookie-consent.js, contact-form.js, hs-scripts, iam-knowledge-base.js, chat-config.js, chat-widget.js. That's 9 scripts. **Fix:** Bundle non-vendor scripts into one file.

- [ ] **Images are unoptimized PNGs (600KB-960KB each)** — `media/hero_parken_speelhallen.png` (962KB), `media/park-map.png` (943KB), `media/hero_interactieve_muur.png` (858KB) — These should be WebP or compressed JPEG. **Fix:** Convert hero images to WebP with fallback, target <200KB each.

- [ ] **No `loading="lazy"` on most images** — Homepage product section SVG icons are inline (fine), but product pages and solution pages likely have `<img>` tags without lazy loading.

- [ ] **Nginx caching headers lost on HTML pages** — `docker/nginx/default.conf` — Cache headers only set inside `location ~* \.(css|js|...)` block which is nested inside `location / { try_files... }`. The nested `add_header Cache-Control` inside the regex location overrides the parent's security headers due to nginx's `add_header` inheritance behavior — security headers are LOST on static assets. **Fix:** Repeat security headers in the nested location block or use `include` directive.

## Broken/Missing Features

- [ ] **Chat proxy not running** — Chat widget (`/api/chat`) proxies to `http://172.17.0.1:3860` which is not responding. All chat messages will fail. Users see "Er ging iets mis" error.

- [ ] **Blog carousel links break from product pages** — `js/blog-carousel.js:29` — Uses relative `blog.html?post=slug` URL. Won't break because blog-carousel.js is only loaded on index.html, but if it were ever added to product pages the links would 404.

- [ ] **Language switch flashes Dutch content before English loads** — `js/site.js:109` — On page load with `?lang=en`, the NL server-rendered content shows briefly before the EN partial is fetched via HTMX.

- [ ] **`/contact` route returns 404** — See Critical Issues above.

## Nice to Have / Improvements

- [ ] **Add WebP versions of all images with `<picture>` fallback** — All product and hero images are PNG. WebP would reduce sizes by 50-70%.

- [ ] **Bundle and minify JavaScript** — 9 separate JS files could be bundled into 2-3 (vendor, app, chat).

- [ ] **Add structured data (JSON-LD)** — No Schema.org markup for Organization, Product, FAQ, or BreadcrumbList. Would significantly help SEO.

- [ ] **Add `rel="noopener"` to all `target="_blank"` links** — Footer social links have `target="_blank"` but no `rel="noopener noreferrer"` (security best practice). Some do have it (oopuo link), inconsistent.

- [ ] **Move inline styles to CSS classes** — Homepage has 50+ inline `style="..."` attributes. Creates maintenance burden and inconsistency.

- [ ] **Add error page (404.html, 500.html)** — No custom error pages configured in nginx. Default nginx error page will show.

- [ ] **Consider server-side language routing** — Current client-side HTMX swap causes content flash. Server-side detection (Accept-Language header or cookie) would be smoother.

- [ ] **Add `preconnect` hints** — For `fonts.googleapis.com`, `www.googletagmanager.com`, `forms.hubspot.com` — reduces connection setup time.

- [ ] **CSP allows `unsafe-inline` and `unsafe-eval` for scripts** — `docker/nginx/default.conf` CSP header — Weakens XSS protection significantly. **Fix:** Use nonces or hashes for inline scripts, remove `unsafe-eval` if not needed.

- [ ] **Sitemap exists but uses hardcoded domain** — `sitemap.xml` references `https://interactivemove.nl/` — ensure this matches the production domain exactly and includes all pages including product clean URLs.

- [ ] **Add `<meta name="robots" content="index, follow">` explicitly** — While `robots.txt` allows all, explicit meta robots tags give more control per page.

- [ ] **Cookie consent: no "manage preferences" granularity** — Current consent is binary (all or necessary). GDPR best practice is granular control (analytics vs marketing separately). The `saveConsent()` function has fields for `analytics` and `marketing` but the UI only offers accept-all or reject-all.
