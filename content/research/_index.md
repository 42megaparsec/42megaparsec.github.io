---
title: "Research"
type: "page"
---

<style>

/* ===== Global ===== */
.research-wrapper {
  max-width: 900px;
  margin: 0 auto;
  padding: 1rem;
  font-size: 1.24rem;
  line-height: 1.68;
  overflow-x: hidden;
}

/* ===== HERO ===== */
.research-hero {
  text-align: center;
  padding: 3.5rem 1.2rem 4rem;
  background: #f6f6f3;
  border-radius: 20px;
  margin-bottom: 3.4rem;
}

.research-hero h1 {
  font-size: 3.05rem;
  font-weight: 700;
  color: #222;
  margin-bottom: 1.3rem;
}

.research-hero .hero-sub {
  font-size: 1.34rem;
  color: #555;
  max-width: 700px;
  margin: 0.6rem auto 2rem;
}

.hero-symbol {
  margin: 1.8rem auto 0;
  padding: 1.1rem 1.5rem;
  border: 1.4px dashed #bbb;
  font-size: 1.15rem;
  border-radius: 12px;
  color: #666;
  display: inline-block;
}

/* ===== GRID ===== */
.theme-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 22px;
  margin-bottom: 3.3rem;
}

.theme-card {
  background: #fafafa;
  border: 1.6px solid #ddd;
  border-radius: 14px;
  padding: 1.6rem 1.4rem;
  cursor: pointer;
  transition: 0.25s ease;
}

