<?php
/**
 * Front page — the Catch AI single-page landing.
 *
 * @package catch-ai
 */

get_header();

// Reusable inline SVG check (lime) used in the pricing lists.
$check_ink  = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><rect width="24" height="24" rx="6" fill="oklch(88% .07 240)"/><path d="M7 12.5l3 3 7-7" stroke="oklch(30% .05 240)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
$check_lime = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="11" fill="oklch(92% .19 120)"/><path d="M7 12.5l3 3 7-7" stroke="oklch(30% .1 130)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
?>

<!-- ============================ HERO ============================ -->
<section class="hero bg-sky">
	<div class="wrap">
		<div class="hero-grid">
			<div class="hero-copy">
				<span class="eyebrow">For Australian Tradies &amp; Small Businesses</span>
				<h1>Every missed call is a job going to <span class="italic">someone else.</span></h1>
				<p class="sub">Catch AI texts your missed callers back in 10 seconds — automatically, in your business name. They wait for you instead of moving on.</p>
				<div class="hero-cta">
					<a class="btn btn-lime" href="#demo">Get it on my phone</a>
					<a class="btn btn-outline" href="#how">How it works</a>
				</div>
				<div class="hero-bullets">
					<span>No contract</span>
					<span>Works on any phone</span>
					<span>Setup in 15 minutes</span>
					<span>Australian numbers</span>
				</div>
			</div>

			<div class="hero-visual">
				<div class="notif">
					<div class="t">New lead &middot; 0418 234 567</div>
					<div class="b">"need a safety inspection before settlement"</div>
				</div>
				<div class="van-card"></div>
				<div class="replied"><b>Catch AI</b> replied in 9s</div>

				<div class="phone">
					<div class="phone-screen">
						<div class="phone-top">
							<span>9:41</span>
							<span class="name">Dave's Plumbing</span>
							<span>&bull;&bull;&bull;</span>
						</div>
						<div class="phone-body">
							<div class="missed">Missed call &middot; 0412 345 678</div>
							<div class="bubble them">Hi! Sorry we missed your call — this is Dave's Plumbing. What can we help with today? 🔧</div>
							<div class="bubble me">need someone to replace a hot water system asap</div>
							<div class="bubble them">Absolutely — that's our bread and butter. What suburb are you in? We'll get someone out today. 👍</div>
							<div class="hotlead">
								<div class="tag">HOT LEAD</div>
								<div class="q">"need someone to replace a hot water system asap"</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- ============================ STATS ============================ -->
<section class="stats bg-ink">
	<div class="wrap">
		<div class="stats-grid">
			<div class="stat">
				<div class="num">59,039</div>
				<div class="lbl">missed calls recovered for Australian businesses so far today</div>
			</div>
			<div class="stat">
				<div class="num">1 in 3</div>
				<div class="lbl">Calls to the average tradie go unanswered every single day</div>
			</div>
			<div class="stat">
				<div class="num">80%</div>
				<div class="lbl">Of callers who get voicemail don't leave a message — they just call someone else</div>
			</div>
			<div class="stat">
				<div class="num">10s</div>
				<div class="lbl">How long it takes us to text your missed caller back — every single time</div>
			</div>
		</div>
	</div>
</section>

<!-- ============================ HOW IT WORKS ============================ -->
<section id="how" class="sec bg-bg">
	<div class="wrap">
		<div class="sec-head">
			<span class="eyebrow">How it works</span>
			<h2>Set it up once.<br>We handle every missed call after that.</h2>
			<p>You keep your existing number. Calls you answer pass through completely normally. We only kick in the moment a call goes unanswered.</p>
		</div>
		<div class="steps">
			<div class="step-card">
				<div class="step-num">1</div>
				<h3>Your phone rings. You can't get to it.</h3>
				<p>You're on the tools, driving between jobs, in a consult room, or tied up with a customer. A potential job calls — and rings out. That's where we come in.</p>
			</div>
			<div class="step-card">
				<div class="step-num">2</div>
				<h3>Your caller gets a text in under 10 seconds.</h3>
				<p>A friendly, professional text goes out from your business name. Plain English, in your voice. No robot language. It looks exactly like you sent it from your own phone.</p>
			</div>
			<div class="step-card">
				<div class="step-num">3</div>
				<h3>You see the conversation and call back the hot ones.</h3>
				<p>When they reply, you get an instant notification with a link to the thread. Read what the job is — then only pick up the phone for the calls worth your time.</p>
			</div>
		</div>
	</div>
</section>

