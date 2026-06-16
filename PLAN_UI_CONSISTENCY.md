# UI Consistency Refactor Plan (Landing/About/Support -> App Pages)

## Information Gathered
- `app/templates/base.html` provides the authenticated layout: mobile header/nav, desktop sidebar, main content slot (`{% block content %}`), and includes `static/css/main.css` plus component CSS.
- `app/templates/landing.html`, `about.html`, and `support.html` each define their own “marketing” styling using embedded `<style>` blocks and custom classes like `landing-header`, `hero`, `about-hero`, `support-hero`, etc.
- Multiple authenticated pages extend `base.html` but currently look inconsistent because they rely on page-specific CSS files that are mostly simple padding and typography and lack the shared “brand system” marketing look/spacing/buttons.
  - Pages: `explore.html`, `fyp.html`, `messaging.html`, `mutuals.html`, `profile.html`, `settings.html`.
  - Some pages also embed inline CSS (e.g., `artist.html`, `user_profile.html`).
- Brand system exists in `static/css/main.css` (CSS variables for colors, spacing, typography, border radius, transitions), but page CSS doesn’t consistently use it.
- `static/css/pages/*` currently contain minimal styles and don’t include a shared “page frame” pattern (hero header, card containers, section headers, consistent buttons/inputs).

## Goal
Refactor the authenticated pages so they visually match the landing/about/support aesthetic (dark theme, Spotify-green accents, consistent hero/section layout, card-like surfaces, consistent buttons/inputs, and shared spacing).

## Plan (File-level)
### 1) Create shared “Marketing-like” page frame CSS
- Add/extend `static/css/pages/shared.css` (new) to define:
  - `.marketing-page` (padding, max width, layout)
  - `.marketing-hero` (title/subtitle block)
  - `.marketing-section` (surface card with hover)
  - `.marketing-section-title`, `.marketing-label`
  - `.marketing-grid` helpers
  - Consistent form styles for settings/message/contact where applicable.

### 2) Update page templates to use shared frame
For each of the following templates, replace the current basic `<div class="*-page">` + `<h1>` with a unified structure:
- Add a hero block at top: title + optional subtitle.
- Wrap main content in `.marketing-section` cards.
- Remove inline `<style>` blocks where present (or keep minimal, but prefer shared.css).

Templates to update:
- `app/templates/explore.html`
- `app/templates/fyp.html`
- `app/templates/messaging.html`
- `app/templates/mutuals.html`
- `app/templates/profile.html`
- `app/templates/settings.html`

Optional (recommended for consistency even if not explicitly mentioned as “rest of pages”):
- `app/templates/artist.html` and `app/templates/user_profile.html` (currently embed inline CSS).

### 3) Wire shared CSS into templates
- Either:
  - Import shared CSS via `{% block extra_css %}` in each page, or
  - Add it globally in `base.html`.
- Prefer global in `base.html` if it won’t affect app pages negatively.

### 4) Clean up conflicting/incorrect CSS variables usage
- Ensure page CSS uses `main.css` variables only.
- Fix any invalid variables referenced by page CSS (if any exist).

### 5) Add “section typography + cards” to page CSS
- Keep existing functional page layout CSS (e.g., messaging flex/columns).
- Augment with the shared frame classes.

## Dependent Files to be Edited
- `static/css/pages/shared.css` (new)
- `app/templates/*` listed in step 2
- `app/templates/base.html` (to include new CSS globally, if chosen)
- `static/css/pages/*.css` for augmenting styling as needed (explore/fyp/profile/settings/messaging/mutuals)

## Followup Steps
1. Run unit/integration tests (to ensure no template syntax breakage).
2. Manual smoke test:
   - Logged-in pages: Explore, For You, Mutuals, Messages, Profile, Settings.
   - Verify typography, spacing, cards, and button/input styling match landing/about/support vibe.

<ask_followup_question>
Proceed with implementing this plan by creating `static/css/pages/shared.css`, updating those templates, and including the CSS via `base.html`? (Yes/No)
</ask_followup_question>

