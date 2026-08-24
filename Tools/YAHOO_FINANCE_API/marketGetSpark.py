import os
import requests

def marketGetSpark(interval, range, symbols):
    """
    :API_description: Retrieve YAHOO FINANCE market Spark
    :param interval: The interval for the spark chart data String(e.g., "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo").
    :param range: The time range for the spark chart data String(e.g., "1d", "1w", "1m").
    :param symbols: The stock symbols to query String(e.g., "PLTR", "AAPL","BRZE","IOT","AVGO").
    :response_schema: 
    ```json
{
  "AVGO": {
    "timestamp": [
      1781530200,
      1781530500,
      1781530800,
      1781531100,
      1781531425
    ],
    "end": 1781553600,
    "symbol": "AVGO",
    "dataGranularity": 300,
    "close": [
      393.65,
      392.06,
      393.11,
      393.55,
      393.92
    ],
    "previousClose": 382.07,
    "chartPreviousClose": 382.07,
    "start": 1781530200
  },
  "BRZE": {
    "timestamp": [
      1781530200,
      1781530500,
      1781530800,
      1781531100,
      1781531423
    ],
    "end": 1781553600,
    "symbol": "BRZE",
    "dataGranularity": 300,
    "close": [
      21.885,
      22.265,
      22.083,
      22.07,
      22.04
    ],
    "previousClose": 21.66,
    "chartPreviousClose": 21.66,
    "start": 1781530200
  },
  "IOT": {
    "timestamp": [
      1781530200,
      1781530500,
      1781530800,
      1781531100,
      1781531420
    ],
    "end": 1781553600,
    "symbol": "IOT",
    "dataGranularity": 300,
    "close": [
      33.96,
      34.21,
      34.338,
      34.055,
      34.005
    ],
    "previousClose": 33.67,
    "chartPreviousClose": 33.67,
    "start": 1781530200
  },
  "PLTR": {
    "timestamp": [
      1781530200,
      1781530500,
      1781530800,
      1781531100,
      1781531425
    ],
    "end": 1781553600,
    "symbol": "PLTR",
    "dataGranularity": 300,
    "close": [
      131.4,
      131.52,
      131.13,
      130.51,
      130.27
    ],
    "previousClose": 127.99,
    "chartPreviousClose": 127.99,
    "start": 1781530200
  }
}
```
    """
    url = "https://yahoo-finance166.p.rapidapi.com/api/market/get-spark"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"interval": interval, "range": range, "symbols": symbols}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == '__main__':
    interval = "5m"
    range = "1d"
    symbols = "AAPL"
    spark_data = marketGetSpark(interval, range, symbols)
    print(spark_data)