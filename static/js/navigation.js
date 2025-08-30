const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.main-nav');

let menuOpen = false;

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
  menuOpen = !menuOpen;
});

window.addEventListener('scroll', function() {
    const scrollPosition = window.scrollY;
    const parallax = document.querySelector('.parallax-section .parallax-background');
    if (parallax) {
        parallax.style.transform = 'translateY(' + (scrollPosition * 0.3) + 'px)';
    }
});
