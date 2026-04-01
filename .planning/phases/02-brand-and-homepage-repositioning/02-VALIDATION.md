---
phase: 2
slug: brand-and-homepage-repositioning
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-01
---

# Phase 2 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | bash + grep (static HTML site — no test framework) |
| **Config file** | none |
| **Quick run command** | `bash .planning/phases/01-safe-update-surface/tools/phrase-audit.sh --summary 2>/dev/null \| head -10` |
| **Full suite command** | `bash .planning/phases/01-safe-update-surface/tools/phrase-audit.sh` |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Grep verify target file for expected content
- **After every plan wave:** Run phrase-audit.sh to confirm reduction in legacy hits
- **Before `/gsd:verify-work`:** Full audit must show zero legacy phrases on homepage, prijzen, over-ons
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 02-01-01 | 01 | 1 | HOME-01 | grep | `grep -l "2in1" index.html partials/index-nl.html partials/index-en.html` | ✅ | ⬜ pending |
| 02-01-02 | 01 | 1 | HOME-02 | grep | `grep -c "interactive programs\|interactieve programma" partials/index-en.html partials/index-nl.html` | ✅ | ⬜ pending |
| 02-02-01 | 02 | 1 | BRND-01,BRND-02,BRND-03 | grep | `grep -ci "spellen\|games" index.html partials/index-nl.html partials/index-en.html` | ✅ | ⬜ pending |
| 02-02-02 | 02 | 1 | BRND-03 | grep | `grep -ci "spellen\|games" partials/prijzen-nl.html partials/prijzen-en.html partials/over-ons-nl.html partials/over-ons-en.html` | ✅ | ⬜ pending |
| 02-03-01 | 03 | 2 | BRND-01,HOME-01,HOME-02 | diff | `diff <(grep -n "spellen\|games\|FAQ" index.html) <(grep -n "spellen\|games\|FAQ" partials/index-nl.html)` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- Existing infrastructure covers all phase requirements — phrase-audit.sh from Phase 1 provides reusable audit tooling. No additional test framework needed.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Product image renders correctly | HOME-01 | Visual check — grep can confirm img tag but not rendering | Open index.html in browser, verify 2-in-1 housing photo displays in product card |
| FAQ answer reads naturally in both languages | HOME-02 | Content quality — automated check confirms text presence but not readability | Read FAQ section in NL and EN, confirm answer is clear and professional |
| Language toggle works after changes | BRND-01 | HTMX swap behavior | Click NL/EN toggle on homepage, verify content switches cleanly |

---

## Validation Sign-Off

- [ ] All tasks have automated verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
