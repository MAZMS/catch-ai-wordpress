#!/bin/bash
# Startup script for the Catch AI WordPress container on Railway.
# Runs after the base image's docker-entrypoint.sh has written wp-config.php.
set -uo pipefail

WP="wp --allow-root --path=/var/www/html"

# 1. Make sure the baked theme is present/updated even if /var/www/html is a volume.
mkdir -p /var/www/html/wp-content/themes
cp -r /usr/src/wordpress/wp-content/themes/catch-ai /var/www/html/wp-content/themes/ 2>/dev/null || true
chown -R www-data:www-data /var/www/html/wp-content/themes/catch-ai 2>/dev/null || true

# 2. Wait for the database to accept connections (up to ~2 minutes).
echo "[catch-ai] Waiting for database at ${WORDPRESS_DB_HOST:-unset}..."
for i in $(seq 1 60); do
  if $WP db check >/dev/null 2>&1; then
    echo "[catch-ai] Database is up."
    break
  fi
  sleep 2
done

# 3. Install WordPress if it isn't installed yet.
if ! $WP core is-installed >/dev/null 2>&1; then
  echo "[catch-ai] Installing WordPress..."
  $WP core install \
    --url="${WP_URL:-http://localhost}" \
    --title="${WP_TITLE:-Catch AI}" \
    --admin_user="${WP_ADMIN_USER:-admin}" \
    --admin_password="${WP_ADMIN_PASSWORD:-changeme123}" \
    --admin_email="${WP_ADMIN_EMAIL:-admin@example.com}" \
    --skip-email || echo "[catch-ai] core install returned non-zero (may already be installed)."
else
  echo "[catch-ai] WordPress already installed."
fi

# 4. Keep home/siteurl in sync with the Railway public domain.
if [ -n "${WP_URL:-}" ]; then
  $WP option update home "${WP_URL}" >/dev/null 2>&1 || true
  $WP option update siteurl "${WP_URL}" >/dev/null 2>&1 || true
fi

# 5. Activate the Catch AI theme and make the landing the front page.
$WP theme activate catch-ai >/dev/null 2>&1 || true
$WP rewrite structure '/%postname%/' >/dev/null 2>&1 || true
$WP rewrite flush >/dev/null 2>&1 || true

echo "[catch-ai] Startup complete. Handing off to Apache."

# 6. Run Apache in the foreground (container's main process).
exec apache2-foreground
