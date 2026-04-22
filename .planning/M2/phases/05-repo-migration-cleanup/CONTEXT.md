# M2 Phase 05: Repo Migration + Cosmetic Cleanup — Context

**Gathered:** 2026-04-21
**Status:** Blocked on Phases 01-04
**Depends on:** All prior M2 phases (prod must be stable on a working pipeline before swapping the git remote)

<domain>
## Phase Boundary

Move the public-facing codebase to a clean, AI-fingerprint-free repo at `oopuo-ship/iam-website` and remove every placeholder comment and unfinished UI element. Move internal workflow documentation (`.planning/`, `.claude/`, brief/action-plan/memory docs, `CLAUDE.md`, spreadsheet) to a private `iam-website-internal` repo.

Out of scope: content changes, feature work, code refactors. This phase is strictly migration + cosmetic cleanup — no behavior changes.
</domain>

<decisions>
## Implementation Decisions

### New repo creation
- **D-01:** New GitHub account: `oopuo-ship` (personal account, not an org). Repo name: `iam-website`. Visibility: public (matches current posture).
- **D-02:** New private repo for internal workflow artifacts: `oopuo-ship/iam-website-internal`. Not forked from anything. Carries `.planning/`, `.claude/`, `CLAUDE.md`, `LOVABLE-BRIEF.md`, `ACTION-PLAN.md`, `MEDIA-GALLERY.md`, `website-adjustments.xlsx`.

### History hygiene
- **D-03:** Public repo starts with a single squashed commit `initial import` authored by the `oopuo-ship` account. No `quick-260402-kn3`, no GSD agent fingerprints, no secret history, no AI-workflow docs anywhere in git history.
- **D-04:** Use `git archive` or a fresh clone + rm -rf .git + git init to produce the starting state. Do not push old history, not even squashed — any prior commit hashes become metadata that links the new repo back to the old.
- **D-05:** Commit authorship: set `user.email` and `user.name` for the `oopuo-ship` account globally in the new repo's local config. Verify no `@anthropic.com` co-author trailers leak into public commits.

