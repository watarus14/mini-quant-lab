import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# main 
def main():
    # 1. Market data
    data = yf.download(
        "SPY",
        period = "5y",
        interval = "1d",
        auto_adjust = True,
        progress = False,
    )

    if data.empty:
        raise RuntimeError("No market data was downloaded.")

    # Handle either a Series-like column or a DataFrame 
    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    close = close.dropna().rename("close")

    # 2. Daily simple returns
    returns = close.pct_change().dropna()
    returns.name = "return"

    # 3. Basic statistics
    mean_return = returns.mean()
    volatility = returns.std(ddof = 1)
    annualized_volatility = volatility * np.sqrt(252)

    print(f"Observations: {len(returns)}")
    print(f"Mean daily return: {mean_return:.6f}")
    print(f"Daily volatility: {volatility:.6f}")
    print(f"Annualized volatility: {annualized_volatility:.4f}")

    # 4. One-day return autocorrelation
    autocorrelation = returns.autocorr(lag=1)
    print(f"Lag-1 autocorrelation: {autocorrelation:.4f}")

    # 5. Plot price and returns
    fig, axes = plt.subplots(
        2, 1, figsize=(11,7), sharex=True 
    )

    axes[0].plot(close.index, close)
    axes[0].set_title("Adjusted Closing Price")
    axes[0].set_ylabel("Price")

    axes[1].plot(returns.index, returns)
    axes[1].set_title("Daily Returns")
    axes[1].set_ylabel("Return")
    axes[1].set_xlabel("Data")

    fig.tight_layout()
    fig.savefig("results/market_analysis.pdf")
    plt.show()

if __name__ == "__main__":
    main()