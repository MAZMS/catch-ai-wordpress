# Catch AI — Elementor page kit

A fully-editable Elementor rebuild of the reference site
(https://catch-ai-web-production.up.railway.app/), built with **native Elementor
containers and widgets** — no page is trapped in an HTML widget. Every heading,
paragraph, image, button, link, background and section is editable in Elementor.
Works on **free Elementor** (no Pro required).

## What's in this folder

| File | Purpose |
|---|---|
| `catch-ai-elementor-template.json` | The importable Elementor **page template** (Templates → Saved Templates → Import). |
| `catch-ai-elementor-data.json` | Raw `_elementor_data` array — used by the WP-CLI one-shot importer. |
| `catch-ai-global-styles.json` | Global **colors + fonts** (applied to the Elementor kit). |
| `apply-global-styles.php` | WP-CLI script that writes the global colors/fonts into the active kit. |
| `import-page.php` | WP-CLI script that creates the live page from `catch-ai-elementor-data.json`. |
| `custom.css` | Optional: sticky header + smooth-scroll (design works without it). |
| `assets/` | The 7 source images (hero + 6 "Who it's for" photos). |
| `build_elementor.py` | The generator, if you want to tweak and regenerate the JSON. |

> **Images:** the template references the images from the live Railway URL, so
> they load immediately on import. To host them on the client's own site instead,
> upload the files in `assets/` to the Media Library and swap each Image widget's
> source (or bulk find-replace the URL — see "Re-hosting images" below).

---

## Design tokens (already configured as globals)

**Fonts** — Headings: `Fraunces` (weight 500) · Body: `Inter`.
**Global colors:**

| Global | Hex | Used for |
|---|---|---|
| Primary | `#181f2e` | dark sections, buttons |
| Secondary | `#505561` | muted text |
| Text | `#161b24` | body copy |
| Accent | `#d5f64e` | lime buttons |
| Sky | `#91d0fc` | hero / demo background |
| Ink 2 | `#0e141f` | "The difference" bg |
| Mint | `#d3edd3` | "Who it's for" bg |
| Background | `#fbfaf6` | page background |
| Accent Green | `#cafacb` | hot-lead box |
| Card | `#ffffff` | cards |
| Border | `#e0ded7` | hairlines |

---

## Import — Option A: WP-CLI (fastest, recommended for staging)

Run from **this folder** on the server (or copy the folder into the WP root):

```bash
# 1. Elementor (skip if already installed)
wp plugin install elementor --activate

# 2. Apply global colors + fonts to the active kit
wp eval-file apply-global-styles.php

# 3. Create the live page "Catch AI — Home" (blank Elementor Canvas template)
wp eval-file import-page.php

# 4. (optional) make it the site homepage — the command prints the page ID,
#    or fetch it:
PID=$(wp post list --post_type=page --title="Catch AI — Home" --field=ID)
wp option update show_on_front page
wp option update page_on_front "$PID"

# 5. Regenerate Elementor CSS
wp elementor flush-css
```

Open the page URL (or the homepage). Then edit it in Elementor:
**Pages → Catch AI — Home → Edit with Elementor**.

## Import — Option B: Elementor GUI (no CLI)

1. **Plugins → Add New →** install & activate **Elementor**.
2. **Templates → Saved Templates → Import Templates →** upload
   `catch-ai-elementor-template.json` → **Import Now**.
3. **Pages → Add New →** title it *Home* → **Edit with Elementor**.
4. In the editor, open the **Templates library (folder icon) → My Templates**,
   find *Catch AI — Home*, click **Insert**.
5. Set the page layout to **Elementor Canvas** (Page settings → gear icon →
   Page Layout → Elementor Canvas) so the design's own header/footer are used.
6. **Publish.** To make it the homepage: **Settings → Reading → A static page →
   Home**.
7. Global colors/fonts: either run `wp eval-file apply-global-styles.php`, or set
   them by hand under **Elementor → Site Settings → Global Colors / Global Fonts**
   using the table above.

## Re-hosting images on the client site (SiteGround)

By default images load from the Railway reference URL. To serve them locally:

```bash
# Upload the 7 images to the Media Library
for f in assets/*.jpg; do wp media import "$f"; done
```

Then either swap each Image widget's source in Elementor, **or** bulk-replace the
base URL across the imported page (use a search-replace plugin like *Better
Search Replace*, or WP-CLI):

```bash
wp search-replace \
  'https://catch-ai-web-production.up.railway.app/wp-content/themes/catch-ai/assets' \
  'https://YOUR-SITE.com/wp-content/uploads/2025/07' \
  wp_postmeta --include-columns=meta_value
wp elementor flush-css
```

(adjust the target path to wherever the uploads landed).

---

## After importing — test checklist

Open the page and verify at **Desktop / Tablet (≤1024) / Mobile (≤767)** using
Elementor's responsive preview (the device icons at the bottom of the editor)
and a real browser resize:

- [ ] **Responsiveness** — hero, pricing, "the difference" and demo split into two
      columns on desktop and **stack to one column** on mobile. The stats row goes
      4→2→1; card grids go 3→ wrap →1.
- [ ] **Links** — nav (How it works / Who it's for / Pricing / FAQ) and footer
      anchors jump to the matching sections; "Get it on my phone" / "Try the demo"
      buttons scroll to the demo section. The section CSS IDs (`site-header`, `how`,
      `who`, `pricing`, `faq`, `demo`) are already set in the template, so the
      anchors work on import — no manual step needed.
- [ ] **Spacing** — section vertical padding ~96px desktop / ~64px mobile; cards
      have even gaps and don't touch the screen edges.
- [ ] **Image scaling** — the 6 "Who it's for" photos and the hero van image scale
      cleanly without distortion; no horizontal scrollbar on mobile.
- [ ] **Fonts** — headings render in Fraunces (serif), body in Inter.
- [ ] **Colors** — hero/demo sky blue, dark navy stats/testimonials/footer, mint
      "Who it's for", lime buttons.
- [ ] **FAQ accordion** — items expand/collapse.

> **Anchors are pre-wired:** each section already carries its CSS ID
> (`site-header`, `how`, `who`, `pricing`, `faq`, `demo`), so the nav and button
> `#…` links resolve on import with no manual step.

## Notes on fidelity & Elementor limits

- Built entirely from native widgets: **Heading, Text Editor, Button, Image,
  Icon List, Accordion**, inside flexbox **Containers**.
- The only HTML widget is the 3 demo **input fields** (free Elementor has no form
  field widget). Everything around it is native and editable. For real
  submissions, drop in a form plugin (Contact Form 7 / WPForms / Fluent Forms) or
  Elementor Pro's Form widget.
- `custom.css` is optional and only adds the sticky header + smooth scrolling the
  original has. The layout/colors need no custom CSS.
- Regenerate the JSON after edits with: `python build_elementor.py`.
