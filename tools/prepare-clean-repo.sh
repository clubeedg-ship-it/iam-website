#!/bin/bash
# prepare-clean-repo.sh — build a clean, AI-fingerprint-free copy of this repo
# for migration to oopuo-ship/iam-website per M2-05 D-03/D-04.
#
# READ-ONLY against the current repo. Writes only to $TARGET.
# Usage:
#   tools/prepare-clean-repo.sh [--dry-run] <target_dir>
#
# The script:
#   1. Copies the current worktree to $TARGET (excluding git history and AI artifacts).
#   2. APPLIES M3 ENGLISH-FIRST RENAMES (HTML + partials) per tools/m3-renames.map.
#   3. REPAIRS REFERENCES across HTML/CSS/JS/conf files.
#   4. GENERATES config/nginx/redirects.conf with 301s for legacy Dutch URLs.
#   5. Runs `git init` in $TARGET with a detached config (no global .gitconfig leaks).
#   6. Stages everything, creates a single "initial import" commit authored by the
#      oopuo-ship identity (REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY).
#   7. Verifies nothing gitignored slipped in.
#   8. Optionally runs `gitleaks detect` if gitleaks is installed.
#
# --dry-run: run rsync + rename-plan + reference-repair-plan + redirect-count
#            against a scratch $TARGET, report counts, skip git init/commit.
#
# Idempotent: re-runs produce the same working-tree content; git history is
# regenerated from scratch each time (the whole point — no old SHAs leak).
# Running with `--dry-run` against a target where renames are already applied
# (English-first already on disk) is a no-op for the rename phase.
set -euo pipefail

# --- CLI args ---
DRY_RUN=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) sed -n '2,24p' "$0"; exit 0 ;;
    --) shift; break ;;
    -*) echo "unknown flag: $1" >&2; exit 2 ;;
    *) break ;;
  esac
done

# --- Identity placeholder — human must set before running ---
AUTHOR_NAME="${AUTHOR_NAME:-REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_NAME}"
AUTHOR_EMAIL="${AUTHOR_EMAIL:-REPLACE_ME_OOPUO_SHIP_GIT_IDENTITY_EMAIL}"
COMMIT_MESSAGE="${COMMIT_MESSAGE:-initial import}"

TARGET="${1:-}"
[[ -n "$TARGET" ]] || { echo "usage: $0 [--dry-run] <target_dir>" >&2; exit 2; }

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
[[ -d "$SRC/.git" || -f "$SRC/.git" ]] || { echo "error: $SRC is not a git repo" >&2; exit 1; }

RENAME_MAP="$SRC/tools/m3-renames.map"
[[ -f "$RENAME_MAP" ]] || { echo "error: rename map not found at $RENAME_MAP" >&2; exit 1; }

log() { printf '[prepare-clean] %s\n' "$*"; }
die() { printf '[prepare-clean] ERROR: %s\n' "$*" >&2; exit 1; }

# --- Fail fast on placeholder identity (skipped in --dry-run) ---
if [[ "$DRY_RUN" -eq 0 ]]; then
  if [[ "$AUTHOR_NAME" == REPLACE_ME_* || "$AUTHOR_EMAIL" == REPLACE_ME_* ]]; then
    die "set AUTHOR_NAME and AUTHOR_EMAIL env vars before running (oopuo-ship identity)"
  fi
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  log "DRY-RUN MODE — will not git init or commit"
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
#   - internal workflow artifacts
#   - large / draft assets
#   - node_modules (rebuilt on deploy)
#   - migration-only tooling (not needed in the delivered repo)
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
  --exclude='tools/prepare-clean-repo.sh' \
  --exclude='tools/m3-renames.map' \
  --exclude='tools/vm-check.sh' \
  "$SRC"/ "$TARGET"/

# --- 1b. M3 English-first restructure (rename + sed + nginx redirects) ---
#
# Data-driven from $RENAME_MAP. Runs entirely inside $TARGET. Does not mutate $SRC.
# On --dry-run, reports planned counts but does not apply moves/sed/writes.

