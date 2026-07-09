# Catch AI — WordPress site (Railway-ready)

An exact WordPress recreation of the **Catch AI** landing page
(https://tradie-text-back.lovable.app/) — automatic missed-call text-back for
Australian tradies and small businesses — packaged to deploy on
[Railway](https://railway.com) with one MySQL database and one WordPress service.

## Repo layout

```
.
├── Dockerfile          WordPress image with the Catch AI theme baked in
├── railway-start.sh    Boot script: waits for DB, installs WP, activates the theme
├── .dockerignore
├── catch-ai/           The WordPress theme (see catch-ai/README.md)
└── README.md
```

## How it runs

- The `Dockerfile` starts from the official `wordpress` image and copies the
  `catch-ai/` theme into it.
- On boot, `railway-start.sh` waits for MySQL, runs `wp core install` if the site
  isn't set up yet, keeps `home`/`siteurl` in sync with the Railway domain, and
  activates the `catch-ai` theme — so the landing page is live with no manual
  wp-admin steps.

## Deploy on Railway

1. Create a project and add a **MySQL** database.
2. Add a service from this repo (Railway auto-detects the `Dockerfile`).
3. Set these variables on the WordPress service (database ones reference the
   MySQL service):

   | Variable | Value |
   |---|---|
   | `WORDPRESS_DB_HOST` | `${{MySQL.MYSQLHOST}}:${{MySQL.MYSQLPORT}}` |
   | `WORDPRESS_DB_USER` | `${{MySQL.MYSQLUSER}}` |
   | `WORDPRESS_DB_PASSWORD` | `${{MySQL.MYSQLPASSWORD}}` |
   | `WORDPRESS_DB_NAME` | `${{MySQL.MYSQLDATABASE}}` |
   | `WP_URL` | `https://<your-generated-domain>` |
   | `WP_TITLE` | `Catch AI` |
   | `WP_ADMIN_USER` | your admin username |
   | `WP_ADMIN_PASSWORD` | a strong password |
   | `WP_ADMIN_EMAIL` | your email |

4. Generate a domain for the WordPress service and set `WP_URL` to it.
5. Redeploy. The site comes up at `WP_URL`; wp-admin is at `WP_URL/wp-admin`.

## Local preview (no WordPress)

Open `catch-ai/preview.html` in a browser to see the exact rendered design.
