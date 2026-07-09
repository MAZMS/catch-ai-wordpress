/* Catch AI — front-end interactivity */
(function () {
	'use strict';

	document.addEventListener('DOMContentLoaded', function () {
		/* ---- FAQ accordion ---- */
		var items = document.querySelectorAll('.faq-item');

		function setOpen(item, open) {
			var answer = item.querySelector('.faq-a');
			var button = item.querySelector('.faq-q');
			// The "+" icon is rotated 45° into an "×" via CSS on .faq-item.open.
			if (open) {
				item.classList.add('open');
				answer.style.maxHeight = answer.scrollHeight + 'px';
				button.setAttribute('aria-expanded', 'true');
			} else {
				item.classList.remove('open');
				answer.style.maxHeight = '0px';
				button.setAttribute('aria-expanded', 'false');
			}
		}

		items.forEach(function (item) {
			// Initialise: first item open by default.
			setOpen(item, item.classList.contains('open'));

			var button = item.querySelector('.faq-q');
			button.addEventListener('click', function () {
				var isOpen = item.classList.contains('open');
				items.forEach(function (other) {
					if (other !== item) setOpen(other, false);
				});
				setOpen(item, !isOpen);
			});
		});

		// Recalculate the open panel height on resize.
		window.addEventListener('resize', function () {
			var openItem = document.querySelector('.faq-item.open .faq-a');
			if (openItem) openItem.style.maxHeight = openItem.scrollHeight + 'px';
		});
	});
})();
