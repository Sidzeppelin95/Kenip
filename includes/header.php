<!doctype html>
<html lang="en">
<head><?php require __DIR__ . '/metadata.php'; ?></head>
<body>
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <div class="brand-group">
      <a class="brand-logo-link" href="#logo-preview" aria-label="Expand Kenip logo"><img class="brand-logo" src="<?= e(site_url('assets/svg/Logo.svg')) ?>" alt="Kenip logo"></a>
      <a class="brand" href="<?= e(site_url()) ?>" aria-label="<?= e(site_config()['owner_name']) ?> home">
        <span class="brand-copy"><strong><?= e(site_config()['owner_name']) ?></strong><small>INDEPENDENT SOFTWARE &amp; SYSTEMS</small></span>
      </a>
    </div>
    <?php require __DIR__ . '/navigation.php'; ?>
    <a class="header-link" href="<?= e(site_url('contact.php')) ?>">Get in touch <span aria-hidden="true">↗</span></a>
  </div>
</header>
<div id="logo-preview" class="logo-preview" role="dialog" aria-modal="true" aria-label="Expanded Kenip logo">
  <a class="logo-preview-backdrop" href="#main-content" aria-label="Close expanded logo"></a>
  <div class="logo-preview-content">
    <a class="logo-preview-close" href="#main-content" aria-label="Close expanded logo">×</a>
    <img src="<?= e(site_url('assets/svg/Logo.svg')) ?>" alt="Kenip logo, expanded">
  </div>
</div>

