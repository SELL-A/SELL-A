import os
import requests

def get_stock_recommendations(symbol):
    """
    :API_description: Retrieves real-time stock market data for specified companies, including current prices, price changes, trading volumes, and exchange details from Nasdaq.
    :param symbol: The stock ticker symbol (e.g., 'AAPL').
    :response_schema: 
    ```json
{
  "finance": {
    "result": [
      {
        "count": 2,
        "quotes": [
          {
            "language": "en-US",
            "region": "US",
            "quoteType": "EQUITY",
            "typeDisp": "Equity",
            "quoteSourceName": "Nasdaq Real Time Price",
            "triggerable": true,
            "customPriceAlertConfidence": "HIGH",
            "sourceInterval": 15,
            "exchangeDataDelayedBy": 0,
            "exchangeTimezoneName": "America/New_York",
            "exchangeTimezoneShortName": "EDT",
            "gmtOffSetMilliseconds": -14400000,
            "esgPopulated": false,
            "tradeable": false,
            "cryptoTradeable": false,
            "hasPrePostMarketData": true,
            "firstTradeDateMilliseconds": 863703000000,
            "priceHint": 2,
            "postMarketChangePercent": -0.34545413,
            "postMarketTime": 1779494399,
            "postMarketPrice": 265.4,
            "postMarketChange": -0.9200134,
            "regularMarketChange": -2.1400146,
            "regularMarketChangePercent": -0.7971446,
            "regularMarketTime": 1779480001,
            "regularMarketPrice": 266.32,
            "regularMarketPreviousClose": 268.46002,
            "exchange": "NMS",
            "market": "us_market",
            "fullExchangeName": "NasdaqGS",
            "shortName": "Amazon.com, Inc.",
            "marketState": "CLOSED",
            "symbol": "AMZN"
          },
          {
            "language": "en-US",
            "region": "US",
            "quoteType": "EQUITY",
            "typeDisp": "Equity",
            "quoteSourceName": "Nasdaq Real Time Price",
            "triggerable": true,
            "customPriceAlertConfidence": "HIGH",
            "sourceInterval": 15,
            "exchangeDataDelayedBy": 0,
            "exchangeTimezoneName": "America/New_York",
            "exchangeTimezoneShortName": "EDT",
            "gmtOffSetMilliseconds": -14400000,
            "esgPopulated": false,
            "tradeable": false,
            "cryptoTradeable": false,
            "hasPrePostMarketData": true,
            "firstTradeDateMilliseconds": 1277818200000,
            "priceHint": 2,
            "postMarketChangePercent": -0.5469395,
            "postMarketTime": 1779494399,
            "postMarketPrice": 423.68,
            "postMarketChange": -2.330017,
            "regularMarketChange": 8.160004,
            "regularMarketChangePercent": 1.9528548,
            "regularMarketTime": 1779480000,
            "regularMarketPrice": 426.01,
            "regularMarketPreviousClose": 417.85,
            "exchange": "NMS",
            "market": "us_market",
            "fullExchangeName": "NasdaqGS",
            "shortName": "Tesla, Inc.",
            "marketState": "CLOSED",
            "symbol": "TSLA"
          }
        ]
      }
    ],
    "error": null
  }
}
```
    """
    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-recommendation-by-symbol"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"symbol": symbol}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")