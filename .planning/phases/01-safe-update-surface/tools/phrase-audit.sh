#!/usr/bin/env bash
#
# phrase-audit.sh -- Reusable legacy phrase audit for IAM website repositioning
#
# Searches all HTML files (excluding .planning/) for legacy phrases that need
# to be updated or removed during the site refresh. Groups output by file family
# per decision D-06.
#
# Usage:
#   bash phrase-audit.sh [--summary | --full | --help]
#
# Modes:
#   --summary   Show hit counts per family in a table (default)
#   --full      Show per-file, per-line hits grouped by family
#   --help      Show this help message
#
# Must be run from the repo root (where index.html lives).

set -euo pipefail

# --- Help ---
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  sed -n '3,17p' "$0"
  exit 0
fi

# --- Mode ---
MODE="${1:---summary}"
if [[ "$MODE" != "--summary" && "$MODE" != "--full" ]]; then
  echo "Error: Unknown mode '$MODE'. Use --summary, --full, or --help." >&2
  exit 1
fi

# --- Repo root check ---
if [[ ! -f "index.html" ]]; then
  echo "Error: index.html not found in current directory." >&2
  echo "This script must be run from the repo root." >&2
  exit 1
fi

# --- Target phrases (per D-05) ---
# Each entry: "display_label|grep_pattern|grep_flags"
# grep_flags: -i for case-insensitive, -F for fixed string
PHRASES=(
  "games|games|-i"
  "free updates|free updates|-i"
  "gratis updates|gratis updates|-i"
  "100+|100+|-F"
  "Choose Your Package|Choose Your Package|-i"
  "Kies Uw Pakket|Kies Uw Pakket|-i"
  "Kies Jouw Pakket|Kies Jouw Pakket|-i"
  "2-in-1|2-in-1|-F"
  "2 in 1|2 in 1|-F"
)

# --- File families (per inventory.md, 20 families) ---
# Format: "family_name|shell|nl_partial|en_partial"
FAMILIES=(
  "index|index.html|partials/index-nl.html|partials/index-en.html"
  "prijzen|prijzen.html|partials/prijzen-nl.html|partials/prijzen-en.html"
  "over-ons|over-ons.html|partials/over-ons-nl.html|partials/over-ons-en.html"
  "onderwijs|onderwijs.html|partials/onderwijs-nl.html|partials/onderwijs-en.html"
  "parken-speelhallen|parken-speelhallen.html|partials/parken-speelhallen-nl.html|partials/parken-speelhallen-en.html"
  "zorg-revalidatie|zorg-revalidatie.html|partials/zorg-revalidatie-nl.html|partials/zorg-revalidatie-en.html"
  "3d-spellen|3d-spellen.html|partials/3d-spellen-nl.html|partials/3d-spellen-en.html"
  "bouw-een-park|bouw-een-park.html|partials/bouw-een-park-nl.html|partials/bouw-een-park-en.html"
  "blog|blog.html|partials/blog-nl.html|partials/blog-en.html"
  "maak-je-spel|maak-je-spel.html|partials/maak-je-spel-nl.html|partials/maak-je-spel-en.html"
  "word-partner|word-partner.html|partials/word-partner-nl.html|partials/word-partner-en.html"
  "cookiebeleid|cookiebeleid.html|partials/cookiebeleid-nl.html|partials/cookiebeleid-en.html"
  "privacybeleid|privacybeleid.html|partials/privacybeleid-nl.html|partials/privacybeleid-en.html"
  "toegankelijkheid|toegankelijkheid.html|partials/toegankelijkheid-nl.html|partials/toegankelijkheid-en.html"
  "interactieve-vloer|products/interactieve-vloer.html|partials/products/interactieve-vloer-nl.html|partials/products/interactieve-vloer-en.html"
  "interactieve-muur|products/interactieve-muur.html|partials/products/interactieve-muur-nl.html|partials/products/interactieve-muur-en.html"
  "interactieve-zandbak|products/interactieve-zandbak.html|partials/products/interactieve-zandbak-nl.html|partials/products/interactieve-zandbak-en.html"
  "interactieve-klimwand|products/interactieve-klimwand.html|partials/products/interactieve-klimwand-nl.html|partials/products/interactieve-klimwand-en.html"
  "2-in-1-vloer-muur|products/2-in-1-vloer-muur.html|partials/products/2-in-1-vloer-muur-nl.html|partials/products/2-in-1-vloer-muur-en.html"
  "software-maatwerk|products/software-maatwerk.html|partials/products/software-maatwerk-nl.html|partials/products/software-maatwerk-en.html"
)

