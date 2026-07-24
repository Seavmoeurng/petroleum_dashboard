import { petroleumData } from './petroleum_data.js';
import { translations } from './translations.js';

// Application State
let state = {
  selectedCountryId: 'GLOBAL',
  searchQuery: '',
  theme: localStorage.getItem('petroleum_theme') || 'dark',
  lang: localStorage.getItem('petroleum_lang') || 'en'
};

// Chart Instance
let chartReserves = null;

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initLang();
  initEvents();
  renderAllViews();
});

// Theme Initialization & Switcher
function initTheme() {
  document.documentElement.setAttribute('data-theme', state.theme);
  updateThemeButton();
}

function toggleTheme() {
  state.theme = state.theme === 'dark' ? 'light' : 'dark';
  localStorage.setItem('petroleum_theme', state.theme);
  document.documentElement.setAttribute('data-theme', state.theme);
  updateThemeButton();
  renderChart();
}

function updateThemeButton() {
  const icon = document.getElementById('themeIcon');
  const label = document.getElementById('themeLabel');
  const t = translations[state.lang];
  if (icon && label) {
    if (state.theme === 'dark') {
      icon.className = 'fa-solid fa-sun';
      label.textContent = t.lightMode;
    } else {
      icon.className = 'fa-solid fa-moon';
      label.textContent = t.darkMode;
    }
  }
}

// Language Initialization & Switcher
function initLang() {
  document.documentElement.setAttribute('lang', state.lang);
  updateLangButton();
}

function toggleLanguage() {
  state.lang = state.lang === 'en' ? 'km' : 'en';
  localStorage.setItem('petroleum_lang', state.lang);
  document.documentElement.setAttribute('lang', state.lang);
  updateLangButton();
  updateThemeButton();
  renderAllViews();
}

function updateLangButton() {
  const btnLabel = document.getElementById('langLabel');
  const t = translations[state.lang];
  if (btnLabel) {
    btnLabel.textContent = t.langLabel;
  }
}

// Event Listeners Initialization
function initEvents() {
  const countryDropdown = document.getElementById('countrySelectDropdown');
  const searchInput = document.getElementById('searchInput');
  const themeBtn = document.getElementById('themeToggleBtn');
  const langBtn = document.getElementById('langToggleBtn');
  const printBtn = document.getElementById('printA4Btn');

  if (langBtn) {
    langBtn.addEventListener('click', toggleLanguage);
  }

  if (printBtn) {
    printBtn.addEventListener('click', () => {
      window.print();
    });
  }

  if (themeBtn) {
    themeBtn.addEventListener('click', toggleTheme);
  }

  if (countryDropdown) {
    countryDropdown.addEventListener('change', (e) => {
      state.selectedCountryId = e.target.value;
      renderAllViews();
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value.toLowerCase().trim();
      renderAllViews();
    });
  }
}

// Master Render Function
function renderAllViews() {
  renderStaticUiText();
  renderBanner();
  renderTopKpis();
  renderChart();
  renderUpstreamKpis();
  renderDownstreamKpis();
  renderFiscalKpis();
  renderRiskKpis();
}

