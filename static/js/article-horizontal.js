(() => {
  const script = document.getElementById("article-horiz-data");
  const preview = document.querySelector("[data-horiz-preview]");
  if (!script || !preview) return;

  let data;
  try {
    data = JSON.parse(script.textContent || "[]");
  } catch {
    return;
  }
  if (!Array.isArray(data) || data.length === 0) return;

  const img = preview.querySelector("[data-horiz-preview-img]");
  const titleEl = preview.querySelector("[data-horiz-preview-title]");
  const descEl = preview.querySelector("[data-horiz-preview-desc]");
  const buttons = document.querySelectorAll("[data-horiz-index]");

  let activeIndex = 0;

  function setActive(index) {
    const item = data[index];
    if (!item) return;

    activeIndex = index;

    buttons.forEach((btn, j) => {
      const on = j === index;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-current", on ? "true" : "false");
    });

    if (titleEl) titleEl.textContent = item.title || "";
    if (descEl) descEl.textContent = item.description || "";

    if (img) {
      const src = item.image || "";
      const alt = item.image_alt || "";
      if (src) {
        img.src = src;
        img.alt = alt;
        img.hidden = false;
      } else {
        img.removeAttribute("src");
        img.alt = "";
        img.hidden = true;
      }
    }
  }

  buttons.forEach((btn, i) => {
    btn.addEventListener("mouseenter", () => setActive(i));
    btn.addEventListener("focus", () => setActive(i));
    btn.addEventListener("click", () => setActive(i));
  });

  /* Keep the page from jumping vertically when focus moves between points (browser scroll-into-view). */
  buttons.forEach((btn) => {
    btn.addEventListener("focus", () => {
      const x = window.scrollX;
      const y = window.scrollY;
      requestAnimationFrame(() => {
        if (window.scrollX !== x || window.scrollY !== y) {
          window.scrollTo(x, y);
        }
      });
    });
  });

  function moveActiveBy(delta) {
    const next = Math.max(
      0,
      Math.min(data.length - 1, activeIndex + delta)
    );
    if (next === activeIndex) return false;
    setActive(next);
    const btn = buttons[next];
    if (btn) {
      try {
        btn.focus({ preventScroll: true });
      } catch {
        btn.focus();
      }
    }
    return true;
  }

  document.addEventListener(
    "keydown",
    (e) => {
      if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
      const t = e.target;
      if (
        t instanceof Element &&
        t.closest(
          "input, textarea, select, [contenteditable='true'], [contenteditable='']"
        )
      ) {
        return;
      }
      const moved =
        e.key === "ArrowRight" ? moveActiveBy(1) : moveActiveBy(-1);
      if (moved) e.preventDefault();
    },
    { passive: false }
  );

  setActive(0);
})();
