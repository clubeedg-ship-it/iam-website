# IAM Website Repositioning

## What This Is

This project turns the existing InterActiveMove marketing website into a cleaner, more accurate bilingual sales site for the current product story. The immediate focus is repositioning the mobile product line around `IAM mobiel`, correcting outdated claims and visuals, and making sure Dutch and English pages stay aligned across the brownfield HTML/HTMX codebase.

## Core Value

Prospective customers should immediately understand what IAM sells now, what the `IAM mobiel` options are, and how to contact the team without being confused by outdated names, package structures, or duplicated copy.

## Requirements

### Validated

- ✓ Bilingual static website with Dutch and English page variants via HTMX partial swaps — existing
- ✓ Product, sector, pricing, and company information pages are already published — existing
- ✓ Media-rich marketing presentation with direct contact CTAs is already established — existing
- ✓ All affected routes and file families inventoried with drift detection — validated in Phase 1
- ✓ Legacy phrase audit tooling established for the refresh — validated in Phase 1
- ✓ Homepage and primary selling pages use current "programs" terminology and real product imagery — validated in Phase 2
- ✓ Homepage FAQ uses approved interactive programs question and answer in NL/EN — validated in Phase 2

### Active

- [ ] Reposition the mobile product line under the stronger umbrella name `IAM mobiel`
- [ ] Update homepage and product-page copy so package names, counts, and value claims reflect the current offer
- [ ] Remove or revise outdated sections and pages requested in `website-adjustments.xlsx`
- [ ] Keep Dutch and English variants synchronized for every affected route
- [ ] Ship the refresh without breaking navigation, media loading, or HTMX language swaps

### Out of Scope

- Full visual redesign or replatform to a CMS — current request is a brownfield content and positioning refresh, not a rebuild
- Backend forms, analytics, or ecommerce integrations — no such scope is indicated by the current site or adjustment brief
- Broad product-strategy invention beyond the supplied spreadsheet direction — the site should clarify the current offer, not create a new business model

## Context

This repo is a static website built from hand-authored HTML, one shared stylesheet, and browser-global JavaScript. The current architecture duplicates content across full pages and `partials/`, so business copy changes are operationally risky unless handled systematically. The uploaded spreadsheet `website-adjustments.xlsx` is the clearest source of intent: it requests homepage updates, FAQ replacement, terminology shifts from `games`/`free updates` to `programs`/`no license costs`, a package restructure around `IAM mobiel`, image cleanup for visible screws, and removal or revision of several page sections.

The existing codebase already serves as the brownfield baseline. `.planning/codebase/*.md` captures the stack, structure, conventions, and the main maintenance concern: duplicated NL/EN content with no single source of truth.

## Constraints

- **Tech stack**: Keep the current static HTML + CSS + HTMX + vanilla JS stack — the request is to update the existing site safely, not to rebuild it
- **Content consistency**: Changes must be applied across full pages and partials — otherwise NL/EN and canonical/partial variants will drift
- **Path safety**: Root pages and nested product pages use different relative paths — content reuse must preserve working asset and partial links
- **Brownfield safety**: Existing published routes, navigation, and contact flows must keep working during the refresh

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Treat this as a brownfield website refresh, not a new-site build | Existing site, media library, navigation, and localization system already exist | — Pending |
| Use `IAM mobiel` as the umbrella framing for the mobile line | The spreadsheet explicitly states this is stronger and more accurate than calling every variant `2-in-1` | — Pending |
| Preserve the current stack for v1 of the refresh | Lowest-risk path for a content-heavy static website with many duplicated files | — Pending |
| Prioritize content accuracy and bilingual consistency before broader optimization | The main business risk is outdated or contradictory public messaging | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `$gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `$gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-01 after Phase 2 completion*
