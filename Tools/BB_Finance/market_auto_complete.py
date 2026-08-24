import os
import requests

def market_auto_complete(query):
    """
    :API_description: Provides auto-complete suggestions for securities related to Apple Inc., including stock details, exchange information, and recent news.
    :param query: The search term for which auto-complete suggestions are needed.
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "quote": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "securityType": { "type": "string" },
              "symbol": { "type": "string" },
              "exchange": { "type": "string" },
              "country": { "type": "string" },
              "currency": { "type": "string" },
              "resourceType": { "type": "string" },
              "fundamentalDataCurrency": { "type": "string" },
              "resourceSubtype": { "type": "string" },
              "region": { "type": "string" },
              "ticker": { "type": "string" },
              "tickerName": { "type": "string" },
              "template": { "type": "string" },
              "tinyName": { "type": "string" },
              "name": { "type": "string" },
              "watchlist": { "type": "boolean" },
              "resourceId": { "type": "string" },
              "id": { "type": "string" },
              "title": { "type": "string" },
              "card": { "type": "string" }
            },
            "required": [
              "securityType",
              "symbol",
              "country",
              "currency",
              "resourceType",
              "fundamentalDataCurrency",
              "resourceSubtype",
              "region",
              "ticker",
              "tickerName",
              "template",
              "tinyName",
              "name",
              "watchlist",
              "resourceId",
              "id",
              "title",
              "card"
            ]
          }
        },
        "news": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": { "type": "string" },
              "id": { "type": "string" },
              "card": { "type": "string" },
              "date": { "type": "integer" },
              "longURL": { "type": "string" },
              "thumbnailImage": { "type": ["string", "null"] }
            },
            "required": ["title", "id", "card", "date", "longURL"]
          }
        }
      },
      "required": ["quote", "news"]
    }
    ```
    """
    url = "https://bb-finance.p.rapidapi.com/market/auto-complete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "bb-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")