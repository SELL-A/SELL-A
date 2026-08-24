import os
import requests

def market_get_day_watch():
    """
    :API_description: Retrieve a comprehensive overview of market metrics, including top gainers, losers, and active stocks across various indices.
    :param: None
    :response_schema: 
    ```json
{
  "data": {
    "id": "0",
    "type": "day_watch",
    "attributes": {
      "top_gainers": [
        {
          "id": 602728,
          "slug": "TE",
          "name": "T1 Energy Inc."
        },
        {
          "id": 612651,
          "slug": "RDW",
          "name": "Redwire Corporation"
        },
        {
          "id": 568975,
          "slug": "ATOM",
          "name": "Atomera Incorporated"
        },
        {
          "id": 639528,
          "slug": "ASPI",
          "name": "ASP Isotopes Inc."
        },
        {
          "id": 614037,
          "slug": "SIDU",
          "name": "Sidus Space, Inc."
        }
      ],
      "top_losers": [
        {
          "id": 462295,
          "slug": "CRBP",
          "name": "Corbus Pharmaceuticals Holdings, Inc."
        },
        {
          "id": 598900,
          "slug": "SY",
          "name": "So-Young International Inc."
        }
      ],
      "cryptocurrencies": [
        {
          "id": 581328,
          "slug": "BTC-USD",
          "name": "Bitcoin USD"
        },
        {
          "id": 579496,
          "slug": "ETH-USD",
          "name": "Ethereum USD"
        },
        {
          "id": 580755,
          "slug": "BNB-USD",
          "name": "Binance Coin USD"
        }
      ],
      "most_active": [
        {
          "id": 1025,
          "slug": "NOK",
          "name": "Nokia Oyj"
        },
        {
          "id": 1150,
          "slug": "NVDA",
          "name": "NVIDIA Corporation"
        }
      ],
      "in_the_news": [
        {
          "id": 792938,
          "slug": "mrosy",
          "name": "MELROSE INDS PLC ADR"
        },
        {
          "id": 539,
          "slug": "ibm",
          "name": "International Business Machines Corporation"
        },
        {
          "id": 3213,
          "slug": "hon",
          "name": "Honeywell International Inc."
        },
        {
          "id": 608967,
          "slug": "rgti",
          "name": "Rigetti Computing, Inc."
        },
        {
          "id": 789023,
          "slug": "infq",
          "name": "Infleqtion, Inc."
        }
      ],
      "faang_stocks": [
        {
          "id": 36222,
          "slug": "META",
          "name": "Meta Platforms, Inc."
        },
        {
          "id": 562,
          "slug": "AMZN",
          "name": "Amazon.com, Inc."
        },
        {
          "id": 146,
          "slug": "AAPL",
          "name": "Apple Inc."
        },
        {
          "id": 575,
          "slug": "MSFT",
          "name": "Microsoft Corporation"
        },
        {
          "id": 544,
          "slug": "GOOG",
          "name": "Alphabet Inc."
        }
      ],
      "sp500_gainers": [
        {
          "id": 1309,
          "slug": "MU",
          "name": "Micron Technology, Inc."
        },
        {
          "id": 1064,
          "slug": "WDC",
          "name": "Western Digital Corporation"
        }
      ],
      "sp500_losers": [
        {
          "id": 1364,
          "slug": "AZO",
          "name": "AutoZone, Inc."
        },
        {
          "id": 8656,
          "slug": "TSCO",
          "name": "Tractor Supply Company"
        },
        {
          "id": 2186,
          "slug": "INTU",
          "name": "Intuit Inc."
        }
      ],
      "cap400_gainers": [
        {
          "id": 9988,
          "slug": "VICR",
          "name": "Vicor Corporation"
        },
        {
          "id": 1986,
          "slug": "AMKR",
          "name": "Amkor Technology, Inc."
        },
        {
          "id": 606246,
          "slug": "ALGM",
          "name": "Allegro MicroSystems, Inc."
        }
      ],
      "cap400_losers": [
        {
          "id": 605263,
          "slug": "VAL",
          "name": "Valaris Limited"
        },
        {
          "id": 35103,
          "slug": "MTDR",
          "name": "Matador Resources Company"
        },
        {
          "id": 16117,
          "slug": "FN",
          "name": "Fabrinet"
        }
      ],
      "cap600_gainers": [
        {
          "id": 2054,
          "slug": "POWI",
          "name": "Power Integrations, Inc."
        },
        {
          "id": 494396,
          "slug": "SEDG",
          "name": "SolarEdge Technologies, Inc."
        },
        {
          "id": 576795,
          "slug": "ACMR",
          "name": "ACM Research, Inc."
        }
      ],
      "cap600_losers": [
        {
          "id": 581877,
          "slug": "TALO",
          "name": "Talos Energy Inc."
        },
        {
          "id": 519725,
          "slug": "GKOS",
          "name": "Glaukos Corporation"
        }
      ]
    }
  }
}
```
    """
    url = "https://seeking-alpha.p.rapidapi.com/market/get-day-watch"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")



