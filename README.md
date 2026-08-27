# NaRu Empowerment Life Coach Group

Marketing site for NaRu Empowerment — transformational coaching for clarity,
confidence, alignment, and professional action.

## Structure

Four chapters plus a home page, all static HTML with no build step required
to serve:

| File | Chapter |
| --- | --- |
| `index.html` | Home |
| `coaching.html` | 01 — Coaching |
| `butterfly-effect.html` | 02 — The Butterfly Effect Methodology |
| `naomi.html` | 03 — Meet Naomi |
| `connect.html` | 04 — Connect |

`assets/site.css` and `assets/butterfly.js` are shared by every page.

## The metamorphosis

`butterfly-effect.html` is the only page carrying the animated background:
a low-poly wireframe that morphs larva → chrysalis → emerging → butterfly
across the page's scroll, completing at ~85% so the finished butterfly lands
on the closing quote band. The motion lags the scroll so it drifts rather
than tracking one-to-one. Every other page is completely static.

The page opts in with `class="bg-live"` on `<body>`, which also switches its
sections to transparent so nothing sits in front of the animation.

## Editing

Page content is generated from a shared shell so the header, nav and footer
can't drift apart:

```bash
cd _dev && python3 build_content.py
```

Edit `_dev/build_content.py` for copy and `_dev/build_pages.py` for the
shell, then re-run. `_dev/bundle.py` packs all five pages into one
self-contained file for sharing.

## Still to do

- Replace the gradient placeholders with real photography (Meet Naomi).
- Wire the two forms to an email provider — they validate and confirm in the
  browser but do not send anywhere yet.
- Confirm the phone, email and copyright details before wider release.
