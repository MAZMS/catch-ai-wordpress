# Catch AI — WordPress Theme

An exact WordPress recreation of the **Catch AI** landing page
(https://tradie-text-back.lovable.app/) — automatic missed-call text-back for
Australian tradies and small businesses.

The original is a React single-page app. This is a self-contained classic
WordPress theme that reproduces the same design, content, fonts, colours and
layout using native PHP templates — no page builder or third-party plugin
required.

## What's included

```
catch-ai/
├── style.css        Theme header + the complete stylesheet (design tokens, all sections)
├── functions.php    Enqueues Google Fonts (Fraunces + Inter), styles and the accordion script
├── header.php       <head>, sticky nav bar
├── front-page.php   The full landing page (hero → stats → how it works → difference →
│                    who it's for → pricing → testimonials → FAQ → demo)
├── footer.php       4-column footer + legal line
├── index.php        Fallback template (renders the same landing content)
├── assets/
│   ├── main.js      FAQ accordion + smooth-scroll behaviour
│   ├── hero-plumber.jpg
│   └── who-*.jpg    The six "Who it's for" card images
├── preview.html     Static preview of the output (open in a browser, no WordPress needed)
└── README.md
```

## Install

**Option A — Upload the zip (recommended)**

1. Zip the `catch-ai` folder so the archive contains `catch-ai/style.css` at its root.
2. In WordPress: **Appearance → Themes → Add New → Upload Theme**.
3. Choose the zip, click **Install Now**, then **Activate**.

**Option B — Manual / FTP**

1. Copy the entire `catch-ai` folder into `wp-content/themes/`.
2. **Appearance → Themes → Activate "Catch AI"**.

## Make the landing page show on the home page

`front-page.php` is used automatically for whatever WordPress serves as the
front page. To be explicit:

1. **Settings → Reading → Your homepage displays → A static page** (or "Your
   latest posts" — either works, `front-page.php` and `index.php` both render
   the landing content).
2. Optionally set **Settings → General → Site Title** to `Catch AI` — it is used
   in the logo, nav brand and footer.

## Customising

- **Text / copy** — edit the relevant section in `front-page.php`. Pricing
  features and FAQ items are simple PHP arrays near the top of each section, so
  you can add/remove rows without touching markup.
- **Colours** — all colours are CSS custom properties in the `:root` block at
  the top of `style.css` (e.g. `--sky`, `--ink`, `--lime`, `--mint`). Change one
  value to re-skin the whole site.
- **Fonts** — Fraunces (headings) and Inter (body) are loaded from Google Fonts
  in `functions.php`.
- **Images** — replace the files in `assets/` (keep the same filenames) to swap
  the hero and "Who it's for" photos.
- **Demo form** — the form in the demo section is a static markup placeholder
  (matches the original's visual). Wire it to a real handler or a form plugin
  (e.g. Contact Form 7 / WPForms / Fluent Forms) when you're ready to collect
  leads.

## Notes on fidelity

- Design tokens (colours, radii, fonts) were captured directly from the original
  site's computed styles, so the palette matches exactly (OKLCH values preserved).
- All body copy, headings, stats, pricing tiers, testimonials and FAQ answers are
  reproduced verbatim from the source.
- The testimonials and the "ABN [YOUR ABN]" placeholder in the footer are the
  same illustrative placeholders the original ships with — replace them with your
  real details.

## Preview without WordPress

Open `preview.html` in any browser (or serve the folder over HTTP) to see the
exact rendered output. This file is for QA only and is not part of the theme's
WordPress runtime.
