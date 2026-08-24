import os
import requests

def stockGetPrice(region, symbol):
    """
    :API_description: Retrieve YAHOO FINANCE real-time stock prices
    :param region: The market region to query(e.g., AR, AU, BR, CA, CN, FR, DE, HK, IN, IT, MX, NZ, SG, KR, ES, TW, GB, US).
    :param symbol: The stock symbol to query(e.g., AAPL).
    :response_schema: 
    ```json
{
  "quoteSummary": {
    "type": "object",
    "description": "Top-level wrapper for quote/price summary data.",
    "properties": {
      "result": {
        "type": "array",
        "description": "Array of quote result objects.",
        "items": {
          "type": "object",
          "properties": {
            "price": {
              "type": "object",
              "description": "Market price and trading metadata for a security.",
              "properties": {
                "maxAge": { "type": "integer" },

                "preMarketChangePercent": {
                  "type": "object",
                  "description": "Pre-market percentage change with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "preMarketChange": {
                  "type": "object",
                  "description": "Pre-market absolute change with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "preMarketTime": { "type": "integer" },
                "preMarketPrice": {
                  "type": "object",
                  "description": "Pre-market price with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "preMarketSource": { "type": "string" },

                "postMarketChangePercent": {
                  "type": "object",
                  "description": "Post-market percentage change with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "postMarketChange": {
                  "type": "object",
                  "description": "Post-market absolute change with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "postMarketTime": { "type": "integer" },
                "postMarketPrice": {
                  "type": "object",
                  "description": "Post-market price with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "postMarketSource": { "type": "string" },

                "regularMarketChangePercent": {
                  "type": "object",
                  "description": "Regular market percentage change with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "regularMarketChange": {
                  "type": "object",
                  "description": "Regular market absolute change with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "regularMarketTime": { "type": "integer" },

                "priceHint": {
                  "type": "object",
                  "description": "Precision hint for displaying price values.",
                  "properties": {
                    "raw": { "type": "integer" },
                    "fmt": { "type": "string" },
                    "longFmt": { "type": "string" }
                  }
                },

                "regularMarketPrice": {
                  "type": "object",
                  "description": "Current regular market price with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "regularMarketDayHigh": {
                  "type": "object",
                  "description": "Highest regular market price of the day.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "regularMarketDayLow": {
                  "type": "object",
                  "description": "Lowest regular market price of the day.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "regularMarketVolume": {
                  "type": "object",
                  "description": "Trading volume during regular market hours.",
                  "properties": {
                    "raw": { "type": "integer" },
                    "fmt": { "type": "string" },
                    "longFmt": { "type": "string" }
                  }
                },

                "averageDailyVolume10Day": {
                  "type": "object",
                  "description": "Average daily volume over the last 10 days; empty object in this sample.",
                  "properties": {}
                },
                "averageDailyVolume3Month": {
                  "type": "object",
                  "description": "Average daily volume over the last 3 months; empty object in this sample.",
                  "properties": {}
                },

                "regularMarketPreviousClose": {
                  "type": "object",
                  "description": "Previous regular market closing price.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },
                "regularMarketSource": { "type": "string" },
                "regularMarketOpen": {
                  "type": "object",
                  "description": "Opening price of the regular market session.",
                  "properties": {
                    "raw": { "type": "number" },
                    "fmt": { "type": "string" }
                  }
                },

                "strikePrice": {
                  "type": "object",
                  "description": "Option strike price; empty object in this equity sample.",
                  "properties": {}
                },
                "openInterest": {
                  "type": "object",
                  "description": "Options open interest; empty object in this sample.",
                  "properties": {}
                },

                "exchange": { "type": "string" },
                "exchangeName": { "type": "string" },
                "exchangeDataDelayedBy": { "type": "integer" },
                "marketState": { "type": "string" },
                "quoteType": { "type": "string" },
                "symbol": { "type": "string" },
                "underlyingSymbol": { "type": ["string", "null"] },
                "shortName": { "type": "string" },
                "longName": { "type": "string" },
                "currency": { "type": "string" },
                "quoteSourceName": { "type": "string" },
                "currencySymbol": { "type": "string" },
                "fromCurrency": { "type": ["string", "null"] },
                "toCurrency": { "type": ["string", "null"] },
                "lastMarket": { "type": ["string", "null"] },

                "volume24Hr": {
                  "type": "object",
                  "description": "24-hour volume; empty object in this sample.",
                  "properties": {}
                },
                "volumeAllCurrencies": {
                  "type": "object",
                  "description": "Volume across all currencies; empty object in this sample.",
                  "properties": {}
                },
                "circulatingSupply": {
                  "type": "object",
                  "description": "Circulating supply; empty object in this sample.",
                  "properties": {}
                },

                "marketCap": {
                  "type": "object",
                  "description": "Market capitalization with raw and formatted values.",
                  "properties": {
                    "raw": { "type": "integer" },
                    "fmt": { "type": "string" },
                    "longFmt": { "type": "string" }
                  }
                }
              }
            }
          }
        }
      },
      "error": { "type": ["null", "string", "object"] }
    }
  }
}
    ```
    """
    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-price"
    rapid_api_key = os.getenv("RAPID_API_KEY")
    querystring = {"region": region, "symbol": symbol}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")