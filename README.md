# Liquidity-risk-optimization
# Liquidity Risk Optimization under Cash Flow Uncertainty

## Overview

Effective liquidity management is critical for firms operating under uncertain cash flows. This project develops a stochastic optimization framework to model how firms dynamically allocate resources between cash holdings, borrowing, and short-term investments while maintaining financial stability.

The model integrates Monte Carlo simulation with linear programming to evaluate optimal liquidity strategies across multiple possible future scenarios. Additionally, risk is quantified using Conditional Value at Risk (CVaR), enabling analysis of extreme downside outcomes.


## Core Contributions

* Developed a **multi-period stochastic liquidity model** simulating 1000 possible cash flow scenarios
* Implemented a **linear optimization framework (PuLP)** to determine optimal borrowing and investment strategies
* Incorporated **real-world financial calibration** using Infosys data
* Modeled **uncertainty through growth dynamics, cost structure, and shock scenarios**
* Evaluated downside risk using **CVaR (Conditional Value at Risk)**
* Generated insights on **risk-return trade-offs and liquidity constraints**


## Methodology

### 1. Stochastic Cash Flow Simulation

* Generated 1000 scenarios over a 12-month horizon
* Modeled inflows and outflows using probabilistic distributions
* Incorporated:

  * Revenue growth trends
  * Fixed vs variable cost structures
  * Adverse shock scenarios


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


### 3. Risk Modeling

* Defined liquidity shortfall as a loss function
* Computed **CVaR at 95% confidence level**
* Evaluated tail-risk behavior across scenarios


### 4. Visualization & Analysis

* Distribution of profit across scenarios
* Borrowing behavior analysis
* Liquidity constraint validation


## Key Insights

* Liquidity constraints are binding across all scenarios
* Firms rely heavily on borrowing to maintain required cash buffers
* Profitability is consistently negative due to financing costs
* The model eliminates downside risk through strict constraints rather than optimizing risk-return trade-offs


## Project Structure

```id="l5a2pq"
data/       → simulated cash flow scenarios  
src/        → simulation, optimization, risk, visualization  
results/    → outputs and plots  
report/     → detailed documentation  
```


## Tech Stack

* Python
* NumPy / Pandas
* PuLP (Linear Programming)
* Matplotlib


## Future Work

* Introduce soft liquidity constraints to enable risk-return optimization
* Extend to stochastic programming framework
* Incorporate dynamic interest rates and macroeconomic factors
* Build interactive dashboard for scenario analysis


## Author

Ishita Ranjan

