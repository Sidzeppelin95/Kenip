<?php if (!empty($breadcrumbs) && is_array($breadcrumbs)): ?>
<nav class="breadcrumbs container" aria-label="Breadcrumb"><ol>
<?php foreach ($breadcrumbs as $index => $crumb): ?><li><?php if (!empty($crumb['href']) && $index < count($breadcrumbs)-1): ?><a href="<?= e(site_url($crumb['href'])) ?>"><?= e($crumb['label']) ?></a><?php else: ?><span aria-current="page"><?= e($crumb['label']) ?></span><?php endif; ?></li><?php endforeach; ?>
</ol></nav>
<?php endif; ?>