# Also track orphaned partials separately
ORPHANED=(
  "partials/content-nl.html"
  "partials/content-en.html"
)

# --- Functions ---

# Search a single file for all target phrases, return matching lines
# Arguments: $1 = filepath
# Output: lines in format "L<num>: <content> [<matched_phrases>]"
search_file() {
  local filepath="$1"
  [[ ! -f "$filepath" ]] && return

  # Collect unique matching lines (line_num:content)
  local raw_hits
  raw_hits=$(
    {
      grep -n -i "games\|free updates\|gratis updates\|Choose Your Package\|Kies Uw Pakket\|Kies Jouw Pakket" "$filepath" 2>/dev/null || true
      grep -n -F "100+" "$filepath" 2>/dev/null || true
      grep -n -F "2-in-1" "$filepath" 2>/dev/null || true
      grep -n -F "2 in 1" "$filepath" 2>/dev/null || true
    } | sort -t: -k1,1n -u
  )

  [[ -z "$raw_hits" ]] && return

  while IFS= read -r line; do
    local line_num="${line%%:*}"
    local content="${line#*:}"

    # Determine which phrases matched this line
    local matched=""
    for phrase_entry in "${PHRASES[@]}"; do
      local label pattern flags
      IFS='|' read -r label pattern flags <<< "$phrase_entry"
      if echo "$content" | grep -q $flags -- "$pattern" 2>/dev/null; then
        if [[ -n "$matched" ]]; then
          matched="$matched, $label"
        else
          matched="$label"
        fi
      fi
    done
    if [[ -n "$matched" ]]; then
      local trimmed
      trimmed=$(echo "$content" | sed 's/^[[:space:]]*//' | cut -c1-120)
      echo "      L${line_num}: \"${trimmed}\" [${matched}]"
    fi
  done <<< "$raw_hits"
}

# Count hits in a single file
# Arguments: $1 = filepath
# Returns count via stdout
count_file_hits() {
  local filepath="$1"
  [[ ! -f "$filepath" ]] && echo "0" && return

  local count=0
  count=$(
    {
      grep -n -i "games\|free updates\|gratis updates\|Choose Your Package\|Kies Uw Pakket\|Kies Jouw Pakket" "$filepath" 2>/dev/null || true
      grep -n -F "100+" "$filepath" 2>/dev/null || true
      grep -n -F "2-in-1" "$filepath" 2>/dev/null || true
      grep -n -F "2 in 1" "$filepath" 2>/dev/null || true
    } | sort -t: -k1,1n -u | wc -l
  )
  echo "$count"
}

# --- Main ---

if [[ "$MODE" == "--full" ]]; then
  GRAND_TOTAL=0

  for family_entry in "${FAMILIES[@]}"; do
    IFS='|' read -r name shell nl en <<< "$family_entry"

    # Collect output for this family
    family_output=""
    family_total=0

    for filepath in "$shell" "$nl" "$en"; do
      if [[ -f "$filepath" ]]; then
        file_hits=$(search_file "$filepath")
        if [[ -n "$file_hits" ]]; then
          hit_count=$(echo "$file_hits" | wc -l | tr -d ' ')
          family_total=$((family_total + hit_count))
          family_output+="    ${filepath}:
