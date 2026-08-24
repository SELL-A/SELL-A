import os
import requests

def multi_convert(from_currency, amount, to_currencies):
    """
    :API_description: Converts a specified amount from one currency to multiple target currencies, providing detailed conversion rates and amounts for each target currency.
    :param from_currency: The currency code to convert from (e.g., 'EUR').
    :param amount: The amount of the currency to convert.
    :param to_currencies: A comma-separated string of currency codes to convert to (e.g., 'GBP,USD,EUR').
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
      "description": "The code of the base currency used for the conversion."
    },
    "base_currency_name": {
      "type": "string",
      "description": "The name of the base currency used for the conversion."
    },
    "to": {
      "type": "string",
      "description": "Comma-separated list of currency codes to which the conversion is applied."
    },
    "amount": {
      "type": "number",
      "description": "The amount of the base currency to be converted."
    },
    "rates": {
      "type": "object",
      "description": "Object containing the conversion rates and converted amounts for each target currency.",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "currency_name": {
            "type": "string",
            "description": "The name of the target currency."
          },
          "currency_code": {
            "type": "string",
            "description": "The code of the target currency."
          },
          "rate": {
            "type": "number",
            "description": "The conversion rate from the base currency to the target currency."
          },
          "converted_amount": {
            "type": "number",
            "description": "The converted amount in the target currency."
          }
        },
        "required": ["currency_name", "currency_code", "rate", "converted_amount"]
      }
    }
  },
  "required": ["success", "errors", "base_currency_code", "base_currency_name", "to", "amount", "rates"]
}
```
    """
    url = "https://forex-apised1.p.rapidapi.com/multi-convert"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"from": from_currency, "amount": amount, "to": to_currencies}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "forex-apised1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

