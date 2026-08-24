import os
import requests

def v1_latest(base, symbols):
    """
    :API_description: Retrieve the latest exchange rates for various commodities in the specified base currency.
    :param base: The base currency (e.g., "USD").
    :param symbols: A comma-separated string of commodity symbols (e.g., "COCOA,COFFEE").
    :response_schema:
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
      "description": "The base currency used for the exchange rates, typically 'USD'."
    },
    "rates": {
      "type": "object",
      "properties": {
        "COCOA": {
          "type": "number",
          "description": "Exchange rate for COCOA."
        },
        "COFFEE": {
          "type": "number",
          "description": "Exchange rate for COFFEE."
        },
        "CORN": {
          "type": "number",
          "description": "Exchange rate for CORN."
        },
        "COTTON": {
          "type": "number",
          "description": "Exchange rate for COTTON."
        },
        "GASOLINE": {
          "type": "number",
          "description": "Exchange rate for GASOLINE."
        },
        "LUMBER": {
          "type": "number",
          "description": "Exchange rate for LUMBER."
        },
        "NATURALGAS": {
          "type": "number",
          "description": "Exchange rate for NATURALGAS."
        },
        "OATS": {
          "type": "number",
          "description": "Exchange rate for OATS."
        },
        "OIL": {
          "type": "number",
          "description": "Exchange rate for OIL."
        },
        "ORANGEJUICE": {
          "type": "number",
          "description": "Exchange rate for ORANGEJUICE."
        },
        "SOYBEAN": {
          "type": "number",
          "description": "Exchange rate for SOYBEAN."
        },
        "SUGAR": {
          "type": "number",
          "description": "Exchange rate for SUGAR."
        },
        "WHEAT": {
          "type": "number",
          "description": "Exchange rate for WHEAT."
        }
      },
      "description": "Object containing exchange rates for various commodities."
    }
  },
  "required": ["success", "errors", "base_currency", "rates"]
}
    """
    url = "https://commodities-apised.p.rapidapi.com/v1/latest"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"base": base, "symbols": symbols}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "commodities-apised.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")