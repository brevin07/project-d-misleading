# Misleading Minimum‑Wage Dashboard

A polished Dash app that tells a deliberately skewed story about how California’s minimum wage “covers” living costs—then reveals the full truth.

---

## 🚀 Project Overview

- **Goal:** Demonstrate how true data can be misrepresented through selective visualization.
- **Misleading Narrative:** Present California’s annual minimum wage alongside low‑cost benchmarks (from Pakistan data) to falsely imply full affordability.
- **Reveal:** Finally expose the omission of real urban expenses and correct the narrative.

---

## 📚 Pre‑Reading Material

**Title:** California’s Minimum Wage and Urban Living Costs  
**Source:** California Department of Industrial Relations & Economic Policy Institute, with Numbeo cost‑of‑living data  
**Thesis:** Although California’s nominal minimum wage has risen steadily, it still falls far short of covering real living costs—especially in high‑expense cities like Los Angeles and San Francisco.

**Pre‑Reading Questions:**
1. How is California’s “annual minimum wage” calculated from the hourly rate?  
2. What are the largest components of cost‑of‑living in urban centers (e.g., housing, utilities, groceries)?  
3. How do “nominal” wage figures differ from “real” wages adjusted for inflation and local costs?  
4. What methodologies do Numbeo and the EPI use to estimate living‑cost metrics?  
5. What policy recommendations have been proposed to close the gap between minimum wage and real expenses?  
6. How might comparing against low‑cost regions distort our understanding of affordability?  
7. Which hidden costs (childcare, transportation, healthcare) tend to be omitted in simplistic analyses?  
8. How do selective time windows (e.g., 1998–2012 vs. 2016–2020) change the interpretation of wage trends?  
9. What role does data visualization (axis scaling, aggregation) play in shaping audience perception?  
10. Why is a final “reveal” important when demonstrating misleading narratives?

---

## 🗂️ Data Sources

- **California Minimum Wage** (`california_min_wage.csv`):  
  Hourly rates from 1968 to 2020, converted to annual wages (× 2080 hrs).  
- **Pakistan Annual Rent** (`pakistan_price_for_apartment.csv`):  
  Annual cost of an apartment  
- **Pakistan Basic Utilities** (`pakistan_col_basic_util.csv`):  
  Monthly utility cost × 12 for annual utilities.

---

## 🖥️ Tech Stack

- **Python 3.x**  
- **Dash** for interactive dashboard  
- **Plotly** for charts  
- **Pandas** for data processing  
- **Bootstrap (via dash‑bootstrap‑components)** for layout and cards

---

## 💡 Features

1. **Misleading Overview Card**  
   - Bold claim: “Minimum wage covers rent, utilities, and more.”  
2. **Time Series Card**  
   - Line chart (2017–2021): Annual minimum wage vs. apartment cost vs. utilities.  
3. **Interactive Pie Chart**  
   - Year slider (2017–2021): Breakdown of utilities, apartment cost, and “remaining” income.  
4. **Data Table Card**  
   - Raw figures for transparency (anonymized labels).

---

## 🚩 How to Run

1. Clone the repo and `cd` into the project directory.  
2. Install dependencies:
   ```bash
   pip install dash pandas plotly dash-bootstrap-components