<!-- ============================ THE DIFFERENCE ============================ -->
<section class="sec bg-ink-2">
	<div class="wrap">
		<div class="sec-head">
			<span class="eyebrow">The difference</span>
			<h2>What happens to a missed call — <span class="italic">with and without</span> Catch AI.</h2>
			<p>You can't always pick up. What happens next determines whether that caller becomes your job or your competitor's.</p>
		</div>
		<div class="compare">
			<div class="compare-card">
				<span class="compare-tag tag-bad">Without Catch AI</span>
				<div class="compare-row"><div class="h">Your phone rings</div><div class="d">You're on a job and can't answer</div></div>
				<div class="compare-row"><div class="h">They hit voicemail</div><div class="d">A generic beep. Nothing personal.</div></div>
				<div class="compare-row"><div class="h">80% hang up without leaving a message</div><div class="d">They're not going to wait around.</div></div>
				<div class="compare-row"><div class="h">They Google the next tradie on the list</div><div class="d">Your competitor picks up. Or texts back first.</div></div>
				<div class="outcome outcome-bad"><b>Outcome:</b> That job is gone. You never even knew it was there.</div>
			</div>
			<div class="compare-card">
				<span class="compare-tag tag-good">With Catch AI</span>
				<div class="compare-row"><div class="h">Your phone rings</div><div class="d">You're on a job and can't answer</div></div>
				<div class="compare-row"><div class="h">They get your text in 10 seconds</div><div class="d">"Hi! Sorry we missed you — what can we help with?"</div></div>
				<div class="compare-row"><div class="h">They reply with the job details</div><div class="d">They're talking to your business — not moving on.</div></div>
				<div class="compare-row"><div class="h">You get notified instantly</div><div class="d">A tap shows you exactly what the job is.</div></div>
				<div class="outcome outcome-good"><b>Outcome:</b> You call back the ones worth your time. Job booked.</div>
			</div>
		</div>
	</div>
</section>

<!-- ============================ WHO IT'S FOR ============================ -->
<section id="who" class="sec bg-mint">
	<div class="wrap">
		<div class="sec-head">
			<span class="eyebrow">Who it's for</span>
			<h2>If you're on the tools,<br>you're missing calls.</h2>
			<p>Catch AI works for any trade or service business where the phone rings and no one can always pick up. Sound familiar?</p>
		</div>
		<div class="who-grid">
			<?php
			$who = array(
				array( 'Tradies', 'Plumbers', 'who-plumber.jpg', 'Knee-deep in a bathroom reno when a burst pipe enquiry calls. That\'s an $800 emergency callout handed to the next name on Google — before you could even dry your hands.' ),
				array( 'Tradies', 'Electricians', 'who-electrician.jpg', 'Up on a roof or inside a live switchboard — your phone might as well be in another suburb. By the time you\'re out, they\'ve already called someone else and booked them in.' ),
				array( 'Tradies', 'Locksmiths', 'who-locksmith.jpg', 'Locked-out callers ring three tradies and book the first one to reply. That first reply is now yours, automatically, in under 10 seconds — every single time.' ),
				array( 'Professionals', 'Real estate agents', 'who-realestate.jpg', 'At an open home when your next listing enquiry calls. Miss that one call and you miss the appraisal — and everything that comes after it.' ),
				array( 'Service Businesses', 'Health &amp; beauty', 'who-beauty.jpg', 'With a client on the table when a new booking enquiry rings. They book with whoever gets back to them first — and it\'s not going to be your voicemail.' ),
				array( 'Tradies', 'Builders', 'who-builder.jpg', 'On a noisy site when a $50k renovation enquiry calls. Can\'t hear it. Can\'t answer. Can\'t even see you missed it for three hours. Catch AI catches it the second it rings out.' ),
			);
			foreach ( $who as $w ) {
				printf(
					'<article class="who-card"><div class="img" style="background-image:url(%1$s)"></div><div class="body"><div class="cat">%2$s</div><h3>%3$s</h3><p>%4$s</p></div></article>',
					catch_ai_asset( $w[2] ),
					esc_html( $w[0] ),
					wp_kses_post( $w[1] ),
					wp_kses_post( $w[3] )
				);
			}
			?>
		</div>
	</div>
</section>

