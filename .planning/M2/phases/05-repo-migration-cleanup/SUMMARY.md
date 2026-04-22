# M2 Phase 05: Repo Migration + Cleanup — Summary

**Branch:** `m2/phase-05` (branched from `m2/phase-04`)
**Completed:** 2026-04-21
**Commits:** 3
**Status:** Code-side complete. Cutover is a future human action governed by `CUTOVER-RUNBOOK.md`; explicitly prohibited in this run.

## Cutover prohibition honored

Per the session override: no new repo created, no `oopuo-ship/*` remotes touched, no DNS/Cloudflare/prod changes, no archive/rename/modification of `clubeedg-ship-it/iam-website` settings. This phase prepared the clean state locally only.

## What shipped

| SC (from ROADMAP.md) | Status | Evidence |
|---|---|---|
| 1. Single squashed initial commit on new repo | **deferred to human** | `tools/prepare-clean-repo.sh` does the squash when run; NOT executed here |
| 2. `.planning/` + `.claude/` + briefs + spreadsheet moved to private repo | **deferred to human** | CUTOVER-RUNBOOK §5 |
| 3. All placeholder comments removed from prod HTML | ✓ | 9 files, 9 stray comments deleted |
| 4. `media/dump iam/` + raw/draft dirs purged from new repo | **deferred** | `prepare-clean-repo.sh` excludes them; not yet executed |
| 5. Branch protection + gitleaks CI + (signed commits OR required review) | **partial** | `.github/workflows/gitleaks.yml` delivered; branch protection is a repo-settings human action |
| 6. Phase 03 deploy workflow points at new repo | **runbook handoff** | no actual remote changes; CUTOVER §8 |

## Decisions honored (D-01..D-19)

- **D-01, D-02 (new repo creation):** NOT done — guardrail absolute. Runbook §1 hands off.
- **D-03, D-04 (history squash):** NOT executed. Delivered `tools/prepare-clean-repo.sh` — read-only against current repo; when run later it rsyncs to a fresh target, does `git init`, single commit, safety scans (no gitignored files leaked, no forbidden paths like `.planning`/`CLAUDE.md`/`LOVABLE-BRIEF.md`/`ACTION-PLAN.md`/`MEDIA-GALLERY.md`/`website-adjustments.xlsx`/`deploy.sh`), optional gitleaks.
- **D-05 (identity):** script fails fast if `AUTHOR_NAME`/`AUTHOR_EMAIL` env vars are still `REPLACE_ME_*`.
- **D-06 (file removals):** `prepare-clean-repo.sh` `--exclude` list matches the CONTEXT list. Worker did NOT delete these files from the current repo — Phase 05's concern is the NEW repo.
- **D-07 (Testimonials placeholder):** removed from `word-partner.html`, `partials/word-partner-nl.html`, `partials/word-partner-en.html`.
- **D-08 (Video placeholder):** removed from `onderwijs.html`, `partials/onderwijs-nl.html`, `partials/onderwijs-en.html`. Surrounding `<video>` blocks preserved.
- **D-09 (Contact privacy notice removed):** removed from `index.html`, `partials/index-nl.html`, `partials/index-en.html`.
- **D-10 (HubSpot form will be embedded here):** grepped; no hits (already cleaned in commit `e01514c`). Re-scan confirmed empty.
- **D-11 (TODO/FIXME/HACK/XXX/placeholder/TBD/lorem sweep):** zero hits in tracked HTML outside of legitimate `placeholder="…"` form attributes and `logo-placeholder` CSS class.
- **D-12 (branch protection):** deferred to CUTOVER-RUNBOOK §6.
- **D-13 (gitleaks CI):** `.github/workflows/gitleaks.yml` added — runs on PR + push to main/staging. Uses `gitleaks/gitleaks-action@v2` with default ruleset.
- **D-14 (.gitignore):** extended to cover `coverage/`, `.nyc_output/`, editor swap files (`*~`, `.*.swp`, `.*.swo`), worktrees (`.claude/worktrees/`), `.env*` glob, `*.pem`, `*.key`, `*_rsa`, `id_ed25519*`, `credentials.json`, `service-account*.json`. Added explicit `!tools/iam-deploy.sh` + `!tools/prepare-clean-repo.sh` exceptions (otherwise `tools/*` broad ignore would strip the two scripts that need to travel with the repo).
- **D-15 (LICENSE):** placeholder file `REPLACE_ME_LICENSE_CHOICE` — human picks license before cutover (HANDOFF §1).
- **D-16 (README.md):** minimal new README — project name, stack one-liner, local dev instructions, deploy one-liner (`push to main; Actions handles it`), contact email. No AI-workflow references.
- **D-17 (Phase 03 workflow duplicated into new repo):** not done — happens at CUTOVER step 4 when the clean state pushes to the new repo (the workflow file travels with the tree).
- **D-18 (cutover procedure):** `CUTOVER-RUNBOOK.md` — 11 sections, 5 gates, copy-paste commands throughout.
- **D-19 (zero downtime):** documented as the target in the runbook; rollback procedure covers the only failure mode.

