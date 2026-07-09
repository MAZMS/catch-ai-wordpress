<?php
/**
 * Header template.
 *
 * @package catch-ai
 */
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="Catch AI texts your missed callers back in 10 seconds — automatically, in your business name. Automatic missed-call text-back for Australian tradies and small businesses.">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<header class="site-header">
	<div class="wrap">
		<a class="brand" href="<?php echo esc_url( home_url( '/' ) ); ?>">
			<span class="logo">C</span>
			<span><?php bloginfo( 'name' ); ?></span>
		</a>

		<nav class="nav" aria-label="Primary">
			<a href="#how">How it works</a>
			<a href="#who">Who it's for</a>
			<a href="#pricing">Pricing</a>
			<a href="#faq">FAQ</a>
		</nav>

		<div class="header-actions">
			<a class="login" href="#">Login</a>
			<a class="btn btn-lime" href="#demo">Try the demo</a>
		</div>
	</div>
</header>