<!-- ============================ PRICING ============================ -->
<section id="pricing" class="sec bg-bg">
	<div class="wrap">
		<div class="sec-head">
			<span class="eyebrow">Pricing</span>
			<h2>Two plans. No lock-in.<br>No setup fee.</h2>
			<p>Both plans are month-to-month. Cancel any time with 30 days notice. Setup takes 15 minutes and we do it with you on a call.</p>
		</div>
		<div class="price-grid">
			<div class="price-card">
				<div class="tier">Tier 1</div>
				<h3>Instant Text Back</h3>
				<p class="price-desc">Every missed call gets a text back within 10 seconds. Simple and effective.</p>
				<div class="amount"><span class="big">$149</span><span class="per">per month &middot; inc. GST</span></div>
				<ul class="feat">
					<li><?php echo $check_ink; ?> Text sent in under 10 seconds of a missed call</li>
					<li><?php echo $check_ink; ?> In your business name and voice — not robot language</li>
					<li><?php echo $check_ink; ?> Two-way SMS — they reply, you respond</li>
					<li><?php echo $check_ink; ?> Instant notification when a customer texts back</li>
					<li><?php echo $check_ink; ?> Simple web inbox — no app download needed</li>
					<li><?php echo $check_ink; ?> Monthly leads-recovered report</li>
					<li><?php echo $check_ink; ?> Works on any phone or number type</li>
				</ul>
				<a class="btn btn-ink btn-block" href="#demo">Try the demo first</a>
				<p class="price-note">No setup fee &middot; No contract &middot; Cancel any time</p>
			</div>

			<div class="price-card dark">
				<span class="popular">Most Popular</span>
				<div class="tier">Tier 2</div>
				<h3>AI Qualifying</h3>
				<p class="price-desc">The AI asks what the job is before you call back. You only talk to the ones worth your time.</p>
				<div class="amount"><span class="big">$249</span><span class="per">per month &middot; inc. GST</span></div>
				<ul class="feat">
					<li><?php echo $check_lime; ?> Everything in Instant Text Back, plus:</li>
					<li><?php echo $check_lime; ?> AI asks: What's the job? Which suburb? How urgent?</li>
					<li><?php echo $check_lime; ?> Pre-qualified lead summary before you call back</li>
					<li><?php echo $check_lime; ?> Filters tyre-kickers before they reach you</li>
					<li><?php echo $check_lime; ?> Questions tailored to your trade or service type</li>
					<li><?php echo $check_lime; ?> Book directly from the conversation</li>
					<li><?php echo $check_lime; ?> Saves 2+ hours of follow-up calls every week</li>
				</ul>
				<a class="btn btn-lime btn-block" href="#demo">Try the demo free</a>
				<p class="price-note">No setup fee &middot; No contract &middot; Cancel any time</p>
			</div>
		</div>

		<div class="price-help">
			<p class="q">Not sure which plan is right for you?</p>
			<p>Book a 15-minute call and we'll help you decide — no pressure.</p>
			<a class="btn btn-outline" href="#demo">Book a 15-minute call</a>
		</div>
	</div>
</section>

<!-- ============================ TESTIMONIALS ============================ -->
<section class="sec bg-ink">
	<div class="wrap">
		<div class="sec-head">
			<span class="eyebrow">What clients say</span>
			<h2>Tradies are recovering jobs<br>they didn't know they were losing.</h2>
		</div>
		<div class="tst-grid">
			<div class="tst-card">
				<div class="stars">★★★★★</div>
				<p class="quote">"I had no idea how many calls I was missing every day. First month, I recovered 11 conversations I would have just lost. That's paid for itself ten times over."</p>
				<div class="tst-author"><span class="tst-av">D</span><span><span class="n">Dave M.</span><br><span class="r">Plumber &middot; Parramatta, NSW</span></span></div>
			</div>
			<div class="tst-card">
				<div class="stars">★★★★★</div>
				<p class="quote">"Set it up in 20 minutes on a Tuesday arvo. By Friday it had already replied to six callers while I was on jobs. Genuinely dead simple — I don't think about it at all now."</p>
				<div class="tst-author"><span class="tst-av">S</span><span><span class="n">Sarah K.</span><br><span class="r">Electrician &middot; Brisbane, QLD</span></span></div>
			</div>
			<div class="tst-card">
				<div class="stars">★★★★★</div>
				<p class="quote">"The AI qualifying is the best part. I used to call back every unknown number and waste half the morning. Now I only call the real jobs. Saves me two hours a week, easy."</p>
				<div class="tst-author"><span class="tst-av">M</span><span><span class="n">Marcus T.</span><br><span class="r">Locksmith &middot; Melbourne, VIC</span></span></div>
			</div>
		</div>
		<p class="tst-disclaimer">Testimonials are representative examples for illustration. Replace with your real clients' words as you collect them.</p>
	</div>
</section>

