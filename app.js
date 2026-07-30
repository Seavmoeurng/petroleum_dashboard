import { petroleumData } from './petroleum_data.js';
import { translations } from './translations.js';

// Application State
let state = {
  selectedCountryId: 'GLOBAL',
  currentTab: 'overview',
  searchQuery: '',
  theme: localStorage.getItem('petroleum_theme') || 'dark',
  lang: localStorage.getItem('petroleum_lang') || 'en',
  selectedScenario: '100'
};

// Chart Instances
let chartReserves = null;
let chartSurvival = null;
let chartDonut = null;

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
  renderEmergencySurvivalChart();
  renderMiniOwnershipDonut();
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

// Country List Navigation Configuration
const countryListConfig = [
  { id: 'GLOBAL', flag: '🌐', rank: 'ALL', nameEn: 'All Countries (Global)', nameKm: 'ទិដ្ឋភាពទូទៅសកល' },
  { id: 'venezuela', flag: '🇻🇪', rank: '#1', nameEn: 'Venezuela', nameKm: 'វេណេស៊ុយអេឡា' },
  { id: 'saudi-arabia', flag: '🇸🇦', rank: '#2', nameEn: 'Saudi Arabia', nameKm: 'អារ៉ាប៊ីសាអ៊ូឌីត' },
  { id: 'iran', flag: '🇮🇷', rank: '#3', nameEn: 'Iran', nameKm: 'អ៊ីរ៉ង់' },
  { id: 'canada', flag: '🇨🇦', rank: '#4', nameEn: 'Canada', nameKm: 'កាណាដា' },
  { id: 'iraq', flag: '🇮🇶', rank: '#5', nameEn: 'Iraq', nameKm: 'អ៊ីរ៉ាក់' },
  { id: 'united-arab-emirates', flag: '🇦🇪', rank: '#6', nameEn: 'UAE', nameKm: 'សហអេមីរ៉ាត់អារ៉ាប់' },
  { id: 'kuwait', flag: '🇰🇼', rank: '#7', nameEn: 'Kuwait', nameKm: 'កូវ៉ែត' },
  { id: 'russia', flag: '🇷🇺', rank: '#8', nameEn: 'Russia', nameKm: 'រុស្ស៊ី' },
  { id: 'united-states', flag: '🇺🇸', rank: '#11', nameEn: 'United States', nameKm: 'សហរដ្ឋអាមេរិក' },
  { id: 'china', flag: '🇨🇳', rank: '#13', nameEn: 'China', nameKm: 'ចិន' },
  { id: 'brazil', flag: '🇧🇷', rank: '#15', nameEn: 'Brazil', nameKm: 'ប្រេស៊ីល' }
];

// Event Listeners Initialization
function initEvents() {
  const searchInput = document.getElementById('searchInput');
  const themeBtn = document.getElementById('themeToggleBtn');
  const langBtn = document.getElementById('langToggleBtn');
  const printBtn = document.getElementById('printA4Btn');
  const tabBtns = document.querySelectorAll('.view-tab-btn');
  const scenarioBtns = document.querySelectorAll('.scenario-btn, .scenario-card');

  if (langBtn) {
    langBtn.addEventListener('click', toggleLanguage);
  }

  if (printBtn) {
    printBtn.addEventListener('click', () => {
      window.print();
    });
  }

  window.addEventListener('beforeprint', () => {
    if (chartReserves) chartReserves.resize();
    if (chartSurvival) chartSurvival.resize();
    if (chartDonut) chartDonut.resize();
  });

  window.addEventListener('afterprint', () => {
    renderAllViews();
  });

  if (themeBtn) {
    themeBtn.addEventListener('click', toggleTheme);
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value.toLowerCase().trim();
      renderAllViews();
    });
  }

  // Internal Card Tab Switcher Handlers
  const cardTabBtns = document.querySelectorAll('.card-tab-btn');
  cardTabBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      // Deactivate all sibling buttons
      const tabsContainer = e.target.closest('.card-tabs');
      tabsContainer.querySelectorAll('.card-tab-btn').forEach(b => b.classList.remove('active'));

      // Activate clicked button
      e.target.classList.add('active');

      // Hide all sibling content panes
      const card = e.target.closest('.tabbed-card');
      card.querySelectorAll('.card-tab-content').forEach(content => {
        content.classList.remove('active');
        content.style.display = 'none';
      });

      // Show target content pane
      const targetId = e.target.getAttribute('data-target');
      const targetPane = document.getElementById(targetId);
      if (targetPane) {
        targetPane.classList.add('active');
        targetPane.style.display = 'block';
      }
    });
  });

  const scenarioBtnsToggle = document.querySelectorAll('.scenario-toggle-btn');
  scenarioBtnsToggle.forEach(btn => {
    btn.addEventListener('click', (e) => {
      // The label handles checking the radio naturally.
      scenarioBtnsToggle.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const radio = btn.querySelector('input[type="radio"]');
      if (radio) {
        state.selectedScenario = radio.value;
        renderSimulatorTool();
      }
    });
  });
}
// Master Render Function
function renderAllViews() {
  renderStaticUiText();
  renderCountrySidebar();
  renderBanner();
  renderTopKpis();
  renderMiniOwnershipDonut();
  renderChart();
  renderEmergencySurvivalChart();
  renderSimulatorTool();
  renderUpstreamKpis();
  renderDownstreamKpis();
  renderFiscalKpis();
  renderRiskKpis();
}

