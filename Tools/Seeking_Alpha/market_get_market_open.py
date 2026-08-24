import os
import requests

def market_get_market_open():
    """
    :API_description: Retrieve the current market status, including whether the market is open and the next opening and closing times.
    :param: None
    :response_schema: 
    ```json
{
  "data": {
    "id": "0",
    "type": "marketOpen",
    "attributes": {
      "marketOpen": true,
      "nextMarketOpen": 1779888600,
      "nextMarketClose": 1779825600
    }
  }
}
```
    """
    url = "https://seeking-alpha.p.rapidapi.com/market/get-market-open"
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