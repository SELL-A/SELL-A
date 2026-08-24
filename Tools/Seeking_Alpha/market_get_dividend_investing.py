import os
import requests

def market_get_dividend_investing():
    """
    :API_description: Retrieve detailed information on dividend-paying stocks, including trending stocks, recent dividend increases, and upcoming ex-dividend dates.
    :param: None
    :response_schema: 
    ```json
{
  "data": {
    "id": "0",
    "type": "dividend_investing",
    "attributes": {
      "trending_dividend_stocks": [
        {
          "slug": "IBM",
          "name": "International Business Machines Corporation",
          "div_yield_fwd": 2.6630948,
          "news_count": 10
        },
        {
          "slug": "PFE",
          "name": "Pfizer Inc.",
          "div_yield_fwd": 6.640927,
          "news_count": 6
        },
        {
          "slug": "XOM",
          "name": "Exxon Mobil Corporation",
          "div_yield_fwd": 2.6594372,
          "news_count": 7
        },
        {
          "slug": "O",
          "name": "Realty Income Corporation",
          "div_yield_fwd": 5.2337956,
          "news_count": 2
        },
        {
          "slug": "UNH",
          "name": "UnitedHealth Group Incorporated",
          "div_yield_fwd": 2.275594,
          "news_count": 2
        },
        {
          "slug": "NEE",
          "name": "NextEra Energy, Inc.",
          "div_yield_fwd": 2.8151326,
          "news_count": 5
        },
        {
          "slug": "OWL",
          "name": "Blue Owl Capital Inc.",
          "div_yield_fwd": 9.145129,
          "news_count": 1
        },
        {
          "slug": "CVX",
          "name": "Chevron Corporation",
          "div_yield_fwd": 3.7193751,
          "news_count": 2
        },
        {
          "slug": "VZ",
          "name": "Verizon Communications Inc.",
          "div_yield_fwd": 5.853154,
          "news_count": 1
        },
        {
          "slug": "ET",
          "name": "Energy Transfer LP Common Units",
          "div_yield_fwd": 6.7264576,
          "news_count": 2
        }
      ],
      "dividend_increases": [
        {
          "slug": "ARCC",
          "name": "Ares Capital"
        },
        {
          "slug": "CALM",
          "name": "Cal-Maine Foods, Inc."
        },
        {
          "slug": "HPQ",
          "name": "HP Inc."
        },
        {
          "slug": "BX",
          "name": "Blackstone Inc."
        },
        {
          "slug": "HBAN",
          "name": "Huntington Bancshares Incorporated"
        },
        {
          "slug": "DVY",
          "name": "iShares Select Dividend ETF"
        },
        {
          "slug": "HDV",
          "name": "iShares Core High Dividend ETF"
        },
        {
          "slug": "EQH",
          "name": "Equitable Holdings, Inc."
        },
        {
          "slug": "DGRO",
          "name": "iShares Core Dividend Growth ETF"
        },
        {
          "slug": "DGRW",
          "name": "WisdomTree US Quality Dividend Growth Fund ETF"
        }
      ],
      "upcoming_exdates": [
        {
          "slug": "MLCI",
          "name": "Mount Logan Capital Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "JCAP",
          "name": "Jefferson Capital, Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "CLPR",
          "name": "Clipper Realty Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "IVR",
          "name": "Invesco Mortgage Capital Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "NKSH",
          "name": "National Bankshares, Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "OMAB",
          "name": "Grupo Aeroportuario del Centro Norte, S.A.B. de C.V.",
          "date": "2026-05-26"
        },
        {
          "slug": "PRU",
          "name": "Prudential Financial, Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "SPOK",
          "name": "Spok Holdings, Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "SBGI",
          "name": "Sinclair, Inc.",
          "date": "2026-05-26"
        },
        {
          "slug": "SWKS",
          "name": "Skyworks Solutions, Inc.",
          "date": "2026-05-26"
        }
      ]
    }
  }
}
```
    """
    url = "https://seeking-alpha.p.rapidapi.com/market/get-dividend-investing"
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