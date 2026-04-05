import pandas as pd
from pulp import *
from parameters import *

def optimize_scenario(df_scenario):

    model = LpProblem("Liquidity_Optimization", LpMaximize)

    C = LpVariable.dicts("Cash", range(T), lowBound=0)
    B = LpVariable.dicts("Borrow", range(T), lowBound=0, upBound=borrow_limit)
    I = LpVariable.dicts("Invest", range(T), lowBound=0)

    inflow = df_scenario["inflow"].values
    outflow = df_scenario["outflow"].values

    # Objective
    model += lpSum([r_invest * I[t] - r_borrow * B[t] for t in range(T)])

    # Constraints
    for t in range(T):

        if t == 0:
            model += C[t] == inflow[t] - outflow[t] + B[t] - I[t]
        else:
            model += C[t] == C[t-1] + inflow[t] - outflow[t] + B[t] - I[t]

        model += C[t] >= min_cash

    model.solve()

    return {
        "final_cash": value(C[T-1]),
        "total_borrow": sum(value(B[t]) for t in range(T)),
        "total_invest": sum(value(I[t]) for t in range(T)),
        "objective": value(model.objective)
    }


if __name__ == "__main__":

    df = pd.read_csv("../data/simulated_scenarios.csv")

    results = []

    for s in df["scenario"].unique():
        df_s = df[df["scenario"] == s].reset_index(drop=True)
        res = optimize_scenario(df_s)
        res["scenario"] = s
        results.append(res)

    results_df = pd.DataFrame(results)
    results_df.to_csv("../results/raw_results.csv", index=False)

    print("Optimization complete. Results saved.")
