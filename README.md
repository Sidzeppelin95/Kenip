# Siddhartha Dutta Sharma — Independent Software Vendor & Technology Partner

Responsive PHP website with structured JSON content and original Python-generated SVG. No JavaScript, database, contact form, SMTP, external form service, analytics, trackers, or frontend framework.

## Structure
Root PHP pages cover Home, Solutions, Capabilities, Technology, Approach, About, Contact, Privacy, Terms, and 404. The work directory contains data-driven categories. Includes provides shared rendering and escaping. Data stores editable content and business settings. Assets contains CSS and SVG. Python contains the SVG engine, validators, sitemap generator, and optional Tkinter Visual Lab. Tests use the standard library.

## Requirements and local review
PHP 8.1+ and Python 3.10+; Tkinter optional. No Composer, Node, npm, or database required.

    php -S 127.0.0.1:8080
    python python/build.py
    python python/validate_content.py
    python python/validate_assets.py
    python -m unittest discover -s tests -v
    find . -name '*.php' -type f -print0 | xargs -0 -n1 php -l

Open http://127.0.0.1:8080. Built-in PHP server is for local review only.

## Configuration
Edit data/site.json. public_email, linkedin_url, github_url, business_website_url, and public_business_location are optional. Email and LinkedIn are intentionally blank rather than invented. production_url remains blank until the actual HTTPS domain is confirmed; base_path supports subdirectory hosting. Update JSON content files to change categories, technologies, navigation, and process steps.

## Sitemap and deployment
Set the verified HTTPS production_url then run python python/generate_sitemap.py and add its URL to robots.txt. Deploy to Apache or Nginx with PHP-FPM and TLS; GitHub Pages cannot execute PHP. Deny web access to includes, data, python, tests, and hidden files in server configuration. Nginx needs equivalent rules because it ignores .htaccess. Verify routes, CSS/SVG, contact links, and 404 over HTTPS.

## Production checklist
Confirm domain, DNS and TLS; configure verified contact and legal details; regenerate sitemap; review host logging and privacy wording; protect private directories; test keyboard focus, reduced motion, mobile layout, query strings, and 404; run validation commands. No live deployment is claimed. The independent practice is distinguished from Kenip Private Limited. Legal entity, jurisdiction, email, domain, and business location must be verified before launch.