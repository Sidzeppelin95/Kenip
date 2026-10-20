# Siddhartha Dutta Sharma — Independent Software Vendor & Technology Partner

A modular, responsive PHP business website with JSON-backed content and Python-generated static SVG illustrations. The public site has no JavaScript, contact form, submission endpoint, database, analytics script, or third-party runtime dependency.

## Requirements
- PHP 8.1+ (PHP 8.2 recommended), with JSON enabled.
- Python 3.10+ for development-time asset generation and validation only.
- No Node.js, npm, build server, database, or Python process is needed in production.

## Project structure
- Root PHP files are the public pages; work/ contains the category directory and reusable category detail route.
- includes/ contains bootstrap/configuration, output escaping, navigation, metadata, breadcrumb, section heading, contact links, header, and footer.
- data/*.json contains site settings, navigation, seven work categories, capabilities, technology domains, and delivery stages.
- assets/css/ contains the shared visual system and responsive rules.
- assets/svg/ contains generated static diagrams; python/graphics/ contains dependency-free generators.
- tests/ validates content, generated illustrations, and expected routes.

## Local PHP preview
From the repository root, run:

    php -S 127.0.0.1:8080

Then open http://127.0.0.1:8080. To verify a custom 404 page in production, configure Apache/Nginx to use /404.php for missing pages. The built-in PHP development server does not automatically route every missing URL to this custom page.

## Generate graphics and validate

    python python/build.py
    python python/validate_content.py
    python python/validate_assets.py
    python -m unittest discover -s tests -v
    find . -type f -name '*.php' -not -path './.git/*' -print0 | xargs -0 -n1 php -l

Generated SVGs are static files committed for production. Python and Tkinter are not server dependencies. python/tools/visual_lab.py is an optional local utility for selecting a diagram and exporting a generated SVG; it requires a desktop Python environment with Tkinter.

## Update business information
Edit data/site.json. public_email, linkedin_url, business_website_url, public_business_location, production_url, and base_path are configurable. Contact details are rendered only when a valid public value is configured. A public GitHub profile is configured as https://github.com/Sidzeppelin95; remove it if it should not be displayed.

- production_url: set to the verified canonical origin, including https://, with no trailing slash.
- base_path: leave empty at domain root; for a subdirectory install, set a path without a trailing slash, e.g. /site.
- public_email: set a verified public business email. It renders as a mailto link.
- linkedin_url and business_website_url: set verified HTTPS URLs only.
- public_business_location: set only a location approved for public display.

Update the JSON arrays to revise category, capability, technology, and approach content. Keep category slugs URL-safe and unique. Do not add unsupported customer results, credentials, or vendor affiliations.

## Sitemap and robots
After setting production_url, run python python/generate_sitemap.py and commit the generated sitemap.xml. Until a domain is configured, the sitemap intentionally contains no URLs rather than inventing a production host. robots.txt points to /sitemap.xml; adjust the path if hosted below a subdirectory.

## Deployment
1. Upload the repository root contents to a PHP-enabled Apache or Nginx document root.
2. Use PHP 8.1+ and disable public display of PHP errors; send errors to server logs.
3. Serve over HTTPS. Configure canonical domain and base path in data/site.json before launch.
4. Configure a custom 404 response to execute 404.php with HTTP status 404.
5. Ensure data/ is not directly browsable by server rules if the host exposes JSON files. The JSON is public content and contains no secrets; never store credentials in it.
6. Set static caching for CSS and SVG at the server/CDN layer. Do not cache PHP HTML as shared public content unless configured safely.
7. Review Privacy and Terms against actual hosting/log retention and legal requirements before launch.
8. Add verified public business contact information only after owner approval.

### Nginx 404 example
Inside the relevant server block, configure error_page 404 /404.php; and ensure PHP-FPM handles /404.php. Validate server configuration before reload. Equivalent configuration differs by host.

## Privacy and scope
The site contains no form, message receiver, newsletter, login, analytics integration, tracking pixel, or SMTP/email delivery code. Hosting providers may still create operational request logs; exact behavior depends on the hosting plan. Privacy and Terms are intentionally general and should be reviewed for the final legal context.

## Validation notes
Run the commands above locally or through repository CI. A successful syntax/content/test run validates the source tree, not a live deployment. No production domain, public business email, LinkedIn profile, legal entity, or hosting log-retention policy is inferred here. No live deployment is claimed by this repository.
