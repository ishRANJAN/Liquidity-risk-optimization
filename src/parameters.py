# Time horizon
T = 12

# Financial constraints
min_cash = 5_000_000
borrow_limit = 20_000_000

# Interest rates (monthly)
r_borrow = 0.12 / 12
r_invest = 0.06 / 12

# Infosys-based scale (approx)
annual_revenue = 160_000_000_000
annual_expenses = 120_000_000_000

monthly_inflow_mean = annual_revenue / 12
monthly_outflow_mean = annual_expenses / 12

# Uncertainty
inflow_std = 0.2 * monthly_inflow_mean
outflow_std = 0.2 * monthly_outflow_mean

# Simulation
num_scenarios = 1000

# --- ADVANCED FEATURES ---

# Growth
growth_rate = 0.01  # 1% monthly

# Cost structure
fixed_cost_ratio = 0.6

# Shock modeling
shock_probability = 0.1
shock_impact = 0.7   
