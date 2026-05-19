// ============================================================
//  PORTFOLIO JS — Scroll animations, nav, interactions
// ============================================================

// ── Intersection Observer: fade-in on scroll ──────────────────
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in-view");
        if (entry.target.classList.contains("skill-item")) {
          const fill = entry.target.querySelector(".skill-bar-fill");
          if (fill) fill.style.width = entry.target.style.getPropertyValue("--width");
        }
      }
    });
  },
  { threshold: 0.15 }
);

document.querySelectorAll(".project-card, .skill-item, .about-inner, .contact-inner").forEach((el) => {
  observer.observe(el);
});

// ── Active nav link on scroll ─────────────────────────────────
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", () => {
  let current = "";
  sections.forEach((section) => {
    if (window.scrollY >= section.offsetTop - 120) {
      current = section.getAttribute("id");
    }
  });
  navLinks.forEach((link) => {
    link.style.color = link.getAttribute("href") === `#${current}` ? "var(--accent)" : "";
  });
  const nav = document.querySelector(".nav");
  nav.style.boxShadow = window.scrollY > 20 ? "0 2px 30px rgba(0,0,0,.5)" : "";
});

// ── Mobile nav toggle ─────────────────────────────────────────
function toggleMenu() {
  const navLinks = document.querySelector(".nav-links");
  navLinks.style.display = navLinks.style.display === "flex" ? "none" : "flex";
  navLinks.style.flexDirection = "column";
  navLinks.style.position = "absolute";
  navLinks.style.top = "100%";
  navLinks.style.left = "0";
  navLinks.style.right = "0";
  navLinks.style.background = "var(--bg)";
  navLinks.style.padding = "1.5rem 3rem";
  navLinks.style.borderBottom = "1px solid var(--border)";
}

// ── Smooth scroll for anchor links ───────────────────────────
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", (e) => {
    e.preventDefault();
    const target = document.querySelector(anchor.getAttribute("href"));
    if (target) {
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
    const navLinks = document.querySelector(".nav-links");
    if (window.innerWidth < 680) navLinks.style.display = "none";
  });
});

// ── Parallax on hero bg text ──────────────────────────────────
const heroBgText = document.querySelector(".hero-bg-text");
if (heroBgText) {
  window.addEventListener("scroll", () => {
    heroBgText.style.transform = `translateY(calc(-50% + ${window.scrollY * 0.15}px))`;
  });
}

// ── PHOTO GALLERY CAROUSEL ────────────────────────────────────
(function () {
  const track = document.getElementById("galleryTrack");
  const dotsContainer = document.getElementById("galleryDots");
  if (!track) return;

  const slides = Array.from(track.querySelectorAll(".gallery-slide"));
  const total = slides.length;
  let current = 0;

  function visibleCount() {
    if (window.innerWidth < 580) return 1;
    if (window.innerWidth < 900) return 2;
    return 3;
  }

  // Build dots
  slides.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.className = "gallery-dot" + (i === 0 ? " active" : "");
    dot.setAttribute("aria-label", `Go to slide ${i + 1}`);
    dot.addEventListener("click", () => goTo(i));
    dotsContainer.appendChild(dot);
  });

  function updateDots() {
    dotsContainer.querySelectorAll(".gallery-dot").forEach((d, i) => {
      d.classList.toggle("active", i === current);
    });
  }

  function getSlideWidth() {
    // Recalculate live from the DOM so it's always accurate
    if (slides[0]) {
      const rect = slides[0].getBoundingClientRect();
      // gap is 1.5rem = 24px
      return rect.width + 24;
    }
    return 0;
  }

  function goTo(index) {
    const vc = visibleCount();
    const max = Math.max(0, total - vc);
    current = Math.max(0, Math.min(index, max));
    const slideWidth = getSlideWidth();
    track.style.transform = `translateX(-${current * slideWidth}px)`;
    updateDots();
  }

  window.galleryNext = function () { goTo(current + 1); };
  window.galleryPrev = function () { goTo(current - 1); };

  window.addEventListener("resize", () => goTo(current));

  // Wait for images to load before initialising position
  window.addEventListener("load", () => goTo(0));

  // Touch / swipe support
  let touchStartX = 0;
  track.addEventListener("touchstart", (e) => { touchStartX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener("touchend", (e) => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) diff > 0 ? galleryNext() : galleryPrev();
  });

  // Click to open lightbox
  slides.forEach((slide) => {
    slide.addEventListener("click", () => {
      const img = slide.querySelector("img");
      if (img) openLightbox(img.src, img.alt);
    });
  });

  // Lightbox
  const lightbox = document.createElement("div");
  lightbox.className = "gallery-lightbox";
  lightbox.innerHTML = `<button class="lightbox-close" aria-label="Close">✕</button><img src="" alt="" />`;
  document.body.appendChild(lightbox);

  const lbImg = lightbox.querySelector("img");
  lightbox.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
  lightbox.addEventListener("click", (e) => { if (e.target === lightbox) closeLightbox(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeLightbox(); });

  function openLightbox(src, alt) {
    lbImg.src = src;
    lbImg.alt = alt || "";
    lightbox.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  function closeLightbox() {
    lightbox.classList.remove("open");
    document.body.style.overflow = "";
  }
})();

// ── Easter egg: Konami code ───────────────────────────────────
const KONAMI = [38,38,40,40,37,39,37,39,66,65];
let konamiIdx = 0;
document.addEventListener("keydown", (e) => {
  if (e.keyCode === KONAMI[konamiIdx]) {
    konamiIdx++;
    if (konamiIdx === KONAMI.length) {
      document.body.style.filter = "hue-rotate(180deg)";
      setTimeout(() => { document.body.style.filter = ""; }, 2000);
      konamiIdx = 0;
    }
  } else {
    konamiIdx = 0;
  }
});