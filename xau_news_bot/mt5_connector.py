import MetaTrader5 as mt5

def connect():
    if not mt5.initialize():
        raise RuntimeError("MT5 failed to initialize")

def account_info():
    acc = mt5.account_info()
    return acc.balance, acc.equity

def get_rates(symbol, timeframe, bars=100):
    return mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
