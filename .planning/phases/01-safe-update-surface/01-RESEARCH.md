# Phase 1: Safe Update Surface - Research

**Researched:** 2026-04-01
**Domain:** Brownfield HTML site inventory, phrase auditing, route dependency mapping, spreadsheet parsing
**Confidence:** HIGH

## Summary

Phase 1 produces documentation and audit tooling -- no live site modifications. The work covers four concerns: (1) building a complete file-family inventory of the 49 HTML files in the repo, (2) creating a reusable phrase-audit script for the six legacy term categories, (3) mapping the route dependency graph for removal candidates (`bouw-een-park`, `3d-spellen`, orphaned `content-*` partials, and "Choose Your Package" sections), and (4) parsing `website-adjustments.xlsx` into structured markdown that downstream phases consume.

The codebase is a static HTML site with no build step, no templating, and no shared includes for navigation or footer. Every page carries its own copy of desktop nav, mobile nav, and footer links. This means removal of any page requires touching navigation in all 48 HTML files (plus `sitemap.xml`). The spreadsheet is readable via Python/pandas+openpyxl and contains 48 rows of structured change requests plus a "More info" sheet with detailed instructions.

**Primary recommendation:** Use `grep -rn` wrapped in a shell script as the phrase audit tool, and produce all inventory/dependency outputs as markdown tables in `.planning/phases/01-safe-update-surface/` so downstream phases have a machine-readable reference.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Inventory every page family on the site, not just the ones explicitly named in the spreadsheet -- nav drift means any file could be affected by removal or restructuring
- **D-02:** Each file family entry captures: shell page path, NL partial path, EN partial path, and a flag noting whether nav/content has drifted between shell and partial
- **D-03:** Orphaned partials (`partials/content-nl.html`, `partials/content-en.html`) are flagged separately as cleanup candidates
- **D-04:** Produce a reusable grep-based audit (shell script or markdown with grep commands) that can be re-run after each phase lands -- not a one-shot snapshot
- **D-05:** Target phrases: `games`, `free updates` / `gratis updates`, `100+`, `Choose Your Package` / `Kies Uw Pakket` / `Kies Jouw Pakket`, `2-in-1`
- **D-06:** Audit output groups results by file family (not by phrase) so editors see all changes needed per file in one place
- **D-07:** Document removal candidates with their full dependency graph: which nav items, footer links, and sitemap entries reference them across all 48 HTML files
- **D-08:** Confirmed removal investigation targets: `bouw-een-park.html` family (3 files), `3d-spellen.html` family (3 files), "Choose Your Package" / "Kies Uw/Jouw Pakket" sections in 12 product partials -- final removal decision deferred to Phase 5 after spreadsheet confirmation
- **D-09:** Orphaned partials (`content-nl.html`, `content-en.html`) are safe to remove since no shell page references them
- **D-10:** Parse `website-adjustments.xlsx` into structured markdown during this phase so all downstream phases have a machine-readable change list -- do not defer spreadsheet interpretation to later phases

### Claude's Discretion
- Output file format and naming for the inventory document
- Exact grep patterns and script structure for the phrase audit
- Level of detail in the route dependency map

### Deferred Ideas (OUT OF SCOPE)
None -- analysis stayed within phase scope
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| QLTY-01 | Visitor can navigate edited routes without broken internal links, missing assets, or dead-end removals | File-family inventory (D-01/D-02), route dependency map (D-07/D-08), and sitemap audit provide the safety net to prevent broken navigation during downstream edits |
| QLTY-02 | Legacy claims targeted by the refresh are removed from the affected duplicated file families before release | Reusable phrase-audit script (D-04/D-05/D-06) enables verifiable tracking of legacy terms across all file families through each subsequent phase |
</phase_requirements>

## Standard Stack

No new libraries or packages are needed. This phase uses only tools already present in the environment.

