# TIME STRUCTURE
T = 12  # 12-month planning horizon

# FINANCIAL CONSTRAINTS
min_cash = 5_000_000        # Minimum liquidity buffer
borrow_limit = 20_000_000   # Maximum borrowing capacity

# INTEREST RATES (MONTHLY)
r_borrow = 0.12 / 12   # Cost of borrowing
r_invest = 0.06 / 12   # Return on surplus cash

# REAL-WORLD CALIBRATION (INFOSYS FY23-24)
scale = 1_000_000  # 1 million

annual_revenue = 1_536_700_000_000 / scale # ORIGINALLY ~₹1.53 lakh crore
annual_expenses = 1_165_000_000_000 / scale # ORIGINALLY ~₹1.16 lakh crore

monthly_inflow_mean = annual_revenue / 12
monthly_outflow_mean = annual_expenses / 12

# UNCERTAINTY MODELING
inflow_std = 0.2 * monthly_inflow_mean   # Assumed volatility
outflow_std = 0.2 * monthly_outflow_mean

# SIMULATION
num_scenarios = 1000  # Monte Carlo scenarios

# ADVANCED FEATURES
# Growth assumption
growth_rate = 0.01  # 1% monthly growth in inflows

# Cost structure
fixed_cost_ratio = 0.6  # % of expenses that are fixed

# Shock modeling
shock_probability = 0.1  # 10% chance of adverse event
shock_impact = 0.7       # Inflows drop to 70%