// Translate Static UI Elements
function renderStaticUiText() {
  const t = translations[state.lang];

  const brandName = document.getElementById('uiBrandName');
  const brandSub = document.getElementById('uiBrandSub');
  const exportA4 = document.getElementById('uiExportA4');
  const searchInput = document.getElementById('searchInput');
  const optGlobal = document.getElementById('optGlobal');

  if (brandName) brandName.innerHTML = `${t.brandName} <span class="brand-highlight">${t.brandHighlight}</span>`;
  if (brandSub) brandSub.innerHTML = `<i class="fa-solid fa-globe"></i> ${t.brandSub}`;
  if (exportA4) exportA4.textContent = t.exportA4;
  if (searchInput) searchInput.placeholder = t.searchPlaceholder;
  if (optGlobal) optGlobal.textContent = t.allCountries;

  // Top KPI titles
  const uiReserves = document.getElementById('uiKpiReservesTitle');
  const uiOwnership = document.getElementById('uiKpiOwnershipTitle');
  const uiFiscal = document.getElementById('uiKpiFiscalTitle');
  const uiSpr = document.getElementById('uiKpiSprTitle');

  if (uiReserves) uiReserves.innerHTML = `<i class="fa-solid fa-drum text-cyan"></i> ${t.kpiReservesTitle}`;
  if (uiOwnership) uiOwnership.innerHTML = `<i class="fa-solid fa-building-flag text-purple"></i> ${t.kpiOwnershipTitle}`;
  if (uiFiscal) uiFiscal.innerHTML = `<i class="fa-solid fa-hand-holding-dollar text-green"></i> ${t.kpiFiscalTitle}`;
  if (uiSpr) uiSpr.innerHTML = `<i class="fa-solid fa-vault text-amber"></i> ${t.kpiSprTitle}`;

  // Section Headers
  const chartTitle = document.getElementById('uiChartTitle');
  const chartSub = document.getElementById('uiChartSub');
  const upstreamTitle = document.getElementById('uiUpstreamTitle');
  const upstreamSub = document.getElementById('uiUpstreamSub');
  const downstreamTitle = document.getElementById('uiDownstreamTitle');
  const fiscalTitle = document.getElementById('uiFiscalTitle');
  const riskTitle = document.getElementById('uiRiskTitle');

  if (chartTitle) chartTitle.innerHTML = `<i class="fa-solid fa-chart-column text-cyan"></i> ${t.chartTitle}`;
  if (chartSub) chartSub.innerHTML = `<i class="fa-solid fa-scale-balanced"></i> ${t.chartSub}`;
  if (upstreamTitle) upstreamTitle.innerHTML = `<i class="fa-solid fa-compass-drafting text-purple"></i> ${t.upstreamTitle}`;
  if (upstreamSub) upstreamSub.innerHTML = `<i class="fa-solid fa-sliders"></i> ${t.upstreamSub}`;
  if (downstreamTitle) downstreamTitle.innerHTML = `<i class="fa-solid fa-gas-pump text-green"></i> ${t.downstreamTitle}`;
  if (fiscalTitle) fiscalTitle.innerHTML = `<i class="fa-solid fa-coins text-amber"></i> ${t.fiscalTitle}`;
  if (riskTitle) riskTitle.innerHTML = `<i class="fa-solid fa-shield-halved text-cyan"></i> ${t.riskTitle}`;
}

// 1. Render Top Header Banner
function renderBanner() {
  const titleElem = document.getElementById('bannerTitle');
  const subtitleElem = document.getElementById('bannerSubtitle');
  const badgesElem = document.getElementById('bannerBadges');
  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    if (titleElem) titleElem.innerHTML = `<i class="fa-solid fa-chart-line text-cyan"></i> ${t.globalBannerTitle}`;
    if (subtitleElem) subtitleElem.textContent = t.globalBannerSub;
    if (badgesElem) {
      badgesElem.innerHTML = `
        <span class="kpi-pill pill-cyan"><i class="fa-solid fa-earth-americas"></i> ${t.badge11Nations}</span>
        <span class="kpi-pill pill-purple"><i class="fa-solid fa-layer-group"></i> ${t.badgeTaxonomy}</span>
        <span class="kpi-pill pill-green"><i class="fa-solid fa-sack-dollar"></i> ${t.badgeFiscal}</span>
      `;
    }
  } else {
    const country = petroleumData.find(c => c.id === state.selectedCountryId);
    if (country) {
      const countryNameDisplay = state.lang === 'km' ? translateCountryName(country.country) : country.country;
      if (titleElem) titleElem.innerHTML = `<i class="fa-solid fa-flag text-cyan"></i> ${countryNameDisplay} ${t.profileTitleSuffix}`;
      if (subtitleElem) subtitleElem.textContent = `${t.provenRankPrefix}${country.rank} | ${t.tradeStatusLabel}${country.tradeStatus}`;
      if (badgesElem) {
        const tradeClass = country.tradeStatus === 'Net Exporter' ? 'pill-green' : 'pill-cyan';
        badgesElem.innerHTML = `
          <span class="kpi-pill ${tradeClass}"><i class="fa-solid fa-arrow-right-arrow-left"></i> ${country.tradeStatus}</span>
          <span class="kpi-pill pill-purple"><i class="fa-solid fa-trophy"></i> Rank #${country.rank}</span>
          <span class="kpi-pill pill-amber"><i class="fa-solid fa-file-contract"></i> ${country.oilReserveSpr.licensingModel}</span>
        `;
      }
    }
  }
}

