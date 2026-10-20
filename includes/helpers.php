<?php
declare(strict_types=1);

function e(mixed $value): string {
    return htmlspecialchars((string)$value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
function site_config(): array {
    static $config = null;
    if ($config === null) {
        $path = DATA_ROOT . '/site.json';
        $decoded = json_decode((string)file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($decoded)) {
            throw new RuntimeException('Site configuration must be a JSON object.');
        }
        $config = $decoded;
    }
    return $config;
}
function site_data(string $filename): array {
    static $cache = [];
    if (!preg_match('/^[a-z0-9-]+\.json$/', $filename)) {
        throw new InvalidArgumentException('Invalid content filename.');
    }
    if (!isset($cache[$filename])) {
        $path = DATA_ROOT . '/' . $filename;
        if (!is_file($path)) {
            throw new RuntimeException('Required content file is missing: ' . $filename);
        }
        $value = json_decode((string)file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($value)) {
            throw new UnexpectedValueException('Content must be a JSON array or object: ' . $filename);
        }
        $cache[$filename] = $value;
    }
    return $cache[$filename];
}
function site_url(string $path = ''): string {
    $base = rtrim((string)(site_config()['base_path'] ?? ''), '/');
    $path = ltrim($path, '/');
    return $base . ($path === '' ? '/' : '/' . $path);
}
function canonical_url(string $path): ?string {
    $domain = rtrim((string)(site_config()['production_url'] ?? ''), '/');
    if (!filter_var($domain, FILTER_VALIDATE_URL) || !str_starts_with($domain, 'https://')) {
        return null;
    }
    return $domain . site_url($path);
}
function safe_external_url(mixed $value): ?string {
    return is_string($value) && filter_var($value, FILTER_VALIDATE_URL) && str_starts_with(strtolower($value), 'https://') ? $value : null;
}
function render_contact_links(): array {
    $config = site_config();
    $links = [];
    if (is_string($config['public_email'] ?? null) && filter_var($config['public_email'], FILTER_VALIDATE_EMAIL)) {
        $links[] = ['label' => 'Email', 'value' => $config['public_email'], 'href' => 'mailto:' . $config['public_email']];
    }
    foreach ([
        'linkedin_url' => 'LinkedIn profile',
        'github_url' => 'GitHub profile',
        'business_website_url' => 'Business website',
    ] as $key => $label) {
        $url = safe_external_url($config[$key] ?? null);
        if ($url !== null) {
            $links[] = ['label' => $label, 'value' => preg_replace('#^https://#', '', $url), 'href' => $url];
        }
    }
    if (is_string($config['public_business_location'] ?? null) && trim($config['public_business_location']) !== '') {
        $links[] = ['label' => 'Public business location', 'value' => $config['public_business_location'], 'href' => null];
    }
    return $links;
}
function current_year(): string { return date('Y'); }
