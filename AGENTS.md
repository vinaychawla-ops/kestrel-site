# AGENTS.md — kestrel-site

Notes for agents working in this repo. The workspace-level lessons
(proxy env, Modal SDK quirks, git-database push flow) live in the operator's
own AGENTS.md; this file is repo-scoped.

## Source of truth

- `stitch-prompt.md` is the design brief. The HTML in `kestrel-clean/` is
  Stitch output **plus** a manual cleanup pass — do not "fix" pages back toward
  Stitch defaults (e.g. do not reintroduce the drifted 4-question Pricing FAQ;
  the brief's 5 topics are canonical).
- `kestrel-clean/CLEANUP_NOTES.md` records exactly what the cleanup changed.
  If any page is ever regenerated from Stitch, re-apply those fixes.

## Cleanup invariants (verify after any edit)

- Exactly one `<h1>` per page.
- Every mobile-menu toggle carries `aria-expanded` and flips it on toggle.
- Global teal `:focus-visible` ring present on every page.
- No `style=""` attributes anywhere.
- Sub-page nav links point at the real sibling files
  (`features.html`, `pricing.html`, `docs.html`, `about.html`, `contact.html`),
  never `#` or dead Stitch routes.
- Pricing FAQ is exactly the brief's 5 questions, as native `<details>` blocks.

## Known tech debt (do not "fix" without asking)

- Tailwind CDN on every page (brief says no frameworks) — removal is a full
  CSS rewrite, explicitly deferred.
- Extra JS beyond the brief's single permitted script (pricing toggle, docs
  tabs/copy, contact fake-submit + PGP copy).
- Logo hotlinks to `lh3.googleusercontent.com` — needs a local asset.
- Contact form is demo-only; footer links partly placeholder; Download CTAs
  point at nonexistent `#downloads`.

## Deploy

- `modal_app.py` serves `kestrel-clean/` via FastAPI `StaticFiles(html=True)`.
- `add_local_dir(..., copy=True)` — never drop `copy=True`; without it Modal
  mounts files at container startup and redeploys can serve stale code.
- The live deployment is the `kestrel-site` Modal app
  (https://chawlavinay--kestrel-site-web.modal.run). Redeploys need a fresh
  one-time Modal token from the owner; tokens are single-use, never stored,
  and the owner revokes them afterwards.

## Excluded from this repo

- `kestrel-export/` (raw 30-file Stitch export with duplicate generations and
  screenshots) and `kestrel-clean.zip` — intermediate artifacts, not source.
