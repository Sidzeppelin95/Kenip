<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-branding"><a class="brand" href="<?= e(site_url()) ?>"><span class="brand-mark" aria-hidden="true">S<span>.</span></span><span class="brand-copy"><strong><?= e(site_config()['owner_name']) ?></strong><small>INDEPENDENT SOFTWARE &amp; SYSTEMS</small></span></a><p>Independent software vendor &amp; technology partner.</p></div>
    <div><h2>Explore</h2><a href="<?= e(site_url('solutions.php')) ?>">Solutions</a><a href="<?= e(site_url('work/')) ?>">Work categories</a><a href="<?= e(site_url('capabilities.php')) ?>">Capabilities</a><a href="<?= e(site_url('technology.php')) ?>">Technology</a></div>
    <div><h2>Practice</h2><a href="<?= e(site_url('approach.php')) ?>">Our approach</a><a href="<?= e(site_url('about.php')) ?>">About</a><a href="<?= e(site_url('contact.php')) ?>">Contact</a></div>
    <div><h2>Information</h2><a href="<?= e(site_url('privacy.php')) ?>">Privacy</a><a href="<?= e(site_url('terms.php')) ?>">Terms</a></div>
  </div>
  <div class="container footer-bottom"><span>© <?= e(current_year()) ?> <?= e(site_config()['owner_name']) ?></span><span>Clarity, evidence, useful engineering.</span></div>
</footer>
</body>
</html>
