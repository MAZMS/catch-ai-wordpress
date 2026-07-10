<?php
/**
 * Import the Catch AI page directly as a live Elementor page (no GUI needed).
 *
 * Run with WP-CLI from this folder:
 *   wp eval-file import-page.php
 *
 * Creates (or updates) a published page "Catch AI — Home" with the Elementor
 * layout, using the blank "Elementor Canvas" template (the design ships its own
 * header/footer). Safe to run repeatedly. Requires Elementor to be active.
 */
if ( ! defined( 'ABSPATH' ) ) {
	echo "Run via WP-CLI:  wp eval-file import-page.php\n";
	exit( 1 );
}

if ( ! did_action( 'elementor/loaded' ) && ! class_exists( '\Elementor\Plugin' ) ) {
	WP_CLI::error( 'Elementor is not active. Run: wp plugin install elementor --activate' );
}

$file = __DIR__ . '/catch-ai-elementor-data.json';
if ( ! file_exists( $file ) ) {
	WP_CLI::error( 'catch-ai-elementor-data.json not found next to this script.' );
}
$data_json = file_get_contents( $file );
if ( ! is_array( json_decode( $data_json, true ) ) ) {
	WP_CLI::error( 'catch-ai-elementor-data.json is not a valid Elementor data array.' );
}

$title = 'Catch AI — Home';

// Find an existing page with this title (avoids duplicates on re-run).
$found = get_posts( array(
	'post_type'      => 'page',
	'post_status'    => 'any',
	'title'          => $title,
	'posts_per_page' => 1,
	'fields'         => 'ids',
) );
$pid = $found ? (int) $found[0] : 0;

if ( ! $pid ) {
	$pid = wp_insert_post( array(
		'post_title'   => $title,
		'post_status'  => 'publish',
		'post_type'    => 'page',
		'post_content' => '',
	) );
	if ( is_wp_error( $pid ) || ! $pid ) {
		WP_CLI::error( 'Failed to create the page.' );
	}
}

update_post_meta( $pid, '_elementor_edit_mode', 'builder' );
update_post_meta( $pid, '_elementor_template_type', 'wp-page' );
update_post_meta( $pid, '_wp_page_template', 'elementor_canvas' );
update_post_meta( $pid, '_elementor_version', defined( 'ELEMENTOR_VERSION' ) ? ELEMENTOR_VERSION : '3.20.0' );
// Elementor stores _elementor_data as a slashed JSON string.
update_post_meta( $pid, '_elementor_data', wp_slash( $data_json ) );

if ( class_exists( '\Elementor\Plugin' ) ) {
	\Elementor\Plugin::$instance->files_manager->clear_cache();
}

WP_CLI::success( "Catch AI page imported as page ID {$pid}." );
WP_CLI::log( "Preview: " . get_permalink( $pid ) );
WP_CLI::log( "To make it the homepage:" );
WP_CLI::log( "  wp option update show_on_front page" );
WP_CLI::log( "  wp option update page_on_front {$pid}" );