## Files delivered

**Repo-root code/config (travels to new repo):**
- `LICENSE` (placeholder — human replaces text before cutover)
- `README.md` (minimal, AI-fingerprint-free)
- `.gitignore` (extended per D-14)
- `.github/workflows/gitleaks.yml`
- `tools/prepare-clean-repo.sh` (doesn't run in current repo; invoked during cutover)

**HTML edits (9 files):**
- `index.html`, `onderwijs.html`, `word-partner.html`
- `partials/index-nl.html`, `partials/index-en.html`
- `partials/onderwijs-nl.html`, `partials/onderwijs-en.html`
- `partials/word-partner-nl.html`, `partials/word-partner-en.html`

**Planning (force-added under `.planning/M2/phases/05-repo-migration-cleanup/`):**
- `CONTEXT.md` (existing)
- `CUTOVER-RUNBOOK.md`
- `HANDOFF-CHECKLIST.md`
- `SUMMARY.md` (this file)

**Cross-phase master doc:**
- `.planning/M2/MASTER-REVIEW-BRIEF.md` (see companion file)

## Commits

```
3159eaf docs(M2-05): cutover runbook + handoff checklist
3262eb7 feat(M2-05): repo-migration prep — LICENSE stub, README, gitleaks CI, clean-repo script, extended .gitignore
6ed3602 chore(M2-05): strip AI-cleanup placeholder comments from HTML per D-07/D-08/D-09/D-10
```

## Verification

- `bash -n tools/prepare-clean-repo.sh` → OK
- `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/gitleaks.yml'))"` → OK
- Placeholder-comment re-scan: `grep -rn --include="*.html" -E "<!-- *(Testimonials|Video) +placeholder|<!-- *Contact privacy notice removed|<!-- *HubSpot form will be embedded" .` → empty
- TODO/FIXME/HACK/XXX/TBD/lorem sweep across tracked HTML (excluding legit `placeholder=` attribute + `logo-placeholder` class) → empty
- Backend regression: `cd api && npm test` → 12/12 still green (no behavior changes this phase)
- `prepare-clean-repo.sh` dry behavior verified by syntax check + visual review; actual run is a cutover-time action

## Handoff to prior-phase items swept

Per the user instruction, code-only handoff items from Phases 01-04 were swept:

- **Phase 02 .gitignore extensions** — closed via D-14 edits (coverage, swap files, .env* glob, keys).
- **Phase 02 tracked-by-force scripts** — closed via `!tools/iam-deploy.sh` exception.
- **Phase 03 gitleaks CI** — delivered in this phase (`.github/workflows/gitleaks.yml`).
- **Phase 05 README/LICENSE** — delivered (LICENSE still a placeholder — human owns the choice).

Infrastructure-bound items (VPS, GitHub Actions Secrets, Cloudflare, OpenRouter rotation, HubSpot env vars, SSH key pairing) left for human completion per the session override.

## STOP-AND-ASK triggers hit

None (excluding override-allowed ones).

## Guardrail Overrides in force

Session-wide:
- STOP-AND-ASK #1 → PLACEHOLDER PROTOCOL
- Stop-after-phase → chained-phase protocol (single phase this run)
- Open PR at phase boundary → deferred to a batch-PR agent
- **NEW: Cutover prohibition** — do NOT create `oopuo-ship/*` repos, push to them, change DNS/Cloudflare, or archive the current repo. Honored: no remote changes, no DNS changes, no GitHub settings changes. Worker produced the clean starting state locally only.

---

*Phase: M2-05-repo-migration-cleanup*
*Chained autonomous run: 2026-04-21*
*End of M2 build-side. Cutover is the next human action.*