### Core
| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| bash/grep | built-in | Phrase audit script | Available everywhere, no install needed, matches the brownfield static-file nature of the project |
| Python 3 + pandas + openpyxl | 3.13.5 / 2.3.3 / 3.1.5 | XLSX parsing | Already installed on this machine; pandas handles the multi-sheet spreadsheet cleanly |

### Supporting
| Tool | Purpose | When to Use |
|------|---------|-------------|
| `wc -l` | Count occurrences per file | Summary statistics in audit output |
| `sort` | Deterministic output ordering | Consistent audit results across runs |
| `diff` | Compare audit runs | Verify phrase count reduction between phases |

## Architecture Patterns

### Recommended Output Structure
```
.planning/phases/01-safe-update-surface/
  01-CONTEXT.md          # already exists
  01-RESEARCH.md         # this file
  01-01-PLAN.md          # plan for file inventory
  01-02-PLAN.md          # plan for phrase audit + route check
  inventory.md           # file-family inventory output
  change-brief.md        # parsed spreadsheet
  removal-deps.md        # route dependency map for removal targets
  tools/
    phrase-audit.sh      # reusable audit script
```

### Pattern 1: File-Family Inventory Table
**What:** A markdown table where each row is a page family (shell + NL partial + EN partial) with a drift flag.
**When to use:** Every time a downstream phase needs to know which files to edit together.
**Example:**
```markdown
| Family | Shell | NL Partial | EN Partial | Drift? |
|--------|-------|------------|------------|--------|
| index | index.html | partials/index-nl.html | partials/index-en.html | YES |
| mobiele-vloer | products/mobiele-vloer.html | partials/products/mobiele-vloer-nl.html | partials/products/mobiele-vloer-en.html | TBD |
```

### Pattern 2: Grouped Phrase Audit Output
**What:** A script that runs grep for all target phrases, then groups output by file family rather than by phrase.
**When to use:** After each phase lands, re-run to verify phrase count decreases.
**Example output format:**
```
=== Family: mobiele-vloer ===
  products/mobiele-vloer.html:
    (no target phrases in shell -- content is in partials)
  partials/products/mobiele-vloer-nl.html:
    L120: "100+ games" (games, 100+)
    L425: "gratis updates" (gratis updates)
  partials/products/mobiele-vloer-en.html:
    L100: "100+ games" (games, 100+)
    L213: "free updates" (free updates)
```

### Pattern 3: Route Dependency Map
**What:** For each removal candidate, list every file and line that links to it, plus sitemap/robots entries.
**When to use:** Before any page removal or nav restructuring in Phase 5.
**Example:**
```markdown
### bouw-een-park.html
- **Sitemap:** sitemap.xml L38
- **Nav references (48 files):**
  - Desktop nav: index.html:46, onderwijs.html:36, ...
  - Mobile nav: index.html:92, onderwijs.html:66, ...
  - Footer: index.html:675, onderwijs.html:202, ...
- **Self-references:** bouw-een-park.html:40,83,255
- **Partials referencing:** partials/bouw-een-park-nl.html, partials/bouw-een-park-en.html (7 refs each)
```

### Anti-Patterns to Avoid
- **One-shot audit snapshot:** A static list of occurrences goes stale after the first edit. The audit must be a re-runnable script.
- **Phrase-grouped output:** Grouping by phrase (all "games" hits, then all "100+" hits) forces editors to mentally merge across sections. Group by file family instead.
- **Partial inventory:** Missing even one file family means a downstream phase could skip a file and introduce NL/EN drift.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| XLSX parsing | Manual cell-by-cell reading | `pandas.read_excel()` with openpyxl engine | The spreadsheet has NaN rows, merged concepts, and two sheets; pandas handles this cleanly |
| Cross-file search | Custom Python crawler | `grep -rn` with `--include="*.html"` | grep is faster, already handles the flat file structure, and is universally available |
| Drift detection | Manual diff of shell vs partial nav | `diff <(grep pattern shell) <(grep pattern partial)` | Shell pages embed full HTML documents; partials are fragments. Diffing specific nav sections catches drift mechanically |

## Common Pitfalls