// Render Left Country Navigation Sidebar List
function renderCountrySidebar() {
  const container = document.getElementById('countryNavList');
  if (!container) return;

  const query = state.searchQuery ? state.searchQuery.toLowerCase() : '';

  container.innerHTML = countryListConfig.map(item => {
    const isActive = state.selectedCountryId === item.id;
    const name = state.lang === 'km' ? item.nameKm : item.nameEn;
    const pillClass = item.id === 'GLOBAL' ? 'country-rank-pill pill-global' : 'country-rank-pill';

    let matchStyle = '';
    if (query) {
      const matches = name.toLowerCase().includes(query) || item.rank.toLowerCase().includes(query);
      if (!matches) {
        matchStyle = 'style="opacity: 0.35;"';
      }
    }

    return `
      <button class="country-nav-item ${isActive ? 'active' : ''}" data-country-id="${item.id}" title="${name}" ${matchStyle}>
        <div class="country-nav-left">
          <span class="country-flag">${item.flag}</span>
          <span class="country-name-text">${name}</span>
        </div>
        <span class="${pillClass}">${item.rank}</span>
      </button>
    `;
  }).join('');

  container.querySelectorAll('.country-nav-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const countryId = btn.getAttribute('data-country-id');
      if (countryId && state.selectedCountryId !== countryId) {
        state.selectedCountryId = countryId;
        renderAllViews();
      }
    });
  });
}

