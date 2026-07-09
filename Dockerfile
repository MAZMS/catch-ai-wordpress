# Catch AI — WordPress on Railway
# Official WordPress image with the Catch AI theme baked in and auto-activated.
# We deliberately avoid `apt-get install` here: on Debian it can pull an Apache
# upgrade that re-enables the default `event` MPM next to `prefork`, breaking
# mod_php with "More than one MPM loaded". Staying stock keeps prefork-only.
FROM wordpress:6.7-php8.3-apache

# WP-CLI (talks to MySQL via PHP, so no mysql client package is required).
COPY --from=wordpress:cli /usr/local/bin/wp /usr/local/bin/wp

# Bake the theme into the image. The official entrypoint seeds
# /usr/src/wordpress -> /var/www/html, so the theme ships with it; the startup
# script also copies it explicitly.
COPY catch-ai /usr/src/wordpress/wp-content/themes/catch-ai

# Startup script: seeds core, waits for the DB (via PHP), installs WordPress,
# keeps the site URL in sync with the Railway domain, activates the theme,
# then hands off to Apache.
COPY railway-start.sh /usr/local/bin/railway-start.sh
RUN chmod +x /usr/local/bin/railway-start.sh

CMD ["railway-start.sh"]
