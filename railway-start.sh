#!/bin/bash
# Startup script for the Catch AI WordPress container on Railway.
# We override the image CMD, so we must do the WordPress setup the official
# entrypoint would normally do (seed core, create wp-config) ourselves.
set -uo pipefail

WP="wp --allow-root --path=/var/www/html"

# 1. Seed WordPress core into /var/www/html if it isn't there yet.
if [ ! -f /var/www/html/wp-load.php ]; then
  echo "[catch-ai] Seeding WordPress core files..."
  cp -a /usr/src/wordpress/. /var/www/html/
fi
# Always refresh the baked theme (covers image updates on redeploy).
mkdir -p /var/www/html/wp-content/themes
cp -a /usr/src/wordpress/wp-content/themes/catch-ai /var/www/html/wp-content/themes/ 2>/dev/null || true
chown -R www-data:www-data /var/www/html

# 2. Parse host/port and wait for the database to accept connections.
#    Uses PHP's mysqli (always present in the image) — no mysql client needed.
DB_HOST_ONLY="${WORDPRESS_DB_HOST%%:*}"
DB_PORT="${WORDPRESS_DB_HOST##*:}"
[ "$DB_PORT" = "$WORDPRESS_DB_HOST" ] && DB_PORT=3306
echo "[catch-ai] Waiting for database at ${DB_HOST_ONLY}:${DB_PORT}..."
for i in $(seq 1 60); do
  if DBH="$DB_HOST_ONLY" DBP="$DB_PORT" php -r '
      mysqli_report(MYSQLI_REPORT_OFF);
      $c=@mysqli_connect(getenv("DBH"),getenv("WORDPRESS_DB_USER"),getenv("WORDPRESS_DB_PASSWORD"),"",(int)getenv("DBP"));
      exit($c?0:1);' >/dev/null 2>&1; then
    echo "[catch-ai] Database is up."
    break
  fi
  sleep 2
done

# 3. Create wp-config.php if missing.
if [ ! -f /var/www/html/wp-config.php ]; then
  echo "[catch-ai] Creating wp-config.php..."
  $WP config create \
    --dbhost="$WORDPRESS_DB_HOST" \
    --dbname="$WORDPRESS_DB_NAME" \
    --dbuser="$WORDPRESS_DB_USER" \
    --dbpass="$WORDPRESS_DB_PASSWORD" \
    --skip-check --force
fi

# 4. Install WordPress if it isn't installed yet.
if ! $WP core is-installed >/dev/null 2>&1; then
  echo "[catch-ai] Installing WordPress..."
  $WP core install \
    --url="${WP_URL:-http://localhost}" \
    --title="${WP_TITLE:-Catch AI}" \
    --admin_user="${WP_ADMIN_USER:-admin}" \
    --admin_password="${WP_ADMIN_PASSWORD:-changeme123}" \
    --admin_email="${WP_ADMIN_EMAIL:-admin@example.com}" \
    --skip-email
else
  echo "[catch-ai] WordPress already installed."
fi

# 5. Keep home/siteurl in sync with the Railway domain and activate the theme.
if [ -n "${WP_URL:-}" ]; then
  $WP option update home "${WP_URL}" >/dev/null 2>&1 || true
  $WP option update siteurl "${WP_URL}" >/dev/null 2>&1 || true
fi
$WP theme activate catch-ai >/dev/null 2>&1 || true
$WP rewrite structure '/%postname%/' --hard >/dev/null 2>&1 || true
chown -R www-data:www-data /var/www/html/wp-content 2>/dev/null || true

echo "[catch-ai] Startup complete. Handing off to Apache."

# 6. Run Apache in the foreground (container's main process).
exec apache2-foreground