// Translate Static UI Elements
function renderStaticUiText() {
  const t = translations[state.lang];

  const brandName = document.getElementById('uiBrandName');
  const brandSub = document.getElementById('uiBrandSub');
  const exportA4 = document.getElementById('uiExportA4');
  const searchInput = document.getElementById('searchInput');
  const uiSidebarTitle = document.getElementById('uiSidebarTitle');
  const uiSidebarSub = document.getElementById('uiSidebarSub');

  if (brandName) brandName.innerHTML = `${t.brandName} <span class="brand-highlight">${t.brandHighlight}</span>`;
  if (brandSub) brandSub.innerHTML = `<i class="fa-solid fa-globe"></i> ${t.brandSub}`;
  if (exportA4) exportA4.textContent = t.exportA4;
  if (searchInput) searchInput.placeholder = t.searchPlaceholder;
  if (uiSidebarTitle) uiSidebarTitle.textContent = t.sidebarTitle;
  if (uiSidebarSub) uiSidebarSub.textContent = t.sidebarSub;

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

  // Emergency Analytics Titles & Scenarios
  const uiSurvivalChartTitle = document.getElementById('uiSurvivalChartTitle');
  const uiSurvivalChartSub = document.getElementById('uiSurvivalChartSub');
  const uiSimulatorTitle = document.getElementById('uiSimulatorTitle');
  const uiSimulatorSub = document.getElementById('uiSimulatorSub');
  const uiScenario100 = document.getElementById('uiScenario100');
  const uiScenario50 = document.getElementById('uiScenario50');
  const uiScenarioRation = document.getElementById('uiScenarioRation');

  if (uiSurvivalChartTitle) uiSurvivalChartTitle.innerHTML = `<i class="fa-solid fa-clock-rotate-left text-amber"></i> ${t.survivalChartTitle}`;
  if (uiSurvivalChartSub) uiSurvivalChartSub.innerHTML = `<i class="fa-solid fa-shield-cat"></i> ${t.survivalChartSub}`;
  if (uiSimulatorTitle) uiSimulatorTitle.innerHTML = `<i class="fa-solid fa-triangle-exclamation text-amber"></i> ${t.simulatorTitle}`;
  if (uiSimulatorSub) uiSimulatorSub.innerHTML = `<i class="fa-solid fa-sliders"></i> ${t.simulatorSub}`;
  if (uiScenario100) uiScenario100.textContent = t.scenario100;
  if (uiScenario50) uiScenario50.textContent = t.scenario50;
  if (uiScenarioRation) uiScenarioRation.textContent = t.scenarioRation;
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
        const tradeClass = country.tradeStatus.includes('Exporter') ? 'pill-green' : 'pill-cyan';
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
    if (elValReserves) elValReserves.textContent = t.kpiReservesValGlobal;
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

  const reservesUnit = state.lang === 'km' ? 'ពាន់លានបារ៉ែល' : 'B bbls';
  if (elValReserves) elValReserves.textContent = `${c.oilReserveSpr.provenReservesNumeric} ${reservesUnit}`;
  if (elFootReserves) elFootReserves.innerHTML = `<i class="fa-solid fa-trophy"></i> ${t.provenRankPrefix}${c.rank}`;

  if (elValOwnership) elValOwnership.textContent = c.oilReserveSpr.licensingModel;
  if (elFootOwnership) elFootOwnership.innerHTML = `<i class="fa-solid fa-building-flag"></i> ${c.oilReserveSpr.ownershipModel}`;

  if (elValFiscal) elValFiscal.textContent = c.taxFiscalRegime.royalties.split('(')[0].trim();
  if (elFootFiscal) elFootFiscal.innerHTML = `<i class="fa-solid fa-receipt"></i> CIT: ${c.taxFiscalRegime.pptCit.split('(')[0].trim()}`;

  if (elValSpr) elValSpr.textContent = c.oilReserveSpr.sprCapacity.split('(')[0].trim();
  if (elFootSpr) elFootSpr.innerHTML = `<i class="fa-solid fa-clock-rotate-left text-amber"></i> Survival: ${c.oilReserveSpr.survivalCategory}`;
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
    'Kuwait': 'កូវ៉ែត',
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
  const barDefault = isLight ? '#0284C7' : '#38BDF8';
  const unitText = state.lang === 'km' ? 'ពាន់លានបារ៉ែល' : 'B bbls';

  // Flexible Filter: All Countries vs Single Country
  let displayData = [...petroleumData].sort((a, b) => a.rank - b.rank);
  if (state.selectedCountryId !== 'GLOBAL') {
    displayData = displayData.filter(d => d.id === state.selectedCountryId);
  }

  const isSingle = displayData.length === 1;
  const labels = displayData.map(d => state.lang === 'km' ? translateCountryName(d.country) : d.country);
  const dataValues = displayData.map(d => d.oilReserveSpr.provenReservesNumeric);
  const customLabels = displayData.map(d => `${d.oilReserveSpr.provenReservesNumeric} ${unitText}`);

  if (chartReserves) chartReserves.destroy();

  // Custom Inline Plugin to draw text & data labels directly on bars
  const dataLabelsPlugin = {
    id: 'customDataLabelsReserves',
    afterDatasetsDraw(chart) {
      const { ctx } = chart;
      ctx.save();
      chart.data.datasets.forEach((dataset, i) => {
        const meta = chart.getDatasetMeta(i);
        meta.data.forEach((bar, index) => {
          const text = customLabels[index];
          if (!text) return;

          ctx.fillStyle = isLight ? '#0F172A' : '#F8FAFC';
          ctx.font = `${isSingle ? '700 13.5px' : '600 11px'} ${state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter'}, sans-serif`;
          ctx.textAlign = 'left';
          ctx.textBaseline = 'middle';
          ctx.fillText(text, bar.x + 6, bar.y);
        });
      });
      ctx.restore();
    }
  };

  chartReserves = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: state.lang === 'km' ? `បម្រុងប្រេងកាត (${unitText})` : `Proven Crude Oil Reserves (${unitText})`,
        data: dataValues,
        backgroundColor: barDefault,
        borderRadius: 4,
        maxBarThickness: isSingle ? 50 : 12,
        categoryPercentage: isSingle ? 0.4 : 0.7,
        barPercentage: isSingle ? 0.5 : 0.8
      }]
    },
    plugins: [dataLabelsPlugin],
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      layout: {
        padding: { top: 4, bottom: 4, left: 0, right: isSingle ? 140 : 85 }
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function (context) {
              const d = displayData[context.dataIndex];
              return ` ${d.oilReserveSpr.provenReservesNumeric} ${unitText} (${state.lang === 'km' ? 'ចំណាត់ថ្នាក់' : 'Rank'} #${d.rank})`;
            }
          }
        }
      },
      scales: {
        x: {
          ticks: { color: textColor, font: { size: 10.5, family: state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter' } },
          grid: { color: gridColor },
          title: { display: true, text: unitText, color: textColor, font: { size: 10.5, family: state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter' } },
          max: isSingle ? Math.ceil(dataValues[0] * 1.35) : undefined
        },
        y: {
          ticks: { color: textColor, font: { size: isSingle ? 12 : 10.5, weight: '700', family: state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter' } },
          grid: { display: false }
        }
      }
    }
  });
}

// 3.5 Render Chart: Emergency Stock Survival Duration Horizontal Bar Chart
function renderEmergencySurvivalChart() {
  const ctx = document.getElementById('chartSurvivalDuration');
  if (!ctx) return;

  const isLight = state.theme === 'light';
  const gridColor = isLight ? '#E2E8F0' : '#334155';
  const textColor = isLight ? '#64748B' : '#94A3B8';
  const barDefault = isLight ? '#D97706' : '#FBBF24';

  let displayData = [...petroleumData].sort((a, b) => a.rank - b.rank);
  if (state.selectedCountryId !== 'GLOBAL') {
    displayData = displayData.filter(d => d.id === state.selectedCountryId);
  }

  // Split into Exporters (>365 days) and Importers
  const exporters = displayData.filter(d => d.oilReserveSpr.survivalDaysNoImport >= 365);
  const importers = displayData.filter(d => d.oilReserveSpr.survivalDaysNoImport < 365);

  // Render Exporter Badges
  const badgesContainer = document.getElementById('exportersBadges');
  const badgeWrapper = document.getElementById('exportersBadgesWrapper');
  if (badgesContainer && badgeWrapper) {
    if (exporters.length > 0) {
      badgeWrapper.style.display = 'block';
      badgesContainer.innerHTML = exporters.map(d => {
        const name = state.lang === 'km' ? translateCountryName(d.country) : d.country;
        const flag = countryListConfig.find(c => c.id === d.id)?.flag || '';
        return `<span class="badge-exporter">${flag} ${name} (>365d)</span>`;
      }).join('');
    } else {
      badgeWrapper.style.display = 'none';
      badgesContainer.innerHTML = '';
    }
  }

  const isSingle = importers.length === 1;
  const labels = importers.map(d => state.lang === 'km' ? translateCountryName(d.country) : d.country);
  const dataValues = importers.map(d => d.oilReserveSpr.survivalDaysNoImport);

  const dayUnit = state.lang === 'km' ? 'ថ្ងៃ' : 'Days';
  const customLabels = importers.map(d => `${d.oilReserveSpr.survivalDaysNoImport} ${dayUnit}`);

  if (chartSurvival) chartSurvival.destroy();
  if (importers.length === 0) return;

  // Custom Inline Plugin to draw data labels to the right of horizontal bars and the 90-day benchmark line
  const survivalPlugin = {
    id: 'customSurvivalPlugin',
    afterDatasetsDraw(chart) {
      const { ctx, chartArea, scales } = chart;
      ctx.save();
      // Draw labels
      chart.data.datasets.forEach((dataset, i) => {
        const meta = chart.getDatasetMeta(i);
        meta.data.forEach((bar, index) => {
          const text = customLabels[index];
          if (!text) return;

          ctx.fillStyle = isLight ? '#0F172A' : '#F8FAFC';
          ctx.font = `${isSingle ? '700 13.5px' : '600 11px'} ${state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter'}, sans-serif`;
          ctx.textAlign = 'left';
          ctx.textBaseline = 'middle';
          ctx.fillText(text, bar.x + 6, bar.y);
        });
      });

      // Draw 90-Day IEA Benchmark Line
      const xScale = scales.x;
      const xPixel = xScale.getPixelForValue(90);
      if (xPixel >= chartArea.left && xPixel <= chartArea.right) {
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.strokeStyle = isLight ? '#EF4444' : '#F87171';
        ctx.setLineDash([4, 4]);
        ctx.moveTo(xPixel, chartArea.top);
        ctx.lineTo(xPixel, chartArea.bottom);
        ctx.stroke();
        ctx.restore();

        ctx.save();
        ctx.fillStyle = isLight ? '#EF4444' : '#F87171';
        ctx.font = `600 11px ${state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter'}, sans-serif`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'bottom';
        ctx.fillText('IEA 90-Day', xPixel, chartArea.top - 2);
      }
      ctx.restore();
    }
  };

  chartSurvival = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: state.lang === 'km' ? 'ថិរវេលាទ្រទ្រង់ប្រេង (ចំនួនថ្ងៃ)' : 'Fuel Autonomy Duration (Days)',
          data: dataValues,
          backgroundColor: barDefault,
          borderRadius: 4,
          maxBarThickness: isSingle ? 30 : 12,
          categoryPercentage: isSingle ? 0.4 : 0.7,
          barPercentage: isSingle ? 0.5 : 0.8
        }
      ]
    },
    plugins: [survivalPlugin],
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      layout: {
        padding: { top: 12, bottom: 4, left: 0, right: isSingle ? 140 : 85 }
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function (context) {
              const d = importers[context.dataIndex];
              const unit = state.lang === 'km' ? 'ថ្ងៃ' : 'Days';
              return ` ${d.oilReserveSpr.survivalDaysNoImport} ${unit} (${d.oilReserveSpr.survivalCategory})`;
            }
          }
        }
      },
      scales: {
        x: {
          ticks: { color: textColor, font: { size: 10.5, family: state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter' } },
          grid: { color: gridColor },
          title: { display: true, text: state.lang === 'km' ? 'ចំនួនថ្ងៃ (Days)' : 'Days of Autonomy', color: textColor, font: { size: 10.5, family: state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter' } },
          max: Math.max(200, isSingle ? Math.ceil(dataValues[0] * 1.2) : 200)
        },
        y: {
          ticks: { color: textColor, font: { size: isSingle ? 12 : 10.5, weight: '700', family: state.lang === 'km' ? 'Noto Serif Khmer' : 'Inter' } },
          grid: { display: false }
        }
      }
    }
  });
}

