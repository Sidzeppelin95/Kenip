<?php
function render_contact_links(): void {
    $settings = site_config();
    $email = $settings['public_email'] ?? null;
    if (is_string($email) && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo '<a class="contact-option" href="mailto:' . e($email) . '"><span>Email</span><strong>' . e($email) . '</strong><span aria-hidden="true">↗</span></a>';
    }
    foreach (['LinkedIn' => 'linkedin_url', 'GitHub' => 'github_url', 'Business website' => 'business_website_url'] as $label => $key) {
        $url = external_url($settings[$key] ?? null);
        if ($url !== null) echo '<a class="contact-option" href="' . e($url) . '" rel="noopener noreferrer"><span>' . e($label) . '</span><strong>' . e(preg_replace('#^https://(www\.)?#', '', $url)) . '</strong><span aria-hidden="true">↗</span></a>';
    }
}
