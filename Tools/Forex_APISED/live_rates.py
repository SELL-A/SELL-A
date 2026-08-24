import os
import requests

def live_rates(base_currency_code: str, currency_codes: str):
    """
    :API_description: Retrieves live exchange rates relative to a specified base currency (USD by default), providing detailed rates for various currencies.
    :param base_currency_code: The base currency code (e.g., "USD").
    :param currency_codes: A comma-separated list of target currency codes (e.g., "GBP,USD,EUR").
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
    "base_currency_code": {
      "type": "string",
      "description": "The code of the base currency used for the exchange rates."
    },
    "base_currency_name": {
      "type": "string",
      "description": "The name of the base currency used for the exchange rates."
    },
    "currency_codes": {
      "type": "string",
      "description": "Comma-separated list of currency codes available in the response."
    },
    "rates": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "currency_name": {
            "type": "string",
            "description": "The name of the currency."
          },
          "currency_code": {
            "type": "string",
            "description": "The code of the currency."
          },
          "rate": {
            "type": "number",
            "description": "The exchange rate of the currency relative to the base currency."
          }
        },
        "required": ["currency_name", "currency_code", "rate"]
      },
      "description": "Object containing exchange rates for various currencies."
    }
  },
  "required": ["success", "errors", "base_currency_code", "base_currency_name", "currency_codes", "rates"]
}
```
    """
    url = "https://forex-apised1.p.rapidapi.com/live-rates"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"base_currency_code": base_currency_code, "currency_codes": currency_codes}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "forex-apised1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

