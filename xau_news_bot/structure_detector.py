def detect_direction(candle):
    body = candle["close"] - candle["open"]
    range_ = candle["high"] - candle["low"]

    if abs(body) < range_ * 0.5:
        return None

    return "buy" if body > 0 else "sell"
