# K.TRITOD — Engineering & Automation Portfolio

**Personal Engineering Portfolio Website of K.TRITOD (TRITOD KRUAWONG)**

Orchestrated, verified, and published across 5 phases (`WEB-01` through `WEB-05`) by the **AI Project Controller (AIPC)**.

---

## 🔬 Core Focus Areas

1. **Analog Integrated Circuit Design & Layout**:
   - Differential Operational Amplifiers, Bandgap References, and Low-Dropout (LDO) Regulators.
   - HSPICE and Spectre circuit simulation across PVT corners (TT, SS, FF, FS, SF) and Monte Carlo statistical yield analysis.
   - Precision IC layout matching (common-centroid, interdigitated), guard ring isolation, and DRC/LVS/PEX extraction.
   - Laboratory bench characterization using oscilloscopes, SMUs, and spectrum analyzers.

2. **Software Automation & Multi-Agent AI**:
   - Automated data wrangling and simulation regression testing in Python.
   - Financial analysis pipelines and Google Sheets integrations using Google Apps Script.
   - Multi-agent AI orchestration architecture using **AI Project Controller (AIPC)**.

---

## 🏛️ Project Architecture & AIPC Lifecycle

This repository was created and verified sequentially through 5 distinct AIPC phases:

| Phase | Name | Objective | Acceptance Criteria | Checkpoint Ref |
|---|---|---|---|---|
| `WEB-01` | Project Initialization | Directory scaffold, `PROJECT.yaml`, `README.md`, base HTML/CSS/JS | `AC-WEB-01` | `aipc/k-tritod-portfolio/phase-web-01/pass` |
| `WEB-02` | Responsive UI | CSS variables, Flexbox/Grid, mobile navigation toggle, keyboard accessibility | `AC-WEB-02` | `aipc/k-tritod-portfolio/phase-web-02/pass` |
| `WEB-03` | Profile and Projects | Complete Home, About, Skills, Projects, and Contact sections with local SVG assets | `AC-WEB-03` | `aipc/k-tritod-portfolio/phase-web-03/pass` |
| `WEB-04` | Functional & Accessibility Tests | 11 automated pytest tests validating HTML/CSS/JS, links, assets, and privacy | `AC-WEB-04` | `aipc/k-tritod-portfolio/phase-web-04/pass` |
| `WEB-05` | GitHub Publication & Final Verification | GitHub Actions CI workflow, `.nojekyll` compatibility, and execution receipt | `AC-WEB-05` | `aipc/k-tritod-portfolio/phase-web-05/pass` |

---

## 🚀 Local Development & Preview

Run a lightweight local HTTP server:

```bash
python -m http.server 8000
```

Open `http://localhost:8000` in any modern web browser.

---

## 🧪 Automated Testing

Execute the comprehensive test suite:

```bash
pytest tests/test_website.py -v
```

All 11 tests verify:
- HTML5 structure, semantic elements, and meta viewport
- Complete presence of all 7 sections (`#home`, `#about`, `#engineering-skills`, `#software-automation`, `#projects`, `#contact`, `#github`)
- Valid internal anchor navigation
- Local resolution and integrity of all SVG images
- Accessible navigation attributes (`aria-expanded`, `aria-controls`, `aria-label`)
- Privacy protection (zero leaks of confidential emails, phone numbers, or personal photos)

---

## 📄 License

MIT License — Copyright (c) 2026 K.TRITOD (TRITOD KRUAWONG).
