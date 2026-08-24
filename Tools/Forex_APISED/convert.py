import os
import requests

def convert(amount, from_currency, to_currency):
    """
    :API_description: Converts a specified amount from one currency to another, returning the conversion rate and the converted amount.
    :param amount: The amount to be converted (string).
    :param from_currency: The currency code to convert from (string).
    :param to_currency: The currency code to convert to (string).
    Should be one of the following values: USD,ALL,DZD,AOA,ARS,AMD,AWG,AUD,AZN,BSD
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
            "description": "The target currency code to which the base currency is converted."
        },
        "amount": {
            "type": "number",
            "description": "The amount of the base currency to be converted."
        },
        "rates": {
            "type": "object",
            "properties": {
                "USD": {
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
            },
            "required": ["USD"]
        }
    },
    "required": ["success", "errors", "base_currency_code", "base_currency_name", "to", "amount", "rates"]
}
```
    """
    url = "https://forex-apised1.p.rapidapi.com/convert"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"amount": amount, "from": from_currency, "to": to_currency}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "forex-apised1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")