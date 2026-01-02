import requests
import datetime

API_KEY = "YOUR_API_KEY_HERE"

HIGH_IMPACT = ["Non-Farm Employment Change", "CPI", "Fed Interest Rate Decision"]

def high_impact_news_now():
    today = datetime.date.today().isoformat()
    url = f"https://financialmodelingprep.com/api/v3/economic_calendar?from={today}&to={today}&apikey={API_KEY}"
    
    data = requests.get(url).json()
    now = datetime.datetime.utcnow()

    for event in data:
        if any(k in event["event"] for k in HIGH_IMPACT):
            event_time = datetime.datetime.fromisoformat(event["date"])
            if abs((event_time - now).total_seconds()) < 900:
                return True
    return False
