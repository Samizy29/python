import MetaTrader5 as mt5
from mt5_connector import connect, account_info, get_rates
from atr_engine import get_atr
from risk_engine import calculate_lot
from structure_detector import detect_direction
from trade_executor import execute_trade
from safety_guard import can_trade, record_trade
from news_calendar import high_impact_news_now

SYMBOL = "XAUUSD"
RISK = 0.01
ATR_MULTIPLIER = 1.5

def run():
    connect()
    balance, equity = account_info()

    if not can_trade(balance, equity):
        print("Trading blocked by prop rules")
        return

    if not high_impact_news_now():
        print("No valid news event")
        return

    rates = get_rates(SYMBOL, mt5.TIMEFRAME_M5, 50)
    atr = get_atr(rates)

    last = rates[-1]
    direction = detect_direction(last)
    if not direction:
        return

    entry = last["close"]
    sl_distance = atr * ATR_MULTIPLIER
    sl = entry - sl_distance if direction == "buy" else entry + sl_distance
    tp = entry + sl_distance * 2 if direction == "buy" else entry - sl_distance * 2

    lot = calculate_lot(balance, RISK, sl_distance)

    execute_trade(SYMBOL, lot, direction, sl, tp)
    record_trade()

    print(f"{direction.upper()} trade executed")

if __name__ == "__main__":
    run()
