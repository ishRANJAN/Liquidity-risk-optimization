import pandas as pd
import matplotlib.pyplot as plt

def plot_results():

    df = pd.read_csv("../results/raw_results.csv")

    # --- 1. Objective Distribution ---
    plt.figure()
    plt.hist(df["objective"], bins=50)
    plt.title("Distribution of Profit (Objective)")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")
    plt.savefig("../results/profit_distribution.png")

    # --- 2. Borrowing Distribution ---
    plt.figure()
    plt.hist(df["total_borrow"], bins=50)
    plt.title("Distribution of Borrowing")
    plt.xlabel("Borrowing Amount")
    plt.ylabel("Frequency")
    plt.savefig("../results/borrowing_distribution.png")

    # --- 3. Final Cash ---
    plt.figure()
    plt.hist(df["final_cash"], bins=20)
    plt.title("Final Cash Distribution")
    plt.xlabel("Cash")
    plt.ylabel("Frequency")
    plt.savefig("../results/cash_distribution.png")

    print("Plots saved in results folder")


if __name__ == "__main__":
    plot_results()
