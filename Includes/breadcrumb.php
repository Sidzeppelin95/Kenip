<?php
function render_breadcrumbs(array $items): void {
    if (!$items) return;
    echo '<nav class="breadcrumbs shell" aria-label="Breadcrumb"><ol><li><a href="index.php">Home</a></li>';
    foreach ($items as $item) {
        echo '<li>';
        if (!empty($item['href'])) echo '<a href="' . e($item['href']) . '">';
        echo e($item['label'] ?? '');
        if (!empty($item['href'])) echo '</a>';
        echo '</li>';
    }
    echo '</ol></nav>';
}
