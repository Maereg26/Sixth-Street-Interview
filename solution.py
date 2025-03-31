import requests

link = 'https://www.alphavantage.co/documentation/#daily'
r = requests.get(link)
data = r.json()

API_key = "HEKMRH828HI04N23"
def lookup(symbol, date, API_key):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "API_key": API_key,
    }

    if "Error Message" in data:
        raise ValueError("Invalid API call. Check the symbol and API key.")
    
    meta_data = data.get("Meta Data", {})
    time_series = data.get("Time Series (Daily)", {})

    if not time_series:
        raise ValueError("No time series data found for the symbol.")
    
    if date not in time_series:
        raise ValueError("Data not available for the given date.")
    
    daily_data = time_series[date]

    response_format = {
        "Meta Data": meta_data,
        "Time Series (Daily)": {
            date: {
                "1. open": daily_data["1. open"],
                "2. high": daily_data["2. high"],
                "3. low": daily_data["3. low"],
                "4. close": daily_data["4. close"],
                "5. volume": daily_data["5. volume"],

            }
        }
    }

    return response_format

def minimum_price(symbol, n, API_key):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "API_key": API_key,
    }

    try:
        time_series = data["Time Series (Daily)"]
        dates = list(time_series.keys())[:n]
        prices = [float(time_series[data]["3. low"]) for date in dates]
        return min(prices)
    except KeyError:
        raise ValueError("Insufficient data provided.")