# Helper: read the map, strip # comments + blank lines, emit `old<TAB>new` pairs.
read_rename_map() {
  awk -F'\t' '
    /^[[:space:]]*#/ { next }
    /^[[:space:]]*$/ { next }
    NF >= 2 && $1 != "" && $2 != "" { print $1 "\t" $2 }
  ' "$RENAME_MAP"
}

# Safety check: every `old_path` in the map must exist in $TARGET; every `new_path`
# must NOT exist (would mean the source is already partially renamed).
# Idempotency: if NONE of the old_paths exist AND ALL new_paths do, the target is
# already English-first — return code 2 (caller treats as no-op).
validate_rename_map() {
  local missing=0 conflicts=0 already_renamed=0 total=0
  while IFS=$'\t' read -r old new; do
    total=$((total + 1))
    if [[ -e "$TARGET/$old" ]]; then
      if [[ -e "$TARGET/$new" && "$old" != "$new" ]]; then
        echo "  CONFLICT: both $old and $new exist in target" >&2
        conflicts=$((conflicts + 1))
      fi
    else
      if [[ -e "$TARGET/$new" ]]; then
        already_renamed=$((already_renamed + 1))
      else
        echo "  MISSING: $old (and no $new either)" >&2
        missing=$((missing + 1))
      fi
    fi
  done < <(read_rename_map)

  if [[ "$already_renamed" -eq "$total" ]]; then
    return 2  # fully idempotent — target already English-first
  fi
  if [[ "$missing" -gt 0 || "$conflicts" -gt 0 ]]; then
    return 1
  fi
  return 0
}

apply_renames() {
  local applied=0
  while IFS=$'\t' read -r old new; do
    if [[ -e "$TARGET/$old" ]]; then
      mkdir -p "$TARGET/$(dirname "$new")"
      if [[ "$DRY_RUN" -eq 1 ]]; then
        :
      else
        mv "$TARGET/$old" "$TARGET/$new"
      fi
      applied=$((applied + 1))
    fi
  done < <(read_rename_map)
  echo "$applied"
}

# Build the list of files whose text references need repair.
# Targets: HTML, CSS, JS, nginx conf, sitemap, robots, partials, server.js, package.json.
# Excludes: media/, node_modules/, .git/.
reference_repair_filelist() {
  find "$TARGET" \
    \( -path "$TARGET/.git" -o -path "$TARGET/media" -o -path "$TARGET/node_modules" -o -path "$TARGET/api/node_modules" \) -prune -o \
    -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' -o -name '*.conf' -o -name '*.xml' -o -name '*.txt' -o -name '*.json' \) \
    -print0
}