// 2. Render Top 4 At-a-Glance KPI Cards
function renderTopKpis() {
  const t = translations[state.lang];

  const elValReserves = document.getElementById('kpiValReserves');
  const elFootReserves = document.getElementById('kpiFootReserves');

  const elValOwnership = document.getElementById('kpiValOwnership');
  const elFootOwnership = document.getElementById('kpiFootOwnership');

  const elValFiscal = document.getElementById('kpiValFiscal');
  const elFootFiscal = document.getElementById('kpiFootFiscal');

  const elValSpr = document.getElementById('kpiValSpr');
  const elFootSpr = document.getElementById('kpiFootSpr');

  if (state.selectedCountryId === 'GLOBAL') {
    if (elValReserves) elValReserves.textContent = '~1.77 T bbls';
    if (elFootReserves) elFootReserves.innerHTML = `<i class="fa-solid fa-chart-simple"></i> ${t.kpiReservesFootGlobal}`;

    if (elValOwnership) elValOwnership.textContent = t.kpiOwnershipValGlobal;
    if (elFootOwnership) elFootOwnership.innerHTML = `<i class="fa-solid fa-shield-halved"></i> ${t.kpiOwnershipFootGlobal}`;

    if (elValFiscal) elValFiscal.textContent = t.kpiFiscalValGlobal;
    if (elFootFiscal) elFootFiscal.innerHTML = `<i class="fa-solid fa-percent"></i> ${t.kpiFiscalFootGlobal}`;

    if (elValSpr) elValSpr.textContent = t.kpiSprValGlobal;
    if (elFootSpr) elFootSpr.innerHTML = `<i class="fa-solid fa-boxes-stacked"></i> ${t.kpiSprFootGlobal}`;
    return;
  }

  const c = petroleumData.find(item => item.id === state.selectedCountryId);
  if (!c) return;

  if (elValReserves) elValReserves.textContent = `${c.oilReserveSpr.provenReservesNumeric}B bbls`;
  if (elFootReserves) elFootReserves.innerHTML = `<i class="fa-solid fa-trophy"></i> ${t.provenRankPrefix}${c.rank}`;

  if (elValOwnership) elValOwnership.textContent = c.oilReserveSpr.licensingModel;
  if (elFootOwnership) elFootOwnership.innerHTML = `<i class="fa-solid fa-building-flag"></i> ${c.oilReserveSpr.ownershipModel}`;

  if (elValFiscal) elValFiscal.textContent = c.taxFiscalRegime.royalties.split('(')[0].trim();
  if (elFootFiscal) elFootFiscal.innerHTML = `<i class="fa-solid fa-receipt"></i> CIT: ${c.taxFiscalRegime.pptCit.split('(')[0].trim()}`;

  if (elValSpr) elValSpr.textContent = c.oilReserveSpr.sprCapacity.split('(')[0].trim();
  if (elFootSpr) elFootSpr.innerHTML = `<i class="fa-solid fa-clock-rotate-left"></i> ${c.oilReserveSpr.stockDuration.split('(')[0].trim()}`;
}

