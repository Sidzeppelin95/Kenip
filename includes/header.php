<!doctype html>
<html lang="en">
<head><?php require __DIR__ . '/metadata.php'; ?></head>
<body>
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="<?= e(site_url()) ?>" aria-label="<?= e(site_config()['owner_name']) ?> home">
      <span class="brand-mark" aria-hidden="true">S<span>.</span></span>
      <span class="brand-copy"><strong><?= e(site_config()['owner_name']) ?></strong><small>INDEPENDENT SOFTWARE &amp; SYSTEMS</small></span>
    </a>
    <?php require __DIR__ . '/navigation.php'; ?>
    <a class="header-link" href="<?= e(site_url('contact.php')) ?>">Get in touch <span aria-hidden="true">↗</span></a>
  </div>
</header>
