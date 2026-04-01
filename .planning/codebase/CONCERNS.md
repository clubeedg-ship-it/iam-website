# Codebase Concerns

## Highest-Risk Areas

### 1. Content Duplication

- The same business content is duplicated across full pages and partials.
- A single product or pricing change can require edits in multiple NL and EN files.
- `website-adjustments.xlsx` already indicates a batch of requested copy changes that will likely touch several duplicated locations.

### 2. Translation Drift

- English partials are partly generated from string replacement in `tools/migrate_i18n.py`.
- Some English content remains partially untranslated or awkward, which suggests generated output still needs manual review.
- Structural drift between NL and EN files is easy to introduce because there is no shared source of truth.

### 3. Monolithic Frontend Assets

- `styles.css` is 5603 lines and mixes global, page, animation, and compliance styles.
- `projector.js` contains multiple unrelated features in one global file.
- This raises regression risk when making targeted UI changes.

### 4. Fragile Relative Paths

- Root pages and product pages use different path prefixes.
- Partial files add another variation in relative linking.
- Copying markup between locations can silently break media, script, or partial paths.

### 5. Manual Operational Workflow

- Requested site updates currently arrive in an external spreadsheet.
- There is no CMS, content schema, or structured import path for those updates.
- This creates a high chance of incomplete rollout when copy, pricing, or naming changes span many pages.

## Specific Repository Signals

- `website-adjustments.xlsx` requests renaming and repositioning around the `2-in-1` / `IAM mobiel` product line.
- The same spreadsheet also requests FAQ wording changes, package restructuring, image cleanup, and removal of some page sections.
- Repository search shows many hard-coded occurrences of terms like `games`, `100+`, `free updates`, and `Choose Your Package`, which aligns with likely change hotspots.

## Technical Quality Gaps

- No automated test or CI safety net exists.
- No content consistency checker exists.
- Inline script snippets and duplicated nav/footer markup increase maintenance load.

## Security / Privacy Notes

- The site appears low-risk from an integration standpoint because it has no backend or third-party analytics in the inspected files.
- Cookie consent claims only necessary cookies are used, but the banner still stores an accept/reject choice in `localStorage`; that is probably acceptable, but legal wording should stay aligned with actual behavior.

## Recommended Attention Order

1. Establish the canonical files that drive each page family before editing content.
2. Apply naming and package changes systematically across full pages and partials.
3. Verify every affected route in both languages after edits.
4. Consider reducing duplication or introducing a content generation source before larger future revisions.
