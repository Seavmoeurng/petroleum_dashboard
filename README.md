# Petroleum Policy, Fiscal & SPR Analytics Dashboard

A modern, interactive executive dashboard providing comprehensive policy, fiscal regime, and Strategic Petroleum Reserve (SPR) analytics across **11 major global benchmark economies** (Venezuela, Saudi Arabia, Iran, Canada, Iraq, UAE, Kuwait, Russia, United States, China, and Brazil).

---

## 🌟 Key Features

- **Executive KPI Analytics**: At-a-glance metrics for Proven Reserves, NOC Ownership Models, Primary Fiscal Rent, and Strategic Petroleum Storage.
- **Dual Language Support (EN / KM)**: Instant 1-click language switching between **English 🇬🇧** and **Khmer 🇰🇭** using Google Fonts (*Kantumruy Pro*).
- **Dark & Light Mode Themes**: 1-click theme switcher with `localStorage` preference persistence.
- **Landscape A4 PDF Export**: Built-in `@media print` styling and dedicated `Export A4` button for crisp PDF reporting.
- **Clean Responsive Web App**: Built with vanilla HTML, CSS, JavaScript (ES Modules), and Chart.js. Zero heavy external dependencies.

---

## 📁 Repository Structure

```
.
├── index.html              # Main HTML Application Entry Point
├── index.css               # Styling System & Light/Dark/Print Themes
├── app.js                  # Application Logic & Event Controllers
├── petroleum_data.js       # Exported ES Module Dataset (11 Nations)
├── translations.js         # i18n Translation Dictionary (English & Khmer)
│
├── raw_sources/            # Raw Source Documents
│   ├── pdf/                # PDF Source Benchmark Documents (1.pdf - 4.pdf)
│   └── excel/              # Excel Benchmark Spreadsheets (.xlsx)
│
└── scripts/                # Data Extraction & Maintenance Python Utilities
    ├── build_petroleum_data.py
    ├── extracted_data.json
    └── extracted_summary.txt
```

---

## 🚀 How to Run Locally

Simply serve the workspace using any static web server (no build step required):

```bash
# Using Python
python -m http.server 8080

# Or using Node npx
npx serve .
```

Open your browser to: `http://localhost:8080`

---

## 🌐 Deploying to GitHub Pages

1. Push this repository to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of Petroleum Dashboard"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```
2. Go to **Repository Settings** > **Pages**.
3. Under **Source**, choose `Deploy from a branch` and select `main` branch / `root (/)` folder.
4. Save and your site will be live on `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`!