// Helper to Translate Country Names to Khmer
function translateCountryName(name) {
  const map = {
    'Venezuela': 'វេណេស៊ុយអេឡា',
    'Saudi Arabia': 'អារ៉ាប៊ីសាអ៊ូឌីត',
    'Iran': 'អ៊ីរ៉ង់',
    'Canada': 'កាណាដា',
    'Iraq': 'អ៊ីរ៉ាក់',
    'United Arab Emirates': 'សហអេមីរ៉ាត់អារ៉ាប់',
    'Kuwait': 'កwait',
    'Russia': 'រុស្ស៊ី',
    'United States': 'សហរដ្ឋអាមេរិក',
    'China': 'ចិន',
    'Brazil': 'ប្រេស៊ីល'
  };
  return map[name] || name;
}

// 3. Render Chart: Proven Oil Reserve Ranking Bar Chart
function renderChart() {
  const ctx = document.getElementById('chartReservesRanking');
  if (!ctx) return;

  const isLight = state.theme === 'light';
  const gridColor = isLight ? '#E2E8F0' : '#334155';
  const textColor = isLight ? '#64748B' : '#94A3B8';
  const barDefault = isLight ? '#94A3B8' : '#334155';
  const barActive = isLight ? '#0284C7' : '#38BDF8';

  const sortedData = [...petroleumData].sort((a, b) => a.rank - b.rank);
  const labels = sortedData.map(d => state.lang === 'km' ? translateCountryName(d.country) : d.country);
  const dataValues = sortedData.map(d => d.oilReserveSpr.provenReservesNumeric);

  const backgroundColors = sortedData.map(d => {
    if (state.selectedCountryId === 'GLOBAL' || d.id === state.selectedCountryId) {
      return barActive;
    }
    return barDefault;
  });

  if (chartReserves) chartReserves.destroy();

  chartReserves = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: state.lang === 'km' ? 'បម្រុងប្រេងកាត (ប៊ីលានបារ៉ែល)' : 'Proven Crude Oil Reserves (Billion bbls)',
        data: dataValues,
        backgroundColor: backgroundColors,
        borderRadius: 4,
        maxBarThickness: 22,
        categoryPercentage: 0.7,
        barPercentage: 0.8
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: {
          ticks: { color: textColor, font: { size: 10, weight: '600', family: state.lang === 'km' ? 'Kantumruy Pro' : 'Inter' } },
          grid: { display: false }
        },
        y: {
          ticks: { color: textColor, font: { family: 'Inter' } },
          grid: { color: gridColor },
          title: { display: true, text: 'Billion bbls', color: textColor, font: { size: 10 } }
        }
      }
    }
  });
}

