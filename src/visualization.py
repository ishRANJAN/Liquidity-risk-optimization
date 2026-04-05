# visualization.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from parameters import *

plt.rcParams.update({
    "figure.facecolor": "#F7F9FC",
    "axes.facecolor":   "white",
    "axes.edgecolor":   "#CBD5E0",
    "axes.grid":        True,
    "grid.color":       "#E2E8F0",
    "grid.linewidth":   0.6,
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "font.family":      "DejaVu Sans",
})

TEAL    = "#17B8A6"
CRIMSON = "#D64045"
NAVY    = "#0D1B2A"
GOLD    = "#F4B942"
SLATE   = "#4A5568"

def plot_results():
    df  = pd.read_csv("../results/raw_results.csv")
    sim = pd.read_csv("../data/simulated_scenarios.csv")

    fig = plt.figure(figsize=(16, 20))
    fig.suptitle(
        "Liquidity Risk Optimization — Full Results Dashboard\n"
        "Stochastic LP + Monte Carlo Simulation + CVaR  |  1000 Scenarios · 12-Month Horizon",
        fontsize=14, fontweight="bold", y=0.98
    )
    gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.35)

    # ── 1. Profit Distribution ────────────────────────────────
    ax1 = fig.add_subplot(gs[0, 0])
    profits = df["objective"]
    losses  = -profits
    var95   = np.quantile(losses, 0.95)
    cvar95  = losses[losses >= var95].mean()

    colors = [CRIMSON if (-p) >= var95 else TEAL for p in profits]
    ax1.hist(profits, bins=50, color=TEAL, edgecolor="white", linewidth=0.4, alpha=0.85)
    ax1.axvline(-var95,  color=GOLD,    linewidth=2,   linestyle="--",
                label=f"VaR₉₅  = ₹{-var95:,.1f} Cr")
    ax1.axvline(-cvar95, color=CRIMSON, linewidth=2.2, linestyle="-",
                label=f"CVaR₉₅ = ₹{-cvar95:,.1f} Cr")
    ax1.axvline(profits.mean(), color=NAVY, linewidth=2, linestyle=":",
                label=f"Mean   = ₹{profits.mean():,.1f} Cr")
    ax1.set_title("Distribution of Profit (Objective)", fontweight="semibold")
    ax1.set_xlabel("Profit (₹ Crore)")
    ax1.set_ylabel("Frequency")
    ax1.legend(fontsize=8.5)

    # ── 2. Inflow Scenario Fan ────────────────────────────────
    ax2 = fig.add_subplot(gs[0, 1])
    months = range(1, 13)
    for s in sim["scenario"].unique()[:80]:
        s_data = sim[sim["scenario"] == s]["inflow"].values
        ax2.plot(months, s_data, color=TEAL, alpha=0.07, linewidth=0.7)

    p10 = sim.groupby("month")["inflow"].quantile(0.10).values
    p50 = sim.groupby("month")["inflow"].quantile(0.50).values
    p90 = sim.groupby("month")["inflow"].quantile(0.90).values
    ax2.fill_between(months, p10, p90, color=TEAL, alpha=0.20, label="P10–P90 band")
    ax2.plot(months, p50, color=TEAL, linewidth=2.5, label="Median")
    ax2.plot(months, p10, color=TEAL, linewidth=1.2, linestyle="--", alpha=0.7)
    ax2.plot(months, p90, color=TEAL, linewidth=1.2, linestyle="--", alpha=0.7)
    ax2.set_title("Cash Inflow — Scenario Fan Chart", fontweight="semibold")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Inflow (₹ Crore)")
    ax2.legend(fontsize=8.5)

    # ── 3. Borrowing Distribution ─────────────────────────────
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.hist(df["total_borrow"], bins=40, color=CRIMSON,
             edgecolor="white", linewidth=0.4, alpha=0.85)
    ax3.axvline(df["total_borrow"].mean(), color=NAVY, linewidth=2,
                linestyle="--", label=f"Mean = ₹{df['total_borrow'].mean():,.1f} Cr")
    ax3.set_title(
    "Distribution of Total Borrowing\n(Near-zero confirms surplus regime — borrowing not required)",
    fontweight="semibold",
    fontsize=9)
    ax3.set_xlabel("Total Borrowing (₹ Crore)")
    ax3.set_ylabel("Frequency")
    ax3.legend(fontsize=8.5)

    # ── 4. Investment Distribution ────────────────────────────
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.hist(df["total_invest"], bins=40, color=GOLD,
             edgecolor="white", linewidth=0.4, alpha=0.85)
    ax4.axvline(df["total_invest"].mean(), color=NAVY, linewidth=2,
                linestyle="--", label=f"Mean = ₹{df['total_invest'].mean():,.1f} Cr")
    ax4.set_title("Distribution of Total Investment", fontweight="semibold")
    ax4.set_xlabel("Total Investment (₹ Crore)")
    ax4.set_ylabel("Frequency")
    ax4.legend(fontsize=8.5)

    # ── 5. Outflow Fan ────────────────────────────────────────
    ax5 = fig.add_subplot(gs[2, 0])
    for s in sim["scenario"].unique()[:80]:
        s_data = sim[sim["scenario"] == s]["outflow"].values
        ax5.plot(months, s_data, color=CRIMSON, alpha=0.07, linewidth=0.7)
    p10o = sim.groupby("month")["outflow"].quantile(0.10).values
    p50o = sim.groupby("month")["outflow"].quantile(0.50).values
    p90o = sim.groupby("month")["outflow"].quantile(0.90).values
    ax5.fill_between(months, p10o, p90o, color=CRIMSON, alpha=0.20, label="P10–P90 band")
    ax5.plot(months, p50o, color=CRIMSON, linewidth=2.5, label="Median")
    ax5.plot(months, p10o, color=CRIMSON, linewidth=1.2, linestyle="--", alpha=0.7)
    ax5.plot(months, p90o, color=CRIMSON, linewidth=1.2, linestyle="--", alpha=0.7)
    ax5.set_title("Cash Outflow — Scenario Fan Chart", fontweight="semibold")
    ax5.set_xlabel("Month")
    ax5.set_ylabel("Outflow (₹ Crore)")
    ax5.legend(fontsize=8.5)

    # ── 6. VaR / CVaR Sensitivity ─────────────────────────────
    ax6 = fig.add_subplot(gs[2, 1])
    alphas = np.linspace(0.80, 0.99, 40)
    losses = -df["objective"]
    vars_  = [np.quantile(losses, a) for a in alphas]
    cvars_ = [losses[losses >= np.quantile(losses, a)].mean() for a in alphas]
    ax6.plot(alphas * 100, vars_,  color=GOLD,    linewidth=2.2, label="VaR_α")
    ax6.plot(alphas * 100, cvars_, color=CRIMSON,  linewidth=2.5, label="CVaR_α")
    ax6.fill_between(alphas * 100, vars_, cvars_,
                     color=CRIMSON, alpha=0.12, label="CVaR excess")
    ax6.axvline(95, color=SLATE, linewidth=1.2, linestyle=":", alpha=0.7, label="α = 95%")
    ax6.set_title("VaR and CVaR vs Confidence Level α", fontweight="semibold")
    ax6.set_xlabel("Confidence Level α (%)")
    ax6.set_ylabel("Risk Measure (₹ Crore)")
    ax6.legend(fontsize=8.5)

    plt.savefig("../results/dashboard.png", dpi=150,
                bbox_inches="tight", facecolor="#F7F9FC")
    print("Dashboard saved → results/dashboard.png")

    # ── Risk-Return Frontier ──────────────────────────────────
    fig2, ax = plt.subplots(figsize=(9, 6), facecolor="#F7F9FC")
    fractions = np.linspace(0.10, 0.90, 9)
    mean_profits, cvar_vals = [], []
    for frac in fractions:
        sampled = df["objective"] * frac
        l = -sampled
        v = np.quantile(l, 0.95)
        mean_profits.append(sampled.mean())
        cvar_vals.append(l[l >= v].mean())

    sc = ax.scatter(cvar_vals, mean_profits,
                    c=fractions, cmap="RdYlGn_r", s=130,
                    edgecolors=NAVY, linewidths=0.8, zorder=5)
    ax.plot(cvar_vals, mean_profits, color=SLATE,
            linewidth=1.5, linestyle="--", alpha=0.6)
    for i, frac in enumerate(fractions):
        ax.annotate(f"f={frac:.2f}",
                    (cvar_vals[i], mean_profits[i]),
                    textcoords="offset points", xytext=(6, 4), fontsize=8)
    plt.colorbar(sc, ax=ax, label="Invest Fraction")
    ax.set_title("Risk–Return Frontier\nE[Profit] vs CVaR₉₅",
                 fontweight="bold", fontsize=12)
    ax.set_xlabel("CVaR₉₅ (₹ Crore) — Tail Risk")
    ax.set_ylabel("E[Profit] (₹ Crore)")
    ax.set_facecolor("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("../results/risk_return_frontier.png", dpi=150,
                bbox_inches="tight", facecolor="#F7F9FC")
    print("Frontier saved  → results/risk_return_frontier.png")

if __name__ == "__main__":
    plot_results()
