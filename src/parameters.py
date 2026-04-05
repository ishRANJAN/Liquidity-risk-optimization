# parameters.py

#TIME STRUCTURE
T = 12  # 12-month planning horizon

# FINANCIAL CONSTRAINTS
min_cash = 5_000_000        # Minimum liquidity buffer
borrow_limit = 20_000_000   # Maximum borrowing capacity

# INTEREST RATES (MONTHLY)
r_borrow = 0.12 / 12   # Cost of borrowing
r_invest = 0.06 / 12   # Return on surplus cash

# REAL-WORLD CALIBRATION (INFOSYS FY23-24)

# Annual revenue  ≈ ₹1,53,670 Cr → monthly ≈ ₹12,806 Cr
# Annual expenses ≈ ₹1,16,500 Cr → monthly ≈ ₹9,708 Cr
monthly_inflow_mean  = 12806.0   # ₹ Crore
monthly_outflow_mean =  9708.0   # ₹ Crore

# UNCERTAINTY MODELING
inflow_std  = 0.18 * monthly_inflow_mean   # 18% monthly volatility
outflow_std = 0.12 * monthly_outflow_mean  # 12% monthly volatility

# FINANCIAL CONSTRAINTS (₹ Crore)
min_cash    =  500.0    # Minimum liquidity buffer
borrow_limit = 3000.0   # Maximum borrowing per month

# INTEREST RATES (monthly)
r_borrow = 0.12 / 12   # 12% p.a. — RBI working capital rate
r_invest = 0.10 / 12   # 10% p.a. — short-term investment return
# Note: r_invest > r_borrow ensures investing surplus is always profitable

# SIMULATION
num_scenarios = 1000

# --ADVANCED FEATURES--

# Growth assumption
growth_rate       = 0.01   # 1% monthly inflow growth

# Cost structure
fixed_cost_ratio  = 0.60   # 60% of expenses are fixed

# Shock modeling
shock_probability = 0.10   # 10% chance of adverse event per month
shock_impact      = 0.70   # Inflows drop to 70% on shock
