import os
import requests

def stockGetChart(region, interval, range, symbol):
    """
    :API_description: Retrieve YAHOO FINANCE stock Chart
    :param region: The market region to query(e.g., AR, AU, BR, CA, CN, FR, DE, HK, IN, IT, MX, NZ, SG, KR, ES, TW, GB, US).
    :param interval: The chart interval(e.g., 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo).
    :param range: The time range for the chart(e.g., 1d, 1wk, 1mo, 5m, 15m).
    :param symbol: The stock symbol(e.g., AAPL).
    :response_schema: 
    ```json
{
  "chart": {
    "result": [
      {
        "meta": {
          "currency": "USD",
          "symbol": "AAPL",
          "exchangeName": "NMS",
          "fullExchangeName": "NasdaqGS",
          "instrumentType": "EQUITY",
          "firstTradeDate": 345479400,
          "regularMarketTime": 1781535106,
          "hasPrePostMarketData": true,
          "gmtoffset": -14400,
          "timezone": "EDT",
          "exchangeTimezoneName": "America/New_York",
          "regularMarketPrice": 296.61,
          "fiftyTwoWeekHigh": 317.4,
          "fiftyTwoWeekLow": 195.07,
          "regularMarketDayHigh": 296.7,
          "regularMarketDayLow": 291.7,
          "regularMarketVolume": 11308571,
          "longName": "Apple Inc.",
          "shortName": "Apple Inc.",
          "chartPreviousClose": 291.13,
          "previousClose": 291.13,
          "scale": 3,
          "priceHint": 2,
          "currentTradingPeriod": {
            "pre": {
              "timezone": "EDT",
              "start": 1781510400,
              "end": 1781530200,
              "gmtoffset": -14400
            },
            "regular": {
              "timezone": "EDT",
              "start": 1781530200,
              "end": 1781553600,
              "gmtoffset": -14400
            },
            "post": {
              "timezone": "EDT",
              "start": 1781553600,
              "end": 1781568000,
              "gmtoffset": -14400
            }
          },
          "tradingPeriods": {
            "pre": [
              [
                {
                  "timezone": "EDT",
                  "start": 1781510400,
                  "end": 1781530200,
                  "gmtoffset": -14400
                }
              ]
            ],
            "post": [
              [
                {
                  "timezone": "EDT",
                  "start": 1781553600,
                  "end": 1781568000,
                  "gmtoffset": -14400
                }
              ]
            ],
            "regular": [
              [
                {
                  "timezone": "EDT",
                  "start": 1781530200,
                  "end": 1781553600,
                  "gmtoffset": -14400
                }
              ]
            ]
          },
          "dataGranularity": "5m",
          "range": "1d",
          "validRanges": [
            "1d",
            "5d",
            "1mo",
            "3mo",
            "6mo",
            "1y",
            "2y",
            "5y",
            "10y",
            "ytd",
            "max"
          ]
        },
        "timestamp": [
          1781510400,
          1781510700,
          1781511000,
          1781511300,
          1781535106
        ],
        "indicators": {
          "quote": [
            {
              "open": [
                293.86,
                293.6042,
                293.38,
                296.5350036621094,
                296.6099853515625
              ],
              "high": [
                294.36,
                294.11,
                293.6,
                293.5988,
                293.4232,
                296.6099853515625
              ],
              "close": [
                293.6499,
                293.38,
                296.6099853515625
              ],
              "low": [
                292,
                292,
                293.33,
                296.6099853515625
              ],
              "volume": [
                0,
                0,
                63862,
                0
              ]
            }
          ]
        }
      }
    ],
    "error": null
  }
}
```
    """
    rapid_api_key = os.getenv('RAPID_API_KEY')
    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-chart"
    querystring = {"region": region, "interval": interval, "range": range, "symbol": symbol}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")