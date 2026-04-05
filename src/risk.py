import pandas as pd
import numpy as np

def compute_cvar(df, alpha=0.95):

    # Define loss
    df["loss"] = df["final_cash"].apply(lambda x: max(0, 5_000_000 - x))

    # Sort losses
    sorted_losses = df["loss"].sort_values(ascending=False)

    # Take worst 5%
    cutoff = int((1 - alpha) * len(sorted_losses))
    worst_losses = sorted_losses[:cutoff]

    # CVaR
    cvar = worst_losses.mean()

    return cvar


if __name__ == "__main__":

    df = pd.read_csv("../results/raw_results.csv")

    cvar = compute_cvar(df)

    print(f"CVaR (95%): {cvar}")
