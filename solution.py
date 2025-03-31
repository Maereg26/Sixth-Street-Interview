import requests

def lookup(symbol, date, apikey):  # Corrected parameter name
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": apikey,  # Corrected parameter name
    }

    r = requests.get('https://www.alphavantage.co/query', params=parameters)
    data = r.json()

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

def minimum_price(symbol, n, apikey):  # Corrected parameter name
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": apikey,  # Corrected parameter name
    }

    r = requests.get('https://www.alphavantage.co/query', params=parameters)
    data = r.json()

    try:
        time_series = data["Time Series (Daily)"]
        dates = list(time_series.keys())[:n]
        prices = [float(time_series[date]["3. low"]) for date in dates]  # Corrected data access
        return min(prices)
    except KeyError:
        raise ValueError("Insufficient data provided.")


def maximum_price(symbol, n, apikey):  # Corrected parameter name, symbol
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": apikey,  # Corrected parameter name
    }

    r = requests.get('https://www.alphavantage.co/query', params=parameters)
    data = r.json()

    try:
        time_series = data["Time Series (Daily)"]
        dates = list(time_series.keys())[:n]
        prices = [float(time_series[date]["2. high"]) for date in dates]
        return max(prices)

    except KeyError:
        raise ValueError("Insufficient data provided.")
