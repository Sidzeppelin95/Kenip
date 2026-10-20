<?php
$sectionEyebrow = $sectionEyebrow ?? '';
$sectionTitle = $sectionTitle ?? '';
$sectionCopy = $sectionCopy ?? '';
?>
<div class="section-heading">
<?php if ($sectionEyebrow !== ''): ?><p class="eyebrow"><?= e($sectionEyebrow) ?></p><?php endif; ?>
<h2><?= e($sectionTitle) ?></h2>
<?php if ($sectionCopy !== ''): ?><p class="section-intro"><?= e($sectionCopy) ?></p><?php endif; ?>
</div>
