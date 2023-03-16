        const images = document.querySelectorAll('.banner img');
		let index = 0;

		function showImage(index) {
			images.forEach(image => image.classList.remove('active'));
			images[index].classList.add('active');
		}

		function nextImage() {
			index++;
			if (index >= images.length) {
				index = 0;
			}
			showImage(index);
		}

		function prevImage() {
			index--;
			if (index < 0) {
				index = images.length - 1;
			}
			showImage(index);
		}

		arrows.forEach(arrow => {
			arrow.addEventListener('click', () => {
				if (arrow.classList.contains('left')) {
					prevImage();
				} else {
					nextImage();
				}
			});
		});

		setInterval(nextImage, 2000);