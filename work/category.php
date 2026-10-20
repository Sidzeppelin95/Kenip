<?php
require dirname(__DIR__).'/includes/bootstrap.php';
$slug = isset($_GET['slug']) && is_string($_GET['slug']) ? strtolower(trim($_GET['slug'])) : '';
$categories = site_data('work-categories.json');
$category = null;
foreach ($categories as $candidate) {
    if (isset($candidate['slug']) && hash_equals((string)$candidate['slug'], $slug)) { $category = $candidate; break; }
}
if ($category === null) {
    http_response_code(404);
    $page=['title'=>'Category not found | '.site_config()['owner_name'],'description'=>'The requested work category was not found.','path'=>'work/category.php'];
    require dirname(__DIR__).'/includes/header.php';
    ?>
    <main id="main-content"><section class="page-hero"><div class="container"><p class="eyebrow">Work / Not found</p><h1>That category <em>isn't here.</em></h1><p class="hero-lede">Choose from the available work categories.</p><a class="button button-primary" href="<?=e(site_url('work/'))?>">Browse work categories ↗</a></div></section></main>
    <?php require dirname(__DIR__).'/includes/footer.php'; exit;
}
$page=['title'=>$category['title'].' | Work Categories','description'=>$category['summary'],'path'=>'work/category.php'];
$breadcrumbs=[['label'=>'Home','href'=>''],['label'=>'Work','href'=>'work/'],['label'=>$category['title']]];
require dirname(__DIR__).'/includes/header.php';
?>
<main id="main-content"><?php require dirname(__DIR__).'/includes/breadcrumb.php';?><section class="page-hero"><div class="container"><p class="eyebrow">Work category / <?=e($category['slug'])?></p><h1><?=e($category['title'])?>.</h1><p class="hero-lede"><?=e($category['summary'])?></p></div></section><section class="section"><div class="container category-content"><div class="prose"><p class="eyebrow">Overview</p><h2>What this domain <em>can involve.</em></h2><p><?=e($category['overview'])?></p><h3>General problem areas</h3><ul><?php foreach($category['problems'] as $problem):?><li><?=e($problem)?></li><?php endforeach;?></ul><h3>Related capabilities</h3><div class="tag-list"><?php foreach($category['capabilities'] as $capability):?><span><?=e($capability)?></span><?php endforeach;?></div></div><aside class="category-aside"><p class="eyebrow">Technical domains</p><ul class="plain-list"><?php foreach($category['technology_domains'] as $domain):?><li><?=e($domain)?></li><?php endforeach;?></ul><p class="eyebrow">Potential engagements</p><ul class="plain-list"><?php foreach($category['engagements'] as $engagement):?><li><?=e($engagement)?></li><?php endforeach;?></ul><p class="small-note">These describe possible scopes of work, not a claim of prior delivery.</p><a class="button button-primary" href="<?=e(site_url('contact.php'))?>">Discuss this domain ↗</a></aside></div></section></main>
<?php require dirname(__DIR__).'/includes/footer.php'; ?>
