<!doctype html>
<html lang="en">
<head><?php require __DIR__ . '/metadata.php'; ?></head>
<body>
<a class="skip" href="<?=e(site_url(''))?>#main-content">Skip to content</a>
<header class="header"><div class="shell head">
<a class="brand" href="<?=e(site_url(''))?>" aria-label="<?=e(site_config()['owner_name'])?> home"><span class="brand-monogram" aria-hidden="true">S<span>.</span></span><span><b><?=e(site_config()['owner_name'])?></b><small>SOFTWARE &amp; SYSTEMS</small></span></a>
<?php require __DIR__ . '/navigation.php'; ?>
<a class="header-cta" href="<?=e(site_url('contact.php'))?>">Get in touch ↗</a>
</div></header>