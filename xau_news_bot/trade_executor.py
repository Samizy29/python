import MetaTrader5 as mt5

def execute_trade(symbol, lot, direction, sl, tp):
    tick = mt5.symbol_info_tick(symbol)
    price = tick.ask if direction == "buy" else tick.bid
    order_type = mt5.ORDER_TYPE_BUY if direction == "buy" else mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 50,
        "magic": 202601,
        "comment": "XAU Prop System",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC
    }
    return mt5.order_send(request)
