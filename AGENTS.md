## Project Guide

This repository uses GSD planning artifacts in `.planning/` as the source of truth for project intent, scope, and execution order.

Read these first before making substantive changes:
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/codebase/*.md`

## Workflow

Use GSD commands for tracked work:
- `$gsd-discuss-phase 1` to gather execution context
- `$gsd-plan-phase 1` to create the first executable plan
- `$gsd-execute-phase 1` only after planning exists

## Current Project

This is a brownfield static marketing website refresh for InterActiveMove.
Primary goals:
- reposition the mobile line under `IAM mobiel`
- correct outdated messaging, imagery, and package structure
- keep Dutch and English variants synchronized

## Codebase Notes

- The site is static HTML + CSS + vanilla JS with HTMX partial swaps
- Content is duplicated across full pages and partials
- Edits must account for root pages, nested product pages, and NL/EN partials together

## Safety

- Prefer systematic phrase audits over one-file edits
- Preserve working navigation, asset paths, and language swaps
- Do not treat this refresh as a redesign or replatform unless scope changes explicitly