<!-- ============================ FAQ ============================ -->
<section id="faq" class="sec bg-bg">
	<div class="wrap">
		<div class="sec-head">
			<span class="eyebrow">FAQ</span>
			<h2>Straight answers.</h2>
		</div>
		<div class="faq-list">
			<?php
			$faqs = array(
				array( 'Does it replace my current phone number?', 'No. You keep your existing mobile or landline exactly as it is. Calls you answer work completely normally — we never touch those. We only kick in when a call genuinely goes unanswered. Setting up the forwarding rule takes about 5 minutes and we walk you through it.' ),
				array( 'Will my customers know the text is automated?', 'Most won\'t. The texts are written in plain, friendly language with your business name — they look exactly like you sent them from your own phone. We write the templates in your voice during the 15-minute setup call. We do include a legally required opt-out option in line with the Spam Act 2003, but the message itself is designed to feel personal, not robotic.' ),
				array( 'What if I actually pick up the call?', 'Nothing happens. We only trigger a text when the call genuinely goes unanswered. If you pick up, the call passes through exactly as normal — no text is sent, no notification fires. Catch AI is completely invisible when you answer.' ),
				array( 'How do I reply to customers who text back?', 'When a customer replies, you get a notification on your phone with a direct link. Tap it and you\'re in a simple inbox where you can read the full thread and reply. No app to download, no password to remember, works on any smartphone — including the one you already use for everything else.' ),
				array( 'Is this legal in Australia?', 'Yes. We only send texts to people who called your number first — they initiated contact, so consent is clear. Every outbound text identifies your business by name and includes an opt-out option as required by the Spam Act 2003. We built compliance in from the start, not as an afterthought.' ),
				array( 'Is there a setup fee or contract?', 'No setup fee. No contract. Both plans are month-to-month and you can cancel any time with 30 days written notice — no penalty, no fee, no fuss. We\'d rather earn your business every month by delivering results than lock you in.' ),
				array( 'How long does setup take?', 'About 15 minutes. We do a short onboarding call with you, set up the number forwarding, write your text templates together in your voice, and test it live before we finish. Most clients are fully live the same day they sign up.' ),
				array( 'What if the system has an outage?', 'We monitor the system around the clock. If there\'s a disruption, we\'ll notify you immediately and work to restore service as fast as possible. In the meantime, your calls simply ring through as normal — no outgoing texts, but no missed calls either. We\'ll proactively reach out if anything affects your service.' ),
			);
			foreach ( $faqs as $i => $faq ) {
				$open = 0 === $i ? ' open' : '';
				printf(
					'<div class="faq-item%1$s"><button class="faq-q" aria-expanded="%2$s"><span>%3$s</span><span class="faq-icon">+</span></button><div class="faq-a"><p>%4$s</p></div></div>',
					esc_attr( $open ),
					0 === $i ? 'true' : 'false',
					esc_html( $faq[0] ),
					esc_html( $faq[1] )
				);
			}
			?>
		</div>
	</div>
</section>

<!-- ============================ DEMO / CTA ============================ -->
<section id="demo" class="sec demo bg-sky">
	<div class="wrap">
		<div class="demo-grid">
			<div class="demo-copy">
				<span class="eyebrow">Try it now</span>
				<h2>Your next missed call doesn't have to be a lost job.</h2>
				<p class="lead">Try it on your own phone in 30 seconds. No account, no credit card, no commitment.</p>
				<div class="demo-steps">
					<div class="demo-step"><span class="n">1</span><p>Enter your name, business name, and mobile number below.</p></div>
					<div class="demo-step"><span class="n">2</span><p>Call our demo number — let it ring out, or decline it.</p></div>
					<div class="demo-step"><span class="n">3</span><p>Check your texts. Reply like one of your customers would — watch what happens next.</p></div>
				</div>
			</div>

			<div class="demo-card">
				<form class="demo-form" method="post" action="#" onsubmit="return false;">
					<div class="field">
						<label for="d-name">Your name</label>
						<input id="d-name" type="text" name="name" placeholder="Dave" autocomplete="name">
					</div>
					<div class="field">
						<label for="d-biz">Business name</label>
						<input id="d-biz" type="text" name="business" placeholder="Dave's Plumbing" autocomplete="organization">
					</div>
					<div class="field">
						<label for="d-phone">Your mobile number</label>
						<input id="d-phone" type="tel" name="phone" placeholder="04__ ___ ___" autocomplete="tel">
					</div>
					<p class="consent">By submitting, I agree to receive one demo call and text to this number to demonstrate the service. Reply STOP to opt out at any time.</p>
					<button type="submit" class="btn btn-lime btn-block">See the demo on my phone</button>
					<div class="demo-mini">
						<span>No sign-up required</span>
						<span>No credit card</span>
						<span>One text, one call</span>
					</div>
				</form>
			</div>
		</div>
	</div>
</section>

<?php get_footer(); ?>