# Build the slug-level sed program from the rename map.
# For each `old<TAB>new` pair we emit a substitution:
#   - full-path references:  old_path → new_path   (e.g. "partials/word-partner-nl.html" → "partials/partner-nl.html")
#   - URL-level references:  bare slugs (strip .html) when old dirname == new dirname
#     (e.g. "/word-partner" → "/partner", but only for root & products — matched by the map pairs themselves).
# We use `|` as sed delimiter since paths contain `/`.
build_sed_program() {
  local tmp
  tmp="$(mktemp)"
  while IFS=$'\t' read -r old new; do
    # 1. Full path substitution.
    printf 's|%s|%s|g\n' "$old" "$new" >> "$tmp"
    # 2. URL-level: strip `.html`, prefix with `/` and wrap in word boundaries via quotes.
    local old_url="/${old%.html}"
    local new_url="/${new%.html}"
    # Normalize: partials/* are not URLs, skip them.
    if [[ "$old" == partials/* ]]; then
      continue
    fi
    # index.html and blog.html aren't in the map (they're unchanged), safe.
    # Emit URL rewrites for href="..." and server.js route strings.
    printf 's|"%s"|"%s"|g\n' "$old_url" "$new_url" >> "$tmp"
    printf "s|'%s'|'%s'|g\n" "$old_url" "$new_url" >> "$tmp"
    printf 's|"%s/"|"%s/"|g\n' "$old_url" "$new_url" >> "$tmp"
  done < <(read_rename_map)
  # Special: data-page attribute values — English slug only, no `/` prefix.
  # Extract the base slugs from the HTML pages section and emit data-page swaps.
  while IFS=$'\t' read -r old new; do
    [[ "$old" == *.html ]] || continue
    [[ "$old" == partials/* ]] && continue
    local old_slug new_slug
    old_slug="$(basename "${old%.html}")"
    new_slug="$(basename "${new%.html}")"
    [[ "$old_slug" == "$new_slug" ]] && continue
    printf 's|data-page="%s"|data-page="%s"|g\n' "$old_slug" "$new_slug" >> "$tmp"
  done < <(read_rename_map)
  echo "$tmp"
}

apply_reference_repair() {
  local sedprog="$1"
  local count=0
  local files_touched=0
  # Build a grep-compatible alternation of all left-hand-sides the sed program
  # touches, so the "would-change" count matches reality.
  # We take the sed program, strip `s|LHS|RHS|g` into just LHS, collapse, and
  # build an ERE alternation. Paths and quoted URLs are literal strings.
  local lhs_file
  lhs_file="$(mktemp)"
  # Extract LHS literals from the sed program — line format is `s|LHS|RHS|g`.
  awk -F'|' 'NF>=4 && $1=="s" { print $2 }' "$sedprog" | sort -u > "$lhs_file"

  while IFS= read -r -d '' f; do
    local hits=0
    local h
    # Count every LHS occurrence. Using fixed-string grep per LHS, summed.
    while IFS= read -r lhs; do
      [[ -z "$lhs" ]] && continue
      h=$(grep -c -F -- "$lhs" "$f" 2>/dev/null || true)
      hits=$((hits + h))
    done < "$lhs_file"
    if [[ "$hits" -gt 0 ]]; then
      files_touched=$((files_touched + 1))
      count=$((count + hits))
      if [[ "$DRY_RUN" -eq 0 ]]; then
        # macOS sed: -i ''  |  GNU sed: -i
        if sed --version >/dev/null 2>&1; then
          sed -i -f "$sedprog" "$f"
        else
          sed -i '' -f "$sedprog" "$f"
        fi
      fi
    fi
  done < <(reference_repair_filelist)
  rm -f "$lhs_file"
  echo "$files_touched $count"
}

# Build nginx redirect file from the rename map. One `return 301 /new;` per old slug.
# Output path: $TARGET/config/nginx/redirects.conf
# Only HTML page renames (root + products) produce URL redirects — partials are not URLs.
generate_nginx_redirects() {
  local out="$TARGET/config/nginx/redirects.conf"
  local rules=0
  local body
  body="$(mktemp)"
  {
    echo "# M3 legacy URL redirects — Dutch slugs → English canonical."
    echo "# Generated by tools/prepare-clean-repo.sh from tools/m3-renames.map."
    echo "# Include this file from the HTTPS server block (before the default location /)."
    echo ""
  } >> "$body"

  while IFS=$'\t' read -r old new; do
    [[ "$old" == *.html ]] || continue
    [[ "$old" == partials/* ]] && continue
    local old_url="/${old%.html}"
    local new_url="/${new%.html}"
    [[ "$old_url" == "$new_url" ]] && continue
    printf 'location = %-40s { return 301 %s; }\n' "$old_url" "$new_url" >> "$body"
    rules=$((rules + 1))
  done < <(read_rename_map)

  # Extra aliases noted in AUDIT §7 not covered by the map 1:1.
  {
    echo ""
    echo "# Legacy aliases (AUDIT.md §7) not covered by the 1:1 rename map."
    echo "location = /zorg                      { return 301 /healthcare; }"
    echo "location = /parken                    { return 301 /entertainment; }"
    rules=$((rules + 2))
    echo ""
    echo "# Trailing-slash normalisation."
    echo "rewrite ^/(.+)/$ /\$1 permanent;"
    echo ""
    echo "# Legacy .html URLs → clean URL."
    echo "location ~ ^/(.+)\\.html\$ { return 301 /\$1; }"
  } >> "$body"

  if [[ "$DRY_RUN" -eq 0 ]]; then
    mkdir -p "$(dirname "$out")"
    mv "$body" "$out"
  else
    rm -f "$body"
  fi
  echo "$rules"
}

# Targeted patch: js/site.js partial-path loader must switch from
#   `partials/${slug}-${lang}.html`
# to English-first convention:
#   lang==='en' → `partials/${slug}.html`   (bare = canonical English)
#   else        → `partials/${slug}-nl.html`
# (Audit §2 documents this; without it the language toggle 404s post-rename.)
patch_site_js_partial_loader() {
  local f="$TARGET/js/site.js"
  [[ -f "$f" ]] || return 0
  # Idempotency: if the new ternary is already there, skip.
  if grep -q "lang === 'en' ? " "$f"; then
    return 0
  fi
  if [[ "$DRY_RUN" -eq 1 ]]; then
    return 0
  fi
  # Two literal-line replacements. Use perl for portability across sed flavors.
  # Original: partials/products/' + slug + '-' + lang + '.html'
  # New:      partials/products/' + slug + (lang === 'en' ? '' : '-' + lang) + '.html'
  perl -i -pe "s{'partials/products/' \\+ slug \\+ '-' \\+ lang \\+ '\\.html'}{'partials/products/' + slug + (lang === 'en' ? '' : '-' + lang) + '.html'};" "$f"
  perl -i -pe "s{'partials/' \\+ slug \\+ '-' \\+ lang \\+ '\\.html'}{'partials/' + slug + (lang === 'en' ? '' : '-' + lang) + '.html'};" "$f"
}

log "applying M3 English-first renames (map: tools/m3-renames.map)"
set +e
validate_rename_map
rc=$?
set -e
case "$rc" in
  0)
    rename_count="$(apply_renames)"
    log "  renames: $rename_count applied$([[ "$DRY_RUN" -eq 1 ]] && echo ' (dry-run)')"
    sedprog="$(build_sed_program)"
    read -r files_touched ref_count < <(apply_reference_repair "$sedprog")
    rm -f "$sedprog"
    log "  reference repair: $ref_count occurrences across $files_touched files$([[ "$DRY_RUN" -eq 1 ]] && echo ' (dry-run)')"
    redirect_rules="$(generate_nginx_redirects)"
    log "  nginx redirect rules generated: $redirect_rules$([[ "$DRY_RUN" -eq 1 ]] && echo ' (dry-run)')"
    patch_site_js_partial_loader
    log "  js/site.js partial loader: patched$([[ "$DRY_RUN" -eq 1 ]] && echo ' (dry-run)')"
    ;;
  2)
    log "  target already English-first — rename phase skipped (idempotent)"
    # Still generate redirects + ensure no stale Dutch refs remain.
    sedprog="$(build_sed_program)"
    read -r files_touched ref_count < <(apply_reference_repair "$sedprog")
    rm -f "$sedprog"
    log "  reference repair: $ref_count occurrences (should be 0)"
    redirect_rules="$(generate_nginx_redirects)"
    log "  nginx redirect rules generated: $redirect_rules"
    ;;
  *)
    die "rename map validation failed — see messages above"
    ;;
esac

if [[ "$DRY_RUN" -eq 1 ]]; then
  log "DRY-RUN complete. Summary:"
  log "  renames planned:    ${rename_count:-0}"
  log "  refs to repair:     ${ref_count:-0} in ${files_touched:-0} files"
  log "  redirect rules:     ${redirect_rules:-0}"
  log "  target inspectable at: $TARGET (no git history)"
  exit 0
fi

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
