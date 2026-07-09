<?php
/**
 * Catch AI theme functions.
 *
 * @package catch-ai
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! function_exists( 'catch_ai_setup' ) ) {
	function catch_ai_setup() {
		add_theme_support( 'title-tag' );
		add_theme_support( 'post-thumbnails' );
		add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );
		add_theme_support(
			'custom-logo',
			array(
				'height'      => 60,
				'width'       => 60,
				'flex-height' => true,
				'flex-width'  => true,
			)
		);

		register_nav_menus(
			array(
				'primary' => __( 'Primary Menu', 'catch-ai' ),
			)
		);
	}
}
add_action( 'after_setup_theme', 'catch_ai_setup' );

/**
 * Enqueue fonts, styles and scripts.
 */
function catch_ai_assets() {
	// Google Fonts: Fraunces (serif headings) + Inter (body).
	wp_enqueue_style(
		'catch-ai-fonts',
		'https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap',
		array(),
		null
	);

	// Main stylesheet (theme root style.css).
	wp_enqueue_style(
		'catch-ai-style',
		get_stylesheet_uri(),
		array( 'catch-ai-fonts' ),
		wp_get_theme()->get( 'Version' )
	);

	// Front-end interactivity (FAQ accordion, smooth nav).
	wp_enqueue_script(
		'catch-ai-script',
		get_template_directory_uri() . '/assets/main.js',
		array(),
		wp_get_theme()->get( 'Version' ),
		true
	);
}
add_action( 'wp_enqueue_scripts', 'catch_ai_assets' );

/**
 * Small helper to output a theme asset URL.
 */
function catch_ai_asset( $path ) {
	return esc_url( get_template_directory_uri() . '/assets/' . ltrim( $path, '/' ) );
}