### Pitfall 1: Missing the shell-vs-partial content split
**What goes wrong:** Treating the shell page as the source of truth for content, when content actually lives in the partials (shell pages load partials via HTMX).
**Why it happens:** Shell pages contain the full Dutch content inline as a default, but the NL partial also has a copy of the same content. Edits to the shell without matching edits to the NL partial cause drift.
**How to avoid:** The inventory must flag which files in a family carry content. For most pages, the shell embeds Dutch defaults but the NL and EN partials are the real edit targets.
**Warning signs:** Shell page content differs from NL partial content for the same page.

### Pitfall 2: Relative path differences between root and product pages
**What goes wrong:** Nav links use `bouw-een-park.html` in root pages but `../bouw-een-park.html` in product pages. A search for exact link text misses one variant.
**Why it happens:** Product pages live one directory deeper (`products/`), so all relative links to root pages require `../` prefix.
**How to avoid:** The route dependency grep must search for both `bouw-een-park.html` and `../bouw-een-park.html` patterns (or use a pattern like `bouw-een-park\.html` without the path prefix).
**Warning signs:** Grep counts don't match expected file counts.

### Pitfall 3: "games" is both a target phrase and legitimate content
**What goes wrong:** The word "games" appears in contexts that should be changed (e.g., "100+ games" -> "60+ programs") and contexts that may be legitimate (e.g., "sportgames" in Dutch compound words, or gaming-specific product descriptions).
**Why it happens:** "games" is a common English loanword in Dutch marketing copy.
**How to avoid:** The audit script should capture surrounding context (grep -n with some context lines) so reviewers can distinguish actionable hits from false positives. Flag compound Dutch words like "sportgames" separately.
**Warning signs:** Very high hit counts for "games" (~238 across 23 files) suggest many are embedded in product descriptions that need case-by-case review.

### Pitfall 4: Spreadsheet structure is not purely tabular
**What goes wrong:** Treating the XLSX as a clean table when rows 9-37 are actually free-text package descriptions embedded in the "Page" column with NaN in all other columns.
**Why it happens:** The spreadsheet was authored as a human-readable brief, not a structured data source. Package tier descriptions, pricing, and positioning guidance are inline notes.
**How to avoid:** Parse the spreadsheet in two passes: (1) extract structured task rows (rows with non-NaN Page, Section, and Task columns), and (2) extract the free-text block (rows 9-37) as the "IAM mobiel" package definition brief.
**Warning signs:** NaN values in Section/Task columns.

### Pitfall 5: "2-in-1" may not appear literally in current HTML
**What goes wrong:** Searching for "2-in-1" returns zero hits, leading to the conclusion it's already been removed.
**Why it happens:** The term may appear in image alt text, CSS class names, or with different formatting (spaces, encoding). Current grep shows 0 hits for "2-in-1" and "2 in 1" across HTML files.
**How to avoid:** Search for variant patterns: `2-in-1`, `2 in 1`, `2in1`, `two-in-one`, and check image filenames and alt attributes. Also check CSS and JS files. The spreadsheet references "2-in-1" as both a product name and an image label to remove.
**Warning signs:** Zero grep hits for a term the spreadsheet explicitly references.

## Code Examples

### Spreadsheet Parsing Script
```python
# Source: verified against actual website-adjustments.xlsx structure
import pandas as pd

xl = pd.ExcelFile('website-adjustments.xlsx')

# Sheet 1: Structured tasks (filter out NaN-only rows)
df = pd.read_excel(xl, sheet_name='Website Adjustments')
tasks = df.dropna(subset=['Section', 'Task'])
# Result: ~10 actionable task rows with Page, Section, Task, Current, New

# Free-text block: rows where Page has content but Section is NaN
notes = df[df['Section'].isna() & df['Page'].notna()]
# Result: package definitions, positioning guidance
```

