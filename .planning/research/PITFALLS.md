# Research: Pitfalls

**Project:** IAM Website Repositioning
**Domain:** Brownfield marketing-site refresh
**Researched:** 2026-04-01
**Confidence:** HIGH

## Pitfall 1: Partial Update Rollout

**Problem:** Updating one page variant but not the matching NL/EN partials leaves the public site inconsistent.

**Warning signs:**
- Same claim still appears in search results or in one language only
- `rg` shows old phrases remaining after an edit

**Prevention:**
- Treat each requested change as a file-family update
- Audit for old phrases like `2-in-1`, `free updates`, `100+ games`, and `Choose Your Package`

**Phase to address:** Phase 1 and final release hardening

## Pitfall 2: Repositioning Without Clear Package Logic

**Problem:** Renaming to `IAM mobiel` without clearly separating `solo`, `duo`, and `premium` leaves users more confused, not less.

**Warning signs:**
- Same page still mixes old and new names
- Single-use and dual-use variants are not clearly distinguished

**Prevention:**
- Define the package ladder first
- Apply naming consistently before polishing supporting pages

**Phase to address:** Package refresh phase

## Pitfall 3: Asset Credibility Gaps

**Problem:** Visible screws or mismatched imagery undermine premium product positioning.

**Warning signs:**
- Old housing photos remain in product galleries
- New copy promises a polished product while images look provisional

**Prevention:**
- Identify approved replacement assets early
- If retouching is not available, remove the weak images instead of leaving them live

**Phase to address:** Product cleanup phase

## Pitfall 4: Over-Editing the Stack

**Problem:** Refactoring structure or replatforming during a content refresh expands scope and delays business value.

**Warning signs:**
- Work starts drifting toward framework or CMS decisions
- Page changes block on tooling rather than copy approval

**Prevention:**
- Keep the existing stack
- Restrict scope to safe, necessary structural cleanup

**Phase to address:** Entire project

## Pitfall 5: Broken Links After Section/Page Removal

**Problem:** Removing pages or blocks without updating navigation and internal links creates dead ends.

**Warning signs:**
- Navigation still points to removed routes
- Sitemap or footer still advertises removed content

**Prevention:**
- Treat removals as route-level changes
- Verify navigation, footer, sitemap, and cross-links before release

**Phase to address:** Final cleanup and release phase