// 4. Render Upstream Policy Scannable KPIs with Rich Icons & i18n
function renderUpstreamKpis() {
  const container = document.getElementById('upstreamKpiList');
  if (!container) return;

  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    container.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-file-signature text-cyan"></i> ${t.labelLicensing}</div>
        <div class="kpi-item-val">${t.valLicensingGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-building-flag text-purple"></i> ${t.labelNoc}</div>
        <div class="kpi-item-val">${t.valNocGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-droplet text-green"></i> ${t.labelConservation}</div>
        <div class="kpi-item-val">${t.valConservationGlobal}</div>
      </div>
    `;
    return;
  }

  const c = petroleumData.find(item => item.id === state.selectedCountryId);
  if (!c) return;

  const p = c.upstreamPolicy;
  container.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-file-signature text-cyan"></i> ${t.labelExploration}</div>
      <div class="kpi-item-val">${p.explorationLicensing}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-building-flag text-purple"></i> ${t.labelRoleNoc}</div>
      <div class="kpi-item-val">${p.roleOfNoc}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-droplet text-green"></i> ${t.labelReservoir}</div>
      <div class="kpi-item-val">${p.resourceConservation}</div>
    </div>
  `;
}

// 5. Render Downstream Policy Scannable KPIs with Rich Icons & i18n
function renderDownstreamKpis() {
  const container = document.getElementById('downstreamKpiList');
  if (!container) return;

  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    container.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-industry text-cyan"></i> ${t.labelRefining}</div>
        <div class="kpi-item-val">${t.valRefiningGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-tags text-purple"></i> ${t.labelPricing}</div>
        <div class="kpi-item-val">${t.valPricingGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-leaf text-green"></i> ${t.labelFuel}</div>
        <div class="kpi-item-val">${t.valFuelGlobal}</div>
      </div>
    `;
    return;
  }

  const c = petroleumData.find(item => item.id === state.selectedCountryId);
  if (!c) return;

  const d = c.downstreamPolicy;
  container.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-industry text-cyan"></i> ${t.labelRefiningPipeline}</div>
      <div class="kpi-item-val">${d.refiningPipelineInfra}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-tags text-purple"></i> ${t.labelRetailPricing}</div>
      <div class="kpi-item-val">${d.retailPricingSubsidy}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-leaf text-green"></i> ${t.labelFuelQuality}</div>
      <div class="kpi-item-val">${d.fuelQualityEnvStandards}</div>
    </div>
  `;
}

// 6. Render Tax Architecture Scannable KPIs with Rich Icons & i18n
function renderFiscalKpis() {
  const container = document.getElementById('fiscalKpiList');
  if (!container) return;

  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    container.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-receipt text-amber"></i> ${t.labelRoyalties}</div>
        <div class="kpi-item-val">${t.valRoyaltiesGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-hand-holding-dollar text-green"></i> ${t.labelStateTake}</div>
        <div class="kpi-item-val">${t.valStateTakeGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-calculator text-purple"></i> ${t.labelCostRecovery}</div>
        <div class="kpi-item-val">${t.valCostRecoveryGlobal}</div>
      </div>
    `;
    return;
  }

  const c = petroleumData.find(item => item.id === state.selectedCountryId);
  if (!c) return;

  const tax = c.taxFiscalRegime;
  container.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-receipt text-amber"></i> ${t.labelStatutoryRoyalties}</div>
      <div class="kpi-item-val">${tax.royalties}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-percent text-purple"></i> ${t.labelCit}</div>
      <div class="kpi-item-val">${tax.pptCit}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-file-invoice text-green"></i> ${t.labelTaxSchedule}</div>
      <div class="kpi-item-val">${tax.comprehensiveTaxSchedule}</div>
    </div>
  `;
}

// 7. Render Risk & Cambodia Strategic Spotlight KPIs with Rich Icons & i18n
function renderRiskKpis() {
  const container = document.getElementById('riskKpiList');
  if (!container) return;

  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    container.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-shield text-cyan"></i> ${t.labelHse}</div>
        <div class="kpi-item-val">${t.valHseGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-piggy-bank text-amber"></i> ${t.labelStabilization}</div>
        <div class="kpi-item-val">${t.valStabilizationGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-lightbulb text-purple"></i> ${t.labelCambodia}</div>
        <div class="kpi-item-val">${t.valCambodiaGlobal}</div>
      </div>
    `;
    return;
  }

  const c = petroleumData.find(item => item.id === state.selectedCountryId);
  if (!c) return;

  const r = c.riskManagement;
  const refs = (c.references || []).join(' | ');

  container.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-shield text-cyan"></i> ${t.labelHseCompliance}</div>
      <div class="kpi-item-val">${r.hseCompliance}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-lightbulb text-amber"></i> ${t.labelLessonCambodia}</div>
      <div class="kpi-item-val" style="color:var(--accent-cyan); font-style:italic;">"${c.transferabilityToCambodia}"</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-book-bookmark text-purple"></i> ${t.labelReferences}</div>
      <div class="kpi-item-val" style="font-size:0.8rem; color:var(--text-secondary);">${refs}</div>
    </div>
  `;
}
