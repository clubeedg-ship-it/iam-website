---
phase: M2-01-security-remediation
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - .gitignore
  - .githooks/pre-commit
  - .githooks/README.md
  - .planning/M2/phases/01-security-remediation/HISTORY-SCAN.md
autonomous: true
decisions: [D-02, D-03, D-04]
success_criteria_addressed: [1, 2, 6]
requirements: [M2-01-SC-1, M2-01-SC-2, M2-01-SC-6]
must_haves:
  truths:
    - "CLAUDE.md is not tracked in git"
    - ".gitignore prevents CLAUDE.md from being re-added"
    - "A repo-local gitleaks pre-commit hook exists and is documented"
    - "History scan has been performed and findings recorded (action gated on human approval)"
  artifacts:
    - path: .gitignore
      contains: "CLAUDE.md"
    - path: .githooks/pre-commit
      provides: "gitleaks scan on staged changes"
    - path: .githooks/README.md
      provides: "activation instructions (git config core.hooksPath .githooks)"
    - path: .planning/M2/phases/01-security-remediation/HISTORY-SCAN.md
      provides: "raw output of git log --all -- .env .env.docker and decision recommendation"
  key_links:
    - from: .githooks/pre-commit
      to: gitleaks binary
      via: "shell invocation with `gitleaks protect --staged --redact`"
---

