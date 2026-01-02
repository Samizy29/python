def calculate_lot(balance, risk_percent, sl_dollars):
    risk_amount = balance * risk_percent
    lot = risk_amount / sl_dollars
    return round(lot, 2)
