import datetime

daily_loss = 0
trade_count = 0
today = datetime.date.today()

def reset():
    global daily_loss, trade_count, today
    if datetime.date.today() != today:
        daily_loss = 0
        trade_count = 0
        today = datetime.date.today()

def can_trade(balance, equity):
    reset()
    if daily_loss >= balance * 0.02:
        return False
    if (balance - equity) >= balance * 0.08:
        return False
    if trade_count >= 2:
        return False
    return True

def record_trade(loss=0):
    global daily_loss, trade_count
    daily_loss += loss
    trade_count += 1
