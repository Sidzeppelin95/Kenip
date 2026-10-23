<!doctype html>
<html lang="en">
<head><?php require __DIR__ . '/metadata.php'; ?></head>
<body>
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <div class="brand-group">
      <a class="brand-logo-link" href="<?= e(site_url('assets/svg/Logo.svg')) ?>" aria-label="View full-size Kenip logo"><img class="brand-logo" src="<?= e(site_url('assets/svg/Logo.svg')) ?>" alt="Kenip logo"></a>
      <a class="brand" href="<?= e(site_url()) ?>" aria-label="<?= e(site_config()['owner_name']) ?> home">
        <span class="brand-copy"><strong><?= e(site_config()['owner_name']) ?></strong><small>INDEPENDENT SOFTWARE &amp; SYSTEMS</small></span>
      </a>
    </div>
    <?php require __DIR__ . '/navigation.php'; ?>
    <a class="header-link" href="<?= e(site_url('contact.php')) ?>">Get in touch <span aria-hidden="true">↗</span></a>
  </div>
</header>