### Phrase Audit Script Structure
```bash
#!/usr/bin/env bash
# phrase-audit.sh -- reusable legacy phrase audit
# Usage: ./phrase-audit.sh [--summary | --full]
# Groups output by file family

PATTERNS=(
  "games"
  "free updates"
  "gratis updates"
  "100+"
  "Choose Your Package"
  "Kies Uw Pakket"
  "Kies Jouw Pakket"
  "2-in-1"
  "2 in 1"
)

# Build combined grep pattern
COMBINED=$(IFS='|'; echo "${PATTERNS[*]}")

# For each HTML file, check all patterns
for f in $(find . -name "*.html" -not -path "./.planning/*" | sort); do
  hits=$(grep -n -i -E "$COMBINED" "$f" 2>/dev/null)
  if [ -n "$hits" ]; then
    echo "=== $f ==="
    echo "$hits"
    echo ""
  fi
done
```

### Drift Detection Between Shell and Partial
```bash
# Compare nav structure in shell vs NL partial
# Shell pages have full <nav>, partials have nav inside #page-wrapper
diff <(grep -n 'href=.*\.html' index.html | head -20) \
     <(grep -n 'href=.*\.html' partials/index-nl.html | head -20)
```

## Verified Codebase Facts

These counts were verified by direct grep on the repository (2026-04-01):

| Metric | Count | Source |
|--------|-------|--------|
| Total HTML files | 49 | `find . -name "*.html"` excluding `.planning/` |
| Root shell pages | 8 | index, prijzen, over-ons, onderwijs, parken-speelhallen, zorg-revalidatie, 3d-spellen, bouw-een-park |
| Product shell pages | 7 | interactieve-vloer, -muur, -zandbak, -klimwand, -tekeningen, mobiele-vloer, software-maatwerk |
| Root partials (NL+EN pairs) | 18 | 9 families x 2 languages (includes orphaned content-*) |
| Product partials (NL+EN pairs) | 14 | 7 families x 2 languages |
| Legal/policy pages (no partials) | 3 | cookiebeleid, privacybeleid, toegankelijkheid |
| Orphaned partials | 2 | partials/content-nl.html, partials/content-en.html (no shell references them) |
| Files referencing "bouw-een-park" or "3d-spellen" | 48 | Every HTML file (nav is duplicated everywhere) |
| Total line references to removal candidates | 266 | grep -rn count |
| Files with "Choose Your Package" variants | 12 | All product partials (NL+EN) |
| Files with "games" | 23 | Across root and product pages/partials |
| Files with "gratis updates" or "free updates" | 6 | Product partials only |
| "2-in-1" literal matches | 0 | Not found in current HTML (may be in images/alt text or already removed) |
| Sitemap entries | 17 | Including bouw-een-park and 3d-spellen |

## Spreadsheet Structure Summary

The `website-adjustments.xlsx` file has two sheets:

### Sheet 1: "Website Adjustments" (48 rows, 10 columns)
- **Rows 0-3:** Structured tasks for Homepage and "Product page 2-in-1" (Page, Section, Task, Current Situation, New Situation, Status, Responsible)
- **Rows 5-7:** More "Product page 2-in-1" tasks (text changes, image fixes)
- **Rows 9-37:** Free-text block defining the IAM mobiel umbrella brand and three package tiers (solo/duo/premium) with pricing and positioning
- **Rows 38-47:** Additional product page tasks (Interactive floor deletions, Interactive wall changes, Sandbox/Climbing wall/Software package section deletions)

### Sheet 2: "More info" (86 rows, 1 column)
- Detailed instructions for Homepage products image, FAQ question/answer replacement
- Detailed 2-in-1 product page text and image change instructions
- Full package specifications for floor-only, wall-only, and floor+wall configurations

