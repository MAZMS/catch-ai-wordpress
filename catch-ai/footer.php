<?php
/**
 * Footer template.
 *
 * @package catch-ai
 */
?>
<footer class="site-footer">
	<div class="wrap">
		<div class="footer-grid">
			<div class="footer-about">
				<div class="footer-brand">
					<span class="logo" style="width:30px;height:30px;border-radius:50%;background:#fff;color:var(--ink);display:flex;align-items:center;justify-content:center;font-family:var(--sans);font-size:15px;font-weight:600;">C</span>
					<span><?php bloginfo( 'name' ); ?></span>
				</div>
				<p>Automatic missed-call text-back for Australian tradies and small businesses. Stop losing jobs to your voicemail.</p>
			</div>

			<div class="footer-col">
				<h4>Product</h4>
				<ul>
					<li><a href="#how">How it works</a></li>
					<li><a href="#pricing">Pricing</a></li>
					<li><a href="#demo">Try the demo</a></li>
					<li><a href="#who">For plumbers</a></li>
					<li><a href="#who">For electricians</a></li>
				</ul>
			</div>

			<div class="footer-col">
				<h4>Company</h4>
				<ul>
					<li><a href="#">About us</a></li>
					<li><a href="#">Contact</a></li>
					<li><a href="#">Blog</a></li>
					<li><a href="#">Case studies</a></li>
				</ul>
			</div>

			<div class="footer-col">
				<h4>Legal</h4>
				<ul>
					<li><a href="#">Privacy Policy</a></li>
					<li><a href="#">Terms of Service</a></li>
					<li><a href="#">Acceptable Use</a></li>
				</ul>
			</div>
		</div>

		<div class="footer-bottom">
			<p>&copy; <?php echo esc_html( date( 'Y' ) ); ?> <?php bloginfo( 'name' ); ?> Australia &middot; ABN [YOUR ABN] &middot; Based in Australia</p>
			<p>All texts comply with the Spam Act 2003 and include a mandatory opt-out.</p>
		</div>
	</div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
