# Research: Stack

**Project:** IAM Website Repositioning
**Domain:** Brownfield bilingual marketing website refresh
**Researched:** 2026-04-01
**Confidence:** HIGH

## Recommendation

Keep the existing static-site stack for this initiative. The requested work is content, packaging, terminology, image, and page-structure correction on top of an already functioning brochure site. A platform rewrite would add scope without improving the immediate business outcome.

## Recommended Stack

- **HTML entry pages + localized partials**: Continue using the existing page model because the current site is already published in that structure
- **Shared CSS in `styles.css`**: Reuse the current visual system and limit changes to content-driven styling or small layout adjustments
- **Vanilla JavaScript in `projector.js` and inline helpers**: Keep current browser behavior and only change JS where the content update requires it
- **HTMX language swaps**: Preserve current bilingual navigation behavior; verify that affected routes still load their partials correctly
- **One-off scripts for content sync**: If repetition becomes too error-prone, use repo-local scripts for audit or propagation, not a new runtime framework

## What Not To Introduce

- Full frontend framework migration
- CMS integration
- Backend services
- Build tooling added solely for this refresh

## Why

The dominant project risk is content drift across duplicated files, not runtime capability. The highest-leverage stack move is to keep the current delivery model and improve editing discipline, validation, and synchronization across files.

## Confidence Notes

- High confidence because the existing stack is fully visible in the repo
- High confidence because the requested changes are mostly editorial and structural within existing pages
- Medium confidence only on whether a helper script may be needed to reduce duplication during execution

## Roadmap Implications

- Early phases should identify canonical edit surfaces before changing copy broadly
- Release hardening should include bilingual and path validation, not stack work
