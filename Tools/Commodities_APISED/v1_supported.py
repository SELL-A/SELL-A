import os
import requests

def v1_supported():
    """
    :API_description: Retrieve lists of supported commodities and currencies, including details like code, name, and measurement units.
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
    "supported_commodities": {
      "type": "array",
      "description": "List of supported commodities with their codes, names, and weight measurements.",
      "items": {
        "type": "object",
        "properties": {
          "commodity_code": {
            "type": "string",
            "description": "Unique code for the commodity."
          },
          "commodity_name": {
            "type": "string",
            "description": "Name of the commodity."
          },
          "commodity_weight_measurement": {
            "type": "string",
            "description": "Unit of measurement for the commodity's weight."
          }
        },
        "required": ["commodity_code", "commodity_name", "commodity_weight_measurement"]
      }
    },
    "supported_currencies": {
      "type": "array",
      "description": "List of supported currencies with their codes and names.",
      "items": {
        "type": "object",
        "properties": {
          "currency_code": {
            "type": "string",
            "description": "Unique code for the currency."
          },
          "currency_name": {
            "type": "string",
            "description": "Name of the currency."
          }
        },
        "required": ["currency_code", "currency_name"]
      }
    }
  },
  "required": ["success", "supported_commodities", "supported_currencies"]
}
```
    """
    url = "https://commodities-apised.p.rapidapi.com/v1/supported"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "commodities-apised.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")