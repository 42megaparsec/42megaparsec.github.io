---
title: "Publications"
subtitle: "Selected Works"
---

<style>

/* ===== Section Titles ===== */
.section-title {
  font-size: 3rem !important;
  font-weight: 700 !important;
  color: #222 !important;
  margin-top: 2.8rem !important;
  margin-bottom: 1.4rem !important;
  text-decoration: underline;
  text-underline-offset: 6px;
}

/* ===== Toggle Buttons ===== */
.toggle-btns {
  display: flex;
  gap: 12px;
  margin: 20px 0;
}

.toggle-btns button {
  padding: 8px 18px;
  border-radius: 8px;
  border: 1px solid #bbb;
  background: #f3f3f3;
  cursor: pointer;
  font-size: 1.6rem;
  font-weight: 500;
  transition: background 0.25s ease, color 0.25s ease;
}

.toggle-btns button.active {
  background: #333;
  color: #fff;
}

/* ===== Wrapper for each section ===== */
.pub-section { display: none; }
.pub-section.active { display: block; }

/* ===== Publication Item Card ===== */
.pub-item {
  padding: 1.2rem 1.4rem;
  margin-bottom: 1.2rem;
  background: #fafafa;
  border-radius: 10px;
  border: 1.5px solid #cccccc;
  line-height: 1.65;
}


/* Header containing title + buttons */
.pub-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 5px;
}

.pub-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 4px;
  gap: 12px;
}

/* 버튼 */
.pub-links {
  display: inline-flex;
  gap: 6px;
  white-space: nowrap;
}

.pub-btn {
  padding: 4px 6px;
  border-radius: 12px;
  border: 1px solid #777;
  font-size: 1.2rem;
  text-decoration: none;
  background: #fff;
  color: #333 !important;
  transition: 0.2s ease;
}

.pub-btn:hover {
  background: #333;
  color: #fff !important;
  border-color: #333;
}

.pub-btn.preprint { background: #eee; }

/* Google Scholar link */
.scholar-btn {
  display: inline-block;
  padding: 8px 15px;
  background-color: #333;
  color: #fff !important;
  border-radius: 6px;
  text-decoration: none;
  font-size: 1.7rem;
}

.scholar-btn:hover { background-color: #555; }

/* === Year / Category Headers (hierarchy fix) === */
.pub-subtitle {
  font-size: 2.3rem !important;
  font-weight: 600 !important;
  color: #222 !important;
  margin-top: 2rem !important;
  margin-bottom: 0.6rem !important;
}

</style>

<script>
function showSection(section) {
  document.getElementById("by-year").classList.remove("active");
  document.getElementById("by-category").classList.remove("active");

  document.getElementById(section).classList.add("active");

  document.getElementById("btn-year").classList.remove("active");
  document.getElementById("btn-category").classList.remove("active");

  if (section === "by-year") {
    document.getElementById("btn-year").classList.add("active");
  } else {
    document.getElementById("btn-category").classList.add("active");
  }
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

# <span class="section-title">View Mode</span>

<div class="toggle-btns">
  <button id="btn-year" class="active" onclick="showSection('by-year')">By Year</button>
  <button id="btn-category" onclick="showSection('by-category')">By Category</button>
</div>


---

# <span class="section-title">Publications</span>

<div id="by-year" class="pub-section active">
  {{< pubs-by-year >}}
</div>

<div id="by-category" class="pub-section">
  {{< pubs-by-category >}}
</div>
