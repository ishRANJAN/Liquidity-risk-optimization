# Liquidity-risk-optimization

# Liquidity Risk Optimization under Cash Flow Uncertainty

## Overview

Effective liquidity management is critical for firms operating under uncertain cash flows. This project develops a stochastic optimization framework to model how firms dynamically allocate resources between cash holdings, borrowing, and short-term investments while maintaining financial stability.

The model integrates Monte Carlo simulation with linear programming to evaluate optimal liquidity strategies across multiple possible future scenarios. Risk is quantified using Conditional Value at Risk (CVaR), enabling analysis of tail outcomes rather than just expected performance.

---

## Core Contributions

* Developed a **multi-period stochastic liquidity model** simulating 1000 possible cash flow scenarios
* Implemented a **linear optimization framework (PuLP)** for dynamic allocation decisions
* Incorporated **real-world financial calibration (Infosys, ₹ Crore scale)**
* Modeled uncertainty via **growth dynamics, cost structure, and shock scenarios**
* Implemented **profit-based CVaR for tail risk evaluation**
* Built a **6-panel analytical dashboard** for scenario, distribution, and risk visualization
* Explored **risk-return trade-offs through investment allocation sensitivity**

---

## Methodology

### 1. Stochastic Cash Flow Simulation

* Generated 1000 scenarios over a 12-month horizon
* Modeled inflows and outflows using probabilistic distributions
* Incorporated:

  * Revenue growth trends
  * Fixed vs variable cost structure
  * Adverse demand shocks

---

### 2. Optimization Model

Formulated a multi-period linear programming model:

* Decision Variables:

  * Cash balance
  * Borrowing
  * Investment

* Objective:
  Maximize net returns:
  (Investment returns − Borrowing costs)

* Constraints:

  * Cash flow continuity
  * Minimum liquidity requirement
  * Borrowing limits

---

### 3. Risk Modeling

* Defined **loss as negative profit**
* Computed:

  * Value at Risk (VaR)
  * Conditional Value at Risk (CVaR)
* Evaluated tail-risk behavior across simulated scenarios

---

### 4. Visualization & Analysis

* Profit distribution with VaR and CVaR markers
* Cash flow uncertainty via scenario fan charts
* Borrowing and investment behavior across scenarios
* Risk sensitivity across confidence levels
* Risk-return frontier (expected profit vs tail risk)

---

## Key Insights

* The model operates in a **surplus regime**, where operating cash flows are sufficient to meet liquidity constraints in most scenarios
* Borrowing is rarely required and appears only under extreme shock conditions
* Excess liquidity is consistently deployed into short-term investments
* Even in lower-tail scenarios, profitability remains positive, indicating strong structural resilience
* Risk-return exploration shows the expected trade-off between higher investment exposure and increased tail risk

---

## Project Structure

```
data/       → simulated cash flow scenarios  
src/        → simulation, optimization, risk, visualization  
results/    → outputs, dashboard, and plots  
report/     → detailed documentation  
```

---

## Tech Stack

* Python
* NumPy / Pandas
* PuLP (Linear Programming)
* Matplotlib

---

## Future Work

* Integrate CVaR directly into optimization for true risk-aware decision making
* Extend to multi-period stochastic programming with scenario trees
* Incorporate dynamic interest rates and macroeconomic shocks
* Build an interactive dashboard (Streamlit / Plotly Dash)

---

## Author

Ishita Ranjan

