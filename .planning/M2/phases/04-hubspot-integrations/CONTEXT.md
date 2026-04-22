# M2 Phase 04: HubSpot Integrations — Context

**Gathered:** 2026-04-21
**Status:** Blocked on Phases 01-03 + IAM dev coordination
**Depends on:** Phase 01 (hardened backend), Phase 02 (VPS), Phase 03 (deploy pipeline). Also depends on the hotfix from commit `e01514c` being live in prod.

<domain>
## Phase Boundary

Promote the HubSpot Forms API v3 hotfix (commit `e01514c`) from a client-direct integration into an enterprise pattern routed through the backend. Contact form and partner form POST to `/api/contact`; the Node service validates, rate-limits, and forwards to HubSpot Forms API v3 server-to-server. Portal ID and form GUID move off the client and into server env.

Out of scope: creating new forms, transactional email pipelines beyond HubSpot's built-in notifications, CRM workflow design, adding new fields to the form in HubSpot.
</domain>

<decisions>
## Implementation Decisions

### Why this phase exists at all
- **D-01:** The hotfix in `e01514c` correctly triggers HubSpot notifications and is shippable. This phase exists because the client-direct pattern exposes portal + form GUIDs in browser source, lacks centralized validation, and can't rate-limit abusive bots independently of HubSpot's own limits. Moving through the backend fixes all three.

### Backend route
- **D-02:** Add `POST /api/contact` to the Express app built in Phase 01. Same port, same service — contact submissions and chat share the hardening middleware stack.
- **D-03:** Route accepts JSON `{ firstname, email, company, message, consent, pageUri, pageName, language? }`. All fields validated with Zod schemas. Empty strings allowed for optional fields; missing required fields returns 400.
- **D-04:** Rate limit: 5 submissions per IP per 10 minutes for `/api/contact` (tighter than chat because form submissions are lower-volume legitimate traffic).
- **D-05:** Honeypot field `website_url` must be empty; if filled, return 200 OK silently (don't tip off bots that detection succeeded). Matches current client behavior.
- **D-06:** Origin allowlist reuses the Phase 01 CORS allowlist — same two domains.
- **D-07:** Server POSTs to `https://api.hsforms.com/submissions/v3/integration/submit/${PORTAL_ID}/${FORM_GUID}` using Node's built-in `fetch`. No HubSpot SDK needed.
- **D-08:** On HubSpot success (200): return `{ ok: true }`. On HubSpot failure: return 502 with `{ ok: false, reason: 'hubspot_unavailable' }` and the client renders the mailto fallback that already exists in `js/contact-form.js`.

### Client-side change
- **D-09:** Update `js/contact-form.js` to POST to `/api/contact` on the same origin, not to `api.hsforms.com`. Remove `HUBSPOT_PORTAL_ID` and `HUBSPOT_FORM_GUID` constants from the client — they live server-side now.
- **D-10:** Payload structure stays identical to today's client → simplifies the diff. The backend shapes the HubSpot v3 `fields` array from the incoming JSON.
- **D-11:** Mailto fallback logic (fixed in `e01514c`) stays exactly as-is — only the POST target URL changes.

### Custom properties
- **D-12:** Include `page_source` (derived from `pageUri`) and `language` (NL/EN) as HubSpot fields ONLY after IAM dev confirms these custom properties exist on the form `82e91e6d-…`. Until confirmed, omit them — HubSpot v3 rejects submissions with unknown field names.
- **D-13:** If dev wants the custom properties but they don't exist in HubSpot yet, add them to the form in HubSpot UI first, then deploy the backend change. Do not deploy code expecting fields that don't exist.

### Verification
- **D-14:** End-to-end QA pass: submit contact form on prod (interactivemove.nl homepage), submit partner form NL (/word-partner), submit partner form EN (/word-partner?lang=en). All three must result in (a) HubSpot record under the published form, (b) email arriving at `klantcontact@interactivemove.nl` (check spam folder first), (c) `pageUri` in HubSpot submission correctly identifying the source page.
- **D-15:** Network-failure smoke test: disable the backend (`systemctl stop iam-api`) and submit a form → client falls through to mailto, reopens mail client with pre-filled body. Bring the service back and confirm normal flow resumes.

### agent discretion
- Exact Zod schema field definitions (build to match the form)
- Whether to log every submission for audit (recommended — pino structured log to journald)
- Whether to return HTML or JSON from `/api/contact` (JSON — client handles UI)
</decisions>

<specifics>
## Specific Ideas

- The hotfix commit `e01514c` verified end-to-end with a live `HTTP 200 {"inlineMessage":""}` response against the real form GUID. Endpoint, portal ID, and form GUID are all known-good.
- Today's `js/contact-form.js` already has honeypot, cooldown, sanitization, consent validation, and mailto fallback. Keep all of this; only swap the POST target.
- `word-partner.html` NL and EN both use `id="partnerContactForm"` (or regional suffix) and call `window.sendContactEmail(event)` — same handler as the main contact form. No second handler needed.
- HubSpot's v3 API accepts submissions with a `language` field only if the form has a custom property of that exact name. For the MVP this was explicitly skipped per user direction ("do not drift from MVP, it must WORK, then we see the rest").
</specifics>

<canonical_refs>
## Canonical References

- `.planning/M2/ROADMAP.md`
- `.planning/M2/phases/01-security-remediation/CONTEXT.md` — the backend this route extends
- Commit `e01514c` — hotfix that switched to Forms API v3 and wired the partner form
- `js/contact-form.js` — current client; target of the client-side diff
- `partials/word-partner-nl.html`, `partials/word-partner-en.html`, `word-partner.html` — partner form markup
- `partials/index-nl.html`, `partials/index-en.html` — main contact form markup
- HubSpot Forms API v3 docs: https://developers.hubspot.com/docs/api/marketing/forms
</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable
- All honeypot, cooldown, sanitization, and validation logic in `js/contact-form.js` stays. Only `submitToHubSpot()` changes — new POST target, simpler payload.
- `api/chat-proxy.js` after Phase 01 becomes the Express app that this route extends.

### Patterns
- Server-to-server call: `fetch()` with explicit timeout (AbortController), 10s budget, JSON body, structured error logging on non-2xx.
- Client-server error contract: `{ ok: true }` vs `{ ok: false, reason: '<machine_code>' }`.

### Integration points
- `/api/contact` must pass through Nginx reverse proxy configured in Phase 02 (D-12 reserved the path).
- Cloudflare WAF: if the rate limit rule from Phase 02 matches `/api/*` broadly, `/api/contact` is covered.
- HubSpot itself: notification to `klantcontact@interactivemove.nl` depends on the dev's form-level notification setting, which is already enabled per conversation history.
</code_context>

<deferred>
## Deferred Ideas

- Partner-only second HubSpot form (separate GUID, separate pipeline) — user explicitly chose single-form MVP.
- Double opt-in / GDPR consent workflow — HubSpot form has a consent checkbox; deeper GDPR workflow deferred.
- Marketing automation workflows (auto-reply, drip) — HubSpot portal concern, not code.
- Alternative CRM (Pipedrive, Salesforce) — HubSpot is the chosen platform.
- SPF/DKIM setup for `interactivemove.nl` — only needed if we want HubSpot to send FROM the domain, which isn't the current setup.
</deferred>

---

*Phase: M2-04-hubspot-integrations*
*Context gathered: 2026-04-21*
