<?php ?><nav aria-label="Main navigation">
<?php foreach (site_data('navigation.json') as $item): ?>
<a href="<?=e(site_url($item['href']))?>"><?=e($item['label'])?></a>
<?php endforeach; ?>
</nav>