# M2 Phase 04 — HubSpot Integrations Handoff Checklist

> Autonomous run wrote backend `/api/contact` + client switch + smoke suite. Three classes of work remain for the IAM dev: (1) confirm HubSpot portal/form IDs and put them in env files, (2) confirm custom properties before enabling them, (3) end-to-end QA on prod.

## 1. Env vars required on the VPS

Set in `/etc/iam-api/env` (prod) and `/etc/iam-api-staging/env` (staging) — the templates from Phase 02 already have placeholders:

| Var | Needed for | Current value in templates |
|-----|------------|----------------------------|
| `HUBSPOT_PORTAL_ID` | `/api/contact` target URL | `REPLACE_ME_HUBSPOT_PORTAL_ID` |
| `HUBSPOT_CONTACT_FORM_GUID` | `/api/contact` target URL | `REPLACE_ME_HUBSPOT_CONTACT_FORM_GUID` |
| `HUBSPOT_PARTNER_FORM_GUID` | Reserved (MVP uses single GUID; future split) | `REPLACE_ME_HUBSPOT_PARTNER_FORM_GUID` |

**Known-good values from hotfix `e01514c`** (verify before copying into env — these may rotate):
- Portal ID: `49291889`
- Contact form GUID: `82e91e6d-7a36-47a4-8171-9f213e17fcb5`

After updating env, `sudo systemctl reload iam-api iam-api-staging`.

If either var is unset, `/api/contact` returns `503 {ok:false, reason:'hubspot_config_missing'}` and the client falls through to the mailto fallback — site stays functional, just no CRM capture.

## 2. HubSpot custom properties — confirm before enabling

Per D-12/D-13, the backend currently does NOT send `page_source` or `language` fields. Those are present in the client payload (`pageUri`, `language`) and available to the route, but `toHubSpotFields()` in `api/contact-route.js` omits them.

Before enabling:
1. In HubSpot → Forms → edit the contact form `82e91e6d-…` → **Add field**.
2. Add `page_source` (single-line text) and `language` (single-select: NL/EN).
3. Save the form. Confirm in the form API preview that these fields now appear.
4. Update `api/contact-route.js` → `toHubSpotFields()` to add:
   ```
   if (parsed.pageUri)  fields.push({ name: 'page_source', value: parsed.pageUri });
   if (parsed.language) fields.push({ name: 'language',    value: parsed.language });
   ```
5. Deploy. Test one submission end-to-end.

Skipping step 1-3 and deploying step 4 will cause HubSpot to reject submissions with "field does not exist", and `/api/contact` will 502.

## 3. End-to-end QA (D-14)

After prod deploy is green:

1. Submit the main contact form on `https://interactivemove.nl/` with a recognizable test name (e.g. `CLAUDE-TEST`). Confirm:
   - Browser sees `{ok:true}`.
   - HubSpot shows a record under the contact form.
   - Email lands at `klantcontact@interactivemove.nl` (check spam first).
2. Submit the partner form at `https://interactivemove.nl/word-partner` (NL). Same checks.
3. Submit the partner form EN at `https://interactivemove.nl/word-partner?lang=en`. Same checks.
4. Delete the `CLAUDE-TEST` records from HubSpot after QA.

## 4. Network-failure smoke (D-15)

On the VPS:
```
sudo systemctl stop iam-api
# Submit the form in a browser — should fall through to mailto
sudo systemctl start iam-api
# Submit again — should succeed
```

## 5. Open questions

- Confirm the two `REPLACE_ME_HUBSPOT_*_FORM_GUID` values are identical (single-form MVP) or need to diverge for partner routing.
- Confirm whether honeypot name `website_url` matches any real HubSpot field on the form — if it does, HubSpot will see (and ignore) empty-string submissions for it, which is fine, but the coincidence is worth knowing.

## 6. What still works if Phase 04 is partially rolled out

- If only env vars are missing but code is deployed → 503 from backend, client mailto fallback kicks in. Site still captures leads via email.
- If only code is deployed but env vars are correct → same 503; the `/api/contact` check is strict.
- If both are deployed correctly but HubSpot upstream is down → 502, mailto fallback kicks in.