### File removals before squash
- **D-06:** Delete from the new repo before the squash commit:
  - `.planning/` (entire tree)
  - `.claude/` (entire tree, including worktrees)
  - `CLAUDE.md`
  - `LOVABLE-BRIEF.md`
  - `ACTION-PLAN.md`
  - `MEDIA-GALLERY.md`
  - `website-adjustments.xlsx`
  - `media/dump iam/` (raw dumps, even if gitignored in current repo)
  - `tools/migrate_i18n.py` if migration is complete (verify with IAM dev first)
  - `tools/vm-check.sh` unless it's needed by `bootstrap.sh`
  - `deploy.sh` (replaced by Phase 03's off-repo `iam-deploy` script)
  - Old screenshots, draft briefs, any `.md` under root that isn't a real README

### Cosmetic cleanup (across all remaining HTML)
- **D-07:** Remove every `<!-- Testimonials placeholder -->` (`partials/word-partner-nl.html`, `partials/word-partner-en.html`, `word-partner.html`).
- **D-08:** Remove every `<!-- Video placeholder -->` (`partials/onderwijs-nl.html`, `partials/onderwijs-en.html`, `onderwijs.html`). Replace with real content or delete the enclosing section entirely — no empty holders.
- **D-09:** Remove every `<!-- Contact privacy notice removed -->` (`partials/index-nl.html`, `partials/index-en.html`, `index.html`) — stray AI cleanup artifact.
- **D-10:** Remove every `<!-- HubSpot form will be embedded here -->` (already handled in `e01514c` for word-partner; re-scan).
- **D-11:** Grep the final tree for `TODO`, `FIXME`, `HACK`, `XXX`, `placeholder`, `TBD`, `lorem` (case-insensitive). Zero hits in tracked files before the squash commit.

### Repo configuration from day one
- **D-12:** Branch protection on `main`: require pull request, require 1 approving review, require status checks to pass, require branches to be up to date, no force push, no deletions.
- **D-13:** GitHub Actions workflow `gitleaks` runs on every PR and push to `main`. Blocks merge on any finding.
- **D-14:** Standard `.gitignore` covering `node_modules/`, `.env*`, `.DS_Store`, `.claude/`, `.planning/`, `CLAUDE.md`, worktrees, coverage outputs, editor swap files.
- **D-15:** New `LICENSE` file — user to decide license (proprietary, MIT, etc.). Default to proprietary if unspecified.
- **D-16:** New minimal `README.md` — project name, tech stack one-liner, "deploy is automatic on push to `main`" one-liner, contact email. No AI-workflow references, no GSD commands, no skill names.

### Pipeline cutover
- **D-17:** Before cutover, the Phase 03 Actions workflow is duplicated into the new repo with updated secrets. Verify it runs green against staging before pointing prod at it.
- **D-18:** Cutover procedure (planned execution order):
  1. Push the clean repo state to `oopuo-ship/iam-website` (public).
  2. Verify Actions green on staging.
  3. Point prod deploy secrets at the new repo.
  4. Manually trigger prod deploy from the new repo's `main`.
  5. Verify prod health check passes.
  6. Archive the old repo (`clubeedg-ship-it/iam-website`) — set to read-only, update README pointing to the new repo.
  7. Delete the old repo after 30 days of green operation from the new one.
- **D-19:** Zero downtime target: users see no interruption during cutover. VPS doesn't know or care which git remote it pulled from.

### agent discretion
- Exact set of placeholder comments to hunt down (full grep pass required during planning)
- Whether to preserve or delete `tools/migrate_i18n.py` (depends on whether migration is truly done)
- LICENSE choice (needs user input)
- README tone and length
</decisions>

<specifics>
## Specific Ideas

- Old repo URL from `deploy.sh`: `https://github.com/clubeedg-ship-it/iam-website.git`. The `clubeedg-ship-it` org name is a leaked AI-agent origin; archiving + deleting is part of the hygiene win.
- Current git log has commits with messages like `docs(quick-260402-kn3):` and `fix(quick-kn3):` — GSD workflow fingerprints. None of that survives the squash.
- `.gitignore` currently lists `CLAUDE.md` but the file IS tracked (`git ls-files CLAUDE.md` returns it). Confirmed in audit verification. `git rm --cached CLAUDE.md` should land in Phase 01 on the old repo AND the file should simply not exist in the new repo.
- The `.claude/worktrees/agent-*/` directories contain full repo copies from past agent runs — they inflate the repo and leak the AI workflow. Must not appear in the new repo.
- Current git log shows the site was running Docker until commit `7b9db71` removed it. Docker configs and deploy scripts from that era should not be imported.
</specifics>

<canonical_refs>
## Canonical References

- `.planning/M2/ROADMAP.md`
- `.planning/M2/phases/01-security-remediation/CONTEXT.md` — any secret removal from old repo happens there
- `.planning/M2/phases/03-cicd/CONTEXT.md` — Actions workflow that moves to the new repo
- Audit report — complete list of cosmetic comments and tracked-but-shouldn't-be files
- Current git state at this phase's start: whatever commit is live on prod when Phases 01-04 are done
</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable
- Actual site HTML, CSS, JS, media — the reason for the whole exercise. All of that ports clean.
- `server.js`, `api/`, `bootstrap.sh`, Actions workflow — all production artifacts move as-is.
- `styles.css` and `projector.js` are untouched.

### Patterns
- File structure stays identical: root HTML pages, `partials/`, `products/`, `media/`, `js/`, `api/`.
- Deploy model stays identical — only the git remote changes.

### Integration points
- GitHub Actions in the new repo connects to the same VPS over the same SSH key (or a rotated one — recommended to rotate during cutover).
- Cloudflare doesn't care which git repo feeds the VPS — no Cloudflare change needed.
- HubSpot doesn't care — form GUIDs are unchanged.
- DNS doesn't change.
</code_context>

<deferred>
## Deferred Ideas

- Migrating issue history, PR history, or stars from the old repo — not worth the effort; start clean.
- Publishing under a separate org for ownership clarity — user chose personal `oopuo-ship` account.
- Monorepo with other oopuo projects — out of scope.
- Changelog or release tags on the new repo — can be added after a few deploys land cleanly.
- Git submodules for shared content — current site doesn't need them.
</deferred>

---

*Phase: M2-05-repo-migration-cleanup*
*Context gathered: 2026-04-21*
