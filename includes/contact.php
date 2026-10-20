<?php $contactLinks = render_contact_links(); ?>
<?php if ($contactLinks): ?><div class="contact-links">
<?php foreach ($contactLinks as $item): ?><div class="contact-link-row"><span><?= e($item['label']) ?></span><?php if ($item['href']): ?><a href="<?= e($item['href']) ?>"<?php if (str_starts_with($item['href'], 'https://')): ?> rel="noopener noreferrer"<?php endif; ?>><?= e($item['value']) ?> <span aria-hidden="true">↗</span></a><?php else: ?><strong><?= e($item['value']) ?></strong><?php endif; ?></div><?php endforeach; ?>
</div><?php else: ?><div class="notice"><strong>Contact details are being configured.</strong><p>Public contact links will appear here once verified. No unverified email address or profile is published.</p></div><?php endif; ?>
