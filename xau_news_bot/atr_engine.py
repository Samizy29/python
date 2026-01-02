import pandas as pd
import ta

def get_atr(rates, period=14):
    df = pd.DataFrame(rates)
    atr = ta.volatility.AverageTrueRange(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=period
    )
    return atr.average_true_range().iloc[-1]
