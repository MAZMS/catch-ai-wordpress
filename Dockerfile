# Catch AI — WordPress on Railway
# Official WordPress image with the Catch AI theme baked in and auto-activated.
FROM wordpress:6.7-php8.3-apache

# WP-CLI (used by the startup script to install WordPress and activate the theme)
COPY --from=wordpress:cli /usr/local/bin/wp /usr/local/bin/wp

# Small deps WP-CLI likes to have (mysql client for db checks, less for pager)
RUN apt-get update \
    && apt-get install -y --no-install-recommends less default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Ensure EXACTLY one Apache MPM is active (prefork, required by mod_php).
# Remove any enabled MPM symlinks, then enable only prefork. The final line
# prints the active MPM into the build logs so the result is verifiable.
RUN set -eux; \
    rm -f /etc/apache2/mods-enabled/mpm_*.load /etc/apache2/mods-enabled/mpm_*.conf; \
    ln -sf /etc/apache2/mods-available/mpm_prefork.load /etc/apache2/mods-enabled/mpm_prefork.load; \
    ln -sf /etc/apache2/mods-available/mpm_prefork.conf /etc/apache2/mods-enabled/mpm_prefork.conf; \
    apache2ctl -t -D DUMP_MODULES 2>&1 | grep -i mpm

# Bake the theme into the image. The official entrypoint seeds
# /usr/src/wordpress -> /var/www/html on first boot, so the theme ships with it.
COPY catch-ai /usr/src/wordpress/wp-content/themes/catch-ai

# Startup script: waits for the DB, installs WordPress if needed,
# keeps the site URL in sync with the Railway domain, activates the theme,
# then hands off to Apache.
COPY railway-start.sh /usr/local/bin/railway-start.sh
RUN chmod +x /usr/local/bin/railway-start.sh

# The base image's ENTRYPOINT (docker-entrypoint.sh) still runs first to
# generate wp-config.php from the WORDPRESS_DB_* env vars, then execs this CMD.
CMD ["railway-start.sh"]
