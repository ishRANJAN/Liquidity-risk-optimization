# Liquidity Risk Optimization under Cash Flow Uncertainty

## 1. Introduction

Liquidity risk arises when a firm cannot meet its short-term obligations due to mismatches between inflows and outflows. Even financially strong firms can face distress if liquidity is poorly managed.

In practice, firms need to balance three things:

* maintaining enough cash to stay safe
* avoiding idle capital
* minimizing expensive borrowing

This project models that trade-off using a stochastic optimization framework.

---

## 2. Problem Statement

At each month ( t = 1, \dots, 12 ), the firm decides:

* cash to hold ( C_t )
* borrowing ( B_t )
* investment ( I_t )

The objective is:

> maximize returns (investment income − borrowing cost)
> while always maintaining a minimum cash buffer

---

## 3. Model Formulation

### Decision Variables

* ( C_t ): cash balance
* ( B_t ): borrowing
* ( I_t ): investment

---

### Objective

Maximize:

[
\sum_t (r_{invest} \cdot I_t - r_{borrow} \cdot B_t)
]

---

### Constraints

**Cash balance**

[
C_t = C_{t-1} + \text{Inflow}_t - \text{Outflow}_t + B_t - I_t
]

**Minimum liquidity**

[
C_t \geq 500
]

**Borrowing limit**

[
0 \leq B_t \leq 3000
]

---

## 4. Data and Assumptions

The model is calibrated using Infosys FY23–24 financial data.

Key assumptions:

* monthly horizon (12 periods)
* 1000 simulated scenarios
* inflow volatility ≈ 18%
* outflow volatility ≈ 12%
* 60% fixed cost structure
* 10% shock probability (−30% inflow)

All values are in ₹ crore.

---

## 5. Simulation

Monte Carlo simulation generates 1000 possible cash flow paths.

For each scenario:

* inflows follow a normal distribution with growth
* shocks randomly reduce inflows
* outflows combine fixed + variable components

This produces a distribution of possible futures rather than a single forecast.

---

## 6. Optimization

For each scenario, a linear program is solved using PuLP.

This determines:

* how much to borrow
* how much to invest
* how cash evolves

Effectively, we solve **1000 LPs**, one per scenario.

---

## 7. Risk Modeling

Risk is measured using:

* **VaR (95%)** → threshold of worst outcomes
* **CVaR (95%)** → average of worst 5% outcomes

Loss is defined as negative profit.

CVaR is preferred since it captures the severity of tail outcomes.

---

## 8. Results

Key observations:

* Profit remains positive across all scenarios
* Borrowing is rarely used
* Surplus cash is consistently invested

This indicates the model operates in a **surplus regime**.

---

## 9. Sensitivity Analysis

### Borrowing Rate

Lower borrowing cost:

* increases profit
* increases downside exposure

Higher borrowing cost:

* reduces profit
* leads to more conservative behavior

---

### Volatility

* Mean profit remains stable
* Distribution widens
* Tail behavior changes

---

### Shock Probability

Most impactful parameter:

* higher shocks → lower profit
* model becomes more conservative
* tail risk behavior shifts significantly

---

## 10. Key Insights

* The system is dominated by surplus cash generation
* Borrowing acts as a fallback, not a primary strategy
* Risk-return tradeoff is clearly observable
* Shock frequency has the strongest effect on outcomes

---

## 11. Limitations

* Risk is evaluated after optimization (not inside objective)
* Cash flows assumed independent
* Interest rates fixed
* Single-firm calibration

---

## 12. Future Work

* integrate CVaR into optimization
* multi-stage stochastic programming
* dynamic interest rates
* cross-firm analysis

---

## 13. Conclusion

This project shows how combining simulation, optimization, and risk metrics can produce structured insights into liquidity management.

At the scale considered, the key problem is not survival but efficient deployment of surplus capital.
