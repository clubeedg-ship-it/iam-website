# Roadmap: IAM Website Repositioning

## Overview

This roadmap moves the existing InterActiveMove site from a partially outdated brownfield state to a commercially accurate bilingual release centered on `IAM mobiel`. The sequence favors safe file-family auditing first, then high-visibility messaging changes, then package restructuring, then detailed product cleanup, and finally bilingual release hardening.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Safe Update Surface** - Inventory affected file families and establish a safe baseline for brownfield edits
- [ ] **Phase 2: Brand and Homepage Repositioning** - Correct the public-facing top-level story around `IAM mobiel`
- [ ] **Phase 3: IAM Mobiel Package Refresh** - Restructure the mobile offer into `solo`, `duo`, and `premium`
- [ ] **Phase 4: Product Detail Cleanup** - Remove stale claims, fix counts, and correct weak imagery on affected product pages
- [ ] **Phase 5: Bilingual Release Hardening** - Synchronize NL/EN variants and validate route, link, and asset integrity

## Phase Details

### Phase 1: Safe Update Surface
**Goal**: Establish the canonical edit surfaces and remove release risk before broad copy changes start.
**Depends on**: Nothing (first phase)
**Requirements**: [QLTY-01, QLTY-02]
**UI hint**: no
**Success Criteria** (what must be TRUE):
  1. All affected routes and duplicated file families are identified before execution proceeds
  2. Legacy phrases targeted by the refresh can be audited reliably across the codebase
  3. A change plan exists for removals so navigation and route integrity are not broken accidentally
**Plans**: 2 plans

Plans:
- [x] 01-01: Build the canonical file inventory for homepage, pricing, mobile-product, and removal targets
- [x] 01-02: Add phrase-audit and route-check workflow for the requested refresh terms

### Phase 2: Brand and Homepage Repositioning
**Goal**: Update the highest-visibility pages so visitors immediately get the current IAM message.
**Depends on**: Phase 1
**Requirements**: [BRND-01, BRND-02, BRND-03, HOME-01, HOME-02]
**UI hint**: yes
**Success Criteria** (what must be TRUE):
  1. Homepage copy and visuals reflect the approved `IAM mobiel` framing
  2. Homepage FAQ uses the approved question and answer about interactive programs
  3. Primary selling pages stop using outdated umbrella wording where it creates confusion
  4. Updated homepage content still renders correctly in both languages
**Plans**: 3 plans

Plans:
- [x] 02-01: Update homepage product imagery and FAQ content
- [x] 02-02: Apply top-level brand and terminology corrections to the main selling surfaces
- [x] 02-03: Sync homepage and core partial variants after the copy shift

### Phase 3: IAM Mobiel Package Refresh
**Goal**: Rebuild the mobile-line offer presentation around the approved package ladder and pricing.
**Depends on**: Phase 2
**Requirements**: [MOBL-01, MOBL-02, MOBL-03]
**UI hint**: yes
**Success Criteria** (what must be TRUE):
  1. Visitors can clearly distinguish `solo`, `duo`, and `premium`
  2. Package descriptions explain floor-only, wall-only, dual-use, and expandability correctly
  3. Package pricing and value language match the approved commercial brief
**Plans**: 3 plans

Plans:
- [ ] 03-01: Restructure package taxonomy and headings for the mobile line
- [ ] 03-02: Rewrite package descriptions, pricing, and supporting value statements
- [ ] 03-03: Validate package presentation across pricing and product-related pages

### Phase 4: Product Detail Cleanup
**Goal**: Clean up the detailed product pages so counts, terminology, and imagery match the refreshed offer.
**Depends on**: Phase 3
**Requirements**: [PROD-01, PROD-02, PROD-04]
**UI hint**: yes
**Success Criteria** (what must be TRUE):
  1. Affected product pages no longer advertise outdated `free updates` language
  2. Requested counts and terms are updated consistently on the affected product surfaces
  3. Weak housing imagery is replaced, retouched, or removed so the page no longer shows visible screws
**Plans**: 3 plans

Plans:
- [ ] 04-01: Replace outdated copy and counts across affected product-page families
- [ ] 04-02: Correct or remove weak image assets in the mobile-product presentation
- [ ] 04-03: Reconcile product-detail pages and their partial variants

### Phase 5: Bilingual Release Hardening
**Goal**: Finalize the refresh by removing obsolete sections/pages and verifying bilingual release quality.
**Depends on**: Phase 4
**Requirements**: [PROD-03, I18N-01, I18N-02]
**UI hint**: yes
**Success Criteria** (what must be TRUE):
  1. Obsolete sections or pages requested in the brief are removed or hidden without leaving broken paths behind
  2. Dutch and English pages both reflect the approved refresh
  3. Language toggles, navigation, internal links, and assets work on all refreshed routes
**Plans**: 3 plans

Plans:
- [ ] 05-01: Remove or revise obsolete sections/pages and update route references
- [ ] 05-02: Perform full NL/EN parity pass across affected routes
- [ ] 05-03: Run release verification for links, assets, and HTMX swap behavior

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Safe Update Surface | 0/2 | Not started | - |
| 2. Brand and Homepage Repositioning | 1/3 | In Progress|  |
| 3. IAM Mobiel Package Refresh | 0/3 | Not started | - |
| 4. Product Detail Cleanup | 0/3 | Not started | - |
| 5. Bilingual Release Hardening | 0/3 | Not started | - |
