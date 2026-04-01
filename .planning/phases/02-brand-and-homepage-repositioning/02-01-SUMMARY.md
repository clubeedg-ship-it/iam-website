---
phase: 02-brand-and-homepage-repositioning
plan: 01
subsystem: homepage
tags: [homepage, terminology, product-image, faq, bilingual]
dependency_graph:
  requires: []
  provides: [homepage-imagery-updated, homepage-faq-updated, homepage-terminology-corrected]
  affects: [partials/index-nl.html, partials/index-en.html, index.html]
tech_stack:
  added: []
  patterns: [bilingual-file-family-sync]
key_files:
  created: []
  modified:
    - index.html
    - partials/index-nl.html
    - partials/index-en.html
decisions:
  - "Preserved multiline formatting in software card description to match existing code style"
metrics:
  duration: "2min 15s"
  completed: "2026-04-01T20:35:00Z"
  tasks_completed: 2
  tasks_total: 2
  files_modified: 3
---

# Phase 02 Plan 01: Update Homepage Product Imagery and FAQ Content Summary

Replace yellow SVG placeholder with real 2-in-1 housing photo, update stat counter and product card terminology from spellen/games to programma's/programs, and replace FAQ 4th item with approved interactive programs question and answer.

## Tasks Completed

### Task 1: Replace SVG placeholder with product image and update stat counter + product card text
- **Commit:** 3663fc8
- **Changes:**
  - Replaced yellow SVG placeholder block (rgba(254,186,4) background, 80x80 SVG, "2-in-1" label, "Vloer + Muur" text) with real product photo `media/products/2in1/1.png`
  - Updated stat counter label from "Spellen Beschikbaar" to "Programma's Beschikbaar" (NL) and "Games Available" to "Programs Available" (EN)
  - Updated 2-in-1 product card description from "interactieve spellen" to "interactieve programma's" (NL) and "interactive games" to "interactive programs" (EN)
  - Updated software card description from "interactieve spellen" to "interactieve programma's" (NL) and "interactive games" to "interactive programs" (EN)
  - All edits applied consistently across index.html, partials/index-nl.html, partials/index-en.html

### Task 2: Replace FAQ question and answer with approved text
- **Commit:** 6f5c95f
- **Changes:**
  - Replaced 4th FAQ item question from "Hoeveel spellen zijn er beschikbaar?" to "Hoeveel interactieve programma's zijn er beschikbaar?" (NL)
  - Replaced 4th FAQ item question from "How many games are available?" to "How many interactive programs are available?" (EN)
  - Replaced FAQ answer with approved text about product-dependent program availability (verbatim from change brief)
  - All old "spellen/games" content removed from FAQ section across all 3 files

## Deviations from Plan

None -- plan executed exactly as written.

## Verification Results

- SVG placeholder fully removed: no `rgba(254,186,4` or `svg.*80.*80` in any file (PASS)
- Real product image: `media/products/2in1/1.png` present in all 3 files (PASS)
- Stat counter updated: "Programma's Beschikbaar" in NL files, "Programs Available" in EN file (PASS)
- Product card + software card use "programma's" / "programs" (PASS)
- FAQ uses approved question and answer verbatim (PASS)
- Shell (index.html) NL content matches NL partial for all changed sections (PASS)
- Nav links untouched: "3D Spellen/Games" nav references preserved at lines 46 and 96 in index.html (PASS)
- NL partial has zero remaining "spellen/Spellen" occurrences (PASS)
- EN partial has only "Game Editor" as remaining "game" reference (PASS, product name)

## Known Stubs

None -- all changes are fully wired with real data.

## Self-Check: PASSED
