const bannerImage = document.querySelector('.banner img');

function loopBannerImage() {
  bannerImage.style.opacity = 1;
  bannerImage.style.filter = 'brightness(1)';
  setTimeout(() => {
    bannerImage.style.opacity = 0;
    bannerImage.style.filter = 'brightness(0)';
    setTimeout(loopBannerImage, 1000);
  }, 5000);
}

loopBannerImage();

