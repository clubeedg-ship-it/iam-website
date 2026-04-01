---
phase: 1
slug: safe-update-surface
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-01
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | bash + grep (no test framework — this phase produces documentation and a shell script) |
| **Config file** | none — outputs are markdown inventory and audit script |
| **Quick run command** | `bash .planning/phases/01-safe-update-surface/audit-phrases.sh 2>/dev/null | head -20` |
| **Full suite command** | `bash .planning/phases/01-safe-update-surface/audit-phrases.sh` |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run quick audit command
- **After every plan wave:** Run full audit
- **Before `/gsd:verify-work`:** Full audit must produce expected output
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 01-01-01 | 01 | 1 | QLTY-01 | file check | `test -f .planning/phases/01-safe-update-surface/FILE-INVENTORY.md` | ❌ W0 | ⬜ pending |
| 01-02-01 | 02 | 1 | QLTY-02 | script check | `test -x .planning/phases/01-safe-update-surface/audit-phrases.sh` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- Existing infrastructure covers all phase requirements — outputs are documentation and a shell script, no test framework needed.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Inventory completeness | QLTY-01 | Must visually confirm all page families are listed | Review FILE-INVENTORY.md against `ls *.html products/*.html partials/*.html partials/products/*.html` |
| Removal dependency accuracy | QLTY-01 | Must confirm nav references are correctly counted | Spot-check 2-3 removal targets against grep output |

---

## Validation Sign-Off

- [ ] All tasks have automated verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
