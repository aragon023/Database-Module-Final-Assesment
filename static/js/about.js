let currentIndex = 0;
const items = document.querySelectorAll(".content-item");

function showContent(newIndex, direction = 'right') {
  if (newIndex === currentIndex) return;

  const current = items[currentIndex];
  const next = items[newIndex];

  current.classList.remove("active");
  current.classList.add(direction === 'right' ? "exit-left" : "exit-right");

  next.classList.remove("exit-left", "exit-right");
  next.classList.add("active");

  // Reseting class after animation
  setTimeout(() => {
    current.classList.remove("exit-left", "exit-right");
  }, 400);

  currentIndex = newIndex;
}

function nextContent() {
  const nextIndex = (currentIndex + 1) % items.length;
  showContent(nextIndex, 'right');
}

function prevContent() {
  const prevIndex = (currentIndex - 1 + items.length) % items.length;
  showContent(prevIndex, 'left');
}
