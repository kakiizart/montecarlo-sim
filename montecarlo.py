import os
import numpy as np
import matplotlib.pyplot as plt

# ---- Parameters ----
S0 = 100       # Initial price
mu = 0.07      # Expected annual return
sigma = 0.20   # Volatility
T = 1.0        # Years
dt = 1/252     # Daily step (trading days)
N = int(T/dt)  # Steps
simulations = 1000  # How many paths
paths_to_plot = 10  # avoid spaghetti

os.makedirs("out", exist_ok=True)
HEADLESS = os.environ.get("HEADLESS", "0") == "1"

final_prices = []

# ---- Simulate paths (Euler-GBM like your version) ----
for i in range(simulations):
    prices = [S0]
    for _ in range(N):
        shock = np.random.normal(loc=(mu*dt), scale=(sigma*np.sqrt(dt)))
        prices.append(prices[-1] * np.exp(shock))
    final_prices.append(prices[-1])
    if i < paths_to_plot:
        plt.plot(prices, alpha=0.75)

plt.title("Monte Carlo Stock Price Simulation ({} of {} paths)".format(paths_to_plot, simulations))
plt.xlabel("Days"); plt.ylabel("Price")

if HEADLESS:
    plt.savefig("out/paths.png", dpi=160, bbox_inches="tight")
    plt.close()
else:
    plt.show()

# ---- Histogram of final prices ----
final_prices = np.array(final_prices)
plt.hist(final_prices, bins=50, density=True, alpha=0.75)
plt.title("Distribution of Final Prices ({} sims)".format(simulations))
plt.xlabel("Final Price"); plt.ylabel("Frequency")

if HEADLESS:
    plt.savefig("out/final_prices_hist.png", dpi=160, bbox_inches="tight")
    plt.close()
else:
    plt.show()

# ---- Quick stats to console ----
p5, p50, p95 = np.percentile(final_prices, [5, 50, 95])
print(f"Mean: {final_prices.mean():.2f}")
print(f"Median (p50): {p50:.2f}")
print(f"5th–95th percentile: [{p5:.2f}, {p95:.2f}]")
