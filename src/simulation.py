import numpy as np
import pandas as pd
from parameters import *

def generate_scenarios():
    all_data = []

    for s in range(num_scenarios):
        inflows = []
        outflows = []

        for t in range(T):

            # --- INFLOW WITH GROWTH ---
            mean_inflow = monthly_inflow_mean * ((1 + growth_rate) ** t)
            inflow = np.random.normal(mean_inflow, inflow_std)

            # --- SHOCK ---
            if np.random.rand() < shock_probability:
                inflow *= shock_impact

            # --- OUTFLOW (FIXED + VARIABLE) ---
            fixed_cost = fixed_cost_ratio * monthly_outflow_mean
            variable_cost = np.random.normal(
                (1 - fixed_cost_ratio) * monthly_outflow_mean,
                outflow_std
            )

            outflow = fixed_cost + variable_cost

            inflows.append(max(inflow, 0))   # no negative inflow
            outflows.append(max(outflow, 0)) # no negative outflow

        for t in range(T):
            all_data.append({
                "scenario": s,
                "month": t,
                "inflow": inflows[t],
                "outflow": outflows[t]
            })

    df = pd.DataFrame(all_data)
    return df


if __name__ == "__main__":
    df = generate_scenarios()
    df.to_csv("../data/simulated_scenarios.csv", index=False)
    print("Simulation complete. Data saved.")
