# Siddhartha Dutta Sharma — Independent Software Vendor & Technology Partner

Responsive PHP website built into the repository's pre-created directory structure. The implementation uses PHP, HTML, CSS, JSON content, and Python-generated SVGs. It has no JavaScript, contact form, message-submission endpoint, SMTP integration, external form service, analytics, or frontend framework.

## Existing project layout

- `Website/` — page templates for home, solutions, capabilities, technology, approach, about, contact, privacy, and 404. The terms URL is handled by the existing privacy template with a query flag; no extra page file is added.
- `Includes/` — shared configuration, escaping/content helpers, metadata, navigation, footer, contact-link rendering, and reusable presentation helpers.
- `Work/` — category overview and data-driven category detail page.
- `data/` — editable JSON content and public-site configuration. The pre-existing filename `data/technology,json` contains a comma rather than a dot; the code intentionally reads and validates that exact filename.
- `assets/css/` and `assets/svg/` — stylesheets and four accessible diagrams.
- `python/` — SVG generation, sitemap generation, validation, and optional Tkinter Visual Lab.
- `tests/` — standard-library unit tests.

## Requirements and local checks

PHP 8.1+ and Python 3.10+ are recommended. Tkinter is optional. No Composer, Node, npm, or database is required.

Run from the repository root:

```sh
python python/build.py
python python/validate_content.py
python python/validate_assets.py
python -m unittest discover -s tests -v
find Website Work Includes -type f -name '*.php' -print0 | xargs -0 -n1 php -l
```

The included `.htaccess` configures Apache rewrites from root URLs to the existing `Website/` and `Work/` templates. For local browsing, use Apache with PHP enabled; PHP's built-in server does not process `.htaccess` automatically.

## Configuration

Edit `data/site.json`. `production_url`, `public_email`, `linkedin_url`, `business_website_url`, `public_business_location`, and `legal_entity_name` are JSON `null` until the actual details are verified. This is intentional: these values are optional and should not be guessed. The GitHub profile URL points to the repository owner account. Set a verified HTTPS `production_url` before generating the sitemap.

## Deployment

Deploy to Apache with PHP-FPM or a supported PHP runtime and TLS. GitHub Pages cannot execute PHP. Configure the production web server to deny direct access to `Includes/`, `data/`, `python/`, and `tests/`; Nginx needs equivalent rules because it ignores `.htaccess`. Review the privacy notice against the actual host's logging and retention practices before launch.

## Before launch

Confirm domain, DNS and TLS; verify public contact and legal details; generate the sitemap after setting the production URL; test routes, CSS/SVG, keyboard focus, reduced motion, mobile layout, and 404 behavior. This repository does not claim a live deployment. The independent practice is distinguished from Kenip Private Limited and other separate legal entities.
