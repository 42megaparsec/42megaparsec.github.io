---
title: "Publications"
subtitle: "Selected Works"
---

<style>

/* ============================
   TITLES
============================ */

.section-title {
  font-size: 2.8rem !important;
  font-weight: 700 !important;
  color: #222 !important;
  margin-top: 3rem !important;
  margin-bottom: 1.2rem !important;
  text-decoration: underline;
  text-underline-offset: 6px;
}


/* ============================
   VIEW MODE TOGGLE
============================ */

.toggle-btns {
  display: flex;
  gap: 10px;
  margin: 25px 0 15px;
}

.toggle-btns button {
  padding: 9px 20px;
  border-radius: 9px;
  border: 1px solid #bbb;
  background: #f2f2f2;
  cursor: pointer;
  font-size: 1.45rem;
  font-weight: 500;
  transition: all 0.22s ease;
}

.toggle-btns button:hover {
  background: #e5e5e5;
}

.toggle-btns button.active {
  background: #333;
  color: #fff;
  border-color: #333;
}


/* ============================
   SECTIONS
============================ */

.pub-section { 
  display: none;
}
.pub-section.active { 
  display: block;
  animation: fadeIn 0.25s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}


/* ============================
   PUBLICATION CARDS
============================ */

.pub-item {
  padding: 1.5rem 1.6rem;
  margin-bottom: 1.6rem;
  background: #fafafa;
  border-radius: 12px;
  border: 1.6px solid #ccc;
  line-height: 1.68;
  scroll-margin-top: 110px;
}

/* 제목 + 버튼들 */
.pub-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  margin-bottom: 6px;
}

.pub-title {
  font-size: 1.55rem;
  font-weight: 640;
  color: #222;
  max-width: 700px;
}

/* 버튼 세트 */
.pub-links {
  display: inline-flex;
  gap: 8px;
  margin-top: 4px;
}

.pub-btn {
  padding: 6px 14px;
  border-radius: 18px;
  border: 1px solid #666;
  font-size: 1.05rem;
  text-decoration: none;
  background: #fff;
  color: #333 !important;
  transition: 0.2s ease;
  white-space: nowrap;
}

.pub-btn:hover {
  background: #333;
  color: #fff !important;
  border-color: #333;
}

.pub-btn.preprint {
  background: #ececec;
}

/* 아래 정보 (저널/연도) */
.pub-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 8px;
  flex-wrap: wrap;
  gap: 8px;
}

.pub-meta {
  font-size: 1.18rem;
  color: #444;
}


/* ============================
   GOOGLE SCHOLAR BUTTON
============================ */

.scholar-btn {
  display: inline-block;
  padding: 10px 18px;
  background-color: #333;
  color: #fff !important;
  border-radius: 8px;
  text-decoration: none;
  font-size: 1.55rem;
  transition: 0.25s ease;
}
.scholar-btn:hover {
  background-color: #555;
}


/* ============================
   YEAR / CATEGORY SUBTITLE
============================ */

.pub-subtitle {
  font-size: 2.15rem !important;
  font-weight: 600 !important;
  color: #222 !important;
  margin-top: 2.3rem !important;
  margin-bottom: 0.7rem !important;
}

.pub-highlight {
  border-color: #4a8f4a !important;
  background: #eef8ee !important;
}

/* ============================
   MOBILE
============================ */

@media (max-width: 760px) {
  .pub-title { font-size: 1.42rem; }
  .pub-btn { padding: 5px 10px; font-size: 0.95rem; }
  .section-title { font-size: 2.3rem !important; }
}

</style>


<script>
function showSection(section) {
  const year = document.getElementById("by-year");
  const cat = document.getElementById("by-category");

  year.classList.remove("active");
  cat.classList.remove("active");

  document.getElementById(section).classList.add("active");

  document.getElementById("btn-year").classList.remove("active");
  document.getElementById("btn-category").classList.remove("active");

  if (section === "by-year") {
    document.getElementById("btn-year").classList.add("active");
  } else {
    document.getElementById("btn-category").classList.add("active");
  }
  reScrollToHash();
}
</script>


### Full list on Google Scholar  
<div style="margin: 20px 0;">
  <a href="https://scholar.google.com/citations?user=pC1TWpgAAAAJ"
     target="_blank" class="scholar-btn">
    View Google Scholar Profile
  </a>
</div>


---

# <span class="section-title">Research Timeline</span>

{{< research-timeline >}}

---

# <span class="section-title">View Mode</span>

<div class="toggle-btns">
<button id="btn-category" class="active" onclick="showSection('by-category')">By Category</button>
  <button id="btn-year" onclick="showSection('by-year')">By Year</button>
  
</div>

---

# <span class="section-title">Publications</span>

<div id="by-year" class="pub-section">
  {{< pubs-by-year >}}
</div>

<div id="by-category" class="pub-section active">
  {{< pubs-by-category >}}
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const hash = window.location.hash;

  if (!hash || !hash.startsWith("#pub-")) return;  
  const pubID = hash.substring(1);  // #pub-3 → "pub-3"

  const active = document.querySelector(".pub-section.active");
  if (!active) return;

  const el = active.querySelector('[data-pub="' + pubID + '"]');
  if (el) {
    el.scrollIntoView({ behavior: "smooth", block: "center" });
    el.classList.add("pub-highlight");
  }
});

function reScrollToHash() {
  const hash = window.location.hash;
  if (!hash || !hash.startsWith("#pub-")) return;

  const pubID = hash.substring(1);
  const active = document.querySelector(".pub-section.active");
  const el = active.querySelector('[data-pub="' + pubID + '"]');
  if (el) {
    el.scrollIntoView({ behavior: "smooth", block: "center" });
  }
}
</script>