// Render NOC Ownership Model Micro-Visual Donut Chart
function renderMiniOwnershipDonut() {
  const ctx = document.getElementById('chartMiniOwnership');
  if (!ctx) return;

  if (chartDonut) chartDonut.destroy();

  chartDonut = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['State Monopoly (9)', 'Private/Auction (2)'],
      datasets: [{
        data: [9, 2],
        backgroundColor: ['#818CF8', '#38BDF8'],
        borderWidth: 0
      }]
    },
    options: {
      cutout: '72%',
      responsive: false,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: { enabled: true }
      }
    }
  });
}

// Render Full-Width Interactive Simulator Tool View
function renderSimulatorTool() {
  const container = document.getElementById('simulatorToolOutput');
  if (!container) return;

  const t = translations[state.lang];
  const scenario = state.selectedScenario;

  // GLOBAL STATE
  if (state.selectedCountryId === 'GLOBAL') {
    let globalDays = 90;
    let scenarioLabel = t.scenario100;
    if (scenario === '50') {
      globalDays = 180;
      scenarioLabel = t.scenario50;
    } else if (scenario === 'ration') {
      globalDays = 112;
      scenarioLabel = t.scenarioRation;
    }

    const isCompliant = globalDays >= 90;
    const badgeClass = isCompliant ? 'status-pill-safe' : 'status-pill-critical';
    const badgeIcon = isCompliant ? 'fa-circle-check' : 'fa-circle-exclamation';
    const badgeText = isCompliant ? 'IEA 90-Day Standard Compliant' : 'Below IEA 90-Day Standard';

    container.innerHTML = `
      <div class="sim-metric-box" style="padding: 0.85rem 1.1rem;">
        <div class="sim-metric-left">
          <span class="sim-metric-title">${t.labelSurvivalDays}</span>
          <span class="sim-metric-value" style="font-size: 2rem;">~${globalDays} ${state.lang === 'km' ? 'ថ្ងៃ' : 'Days'}</span>
          <span class="sim-metric-sub"><i class="fa-solid fa-earth-americas text-cyan"></i> Global Average Fuel Autonomy (${scenarioLabel})</span>
        </div>
        <span class="${badgeClass}" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">
          <i class="fa-solid ${badgeIcon}"></i> ${badgeText}
        </span>
      </div>

      <div class="sim-details-list" style="gap: 0.4rem;">
        <div class="sim-detail-item" style="padding: 0.45rem 0.65rem; font-size: 0.78rem;">
          <i class="fa-solid fa-shield-halved text-cyan" style="margin-top:2px;"></i>
          <div><strong>${state.lang === 'km' ? 'ប្រទេសនាំចេញ (Exporters)' : 'Net Exporters'} (Saudi, Russia, UAE, Iran, Iraq, Kuwait, Venezuela):</strong> ${state.lang === 'km' ? 'ទ្រទ្រង់បានលើសពី ៣៦៥ ថ្ងៃ (ផលិតកម្មក្នុងស្រុកគ្រប់គ្រាន់)' : '>365 Days Autonomy (Domestic crude self-sufficient)'}</div>
        </div>
        <div class="sim-detail-item" style="padding: 0.45rem 0.65rem; font-size: 0.78rem;">
          <i class="fa-solid fa-building-columns text-purple" style="margin-top:2px;"></i>
          <div><strong>${state.lang === 'km' ? 'ប្រទេសនាំចូលធំៗ (Major Importers)' : 'Major Dual/Importers'}:</strong> USA (~120d SPR), China (~100d SPR), Canada (>180d Hubs), Brazil (~45d Buffer)</div>
        </div>
        <div class="sim-detail-item" style="padding: 0.45rem 0.65rem; font-size: 0.78rem;">
          <i class="fa-solid fa-flag text-amber" style="margin-top:2px;"></i>
          <div><strong>${t.cambodiaSpotlightTitle}:</strong> ${state.lang === 'km' ? 'កម្ពុជាមានស្តុកប្រេងអាសន្ន ~២១ ដល់ ៣០ ថ្ងៃ (ពឹងផ្អែកលើការនាំចូល ១០០%)' : 'Cambodia baseline survival is ~21-30 days commercial stock (100% import dependent)'}</div>
        </div>
      </div>
    `;
    return;
  }

  // COUNTRY SPECIFIC STATE
  const c = petroleumData.find(item => item.id === state.selectedCountryId);
  if (!c) return;

  const baseDays = c.oilReserveSpr.survivalDaysNoImport;
  let calcDays = baseDays;
  let statusClass = 'status-pill-safe';
  let statusText = c.oilReserveSpr.survivalCategory;

  if (c.tradeStatus === 'Net Exporter' && baseDays >= 365) {
    calcDays = '>365';
    statusClass = 'status-pill-exporter'; // Usually green or cyan
    statusText = state.lang === 'km' ? 'ស្វ័យគ្រប់គ្រង (Self-Sufficient Exporter)' : 'Self-Sufficient Net Exporter';
  } else {
    if (scenario === '50') {
      calcDays = Math.round(baseDays * 2);
    } else if (scenario === 'ration') {
      calcDays = Math.round(baseDays * 1.25);
    }

    if (calcDays >= 90) {
      statusClass = 'status-pill-safe'; // Green
    } else if (calcDays >= 30) {
      statusClass = 'status-pill-warning'; // Yellow/Amber
    } else {
      statusClass = 'status-pill-critical'; // Red
    }
  }

  const daysDisplay = typeof calcDays === 'number' ? `~${calcDays} ${state.lang === 'km' ? 'ថ្ងៃ' : 'Days'}` : `${calcDays} ${state.lang === 'km' ? 'ថ្ងៃ' : 'Days'}`;

  container.innerHTML = `
    <div class="sim-metric-box" style="padding: 0.85rem 1.1rem;">
      <div class="sim-metric-left">
        <span class="sim-metric-title">${t.labelSurvivalDays}</span>
        <span class="sim-metric-value" style="font-size: 2rem;">${daysDisplay}</span>
        <span class="sim-metric-sub"><i class="fa-solid fa-battery-half text-amber"></i> ${c.oilReserveSpr.survivalCategory}</span>
      </div>
      <span class="${statusClass}" style="font-size: 0.8rem; padding: 0.35rem 0.75rem;">${statusText}</span>
    </div>

    <div class="sim-details-list" style="gap: 0.4rem;">
      <div class="sim-detail-item" style="padding: 0.45rem 0.65rem; font-size: 0.78rem;">
        <i class="fa-solid fa-gas-pump text-amber" style="margin-top:2px;"></i>
        <div><strong>${t.labelDailyConsumption}:</strong> ${c.oilReserveSpr.dailyConsumptionBpd} | <strong>${t.labelImportReliance}:</strong> ${c.oilReserveSpr.netImportReliance}</div>
      </div>
      <div class="sim-detail-item" style="padding: 0.45rem 0.65rem; font-size: 0.78rem;">
        <i class="fa-solid fa-shield-halved text-cyan" style="margin-top:2px;"></i>
        <div><strong>${t.labelEmergencyNote}:</strong> ${c.oilReserveSpr.emergencyScenarioNote}</div>
      </div>
      <div class="sim-detail-item" style="padding: 0.45rem 0.65rem; font-size: 0.78rem;">
        <i class="fa-solid fa-scale-balanced text-purple" style="margin-top:2px;"></i>
        <div><strong>IEA Benchmark:</strong> 90 Days Target | <strong>Cambodia Baseline:</strong> 21-30 Days Commercial Requirement</div>
      </div>
    </div>
  `;
}