${file_hits}
"
        else
          family_output+="    ${filepath}: (no hits)
"
        fi
      fi
    done

    if [[ $family_total -gt 0 ]]; then
      echo "=== Family: ${name} ==="
      echo "$family_output"
      echo "    Total: ${family_total} hits"
      echo ""
      GRAND_TOTAL=$((GRAND_TOTAL + family_total))
    fi
  done

  # Check orphaned partials
  orphan_output=""
  orphan_total=0
  for filepath in "${ORPHANED[@]}"; do
    if [[ -f "$filepath" ]]; then
      file_hits=$(search_file "$filepath")
      if [[ -n "$file_hits" ]]; then
        hit_count=$(echo "$file_hits" | wc -l | tr -d ' ')
        orphan_total=$((orphan_total + hit_count))
        orphan_output+="    ${filepath}:
${file_hits}
"
      fi
    fi
  done

  if [[ $orphan_total -gt 0 ]]; then
    echo "=== Orphaned Partials ==="
    echo "$orphan_output"
    echo "    Total: ${orphan_total} hits"
    echo ""
    GRAND_TOTAL=$((GRAND_TOTAL + orphan_total))
  fi

  echo "========================================="
  echo "GRAND TOTAL: ${GRAND_TOTAL} lines with legacy phrases"
  echo "========================================="

elif [[ "$MODE" == "--summary" ]]; then
  # Print header
  printf "%-28s | %5s | %5s | %5s | %5s\n" "Family" "Shell" "NL" "EN" "Total"
  printf "%-28s-+-%5s-+-%5s-+-%5s-+-%5s\n" "----------------------------" "-----" "-----" "-----" "-----"

  TOTAL_SHELL=0
  TOTAL_NL=0
  TOTAL_EN=0
  TOTAL_ALL=0

  for family_entry in "${FAMILIES[@]}"; do
    IFS='|' read -r name shell nl en <<< "$family_entry"

    shell_count=$(count_file_hits "$shell")
    nl_count=$(count_file_hits "$nl")
    en_count=$(count_file_hits "$en")
    row_total=$((shell_count + nl_count + en_count))

    if [[ $row_total -gt 0 ]]; then
      printf "%-28s | %5s | %5s | %5s | %5s\n" "$name" "$shell_count" "$nl_count" "$en_count" "$row_total"
    fi

    TOTAL_SHELL=$((TOTAL_SHELL + shell_count))
    TOTAL_NL=$((TOTAL_NL + nl_count))
    TOTAL_EN=$((TOTAL_EN + en_count))
    TOTAL_ALL=$((TOTAL_ALL + row_total))
  done

  # Check orphaned partials
  orphan_nl=0
  orphan_en=0
  for filepath in "${ORPHANED[@]}"; do
    if [[ -f "$filepath" ]]; then
      c=$(count_file_hits "$filepath")
      if [[ "$filepath" == *-nl.html ]]; then
        orphan_nl=$((orphan_nl + c))
      else
        orphan_en=$((orphan_en + c))
      fi
    fi
  done
  orphan_total=$((orphan_nl + orphan_en))
  if [[ $orphan_total -gt 0 ]]; then
    printf "%-28s | %5s | %5s | %5s | %5s\n" "(orphaned partials)" "0" "$orphan_nl" "$orphan_en" "$orphan_total"
    TOTAL_NL=$((TOTAL_NL + orphan_nl))
    TOTAL_EN=$((TOTAL_EN + orphan_en))
    TOTAL_ALL=$((TOTAL_ALL + orphan_total))
  fi

  printf "%-28s-+-%5s-+-%5s-+-%5s-+-%5s\n" "----------------------------" "-----" "-----" "-----" "-----"
  printf "%-28s | %5s | %5s | %5s | %5s\n" "TOTAL" "$TOTAL_SHELL" "$TOTAL_NL" "$TOTAL_EN" "$TOTAL_ALL"
fi

exit 0
