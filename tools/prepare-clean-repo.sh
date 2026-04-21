#!/bin/bash
# prepare-clean-repo.sh — build a clean, AI-fingerprint-free copy of this repo
# for migration to oopuo-ship/iam-website per M2-05 D-03/D-04.
#
# READ-ONLY against the current repo. Writes only to $TARGET.
# Usage:
#   tools/prepare-clean-repo.sh <target_dir>
#
# The script:
#   1. Copies the current worktree to $TARGET (excluding git history and AI artifacts).
#   2. Runs `git init` in $TARGET with a detached config (no global .gitconfig leaks).
#   3. Stages everything, creates a single "initial import" commit authored by the
#      oopuo-ship identity (REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY).
#   4. Verifies nothing gitignored slipped in.
#   5. Optionally runs `gitleaks detect` if gitleaks is installed.
#
# Idempotent: re-runs produce the same working-tree content; git history is
# regenerated from scratch each time (the whole point — no old SHAs leak).
set -euo pipefail

# --- Identity placeholder — human must set before running ---
AUTHOR_NAME="${AUTHOR_NAME:-REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_NAME}"
AUTHOR_EMAIL="${AUTHOR_EMAIL:-REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_EMAIL}"
COMMIT_MESSAGE="${COMMIT_MESSAGE:-initial import}"

TARGET="${1:-}"
[[ -n "$TARGET" ]] || { echo "usage: $0 <target_dir>" >&2; exit 2; }

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
[[ -d "$SRC/.git" || -f "$SRC/.git" ]] || { echo "error: $SRC is not a git repo" >&2; exit 1; }

log() { printf '[prepare-clean] %s\n' "$*"; }
die() { printf '[prepare-clean] ERROR: %s\n' "$*" >&2; exit 1; }

# --- Fail fast on placeholder identity ---
if [[ "$AUTHOR_NAME" == REPLACE_ME_* || "$AUTHOR_EMAIL" == REPLACE_ME_* ]]; then
  die "set AUTHOR_NAME and AUTHOR_EMAIL env vars before running (oopuo-ship identity)"
fi

log "source : $SRC"
log "target : $TARGET"

# --- 1. Copy tree (rsync with exclusions). Overwrite target if present. ---
if [[ -e "$TARGET" ]]; then
  log "target exists — cleaning"
  rm -rf "${TARGET:?}/"
fi
mkdir -p "$TARGET"

# List of paths to EXCLUDE (per D-06).
#   - git history
#   - AI workflow artifacts
#   - large / draft assets
#   - node_modules (rebuilt on deploy)
rsync -a --delete \
  --exclude='.git' \
  --exclude='.planning/' \
  --exclude='.claude/' \
  --exclude='.kiro/' \
  --exclude='.github/worktrees/' \
  --exclude='CLAUDE.md' \
  --exclude='LOVABLE-BRIEF.md' \
  --exclude='ACTION-PLAN.md' \
  --exclude='MEDIA-GALLERY.md' \
  --exclude='website-adjustments.xlsx' \
  --exclude='media/dump iam/' \
  --exclude='aditionals/' \
  --exclude='deploy.sh' \
  --exclude='node_modules/' \
  --exclude='api/node_modules/' \
  --exclude='.env' \
  --exclude='.env.*' \
  --exclude='*.pem' \
  --exclude='*.key' \
  --exclude='var/' \
  "$SRC"/ "$TARGET"/

# --- 2. Fresh git init with scoped config ---
cd "$TARGET"
git init --initial-branch=main >/dev/null
git config --local user.name  "$AUTHOR_NAME"
git config --local user.email "$AUTHOR_EMAIL"
git config --local commit.gpgsign false
# No global config bleed: commit.template, commit.gpgsign, core.hooksPath etc. are all
# unset for this repo's local config.
log "git init complete with identity: $AUTHOR_NAME <$AUTHOR_EMAIL>"

# --- 3. Stage + commit ---
git add -A

# Safety scan before commit: no gitignored files snuck through (e.g. someone
# force-adds something).
violations="$(git ls-files --ignored --exclude-standard -c || true)"
if [[ -n "$violations" ]]; then
  die "gitignored files are staged — refusing to commit:"$'\n'"$violations"
fi

git commit -m "$COMMIT_MESSAGE" \
  --author="$AUTHOR_NAME <$AUTHOR_EMAIL>" \
  --no-verify >/dev/null
log "initial commit: $(git rev-parse --short HEAD)"

# --- 4. Post-commit verification ---
echo "---"
log "file count : $(git ls-files | wc -l | tr -d ' ')"
log "commit count: $(git rev-list --count HEAD)"
if [[ "$(git rev-list --count HEAD)" != "1" ]]; then
  die "expected exactly 1 commit; got $(git rev-list --count HEAD)"
fi

# Leakage smoke tests:
for forbidden in CLAUDE.md LOVABLE-BRIEF.md ACTION-PLAN.md MEDIA-GALLERY.md website-adjustments.xlsx deploy.sh; do
  if git ls-files | grep -Fxq "$forbidden"; then
    die "forbidden file leaked into clean tree: $forbidden"
  fi
done
if git ls-files | grep -qE '^\.planning/|^\.claude/|^\.kiro/'; then
  die "internal workflow tree leaked into clean repo"
fi

# --- 5. gitleaks (optional) ---
if command -v gitleaks >/dev/null 2>&1; then
  log "running gitleaks detect"
  gitleaks detect --source="$TARGET" --no-git --redact --exit-code=1 || die "gitleaks flagged the clean tree"
  log "gitleaks clean"
else
  log "gitleaks not installed — skipping (run on VPS or in CI)"
fi

log "DONE. $TARGET contains the clean starting state."
echo
echo "Next (HUMAN):"
echo "  cd $TARGET"
echo "  git remote add origin git@github.com:oopuo-ship/iam-website.git"
echo "  git push -u origin main"
