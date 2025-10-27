<template>
  <div class="movie-page">
    <!-- top nav -->
    <header class="navbar">
      <div class="navbar-container">
        <div class="navbar-left">
          <button class="menu-btn" aria-label="menu">☰</button>
          <div class="logo">
            <span class="tmdb-text">TMDB</span>
            <div class="tmdb-dot" aria-hidden="true"></div>
          </div>
          <nav class="nav-links">
            <a href="#">Movies</a>
            <a href="#">TV Shows</a>
            <a href="#">People</a>
            <a href="#">More</a>
          </nav>
        </div>

        <div class="navbar-right">
          <button class="icon-btn" aria-label="add">+</button>
          <a href="#" class="nav-btn">Login</a>
          <a href="#" class="nav-btn join">Join TMDB</a>
          <button class="icon-btn search-btn" aria-label="search">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24">
              <path d="M21 21l-4.35-4.35m2.1-5.4a7.5 7.5 0 11-15 0 7.5 7.5 0 0115 0z"
                stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>
    </header>

    <div class="subnav-white">
      <div class="subnav-inner">
        <a href="#" class="subnav-link active">Overview <span class="caret">▾</span></a>
        <a href="#" class="subnav-link">Media <span class="caret">▾</span></a>
        <a href="#" class="subnav-link">Fandom <span class="caret">▾</span></a>
        <a href="#" class="subnav-link">Share <span class="caret">▾</span></a>
      </div>
    </div>

    <section class="hero" :style="heroStyle">
      <div class="hero-overlay"></div>
      <div class="hero-content container">
        <div class="left-col">
          <div class="poster-card">
            <img v-if="movie && movie.Poster !== 'N/A'" :src="movie.Poster" :alt="movie.Title" />
            <div v-else class="poster-placeholder">No Poster</div>

            <div class="stream-badge">
              <div class="badge-icon">Disney+</div>
              <div class="badge-text">Now Streaming<br/><strong>Watch Now</strong></div>
            </div>
          </div>
        </div>

        <div class="right-col">
          <div class="title-row">
            <h1 class="title">
              {{ movie?.Title ?? 'Loading...' }}
              <span class="year">({{ movie?.Year }})</span>
            </h1>
            <div class="meta-line">
              {{ movie?.Released ?? '' }} • {{ movie?.Genre ?? '' }} • {{ movie?.Runtime ?? '' }}
            </div>
          </div>

          <div class="action-row">
            <div class="score">
              <div class="score-circle">
                <div class="score-number">{{ scorePercent }}</div>
              </div>
              <div class="score-label">User<br/>Score</div>
            </div>

            <div class="icons">
              <button class="ic">Like</button>
              <button class="ic">Watchlist</button>
              <button class="ic play">Play Trailer</button>
            </div>
          </div>

          <div class="overview-block">
            <p class="tagline" v-if="movie?.Type">{{ movie?.Type }}</p>
            <h2>Overview</h2>
            <p class="overview-text">{{ movie?.Plot ?? '' }}</p>
          </div>

          <div class="credits">
            <div class="credits-col" v-for="(col, idx) in creditsColumns" :key="idx">
              <div v-for="item in col" :key="item.name" class="credit-item">
                <div class="credit-name">{{ item.name }}</div>
                <div class="credit-role">{{ item.role }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer">Built with Vue — TMDB style sample</footer>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const API = 'http://www.omdbapi.com/?i=tt3896198&apikey=d2132124'
const movie = ref(null)

async function fetchMovie () {
  try {
    const r = await fetch(API)
    const data = await r.json()
    movie.value = data
  } catch (e) {
    movie.value = { Title: 'Error', Plot: 'Could not load data.' }
  }
}

onMounted(fetchMovie)

const scorePercent = computed(() => {
  if (!movie.value) return '—'
  const r = parseFloat(movie.value.imdbRating)
  if (!isNaN(r)) return Math.round((r / 10) * 100)
  return '76'
})

const creditsColumns = computed(() => {
  const items = [
    { name: movie.value?.Director ?? 'James Gunn', role: 'Director' },
    { name: movie.value?.Writer ?? 'James Gunn', role: 'Writer' },
    { name: movie.value?.Actors ?? 'Chris Pratt', role: 'Cast' },
    { name: 'Bill Mantlo', role: 'Characters' },
    { name: 'Keith Giffen', role: 'Characters' },
    { name: 'Steve Englehart', role: 'Characters' },
    { name: 'Larry Lieber', role: 'Characters' },
    { name: 'Steve Gan', role: 'Characters' },
    { name: 'Jack Kirby', role: 'Characters' },
    { name: 'Jim Starlin', role: 'Characters' },
    { name: 'Stan Lee', role: 'Characters' },
    { name: 'Steve Gerber', role: 'Characters' }
  ]
  const cols = [[], [], []]
  items.forEach((it, i) => cols[i % 3].push(it))
  return cols
})

const heroStyle = computed(() => {
  if (!movie.value || !movie.value.Poster || movie.value.Poster === 'N/A') {
    return { backgroundColor: '#07122a' }
  }
  return {
    backgroundImage: `linear-gradient(rgba(7,12,24,0.45), rgba(7,12,24,0.6)), url(${movie.value.Poster})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center center'
  }
})
</script>

<style scoped>

:root{
  --container-w:1200px;
  --dark: #07122a;
  --accent: #01b4e4;
}

.movie-page {
  min-height: 100vh;
  background: var(--dark);
  color: #e6f0f8;
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Arial;
}


.navbar {
  background: #032541;
  height: 64px;
  display: flex;
  align-items: center;
  color: #fff;
  box-shadow: 0 1px 0 rgba(0,0,0,0.3);
  position: relative;
  z-index: 20;
}
.navbar-container {
  max-width: var(--container-w);
  margin: 0 auto;
  width: 100%;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.navbar-left { display:flex; align-items:center; gap:18px; }
.menu-btn { display:none; background:none; border:none; color:white; font-size:20px; cursor:pointer; }
.logo { display:flex; align-items:center; gap:8px; font-weight:800; font-size:22px; letter-spacing:-0.6px; }
.tmdb-text { color:#7fe0f9; }
.tmdb-dot { width:28px; height:12px; border-radius:8px; background: linear-gradient(90deg,#7fe0f9,#01d277); }

.nav-links { display:flex; gap:18px; align-items:center; }
.nav-links a { color:#fff; text-decoration:none; font-weight:600; }
.nav-links a:hover { color: var(--accent); }

/* right */
.navbar-right { display:flex; gap:12px; align-items:center; }
.icon-btn { background:none; border:none; color:white; cursor:pointer; font-size:16px; padding:8px; border-radius:6px; transition:background .15s; }
.icon-btn:hover { background: rgba(255,255,255,0.06); }
.nav-btn { color:#fff; text-decoration:none; padding:8px 12px; border-radius:6px; font-weight:600; }
.nav-btn.join { background: var(--accent); color:#032541; font-weight:700; }

.subnav-white {
  width:100%;
  background:#fff;
  height:56px;
  display:flex;
  align-items:center;
  justify-content:center;
  box-shadow: 0 1px 0 rgba(13,26,34,0.06);
  z-index:18;
}
.subnav-inner {
  max-width: var(--container-w);
  width:100%;
  display:flex;
  justify-content:center;
  align-items:center;
  gap:48px;
  padding: 0 20px;
}
.subnav-link { color:#03273a; text-decoration:none; font-weight:700; font-size:15px; padding: 12px 6px; display:inline-flex; gap:8px; }
.subnav-link:hover { color: var(--accent); }
.subnav-link.active { position:relative; color:#022b3a; }
.subnav-link.active::after {
  content: "";
  position:absolute;
  left:50%;
  transform: translateX(-50%);
  bottom: -8px;
  width:56px;
  height:4px;
  border-radius:2px;
  background: linear-gradient(90deg,#01b4e4 0%, #67e3c8 100%);
  box-shadow: 0 2px 6px rgba(1,180,228,0.12);
}
.caret { font-size:12px; color:#6b8c99; }


.hero { position:relative; padding: 34px 0 60px; min-height:520px; display:flex; align-items:flex-start; margin-top: -6px; z-index:1; }
.hero-overlay { position:absolute; inset:0; background: linear-gradient(90deg, rgba(7,18,34,0.8) 0%, rgba(7,18,34,0.95) 35%, rgba(7,18,34,0.96) 100%); z-index:2; border-top:6px solid transparent; }
.hero-content.container { position:relative; z-index:3; max-width:var(--container-w); margin:0 auto; display:flex; gap:28px; padding:0 22px; align-items:flex-start; }

/* poster */
.left-col { width: 360px; min-width:300px; }
.poster-card { border-radius:10px; overflow:hidden; box-shadow: 0 18px 40px rgba(2,6,12,0.6); position:relative; background: linear-gradient(180deg, rgba(2,6,12,0.9), rgba(2,6,12,0.8)); }
.poster-card img { display:block; width:100%; height:auto; }
.poster-placeholder { width:100%; height:420px; display:flex; align-items:center; justify-content:center; color:#9fb0c8; }

/* stream badge */
.stream-badge { position:absolute; left:12px; bottom:12px; display:flex; gap:10px; background: rgba(2,38,48,0.9); padding:12px 14px; border-radius:8px; color:#bfeaf7; box-shadow:0 8px 20px rgba(2,6,12,0.6); }
.badge-icon { background: linear-gradient(90deg,#0b6b9a,#073b5e); padding:6px 10px; border-radius:6px; font-weight:700; font-size:14px; }
.badge-text { font-size:13px; line-height:1; }

/* right column */
.right-col { flex:1; padding-top:6px; }
.title { font-size:42px; margin:0 0 8px 0; font-weight:800; letter-spacing:-0.4px; color:#fff; }
.year { font-weight:600; color:#cbdcf1; font-size:20px; margin-left:8px; }
.meta-line { color:#9fb0c8; margin-bottom:16px; font-size:15px; }

/* action row */
.action-row { display:flex; align-items:center; gap:24px; margin-bottom:12px; }
.score { display:flex; align-items:center; gap:12px; }
.score-circle { width:78px; height:78px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:conic-gradient(#2de08f 0deg, #2de08f 216deg, rgba(255,255,255,0.06) 216deg); box-shadow: 0 6px 18px rgba(2,6,12,0.6); }
.score-number { font-weight:800; color:#062b23; font-size:20px; background:white; width:42px; height:42px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.score-label { color:#cfeefb; font-weight:600; font-size:13px; }

/* icons */
.icons { display:flex; gap:12px; align-items:center; }
.ic { background: rgba(255,255,255,0.05); border: none; padding:10px 14px; border-radius:8px; color:#d6eefb; font-weight:600; cursor:pointer; }
.ic.play { background: rgba(1,180,228,0.95); color:#072b31; }

.overview-block { margin-top:18px; max-width:760px; }
.tagline { color:#badbf1; font-style:italic; margin-bottom:6px; }
.overview-block h2 { color:#ffffff; margin:6px 0 8px 0; }
.overview-text { color:#d6e9f6; line-height:1.6; max-width:900px; }
.credits { display:flex; gap:36px; margin-top:22px; }
.credits-col { flex:1; min-width:120px; }
.credit-item { margin-bottom:18px; }
.credit-name { font-weight:700; color:#fff; }
.credit-role { color:#9fb0c8; font-size:13px }

/* footer */
.footer { text-align:center; color:#8ea9bf; padding:26px 0 40px; }

@media (max-width: 1000px) {
  .left-col { width:240px; min-width:240px; }
  .title { font-size:36px; }
}

@media (max-width: 720px) {
  .menu-btn { display:block; }
  .nav-links { display:none; }
  .navbar-container { padding: 8px 14px; }
  .subnav-inner { gap:18px; overflow-x:auto; -webkit-overflow-scrolling: touch; padding:0 12px; }
  .subnav-link.active::after { width:44px; bottom:-6px; }
  .container { flex-direction:column; align-items:center; padding:0 14px; }
  .left-col { width:160px; min-width:160px; order:0; }
  .hero-content.container {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  .poster-card {
    margin: 0 auto;
  }
  .right-col { padding-top:18px; width:100%; }
  .title { font-size:26px; text-align:left; }
  .action-row { align-items:center; gap:14px; flex-wrap:wrap; }
  .score { order:0; }
  .icons { order:1; }
  .credits { flex-direction:row; gap:14px; }
  .hero { padding:20px 0 36px; min-height:360px; }
  .hero-overlay { background: linear-gradient(180deg, rgba(7,18,34,0.92) 0%, rgba(7,18,34,0.98) 60%); }
}

@media (max-width:420px) {
  .left-col { width:140px; min-width:140px; }
  .title { font-size:20px; }
  .meta-line { font-size:13px; }
  .overview-text { font-size:14px; }
  .right-col {
    text-align: center;
  }
  .icons {
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>
