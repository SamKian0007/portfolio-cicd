(() => {
  const navItems = [...document.querySelectorAll(".nav-item")];
  const sections = ["about", "experience", "projects", "articles"]
    .map(id => document.getElementById(id))
    .filter(Boolean);

  const isMobileMode = () => window.matchMedia("(max-width: 900px), (pointer: coarse) and (max-width: 1100px)").matches;

  const setActive = (id) => {
    navItems.forEach(a => a.classList.toggle("is-active", a.dataset.target === id));
  };

  navItems.forEach(a => {
    a.addEventListener("click", (e) => {
      const id = a.getAttribute("href")?.replace("#","");
      const target = document.getElementById(id);
      if (!target) return;

      e.preventDefault();
      setActive(id);

      if (isMobileMode()) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      } else {
        const scroller = document.querySelector(".right");
        if (!scroller) return;
        const style = window.getComputedStyle(target);
        const offset = parseFloat(style.scrollMarginTop) || 0;
        scroller.scrollTo({ top: target.offsetTop - offset, behavior: "smooth" });
      }
    });
  });

  document.querySelectorAll(".card-row.card-link").forEach(card => {
    card.addEventListener("click", (e) => {
      if (e.target.closest("a")) return;
      const a = card.querySelector('a[href]:not([href="#"]):not([data-lightbox-trigger])');
      if (a && a.href) window.open(a.href, "_blank", "noopener,noreferrer");
    });
    card.setAttribute("tabindex", "0");
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        const a = card.querySelector('a[href]:not([href="#"]):not([data-lightbox-trigger])');
        if (a && a.href) window.open(a.href, "_blank", "noopener,noreferrer");
      }
    });
  });

  const left = document.querySelector(".left");
  const right = document.querySelector(".right");

  const isDesktopMode = () => window.matchMedia("(min-width: 901px)").matches;

  if (left && right) {
    left.addEventListener("wheel", (e) => {
      if (!isDesktopMode()) return;
      e.preventDefault();
      let deltaY = e.deltaY;
      if (e.deltaMode === 1) {
        deltaY *= 16;
      } else if (e.deltaMode === 2) {
        deltaY *= window.innerHeight;
      }
      right.scrollBy({ 
        top: deltaY, 
        left: 0, 
        behavior: "auto" 
      });
    }, { passive: false });
  }

  let io = null;
  const setupSpy = () => {
    if (io) { io.disconnect(); io = null; }
    if (isMobileMode()) return;

    const scroller = document.querySelector(".right");
    if (!scroller || !sections.length) return;

    io = new IntersectionObserver((entries) => {
      const visible = entries
        .filter(e => e.isIntersecting)
        .sort((a,b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible?.target?.id) setActive(visible.target.id);
    }, { root: scroller, threshold: [0.25, 0.4, 0.6] });

    sections.forEach(s => io.observe(s));
  };

  setupSpy();
  window.addEventListener("resize", setupSpy);

  /* Project lightbox: modal gallery on home page */
  const galleryDataScript = document.getElementById("projects-gallery-data");
  if (galleryDataScript) {
    let galleryData = [];
    try {
      galleryData = JSON.parse(galleryDataScript.textContent);
    } catch (err) {}
    const lightbox = document.getElementById("lightbox");
    const overlay = lightbox?.querySelector("[data-lightbox-close]");
    const closeBtn = lightbox?.querySelector(".lightbox-close-btn");
    const prevBtn = lightbox?.querySelector("[data-lightbox-prev]");
    const nextBtn = lightbox?.querySelector("[data-lightbox-next]");
    const imgEl = lightbox?.querySelector("[data-lightbox-img]");
    const counterEl = lightbox?.querySelector("[data-lightbox-counter]");
    const thumbsEl = lightbox?.querySelector("[data-lightbox-thumbs]");
    let currentImages = [];
    let currentIndex = 0;
    let keyHandler = null;

    const showImage = (index) => {
      if (!imgEl || !currentImages.length) return;
      currentIndex = (index + currentImages.length) % currentImages.length;
      const img = currentImages[currentIndex];
      imgEl.src = img.url;
      imgEl.alt = img.alt;
      if (counterEl) counterEl.textContent = `${currentIndex + 1} / ${currentImages.length}`;
      thumbsEl?.querySelectorAll(".lightbox-thumb").forEach((t, i) => t.classList.toggle("is-active", i === currentIndex));
    };

    const openLightbox = (projectIndex) => {
      const images = galleryData[projectIndex];
      if (!images || !images.length || !lightbox) return;
      currentImages = images;
      currentIndex = 0;
      if (thumbsEl) {
        thumbsEl.innerHTML = "";
        images.forEach((img, i) => {
          const btn = document.createElement("button");
          btn.type = "button";
          btn.className = "lightbox-thumb" + (i === 0 ? " is-active" : "");
          btn.setAttribute("aria-label", `View image ${i + 1}`);
          btn.dataset.index = i;
          const thumbImg = document.createElement("img");
          thumbImg.src = img.url;
          thumbImg.alt = "";
          thumbImg.loading = "lazy";
          btn.appendChild(thumbImg);
          btn.addEventListener("click", () => showImage(parseInt(btn.dataset.index, 10)));
          thumbsEl.appendChild(btn);
        });
      }
      showImage(0);
      lightbox.hidden = false;
      document.body.style.overflow = "hidden";
      keyHandler = (e) => {
        if (e.key === "Escape") closeLightbox();
        else if (e.key === "ArrowLeft") { e.preventDefault(); showImage(currentIndex - 1); }
        else if (e.key === "ArrowRight") { e.preventDefault(); showImage(currentIndex + 1); }
      };
      document.addEventListener("keydown", keyHandler);
    };

    const closeLightbox = () => {
      if (!lightbox) return;
      lightbox.hidden = true;
      document.body.style.overflow = "";
      if (keyHandler) document.removeEventListener("keydown", keyHandler);
      keyHandler = null;
    };

    overlay?.addEventListener("click", closeLightbox);
    closeBtn?.addEventListener("click", closeLightbox);
    prevBtn?.addEventListener("click", (e) => { e.stopPropagation(); showImage(currentIndex - 1); });
    nextBtn?.addEventListener("click", (e) => { e.stopPropagation(); showImage(currentIndex + 1); });

    document.querySelectorAll("[data-lightbox-trigger]").forEach(trigger => {
      trigger.addEventListener("click", (e) => {
        e.preventDefault();
        const index = parseInt(trigger.dataset.projectIndex, 10);
        if (!Number.isNaN(index)) openLightbox(index);
      });
    });
  }

  /* Project gallery viewer (dedicated page): prev/next, thumbnails, keyboard, hash */
  const gallery = document.querySelector("[data-gallery]");
  if (!gallery) return;

  const slides = [...gallery.querySelectorAll(".project-gallery-slide")];
  const thumbs = [...gallery.querySelectorAll(".project-gallery-thumb")];
  const prevBtn = gallery.querySelector("[data-prev]");
  const nextBtn = gallery.querySelector("[data-next]");
  const currentEl = gallery.querySelector("[data-current]");
  const total = slides.length;
  if (!total || !currentEl) return;

  let index = 0;

  const getIndexFromHash = () => {
    const hash = window.location.hash.slice(1);
    const n = parseInt(hash, 10);
    if (!Number.isNaN(n) && n >= 1 && n <= total) return n - 1;
    return 0;
  };

  const setHash = (i) => {
    const newHash = i + 1;
    const url = `${window.location.pathname}#${newHash}`;
    if (window.history.replaceState) {
      window.history.replaceState(null, "", url);
    } else {
      window.location.hash = newHash;
    }
  };

  const go = (i) => {
    index = (i + total) % total;
    slides.forEach((s, j) => s.toggleAttribute("data-active", j === index));
    thumbs.forEach((t, j) => t.classList.toggle("is-active", j === index));
    currentEl.textContent = index + 1;
    setHash(index);
  };

  const initIndex = getIndexFromHash();
  index = initIndex;
  go(index);

  prevBtn?.addEventListener("click", () => go(index - 1));
  nextBtn?.addEventListener("click", () => go(index + 1));

  thumbs.forEach((thumb, i) => {
    thumb.addEventListener("click", () => go(i));
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") {
      e.preventDefault();
      go(index - 1);
    } else if (e.key === "ArrowRight") {
      e.preventDefault();
      go(index + 1);
    }
  });

  window.addEventListener("hashchange", () => {
    const i = getIndexFromHash();
    if (i !== index) go(i);
  });
})();
