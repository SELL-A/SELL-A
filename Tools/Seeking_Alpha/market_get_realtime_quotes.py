import os
import requests

def market_get_realtime_quotes(sa_ids):
    """
    :API_description: Retrieve real-time stock quotes with detailed trading metrics and extended market data for specified tickers.
    :param sa_ids: A comma-separated string of stock IDs for which real-time quotes are requested The value of 'id' field returned in .../v2/auto-complete endpoint. This endpoint helps to query for real time quotes. Separating by comma to query multiple IDs at once. Ex : 612888,16123.
    :response_schema: 
    ```json
{
  "real_time_quotes": [
    {
      "ticker_id": 612888,
      "sa_id": 612888,
      "sa_slug": "euda",
      "symbol": "EUDA",
      "high": 18.03,
      "low": 17.1,
      "open": 17.71,
      "prev_close": 17.36,
      "last": 17.64,
      "volume": 7711.594664,
      "last_time": "2026-05-26T12:02:51.000-04:00",
      "info": "Delayed",
      "src": "XigniteQuotePuller",
      "updated_at": "2026-05-26T13:18:30.730-04:00"
    },
    {
      "ticker_id": 16123,
      "sa_id": 16123,
      "sa_slug": "tsla",
      "symbol": "TSLA",
      "high": 434.56,
      "low": 426.13,
      "open": 430.15,
      "prev_close": 426.01,
      "last": 431.97,
      "volume": 27741378.481827,
      "last_time": "2026-05-26T13:18:15.000-04:00",
      "info": "Realtime",
      "src": "XigniteQuotePuller",
      "updated_at": "2026-05-26T13:18:30.676-04:00"
    }
  ]
}
```
    """
    url = "https://seeking-alpha.p.rapidapi.com/market/get-realtime-quotes"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"sa_ids": sa_ids}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
