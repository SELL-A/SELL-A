import os
import requests

def market_get_equity(filterCategory):
    """
    :API_description: Retrieve metadata for various financial instruments, including unique identifiers, types, and attributes.
    :param filterCategory: The category used to filter the equity data, e.g., "global-equity" One of the following : us-equity-markets|us-equity-sectors|us-equity-factors|global-equity|countries-equity.
    :response_schema: 
    ```json
{
  "data": [
    {
      "id": "11748",
      "type": "tag",
      "attributes": {
        "slug": "vt",
        "name": "VT",
        "company": "Vanguard Total World Stock Index Fund ETF",
        "tagKind": "Tags::Ticker",
        "alias_name": "World Index",
        "div_yield_fwd": null,
        "sector": null,
        "position": 10
      },
      "links": {
        "self": "/symbol/VT"
      }
    },
    {
      "id": "17410",
      "type": "tag",
      "attributes": {
        "slug": "vxus",
        "name": "VXUS",
        "company": "Vanguard Total International Stock Index Fund ETF",
        "tagKind": "Tags::Ticker",
        "alias_name": "World Ex-US",
        "div_yield_fwd": null,
        "sector": null,
        "position": 20
      },
      "links": {
        "self": "/symbol/VXUS"
      }
    },
    {
      "id": "379",
      "type": "tag",
      "attributes": {
        "slug": "vwo",
        "name": "VWO",
        "company": "Vanguard Emerging Markets Stock Index Fund ETF",
        "tagKind": "Tags::Ticker",
        "alias_name": "Emerging Markets",
        "div_yield_fwd": null,
        "sector": null,
        "position": 30
      },
      "links": {
        "self": "/symbol/VWO"
      }
    },
    {
      "id": "7838",
      "type": "tag",
      "attributes": {
        "slug": "vea",
        "name": "VEA",
        "company": "Vanguard Developed Markets Index Fund ETF",
        "tagKind": "Tags::Ticker",
        "alias_name": "Developed Markets",
        "div_yield_fwd": null,
        "sector": null,
        "position": 40
      },
      "links": {
        "self": "/symbol/VEA"
      }
    },
    {
      "id": "377",
      "type": "tag",
      "attributes": {
        "slug": "vgk",
        "name": "VGK",
        "company": "Vanguard European Stock Index Fund ETF",
        "tagKind": "Tags::Ticker",
        "alias_name": "Europe",
        "div_yield_fwd": null,
        "sector": null,
        "position": 50
      },
      "links": {
        "self": "/symbol/VGK"
      }
    }
  ]
}
```
    """
    url = "https://seeking-alpha.p.rapidapi.com/market/get-equity"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"filterCategory": filterCategory}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")