# risk.py
import pandas as pd
import numpy as np

def compute_cvar(df, alpha=0.95):
    """
    CVaR_alpha = E[Loss | Loss >= VaR_alpha]
    Loss = negative profit (objective)
    """
    losses = -df["objective"]   

    # VaR
    var_alpha = np.quantile(losses, alpha)
    
    # Tail losses
    tail_losses = losses[losses >= var_alpha]

    # Safety check
    if len(tail_losses) == 0:
        print("No tail losses found.")
        return 0

    cvar = tail_losses.mean()

    print(f"VaR  ({int(alpha*100)}%): {var_alpha:,.2f}")
    print(f"CVaR ({int(alpha*100)}%): {cvar:,.2f}")

    return cvar


if __name__ == "__main__":
    df = pd.read_csv("../results/raw_results.csv")
    compute_cvar(df)