.theme-card:hover { background: #f1f1f1; }

.theme-title {
  font-size: 1.58rem;
  font-weight: 700;
  margin-bottom: 0.55rem;
  color: #222;
}

.theme-desc {
  font-size: 1.22rem;
  color: #555;
}

/* ===== ACCORDION ===== */
.acc-btn {
  width: 100%;
  background: transparent;
  border: none;
  border-bottom: 2px solid #ccc;
  padding: 1.35rem 0;
  text-align: left;
  font-size: 2.0rem;
  font-weight: 760;
  color: #222;
  cursor: pointer;
  margin-bottom: 0.4rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.acc-btn .arrow {
  font-size: 1.6rem;
  color: #777;
  transition: transform 0.25s ease;
}

.acc-btn.open .arrow { transform: rotate(90deg); }

.acc-content {
  display: none;
  padding: 1.2rem 0 2.6rem;
  border-bottom: 1px solid #ddd;
  font-size: 1.5rem;
}

/* ===== Images ===== */
.rep-img {
  width: 100%;
  max-width: 450px;
  display: block;
  margin: 1.1rem 0rem 1.8rem 1.5rem;
  border-radius: 10px;
  border: 1px solid #000;
}

/* ===== APPROACH BLOCK ===== */
.approach-block { margin-top: 2.2rem; }

.approach-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.approach-title {
  font-size: 1.55rem;
  font-weight: 700;
  margin-bottom: 0.55rem;
  padding-left: 1rem;
  border-left: 4px solid #cfcfcf;
}

/* Publication button */
.pub-btn {
  padding: 6px 14px;
  border-radius: 16px;
  border: 1px solid #555;
  background: #fff;
  text-decoration: none;
  color: #333;
  font-size: 1rem;
  white-space: nowrap;
  transition: 0.2s ease;
}

.pub-btn:hover {
  background: #333;
  color: #fff;
}

/* Bullet paragraphs */
.approach-block p {
  font-size: 1.32rem;
  margin: 0.45rem 0;
  padding-left: 2rem;
  position: relative;
}

.approach-block p::before {
  content: "•";
  position: absolute;
  left: 1rem;
  top: 0.05rem;
  font-size: 1.35rem;
  color: #000;
}

/* Paper reference */
.paper-ref {
  font-size: 1.05rem;
  color: #666;
  margin: -0.6rem 0 0.4rem 1.5rem;
}

/* ===== FURTHER DETAILS FIX ===== */
.further {
  margin-top: 2.2rem;
  background: #fdfdfd;
  padding: 1.6rem 1.4rem;
  border-radius: 14px;
  border: 1px solid #e4e4e4;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}

/* 제목 크기 줄이지 않음 */
.further-title {
  font-size: 1.32rem;
  font-weight: 700;
  margin-bottom: 0.55rem;
  color: #333;
}

/* 여기서부터 수정 포인트 */

/* p 자동 불릿 제거 */
.further p::before {
  content: none !important;
  display: none !important;
}

.further > p {
  display: none !important;
}

/* 실제 불릿 표시 */
.further ul {
  list-style: disc !important;
  padding-left: 1.6rem;
  margin-left: 0.4rem;
  font-size: 1.15rem;   /* 글씨 크기 ↓ */
  line-height: 1.5;
  color: #444;
}

.further li {
  margin-bottom: 0.45rem;
}

.further ul, 
.further li {
  list-style: disc !important;
  display: list-item !important;
}

.further ul {
  list-style: none !important;
}

.further li {
  list-style-type: disc !important;
}

</style>

<script>
function toggleAcc(id) {
  const c = document.getElementById(id);
  const b = c.previousElementSibling;
  const open = c.style.display === "block";
  c.style.display = open ? "none" : "block";
  if (!open) b.classList.add("open"); else b.classList.remove("open");
}
</script>

<div class="research-wrapper">

<div class="research-hero">
  <h1>Understanding flow and structure in complex networks</h1>
  <div class="hero-sub">
    My work investigates how networks move flows, form communities, synchronize dynamics, and extract signal from noise. It seeks the principles that explain how coherent patterns arise within complex systems.
  </div>
  <img src="/images/hero.png" class="hero-symbol">
</div>

<div class="theme-grid">
  <div class="theme-card" onclick="toggleAcc('acc-trade'); document.getElementById('acc-trade').scrollIntoView({behavior:'smooth'})">
    <div class="theme-title">Trade Network</div>
    <div class="theme-desc">Self-consistent gravity modeling, flow-based mass inference, and network-driven analysis of trade shocks and structural vulnerability</div>
  </div>

  <div class="theme-card" onclick="toggleAcc('acc-community'); document.getElementById('acc-community').scrollIntoView({behavior:'smooth'})">
    <div class="theme-title">Community Structure</div>
    <div class="theme-desc">Fuzzy boundaries and interpretable community structure</div>
  </div>

  <div class="theme-card" onclick="toggleAcc('acc-sync'); document.getElementById('acc-sync').scrollIntoView({behavior:'smooth'})">
    <div class="theme-title">Synchronization</div>
    <div class="theme-desc">Structural strategies that enhance global synchronization</div>
  </div>

  <div class="theme-card" onclick="toggleAcc('acc-bio'); document.getElementById('acc-bio').scrollIntoView({behavior:'smooth'})">
    <div class="theme-title">Biological Network</div>
    <div class="theme-desc">Excitation pathways in photosynthetic supercomplexes</div>
  </div>

  <div class="theme-card" onclick="toggleAcc('acc-cli'); document.getElementById('acc-cli').scrollIntoView({behavior:'smooth'})">
    <div class="theme-title">Climate Dynamics</div>
    <div class="theme-desc">Spatiotemporal dynamics of sea surface temperature</div>
  </div>

  <div class="theme-card" onclick="toggleAcc('acc-opt'); document.getElementById('acc-opt').scrollIntoView({behavior:'smooth'})">
    <div class="theme-title">Optimization Algorithm</div>
    <div class="theme-desc">Evolutionary strategies for optimization in heterogeneous environments</div>
  </div>

  <div class="theme-card" onclick="toggleAcc('acc-filter'); document.getElementById('acc-filter').scrollIntoView({behavior:'smooth'})">
    <div class="theme-title">Filtering Algorithm</div>
    <div class="theme-desc">Detecting unreliable evaluators through deviation analysis</div>
  </div>
</div>

<!-- ========================= -->
<!-- ===== 1. TRADE NETWORK ===== -->
<!-- ========================= -->

<button class="acc-btn" onclick="toggleAcc('acc-trade')">
  Trade Network <span class="arrow">▶</span>
</button>

<div id="acc-trade" class="acc-content">

  <p>
  Trade networks encode capacity, structure, and dynamic response simultaneously. My work develops flow-only inference methods, multiresolution structural analysis, and shock-propagation models to reveal hidden constraints and systemic vulnerabilities.
  </p>

  <!-- Approach 1 -->
  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach 1 — Flow-only Gravity Model (Mass Inference)</div>
      <a href="/publications/#pub-3" class="pub-btn" target="_blank">View publication</a>
    </div>
    <img src="/images/gravity1.png" class="rep-img">
    <p>RQ: Can node-level trade capacity be inferred directly from flows without GDP-like proxies?</p>
    <p>Method: A fixed-point decomposition that reconstructs intrinsic mass and a system-wide deterrence function purely from the bilateral flow matrix.</p>
    <p>Result: Separates intrinsic trade capacity from external constraints and yields a self-consistent representation of global trade structure.</p>
  </div>

  <!-- Approach 2 -->
  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach 2 — Multiresolution Trade Community Structure</div>
      <a href="/publications/#pub-6" class="pub-btn" target="_blank">View publication</a>
    </div>
    <img src="/images/wonguk.png" class="rep-img">
    <div class="paper-ref">© Cho, Lee & Kim, Scientific Reports 13 (2023). CC BY 4.0</div>
    <p>RQ: How do trade blocs reorganize across scales and where do structural inconsistencies emerge?</p>
    <p>Method: Aggregating community-detection outputs across a continuum of resolutions to expose hierarchical bloc structure.</p>
    <p>Result: Identifies scale-dependent inconsistencies that correlate with geopolitical and economic vulnerability.</p>
  </div>

  <!-- Approach 3 -->
  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach 3 — Shock Propagation in Product Flow Networks</div>
      <a href="/publications/#pub-11" class="pub-btn" target="_blank">View publication</a>
    </div>
    <img src="/images/product.png" class="rep-img">
    <p>RQ: How do supply shocks propagate through real agricultural distribution networks?</p>
    <p>Method: A dynamic price-adjustment model applied to an empirical cabbage-flow network.</p>
    <p>Result: Upstream fluctuations trigger nonlinear downstream price responses driven by the network structure.</p>
  </div>
  <div class="further">
    <div class="further-title">Further Details</div><ul>
      <li>Trade flows reflect both intrinsic capacity and externally imposed constraints; combining mass inference and multiresolution community analysis clarifies how these forces interact.</li>
      <li>Flow-only approaches provide a baseline against which geopolitical or policy-driven distortions become more visible.</li>
      <li>Scale-dependent community structure explains why similar trade volumes can imply different vulnerability profiles across countries.</li>
      <li>Shock-propagation work shows how local supply changes amplify or dissipate depending on the broader trade architecture.</li>
      <li>These approaches outline a unified view of trade as a layered flow system governed by capacity, structure, and dynamic response.</li>
    </ul>
  </div>

</div>

<!-- ================================ -->
<!-- ===== 2. COMMUNITY STRUCTURE ===== -->
<!-- ================================ -->

<button class="acc-btn" onclick="toggleAcc('acc-community')">
  Community Structure <span class="arrow">▶</span>
</button>

<div id="acc-community" class="acc-content">

  <p>
  Community structure is rarely stable or hierarchical. My work examines how stochastic variation and scale-dependent reorganizations expose deeper mesoscale tensions hidden from single-resolution methods.
  </p>

  <!-- Approach 1 -->
  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach 1 — Community Inconsistency (CoI)</div>
      <a href="/publications/#pub-9" class="pub-btn" target="_blank">View publication</a>
    </div>
    <img src="/images/CoI.png" class="rep-img">
    <p>RQ: How reliable are communities under repeated stochastic detections?</p>
    <p>Method: Quantifying global and local inconsistency across multiple detection runs to map a resolution–stability landscape.</p>
    <p>Result: Distinguishes structurally meaningful communities from unstable partitions arising from stochastic ambiguity.</p>
  </div>

  <!-- Approach 2 -->
  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach 2 — Scale-Dependent Community Anomalies</div>
      <a href="/publications/#pub-2" class="pub-btn" target="_blank">View publication</a>
    </div>
    <p>RQ: Do communities reorganize smoothly as resolution varies?</p>
    <p>Method: Tracking discontinuous changes, particularly sudden drops, in community count across resolutions.</p>
    <p>Result: Reveals nontrivial split–merge dynamics that challenge simple hierarchical interpretations.</p>
  </div>

  <div class="further">
    <div class="further-title">Further Details</div>
    <ul>
      <li>Both inconsistency analysis and scale anomalies show that mesoscale structure is rarely hierarchical or stable across scales.</li>
      <li>Global and local inconsistency together reveal which communities persist under both stochastic and scale variations.</li>
      <li>Anomaly detection indicates transitions between competing mesoscale organizations linked to functional or geopolitical tensions.</li>
      <li>This framework maps a landscape of plausible community structures rather than selecting a single partition.</li>
      <li>Applicable to biological, social, economic, and climate networks with overlapping mesoscale organization.</li>
    </ul>
  </div>

</div>

<!-- =========================== -->
<!-- ===== 3. SYNCHRONIZATION ===== -->
<!-- =========================== -->

<button class="acc-btn" onclick="toggleAcc('acc-sync')">Synchronization <span class="arrow">▶</span></button>

<div id="acc-sync" class="acc-content">

  <p>
  Synchronization improves most when interventions respect steady-state phase geometry rather than purely topological heuristics. My work studies optimal node and link additions within this unified phase-centric perspective.
  </p>

  <!-- Approach 1 -->
  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach 1 — Optimal Node Addition</div>
      <a href="/publications/#pub-7" class="pub-btn" target="_blank">View publication</a>
    </div>
    <p>RQ: Which natural frequency should a newly added oscillator adopt to enhance synchrony?</p>
    <p>Method: A link-wise order-parameter approach that uses steady-state phase geometry to set optimal frequencies.</p>
    <p>Result: Achieves stronger synchrony gains than global-order-parameter approaches.</p>
  </div>

  <!-- Approach 2 -->
  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach 2 — Optimal Link Addition</div>
      <a href="/publications/#pub-4" class="pub-btn" target="_blank">View publication</a>
    </div>
    <p>RQ: Which candidate link most effectively improves network synchrony?</p>
    <p>Method: Ranking edges using pseudo–steady-state phase differences and Lyapunov alignment indicators.</p>
    <p>Result: Identifies structural hotspots where new links most effectively boost coherence across diverse network types.</p>
  </div>

  <div class="further">
    <div class="further-title">Further Details</div>
    <ul>
      <li>Node and link addition highlight a single principle: synchronization improves when interventions align with phase geometry.</li>
      <li>Phase-based metrics reveal long-range influence patterns invisible to purely topological measures.</li>
      <li>Optimal interventions require aligning intrinsic dynamics with structural features.</li>
      <li>This perspective provides a systematic basis for designing oscillator networks.</li>
      <li>Extensible to multilayer oscillators, time-varying links, and heterogeneous couplings.</li>
    </ul>
  </div>

</div>

<!-- ============================== -->
<!-- ===== 4. BIOLOGICAL NETWORK ===== -->
<!-- ============================== -->

<button class="acc-btn" onclick="toggleAcc('acc-bio')">Biological Network <span class="arrow">▶</span></button>

<div id="acc-bio" class="acc-content">

  <p>
  Photosystem II demonstrates how biological systems integrate structural organization with quantum dynamics. My work reveals how pigment heterogeneity shapes excitation routing and functional robustness.
  </p>

  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach — Photosynthetic Excitation Network</div>
      <a href="/publications/#pub-1" class="pub-btn" target="_blank">View publication</a>
    </div>
    <img src="/images/PS2.png" class="rep-img">
    <div class="paper-ref">© Kim, Lee et al., Science Advances 11 (2025). CC BY 4.0</div>
    <p>RQ: Why do chlorophyll a and b coexist in PSII?</p>
    <p>Method: Network-based quantum dynamic simulations of excitation transport across the full PSII supercomplex.</p>
    <p>Result: The natural a/b ratio routes energy through stability-preserving domains that prevent overflow under varying light intensities.</p>
  </div>

  <div class="further">
    <div class="further-title">Further Details</div>
    <ul>
      <li>Viewing PSII as a quantum transport network unifies physical, structural, and functional aspects.</li>
      <li>Pigment heterogeneity reshapes transport routes rather than merely adding spectral diversity.</li>
      <li>Domain-level routing maintains efficiency while preventing photodamage under fluctuating loads.</li>
      <li>The approach generalizes to other light-harvesting systems with coupled energetic and structural features.</li>
      <li>Provides a template for linking quantum dynamics to large-scale biological network organization.</li>
    </ul>
  </div>

</div>

<!-- ============================== -->
<!-- ===== 5. CLIMATE DYNAMICS ===== -->
<!-- ============================== -->

<button class="acc-btn" onclick="toggleAcc('acc-cli')">Climate Dynamics <span class="arrow">▶</span></button>

<div id="acc-cli" class="acc-content">

  <p>
  Sea surface temperature variability emerges from coherent thermal provinces interacting through directional heat pathways. I use network-based heat flow models to reveal long-range climatic cascades and cross-basin coupling.
  </p>

  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach — Network Analysis of SST Interactions</div>
      <a href="/publications/#pub-5" class="pub-btn" target="_blank">View publication</a>
    </div>
    <p>RQ: How do regional SST patterns interact to shape global heat redistribution?</p>
    <p>Method: A heat-equation network model representing ocean regions as nodes with directional heat-transfer links.</p>
    <p>Result: Reveals key communities such as ENSO and Indian–Atlantic coupling and clarifies their roles in global cascading heat dynamics.</p>
  </div>

  <div class="further">
    <div class="further-title">Further Details</div>
    <ul>
      <li>SST networks show climate variability arising from coherent thermal provinces linked by directional heat flow.</li>
      <li>Community structures, heat hubs, and cross-basin couplings form a multi-scale architecture affecting long-range dynamics.</li>
      <li>Directional heat flow reveals asymmetries hidden from correlation-based approaches.</li>
      <li>Links local SST variability to basin-spanning cascades and regime shifts.</li>
      <li>Provides a structural basis for comparing observations with climate model scenarios.</li>
    </ul>
  </div>

</div>

<!-- ============================== -->
<!-- ===== 6. OPTIMIZATION ALGORITHM ===== -->
<!-- ============================== -->

<button class="acc-btn" onclick="toggleAcc('acc-opt')">Optimization Algorithm <span class="arrow">▶</span></button>

<div id="acc-opt" class="acc-content">

  <p>
  Optimization on rugged landscapes benefits from structured heterogeneity. My work explores how local environmental diversity accelerates global search in evolutionary algorithms.
  </p>

  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach — Genetic Algorithms Under Heterogeneous Environments</div>
      <a href="/publications/#pub-8" class="pub-btn" target="_blank">View publication</a>
    </div>
    <img src="/images/GA.png" class="rep-img">
    <p>RQ: Do heterogeneous local environments improve the efficiency of evolutionary search?</p>
    <p>Method: A ring-based GA where entities evolve under location-dependent environmental conditions.</p>
    <p>Result: Achieves faster convergence to low-energy states in 3D spin-glass systems through structured cross-environment mating.</p>
  </div>

  <div class="further">
    <div class="further-title">Further Details</div>
    <ul>
      <li>Heterogeneous environments highlight the interplay between local convergence and global exploration.</li>
      <li>Structured diversity prevents premature convergence while accelerating search on rugged landscapes.</li>
      <li>Spin-glass benchmarks demonstrate the value of environmental gradients.</li>
      <li>Suggests a general principle: structured heterogeneity can outperform uniform search strategies.</li>
      <li>Applicable to combinatorial design, machine learning tuning, and physical energy minimization.</li>
    </ul>
  </div>

</div>

<!-- ============================== -->
<!-- ===== 7. FILTERING ALGORITHM ===== -->
<!-- ============================== -->

<button class="acc-btn" onclick="toggleAcc('acc-filter')">Filtering Algorithm <span class="arrow">▶</span></button>

<div id="acc-filter" class="acc-content">

  <p>
  Rating systems often suffer from careless or adversarial users. I propose a deviation-based reliability framework that infers trust directly from rating behavior.
  </p>

  <div class="approach-block">
    <div class="approach-header">
      <div class="approach-title">Approach — Deviation-based Spam Filtering</div>
      <a href="/publications/#pub-10" class="pub-btn" target="_blank">View publication</a>
    </div>
    <img src="/images/DR.png" class="rep-img">
    <p>RQ: Can evaluator trustworthiness be inferred directly from rating behavior?</p>
    <p>Method: Deviation-based reliability scores measuring the statistical significance of each user's departures from collective norms.</p>
    <p>Result: Effectively filters careless or malicious evaluators and produces more stable rankings than simple averages.</p>
  </div>

  <div class="further">
    <div class="further-title">Further Details</div>
    <ul>
      <li>Deviation-based reliability infers trust without relying on user metadata or manual thresholds.</li>
      <li>Detects statistical inconsistencies even when absolute scores look normal.</li>
      <li>Stabilizes item rankings under random noise and targeted manipulation.</li>
      <li>Generalizes to sparse, biased, or strategically distorted evaluation systems.</li>
      <li>Applicable to recommendation platforms, peer review, and fraud detection.</li>
    </ul>
  </div>

</div>



</div> <!-- end wrapper -->