<objective>
Establish secret-hygiene baseline: stop tracking `CLAUDE.md`, install a repo-local gitleaks pre-commit hook (activated in Phase 02's bootstrap), and produce a history-scan report that the human can approve before any `git filter-repo` is executed.

Purpose: close audit findings SC-2 and SC-6, and gather the evidence needed to decide D-02 without executing destructive history rewrites autonomously.
Output: `.gitignore` update, `.githooks/` hook + README, HISTORY-SCAN.md report, credential-rotation checklist prose in SUMMARY (added at end of phase).
</objective>

<context>
@.planning/M2/GUARDRAILS.md
@.planning/M2/phases/01-security-remediation/CONTEXT.md
@.planning/M2/ROADMAP.md
</context>

<tasks>

<task type="auto">
  <name>Task 1: Untrack CLAUDE.md and update .gitignore (D-03)</name>
  <files>.gitignore, CLAUDE.md (untrack only, do not delete working file)</files>
  <read_first>
    - .gitignore (current contents)
    - Output of `git ls-files CLAUDE.md` to confirm it is tracked
  </read_first>
  <action>
    1. Run `git ls-files CLAUDE.md` — if empty, log "already untracked" and skip rm step.
    2. Run `git rm --cached CLAUDE.md` (NOT `git rm` — the working file must remain on disk so the local workflow keeps working).
    3. Append to `.gitignore` (create if missing) these exact lines under a `# AI workflow artifacts (D-03)` header:
       ```
       # AI workflow artifacts (D-03)
       CLAUDE.md
       .claude/
       .kiro/
       ```
    4. Stage both files. Do NOT commit yet (commit happens at plan end per atomic-commit rule).
    5. Commit with message: `chore(M2-01): untrack CLAUDE.md and ignore AI artifacts per D-03`
  </action>
  <verify>
    <automated>git ls-files CLAUDE.md | wc -l | grep -q '^ *0$' && grep -q '^CLAUDE.md$' .gitignore</automated>
  </verify>
  <acceptance_criteria>
    - `git ls-files CLAUDE.md` returns empty
    - `.gitignore` contains a line exactly matching `CLAUDE.md`
    - `.gitignore` contains `.claude/` and `.kiro/`
    - Working tree still contains `CLAUDE.md` as an untracked file (`test -f CLAUDE.md`)
  </acceptance_criteria>
  <done>CLAUDE.md is untracked, .gitignore updated, change committed with D-03 reference.</done>
</task>

<task type="auto">
  <name>Task 2: Add gitleaks pre-commit hook files under .githooks/ (D-04)</name>
  <files>.githooks/pre-commit, .githooks/README.md</files>
  <read_first>
    - .planning/M2/phases/01-security-remediation/CONTEXT.md (D-04 exact wording)
    - .planning/M2/GUARDRAILS.md (no --no-verify; hooks must be enforceable)
  </read_first>
  <action>
    Create `.githooks/pre-commit` (executable, chmod 755) with this exact body:
    ```bash
    #!/usr/bin/env bash
    # M2-01 D-04: gitleaks pre-commit hook
    set -euo pipefail

    if ! command -v gitleaks >/dev/null 2>&1; then
      echo "ERROR: gitleaks not installed. Install: https://github.com/gitleaks/gitleaks" >&2
      echo "       Or run bootstrap.sh (M2 Phase 02) which installs it automatically." >&2
      exit 1
    fi

    gitleaks protect --staged --redact --verbose
    ```
    Create `.githooks/README.md` with:
    - Purpose paragraph (D-04 rationale, ties to SC-6)
    - Activation command verbatim: `git config core.hooksPath .githooks`
    - Note that Phase 02 `bootstrap.sh` will run this automatically on VPS checkouts
    - Note: do NOT use `--no-verify` to bypass (per GUARDRAILS.md)
    Ensure file is executable: `chmod +x .githooks/pre-commit`.
    Commit: `feat(M2-01): add gitleaks pre-commit hook files per D-04`
  </action>
  <verify>
    <automated>test -x .githooks/pre-commit && grep -q 'gitleaks protect --staged' .githooks/pre-commit && grep -q 'core.hooksPath .githooks' .githooks/README.md</automated>
  </verify>
  <acceptance_criteria>
    - `.githooks/pre-commit` exists and is executable (`test -x`)
    - File contains the string `gitleaks protect --staged`
    - `.githooks/README.md` contains the activation command `git config core.hooksPath .githooks`
    - Neither file references `--no-verify` as a bypass
  </acceptance_criteria>
  <done>Hook files committed; activation instructions documented; bootstrap responsibility noted.</done>
</task>

<task type="auto">
  <name>Task 3: Scan history for secret additions and record findings (D-02, gated)</name>
  <files>.planning/M2/phases/01-security-remediation/HISTORY-SCAN.md</files>
  <read_first>
    - .planning/M2/GUARDRAILS.md ("No `git filter-repo` ... without explicit human approval")
    - .planning/M2/phases/01-security-remediation/CONTEXT.md (D-02 condition)
  </read_first>
  <action>
    This task MUST NOT rewrite history. It ONLY reports.

    1. Run and capture output of:
       - `git log --all --oneline -- .env .env.docker`
       - `git log --all -p -- .env .env.docker | head -500` (capped — truncation note if hit)
       - `git log --all --oneline -S OPENROUTER_API_KEY`
       - `git log --all --oneline -S sk-or-`
    2. Write `.planning/M2/phases/01-security-remediation/HISTORY-SCAN.md` with sections:
       - `## Commits touching .env / .env.docker` (list or "none found")
       - `## Commits referencing OpenRouter key patterns`
       - `## Recommendation` — if additions found: "HUMAN APPROVAL REQUIRED before filter-repo. Command to review:" followed by the exact `git filter-repo --invert-paths --path .env --path .env.docker` command (but DO NOT execute). If none: "Skip filter-repo per D-02; nothing to scrub."
       - `## D-01 credential rotation checklist` — bullet list: (a) rotate OpenRouter API key at openrouter.ai/keys, (b) rotate any DB credential referenced in .env.docker, (c) update server `.env` files in Phase 02. Mark all items as HUMAN ACTION per GUARDRAILS.
    3. Commit: `docs(M2-01): record history scan and rotation checklist per D-01/D-02`

    STOP-AND-ASK trigger: if scan shows additions AND PLAN author (executor) is tempted to run filter-repo — halt, surface the finding, wait for human.
  </action>
  <verify>
    <automated>test -f .planning/M2/phases/01-security-remediation/HISTORY-SCAN.md && grep -q 'D-01 credential rotation checklist' .planning/M2/phases/01-security-remediation/HISTORY-SCAN.md && grep -q 'Recommendation' .planning/M2/phases/01-security-remediation/HISTORY-SCAN.md</automated>
  </verify>
  <acceptance_criteria>
    - HISTORY-SCAN.md exists in the phase directory
    - Contains the four scan outputs (or "none found" for each)
    - Contains explicit `## Recommendation` section
    - Contains `## D-01 credential rotation checklist` marked HUMAN ACTION
    - Repo state unchanged apart from the new doc: `git diff HEAD~1 --stat` shows only HISTORY-SCAN.md
    - NO filter-repo was executed (`git reflog` does not show `filter-repo` in last 10 entries)
  </acceptance_criteria>
  <done>History scan recorded; rotation checklist documented as human action; no destructive operations performed.</done>
</task>

</tasks>

<verification>
- `git ls-files CLAUDE.md` returns empty
- `.gitignore` contains `CLAUDE.md`
- `.githooks/pre-commit` executable and references `gitleaks protect --staged`
- HISTORY-SCAN.md exists with recommendation + rotation checklist
- Three atomic commits created, each referencing D-XX
</verification>

<success_criteria>
Closes M2-01 ROADMAP success criteria 2 (CLAUDE.md untracked) and 6 (pre-commit scanner). Prepares ground for SC-1 (history scan + rotation checklist surface what the human must do).
</success_criteria>

<output>
Contributes to `.planning/M2/phases/01-security-remediation/SUMMARY.md` (written at end of phase by final plan).
</output>
