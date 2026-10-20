<?php
http_response_code(404);require __DIR__.'/includes/bootstrap.php';
$page=['title'=>'Page not found | '.site_config()['owner_name'],'description'=>'The requested page could not be found.','path'=>'404.php'];
require __DIR__.'/includes/header.php';
?>
<main id="main-content"><section class="page-hero error-page"><div class="container"><p class="eyebrow">Error / 404</p><h1>This path leads <em>nowhere useful.</em></h1><p class="hero-lede">The page may have moved, or the address may be incorrect. Return to the home page or explore the main sections.</p><div class="button-row"><a class="button button-primary" href="<?=e(site_url())?>">Return home ↗</a><a class="button button-secondary" href="<?=e(site_url('solutions.php'))?>">Explore solutions ↗</a></div></div></section></main>
<?php require __DIR__.'/includes/footer.php'; ?>
