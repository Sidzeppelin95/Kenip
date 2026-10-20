<?php $navigation = site_data('navigation.json'); ?>
<nav class="navigation" aria-label="Main navigation">
<?php foreach ($navigation as $item): ?>
<a href="<?= e(site_url($item['href'])) ?>"><?= e($item['label']) ?></a>
<?php endforeach; ?>
</nav>