### Key Actionable Tasks (extracted)
| Row | Page | Task | Detail |
|-----|------|------|--------|
| 0 | Homepage | Update image | Yellow square -> real 2-in-1 housing image |
| 1-2 | Homepage | Update FAQ | "How many games" -> "How many interactive programs" with new answer |
| 3,5-7 | Product page 2-in-1 | Text + image changes | "free updates" -> "no license costs", "games" -> "programs", remove screws photos |
| 38 | Interactive floor | Delete text | Remove "free updates" and game content text |
| 41 | Interactive floor | Change movie | Unspecified change |
| 42-44 | Interactive wall | Multiple | Remove "2 in 1" from picture, "100+ games" -> "60+ games", remove "free updates" |
| 45 | Sandbox | Delete section | Remove "Choose Your Package" |
| 46 | Climbing wall | Delete page | Remove entire page |
| 47 | Software & Custom Dev | Delete section | Remove "Choose Your Package" |

## Open Questions

1. **Climbing wall page deletion scope**
   - What we know: Row 46 says "Delete page" for "Products Interactive Climbing Wall"
   - What's unclear: This conflicts with D-08 which only lists `bouw-een-park` and `3d-spellen` as removal investigation targets, not `interactieve-klimwand`
   - Recommendation: Flag in inventory for Phase 5 confirmation. The climbing wall page has the same nav dependency footprint as the other removal candidates (referenced in all 48 files).

2. **"2-in-1" term not found in HTML**
   - What we know: grep returns 0 matches for "2-in-1" and "2 in 1" across all HTML files
   - What's unclear: The spreadsheet extensively references "2-in-1" as a current product name. The term may exist in image filenames, alt text with different encoding, or may have already been partially cleaned up.
   - Recommendation: Expand the phrase audit to search media filenames and check for URL-encoded variants. Also check if the term appears only in the spreadsheet as a reference name rather than literal site copy.

3. **Drift detection methodology**
   - What we know: CONTEXT.md states shell-partial drift has already occurred (e.g., index.html nav differs from partials/index-nl.html)
   - What's unclear: Exact extent of drift across all 15+ file families
   - Recommendation: Use diff-based comparison of nav sections between shell and NL partial for each family. Mark drift status in inventory. Full drift audit is part of Plan 01-01.

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | bash (shell script assertions) |
| Config file | none -- see Wave 0 |
| Quick run command | `bash .planning/phases/01-safe-update-surface/tools/phrase-audit.sh --summary` |
| Full suite command | `bash .planning/phases/01-safe-update-surface/tools/phrase-audit.sh --full` |

### Phase Requirements to Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| QLTY-01 | All routes navigable, no broken links from removals | smoke | `grep -rn 'href=.*\.html' --include='*.html' \| sort -u` cross-referenced against existing files | No -- Wave 0 |
| QLTY-02 | Legacy phrases auditable across file families | smoke | `bash phrase-audit.sh --summary` returns counts per family | No -- Wave 0 |

### Sampling Rate
- **Per task commit:** `bash phrase-audit.sh --summary`
- **Per wave merge:** Full audit + route cross-reference
- **Phase gate:** Inventory complete, audit script produces correct grouped output, route dependency map covers all removal candidates

### Wave 0 Gaps
- [ ] `phrase-audit.sh` -- covers QLTY-02 (reusable audit script)
- [ ] Route cross-reference check -- covers QLTY-01 (verify all hrefs point to existing files)

## Sources

### Primary (HIGH confidence)
- Direct codebase inspection via grep and find (all counts verified 2026-04-01)
- `website-adjustments.xlsx` parsed via pandas+openpyxl (full content extracted)
- `.planning/codebase/STRUCTURE.md`, `CONCERNS.md`, `CONVENTIONS.md` -- project-authored codebase maps

### Secondary (MEDIUM confidence)
- `.planning/phases/01-safe-update-surface/01-CONTEXT.md` -- user decisions from discussion phase

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- no new tools needed, all verified present
- Architecture: HIGH -- output format is documentation, not code; patterns are straightforward markdown + shell
- Pitfalls: HIGH -- all identified through direct codebase inspection and spreadsheet parsing
- Spreadsheet structure: HIGH -- fully parsed and verified

**Research date:** 2026-04-01
**Valid until:** 2026-05-01 (stable -- static HTML site with no upstream dependency changes expected)
