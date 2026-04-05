# Liquidity Risk Optimization under Cash-Flow Uncertainty

Monte Carlo simulation + linear programming model to study how firms manage cash, borrowing, and short-term investments under uncertain cash flows.

Calibrated using Infosys FY23–24 scale · 12-month horizon · 1000 simulated scenarios

---

## What this project does

Firms face a continuous tradeoff: hold too much cash and forfeit returns; hold too little and risk insolvency. This project builds a stochastic optimization framework to determine the optimal dynamic policy for cash, borrowing, and investment under uncertain cash flows.


All results come from running the same model under different assumptions (interest rate, volatility, shocks).

---

## Results (baseline case)

| Metric      | Value   |
| ----------- | ------- |
| Mean Profit | ₹332 Cr |
| VaR (95%)   | ₹190 Cr |
| CVaR (95%)  | ₹154 Cr |

Key observation:

The model operates in a surplus regime — borrowing is near-zero across scenarios, and surplus capital is consistently deployed into short-term investments. Even in the worst 5% of scenarios, the firm remains profitable.

---

## Project structure

```
src/       → model code (simulation, optimization, risk, plots)
data/      → generated scenarios
results/   → outputs + visuals
report/    → full write-up
analysis.ipynb
```

---

## Tech Stack

Python · Pandas · NumPy · PuLP · Matplotlib
