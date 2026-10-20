<?php
function render_section_heading(string $eyebrow, string $heading, string $description = ''): void {
    echo '<div class="section-heading"><p class="eyebrow">' . e($eyebrow) . '</p><h2>' . e($heading) . '</h2>';
    if ($description !== '') echo '<p class="lede">' . e($description) . '</p>';
    echo '</div>';
}
