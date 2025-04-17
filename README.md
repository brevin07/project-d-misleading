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
**Source:** Drexel University Hunger‑Free Campus Research Brief, **“Wage Brief 2021”**  
> *“In 2021, a worker receiving minimum wage would be unable to afford a fairly priced two‑bedroom apartment in any U.S. county.”*   
**Thesis:** Although California’s nominal minimum wage has risen steadily, it still falls far short of covering real living costs—especially in high‑expense cities like Los Angeles and San Francisco.

**Pre‑Reading Questions:**
1. **How does the Drexel brief define a “fairly priced” two‑bedroom apartment?**  
2. **What affordability threshold (rent‑to‑income ratio) does the report use to judge housing unaffordability?**  
3. **Which data sources and time period did Drexel use to calculate minimum‑wage purchasing power in 2021?**  
4. **How many U.S. counties did the analysis cover, and what variations did it find across regions?**  
5. **What assumptions does the brief make about full‑time work hours when converting hourly wage to annual income?**  
6. **In what ways does the report adjust for local cost differences (e.g., urban vs. rural)?**  
7. **What other household expenses (utilities, transportation, etc.) does the brief mention—or deliberately omit—when assessing affordability?**  
8. **What policy recommendations or “next steps” does the Drexel brief propose to address the affordability gap?**  
9. **How might focusing solely on housing costs mask other financial pressures on minimum‑wage workers?**  
10. **Why is it important to consider both nominal wage increases and real purchasing power together?**

---

## 🗂️ Data Sources

- **California Minimum Wage** (`california_min_wage.csv`):  
  Hourly rates from 1968 to 2020, converted to annual wages (× 2080 hrs).  
- **Pakistan Annual Rent** (`pakistan_price_for_apartment.csv`):  
  Annual cost of an apartment  
- **Pakistan Basic Utilities** (`pakistan_col_basic_util.csv`):  
  Monthly utility cost × 12 for annual utilities.


---

## 🔍 Citation

- Drexel University Hunger‑Free Campus, **Wage Brief 2021**:  
  <https://drexel.edu/~/media/Files/hunger-free-center/research-briefs/wage-brief-2021.a> 

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
