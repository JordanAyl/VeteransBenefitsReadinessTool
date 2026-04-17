# Veterans Education & Financial Readiness Planner

**A production-style Streamlit app that helps U.S. veterans model Post-9/11 GI Bill housing and benefits alongside cash flow, savings, and expenses—so they can see whether their finances can carry them through school.**

[![CI](https://github.com/JordanAyl/VeteransBenefitsReadinessTool/actions/workflows/ci.yml/badge.svg)](https://github.com/JordanAyl/VeteransBenefitsReadinessTool/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What this demonstrates

- **Product sense:** A real user problem (benefits plus personal runway) packaged as a focused tool with clear assumptions.
- **Engineering:** Typed domain models, separation of config / calculations / UI, reproducible data pipeline from official PDFs, automated CI.
- **Polish:** Theme-aware UI, structured sidebar, charts and tables, documentation aimed at reviewers.

---

## Why this project

Transitioning veterans often juggle two questions at once: **how benefits translate into dollars each term** and **whether savings and income cover rent and life until graduation**. This app combines benefit estimation and month-by-month balance projection in one place, with a clear UI, theme-aware styling, and transparent assumptions.

---

## Live demo

**[Run the app on Streamlit Cloud →](https://educationbenefitplanner.streamlit.app/)**

---

## What it does

| Area | Capabilities |
|------|----------------|
| **Planning horizon** | Forecast window (up to one year), optional term blocks (Winter / Spring / Summer / Fall) with enrollment intensity to vary housing multipliers. |
| **Housing (MHA)** | Location picker backed by **2026 DoD BAH** (*with dependents*, **E-5** monthly rate by military housing area). Rates are embedded from official tables; optional PDF regeneration via `scripts/extract_bah_2026.py`. |
| **GI Bill modeling** | Percentage of eligibility, rate of pursuit, credits, tuition—used to estimate **monthly housing**, **books stipend**, and **tuition covered vs. out-of-pocket** (simplified rules for planning only). |
| **Cash flow** | Savings starting point, VA disability and other income, fixed and variable expenses → **monthly table** and **interactive balance chart** (Altair). |
| **UX** | Grouped sidebar inputs, tabbed results (Overview / Monthly detail / Feedback), light & dark theme support, responsive-oriented layout. |

> **Disclaimer:** Outputs are **planning estimates**, not official VA or DoD determinations. Always verify payments and eligibility with the VA and your certifying official.

---

## Tech stack

- **Python** — application and domain logic  
- **Streamlit** — UI, session state, deployment story  
- **Pydantic / dataclasses** — structured benefit configuration (`models.py`)  
- **Pandas** — time-series style forecast table  
- **Altair** — balance-over-time visualization

---

## Project structure

```text
VeteransBenefitsReadinessTool/
├── .github/workflows/ci.yml        # GitHub Actions: install + compile + import smoke test
├── .streamlit/config.toml          # Streamlit theme and server defaults
├── data/
│   └── 2026 BAH Rates.pdf # Source for embedded BAH table (with-dependents section)
├── scripts/
│   └── extract_bah_2026.py         # Regenerates bah_rates_2026_data.py from the PDF
├── src/veteran_education_financial_readiness/
│   ├── app.py                      # Streamlit UI, CSS, layout
│   ├── bah_rates_2026_data.py      # MHA → E-5 w/ dependents monthly rate (generated)
│   ├── calculations.py             # Housing, books, tuition estimates
│   ├── config.py                   # Annual caps / defaults
│   └── models.py                   # Benefit profile & enums
├── requirements.txt
└── README.md
```

---

## Run locally

**Prerequisites:** Python 3.10+ (3.12+ recommended; use the `py` launcher on Windows if `python` is not on PATH).

```powershell
git clone https://github.com/JordanAyl/veteran-benefits-forecaster.git
cd VeteransBenefitsReadinessTool
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # Windows PowerShell
pip install -r requirements.txt
```

Start the app from the **package directory** so imports resolve:

```powershell
cd src\veteran_education_financial_readiness
python -m streamlit run app.py
```

Open **http://localhost:8501** in your browser. Optional defaults (theme, browser stats) live in `.streamlit/config.toml`.

**macOS / Linux:**

```bash
cd src/veteran_education_financial_readiness
python -m streamlit run app.py
```

---

## Regenerating BAH data (optional)

If you replace `data/2026 BAH Rates.pdf` with an updated PDF:

1. Install **`pdfplumber`** (not listed in `requirements.txt`; used only for extraction):  
   `pip install pdfplumber`
2. Run:  
   `python scripts/extract_bah_2026.py`  
   This overwrites `src/veteran_education_financial_readiness/bah_rates_2026_data.py` using rows from **WITH DEPENDENTS** sections only.

---

## About the author

Built by a **Navy veteran** moving into computer science—this project reflects real friction veterans hit when estimating **benefit dollars**, **housing**, and **runway** without a single integrated tool. It showcases **domain-informed product thinking**, **clear data modeling**, and **polished, accessible UI** suitable for portfolio and interview discussion.

---

## License

This project is released under the [MIT License](LICENSE).