// 4. Render Upstream Policy Scannable KPIs with Rich Icons & i18n
function renderUpstreamKpis() {
  const container1 = document.getElementById('upstreamKpiList');
  const container2 = document.getElementById('upstreamKpiList2');
  if (!container1 || !container2) return;

  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    container1.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-file-signature text-cyan"></i> ${t.labelLicensing}</div>
        <div class="kpi-item-val">${t.valLicensingGlobal}</div>
      </div>
    `;
    container2.innerHTML = `
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
  container1.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-file-signature text-cyan"></i> ${t.labelExploration}</div>
      <div class="kpi-item-val">${p.explorationLicensing}</div>
    </div>
  `;
  container2.innerHTML = `
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
  const container1 = document.getElementById('downstreamKpiList');
  const container2 = document.getElementById('downstreamKpiList2');
  if (!container1 || !container2) return;

  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    container1.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-tags text-purple"></i> ${t.labelPricing}</div>
        <div class="kpi-item-val">${t.valPricingGlobal}</div>
      </div>
    `;
    container2.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-industry text-cyan"></i> ${t.labelRefining}</div>
        <div class="kpi-item-val">${t.valRefiningGlobal}</div>
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
  container1.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-tags text-purple"></i> ${t.labelRetailPricing}</div>
      <div class="kpi-item-val">${d.retailPricingSubsidy}</div>
    </div>
  `;
  container2.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-industry text-cyan"></i> ${t.labelRefiningPipeline}</div>
      <div class="kpi-item-val">${d.refiningPipelineInfra}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-leaf text-green"></i> ${t.labelFuelQuality}</div>
      <div class="kpi-item-val">${d.fuelQualityEnvStandards}</div>
    </div>
  `;
}

// 6. Render Tax Architecture Scannable KPIs with Rich Icons & i18n
function renderFiscalKpis() {
  const container1 = document.getElementById('fiscalKpiList');
  const container2 = document.getElementById('fiscalKpiList2');
  if (!container1 || !container2) return;

  const t = translations[state.lang];

  if (state.selectedCountryId === 'GLOBAL') {
    container1.innerHTML = `
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-receipt text-amber"></i> ${t.labelRoyalties}</div>
        <div class="kpi-item-val">${t.valRoyaltiesGlobal}</div>
      </div>
      <div class="kpi-summary-item">
        <div class="kpi-item-label"><i class="fa-solid fa-hand-holding-dollar text-green"></i> ${t.labelStateTake}</div>
        <div class="kpi-item-val">${t.valStateTakeGlobal}</div>
      </div>
    `;
    container2.innerHTML = `
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
  container1.innerHTML = `
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-receipt text-amber"></i> ${t.labelStatutoryRoyalties}</div>
      <div class="kpi-item-val">${tax.royalties}</div>
    </div>
    <div class="kpi-summary-item">
      <div class="kpi-item-label"><i class="fa-solid fa-percent text-purple"></i> ${t.labelCit}</div>
      <div class="kpi-item-val">${tax.pptCit}</div>
    </div>
  `;
  container2.innerHTML = `
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
