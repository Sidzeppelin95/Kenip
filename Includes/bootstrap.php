<?php
declare(strict_types=1);
require_once __DIR__ . '/config.php';
ini_set('display_errors', '0');
ini_set('log_errors', '1');
error_reporting(E_ALL);
function e(mixed $value): string { return htmlspecialchars((string)$value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }
function site_data(string $name): array {
    static $cache = [];
    $map = ['technology.json' => 'technology,json', 'work-categories.json' => 'workcategories.json'];
    $name = $map[$name] ?? $name;
    if (basename($name) !== $name || !preg_match('/^[a-z0-9-]+(?:\.json|,json)$/', $name)) throw new InvalidArgumentException('Invalid content filename');
    if (isset($cache[$name])) return $cache[$name];
    $path = DATA_ROOT . '/' . $name;
    if (!is_file($path)) throw new RuntimeException('Content file unavailable: ' . $name);
    $data = json_decode((string)file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
    if (!is_array($data)) throw new UnexpectedValueException('Content must be a JSON array or object: ' . $name);
    return $cache[$name] = $data;
}
function site_config(): array { return site_data('site.json'); }
function site_url(string $path = ''): string {
    $base = rtrim((string)(site_config()['base_path'] ?? ''), '/');
    $path = ltrim($path, '/');
    return $base . ($path === '' ? '/' : '/' . $path);
}
function canonical_url(string $path): ?string {
    $base = rtrim((string)(site_config()['production_url'] ?? ''), '/');
    return str_starts_with($base, 'https://') ? $base . '/' . ltrim($path, '/') : null;
}
function external_url(mixed $value): ?string {
    return is_string($value) && filter_var($value, FILTER_VALIDATE_URL) && preg_match('#^https://#i', $value) ? $value : null;
}
