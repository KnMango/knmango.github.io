const slideContainer = document.querySelector('.slide-container');
const slides = document.querySelectorAll('.slide');
const indicator = document.querySelector('.indicator');
const pauseToggleBtn = document.querySelector('.pause-toggle');

let currentSlide = 0;
const totalSlides = slides.length;

let isPaused = false;
let intervalId = null;

function updateSlide() {
  slideContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
  if (indicator) {
    indicator.textContent = `${currentSlide + 1} / ${totalSlides}`;
  }
}

function goToPrev() {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  updateSlide();
}

function goToNext() {
  currentSlide = (currentSlide + 1) % totalSlides;
  updateSlide();
}

function startAutoSlide() {
  if (!intervalId) {
    intervalId = setInterval(() => {
      if (!isPaused) {
        goToNext();
      }
    }, 5000);
  }
}

function stopAutoSlide() {
  clearInterval(intervalId);
  intervalId = null;
}

function togglePause() {
  isPaused = !isPaused;
  pauseToggleBtn.textContent = isPaused ? '▶' : '⏸';
}

document.querySelector('.prev')?.addEventListener('click', () => {
  goToPrev();
});

document.querySelector('.next')?.addEventListener('click', () => {
  goToNext();
});

pauseToggleBtn?.addEventListener('click', togglePause);

const banner = document.querySelector('.banner');

banner.addEventListener('mouseenter', () => {
  isPaused = true;
});

banner.addEventListener('mouseleave', () => {
  if (!pauseToggleBtn.textContent.includes('▶')) {
    isPaused = false;
  }
});

updateSlide();
startAutoSlide(); 