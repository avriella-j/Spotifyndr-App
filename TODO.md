# TODO - UI consistency fixes (templates + CSS only)

## Step 1: Convert about/support templates to extend base
- [x] Update `app/templates/about.html` to `{% extends "base.html" %}` and move content into `{% block content %}`.
- [x] Update `app/templates/support.html` to `{% extends "base.html" %}` and move content into `{% block content %}`.
- [ ] Remove inline `<style>` from both templates (we will rely on existing CSS, and/or add page CSS if needed).



## Step 2: Fix/align navigation + base layout
- [ ] Ensure `app/templates/base.html` includes styles + uses the nav partials (desktop + mobile).

## Step 3: Ensure base applies global theme correctly
- [ ] Update `static/css/main.css` variables to include the requested `--bg-primary`, `--accent`, etc., while keeping existing variables working.

## Step 4: Populate/adjust page CSS to match markup
- [ ] Verify `static/css/pages/*.css` (profile/explore/messaging/fyp/mutuals/settings) are sufficient and fill any missing rules.

## Step 5: Page template markup alignment (no JS changes)
- [ ] Make `explore.html` swipe-card markup/classes match existing JS selectors.
- [ ] Make messaging layout/bubble classes match existing JS expectations.

## Step 6: Final verification
- [ ] Manually open key authenticated pages and confirm consistent styling.
- [ ] Smoke test CSS loading (base + component + page CSS).

