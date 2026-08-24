import os
import requests

def v1_market_data(symbols, base="USD"):
    """
    :API_description: Retrieves real-time or historical pricing data for various commodities in USD, including opening, highest, lowest, previous, and current prices.
    :param symbols: A comma-separated string of commodity symbols (e.g., "COCOA,COFFEE,CORN").
    :param base: The base currency for the price data (default "USD").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates whether the API request was successful."
    },
    "errors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of error messages, if any, returned by the API."
    },
    "base_currency": {
      "type": "string",
      "description": "The base currency used for the rates in the response."
    },
    "rates": {
      "type": "object",
      "description": "Contains the rates for various commodities.",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "open": {
            "type": "number",
            "description": "The opening price of the commodity."
          },
          "high": {
            "type": "number",
            "description": "The highest price of the commodity during the period."
          },
          "low": {
            "type": "number",
            "description": "The lowest price of the commodity during the period."
          },
          "prev": {
            "type": "number",
            "description": "The previous closing price of the commodity."
          },
          "current": {
            "type": "number",
            "description": "The current price of the commodity."
          }
        },
        "required": ["open", "high", "low", "prev", "current"]
      }
    }
  },
  "required": ["success", "errors", "base_currency", "rates"]
}
    ```
    """
    url = "https://commodities-apised.p.rapidapi.com/v1/market-data"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"symbols": symbols, "base": base}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "commodities-apised.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")