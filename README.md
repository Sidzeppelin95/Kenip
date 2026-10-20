# Kenip — Siddhartha Dutta Sharma

This repository contains the website source and a static, GitHub Pages-compatible website at the repository root.

## Why both PHP and HTML exist

GitHub Pages serves static files; it does **not** execute PHP. The public Pages deployment therefore needs a root index.html and HTML pages for each route. The PHP implementation is retained for PHP-capable hosting, while the committed HTML pages are what GitHub Pages renders. Do not configure Pages to publish the README or a source-only folder.

## Published routes

- /Kenip/ — home
- /Kenip/solutions/
- /Kenip/work/
- /Kenip/capabilities/
- /Kenip/technology/
- /Kenip/approach/
- /Kenip/about/
- /Kenip/contact/
- /Kenip/privacy/
- /Kenip/terms/
- /Kenip/404.html — not-found page

The static pages use assets/css/static-site.css, semantic HTML, accessible navigation and no JavaScript dependency, contact form, or server-side submission endpoint. Update the matching HTML page and test whenever route content changes. Verify public contact details and legal copy before publishing claims that require owner or jurisdiction-specific review.

## Validation

Run the static route checks with:

    python -m unittest discover -s tests -p 'test_static_site.py' -v

The PHP source also remains available for local PHP hosting; PHP files are not interpreted by GitHub Pages.

## Deployment

In repository Settings → Pages, select Deploy from a branch, choose main and / (root). The root index.html is the required entry point. After merging a reviewed PR, allow the Pages build to finish, then verify the homepage and every route above. This PR does not change repository Pages settings or claim a deployment has completed.
