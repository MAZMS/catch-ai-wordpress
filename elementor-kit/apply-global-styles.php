<?php
/**
 * Apply Catch AI global colors + fonts to the active Elementor kit.
 *
 * Run with WP-CLI from this folder:
 *   wp eval-file apply-global-styles.php
 *
 * Safe to run repeatedly (idempotent). Requires Elementor to be active.
 */
if ( ! defined( 'ABSPATH' ) ) {
	echo "Run via WP-CLI:  wp eval-file apply-global-styles.php\n";
	exit( 1 );
}

$kit_id = (int) get_option( 'elementor_active_kit' );
if ( ! $kit_id ) {
	WP_CLI::error( 'No active Elementor kit found. Activate Elementor first (wp plugin activate elementor).' );
}

$file = __DIR__ . '/catch-ai-global-styles.json';
if ( ! file_exists( $file ) ) {
	WP_CLI::error( 'catch-ai-global-styles.json not found next to this script.' );
}
$gs = json_decode( file_get_contents( $file ), true );
if ( ! is_array( $gs ) ) {
	WP_CLI::error( 'catch-ai-global-styles.json is not valid JSON.' );
}

$settings = get_post_meta( $kit_id, '_elementor_page_settings', true );
if ( ! is_array( $settings ) ) {
	$settings = array();
}

$settings['system_colors']     = $gs['system_colors'];
$settings['custom_colors']     = $gs['custom_colors'];
$settings['system_typography'] = $gs['system_typography'];
$settings['custom_typography'] = isset( $gs['custom_typography'] ) ? $gs['custom_typography'] : array();

// Also set sensible site-wide defaults so headings use Fraunces, body uses Inter.
$settings['body_typography_typography']    = 'custom';
$settings['body_typography_font_family']   = 'Inter';
$settings['body_typography_font_weight']   = '400';
foreach ( array( 'h1', 'h2', 'h3', 'h4', 'h5', 'h6' ) as $h ) {
	$settings[ $h . '_typography_typography' ]  = 'custom';
	$settings[ $h . '_typography_font_family' ] = 'Fraunces';
	$settings[ $h . '_typography_font_weight' ] = '500';
}

update_post_meta( $kit_id, '_elementor_page_settings', $settings );

if ( class_exists( '\Elementor\Plugin' ) ) {
	\Elementor\Plugin::$instance->files_manager->clear_cache();
}

WP_CLI::success( "Global colors & fonts applied to Elementor kit #{$kit_id}." );
