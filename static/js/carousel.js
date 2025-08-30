const track = document.querySelector('.carousel-track');
const logos = Array.from(track.children);

let trackWidth = track.scrollWidth;
let containerWidth = track.parentElement.offsetWidth;

// Clone logos repeatedly until the track is at least four times the container width
while (track.scrollWidth < containerWidth * 4) {
  logos.forEach(logo => {
    const clone = logo.cloneNode(true);
    track.appendChild(clone);
  });
}

// Scrolling 
let scrollAmount = 0;
let isPaused = false;
const speed = 0.5;

function animateCarousel() {
  if (!isPaused) {
    scrollAmount += speed;

    if (scrollAmount >= track.scrollWidth / 2) {
      scrollAmount = 0;
      track.style.transform = `translateX(0)`;
    } else {
      track.style.transform = `translateX(-${scrollAmount}px)`;
    }
  }

  requestAnimationFrame(animateCarousel);
}

animateCarousel();

// Pause when mouse hovers 
const carousel = document.querySelector('.logo-carousel');
carousel.addEventListener('mouseenter', () => isPaused = true);
carousel.addEventListener('mouseleave', () => isPaused = false);