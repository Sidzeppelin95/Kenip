<?php
require dirname(__DIR__) . '/Includes/bootstrap.php';
$isTerms = isset($_GET['document']) && $_GET['document'] === 'terms';
$page = $isTerms
    ? ['title' => 'Terms | ' . site_config()['owner_name'], 'description' => 'General terms for using this informational technology website.', 'path' => 'terms.php']
    : ['title' => 'Privacy | ' . site_config()['owner_name'], 'description' => 'A plain-language overview of website privacy functionality.', 'path' => 'privacy.php'];
require dirname(__DIR__) . '/Includes/header.php';
?>
<main id="main-content">
<?php if ($isTerms): ?>
<section class="pagehero shell"><p class="eyebrow">Website information / Terms</p><h1>Clear expectations.<br><em>Straightforward terms.</em></h1><p class="lede">The website is provided for general information about an independent technology practice.</p></section>
<section class="section shell legal"><p class="muted">Last reviewed: October 2026</p><h2>Informational content</h2><p>Descriptions of technology domains and potential engagements are general information. They do not guarantee a service, implementation, result, delivery date, or performance improvement.</p><h2>Project-specific work</h2><p>Scope, deliverables, intellectual property, confidentiality, payment, support, warranties, and acceptance should be established in a separate written agreement before work begins.</p><h2>Third-party technologies</h2><p>Technology names are descriptive. Mention does not imply sponsorship, certification, endorsement, or official partnership.</p><h2>Legal review</h2><p>The operator's legal identity, applicable jurisdiction, and engagement-specific terms must be confirmed before production launch. This general notice is not legal advice.</p></section>
<?php else: ?>
<section class="pagehero shell"><p class="eyebrow">Website information / Privacy</p><h1>Privacy, without <em>unnecessary collection.</em></h1><p class="lede">This website is intentionally lightweight and does not include client-side tracking scripts or a contact form.</p></section>
<section class="section shell legal"><p class="muted">Last reviewed: October 2026</p><h2>Information you provide</h2><p>This website has no contact form, account registration, or message-submission endpoint. If you use a separately configured email or profile link, that interaction is handled by the relevant service and subject to its policies.</p><h2>Technical logs</h2><p>The hosting provider may process standard request data, such as IP address, request path, and timestamps, in server logs for security and operations. Retention and access depend on the hosting configuration and should be confirmed with the operator.</p><h2>Cookies, analytics, and embedded services</h2><p>The site itself does not intentionally set analytics cookies, load tracking pixels, or embed third-party widgets. Hosting and infrastructure services may have their own technical processing.</p><h2>Questions and updates</h2><p>Public contact details will be displayed only after they have been verified and configured. This notice should be reviewed against the actual hosting setup before production launch.</p></section>
<?php endif; ?>
</main>
<?php require dirname(__DIR__) . '/Includes/footers.php'; ?>
