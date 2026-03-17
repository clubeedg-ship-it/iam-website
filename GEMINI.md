# Gemini CLI Project Rules

## Architecture
This project uses a "Shell & Partial" architecture. The python script `build_shells.py` acts as the master template generator that wraps page-specific content (from the `partials/` directory) into complete HTML files.

## Mandatory Rules

### 1. Single Source of Truth for Layout
All structural changes affecting the overall layout (headers, footers, meta tags, global script tags) MUST be made within the `build_shells.py` script's template. 
- Do NOT make manual edits to the layout shell of generated HTML files (e.g., `index.html`, `blog.html`). 
- Always run `python build_shells.py` to propagate layout changes to all pages.

### 2. Styling
- Avoid inline styles (`style="..."`).
- Use CSS classes defined in `styles.css` for all styling requirements to maintain consistency.

### 3. Asset Pathing
- Use consistent relative paths for all assets (images, scripts, styles) across the site to ensure they load correctly regardless of the hosting environment.

### 4. GDPR Compliance
- Third-party scripts, especially analytics or tracking (like Google Tag Manager), MUST NOT be loaded before explicit user consent is granted via the cookie consent mechanism.

### 5. Content & Internationalization (i18n)
- Page-specific content lives in the `partials/` directory, separated by language (e.g., `index-nl.html`, `index-en.html`).
- Ensure absolute structural parity between the Dutch (NL) and English (EN) partials.
- Avoid relying solely on client-side JS (`js/site.js`) to swap major content blocks if it causes a "flash of unstyled/incorrect content" on initial load. The generated HTML should default to the correct language structure where possible.

### 6. HTML Validity
- Ensure all HTML is structurally valid. 
- Watch out for common errors like duplicate closing tags (e.g., `</main>`) or duplicate script inclusions in both the shell and the partials.
