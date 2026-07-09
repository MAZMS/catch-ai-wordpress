<?php
/**
 * Fallback template. Catch AI is a single-page landing theme, so any request
 * that isn't the static front page simply renders the landing content.
 *
 * @package catch-ai
 */

// Reuse the landing page so the theme always displays the Catch AI design.
get_template_part( 'front-page' );
