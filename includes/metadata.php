<?php
$settings = site_config();
$title = $page['title'] ?? $settings['brand_name'];
$description = $page['description'] ?? $settings['default_description'];
$canonical = canonical_url($page['path'] ?? '');
?>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="<?= e($description) ?>">
<meta name="theme-color" content="#111a20">
<meta property="og:type" content="website">
<meta property="og:title" content="<?= e($title) ?>">
<meta property="og:description" content="<?= e($description) ?>">
<?php if ($canonical !== null): ?>
<link rel="canonical" href="<?= e($canonical) ?>">
<meta property="og:url" content="<?= e($canonical) ?>">
<?php endif; ?>
<title><?= e($title) ?></title>
<link rel="icon" href="<?= e(site_url('assets/svg/hero-network.svg')) ?>" type="image/svg+xml">
<link rel="stylesheet" href="<?= e(site_url('assets/css/main.css')) ?>">
<link rel="stylesheet" href="<?= e(site_url('assets/css/layout.css')) ?>">
<link rel="stylesheet" href="<?= e(site_url('assets/css/components.css')) ?>">
<link rel="stylesheet" href="<?= e(site_url('assets/css/animations.css')) ?>">
<link rel="stylesheet" href="<?= e(site_url('assets/css/responsive.css')) ?>">
