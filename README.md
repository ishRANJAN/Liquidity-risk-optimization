# Liquidity Risk Optimization under Cash-Flow Uncertainty

**Stochastic Programming · Monte Carlo Simulation · CVaR Risk Control**
**Calibrated to Infosys FY23–24 · RBI interest rates · 1,000 scenarios · 12-month horizon**

---

## What This Does

Firms face a continuous tradeoff: hold too much cash and forfeit returns; hold too little and risk insolvency. This project builds a stochastic optimization framework to determine the optimal dynamic policy for cash, borrowing, and investment under uncertain cash flows.

**Pipeline:**

Monte Carlo Simulation → Linear Programming (PuLP) → CVaR Risk Measurement → Sensitivity Analysis → Risk–Return Frontier

For full methodology, mathematical formulation, and detailed findings, see the `report/` directory.

---

## Key Results

| Metric                | Value     |
| --------------------- | --------- |
| E[Profit]             | ₹332.6 Cr |
| VaR₉₅                 | ₹190.3 Cr |
| CVaR₉₅                | ₹153.8 Cr |
| Shortfall Probability | < 1%      |

The model operates in a **surplus regime** — borrowing is near-zero across scenarios, and surplus capital is consistently deployed into short-term investments. Even in the worst 5% of scenarios, the firm remains profitable.

---

## Reproducing the Results

```bash
pip install -r requirements.txt

cd src
python3 simulation.py
python3 optimization.py
python3 risk.py
python3 visualization.py
```

Or run:

```bash
jupyter notebook
```

and open `analysis.ipynb` for an interactive walkthrough.

---

## Structure

```text
src/          → simulation, optimization, risk, visualization, parameters
data/         → generated scenario data (1,000 × 12)
results/      → dashboard.png, risk_return_frontier.png, raw outputs
report/       → full academic documentation
analysis.ipynb
requirements.txt
```

---

## Tech Stack

Python · NumPy · Pandas · PuLP · Matplotlib · SciPy · Jupyter
