import os
import requests
def available():
    """
    :API_description: Retrieves a list of currencies, each identified by its ISO 4217 code and name, useful for currency-related operations.
    :param None
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
    "currencies": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "currency_code": {
            "type": "string",
            "description": "The ISO 4217 currency code."
          },
          "currency_name": {
            "type": "string",
            "description": "The name of the currency."
          }
        },
        "required": ["currency_code", "currency_name"]
      },
      "description": "List of currency objects, each containing a currency code and name."
    }
  },
  "required": ["success", "errors", "currencies"]
}
    ```
    """
    url = "https://forex-apised1.p.rapidapi.com/available"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "forex-apised1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

