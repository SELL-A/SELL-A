import os
import requests
def Convert(from_currency: str, to_currency: str, amount: float):
    """
    :API_description: Converts a specified amount from one currency to another.
    :param from_currency: The currency code to convert from (e.g., 'EUR').
    :param to_currency: The currency code to convert to (e.g., 'KWD').
    :param amount: The amount to be converted(e.g., '10').
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates whether the API call was successful."
    },
    "validationMessage": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "An array of validation messages, typically empty if there are no errors."
    },
    "result": {
      "type": "object",
      "properties": {
        "from": {
          "type": "string",
          "description": "The currency code from which the amount is being converted."
        },
        "to": {
          "type": "string",
          "description": "The currency code to which the amount is being converted."
        },
        "amountToConvert": {
          "type": "number",
          "description": "The amount of currency to be converted."
        },
        "convertedAmount": {
          "type": "number",
          "description": "The resulting amount after conversion."
        }
      },
      "required": ["from", "to", "amountToConvert", "convertedAmount"]
    }
  },
  "required": ["success", "validationMessage", "result"]
}
```
    """
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"from": from_currency, "to": to_currency, "amount": amount}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

