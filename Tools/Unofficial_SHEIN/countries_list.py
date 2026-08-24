import os
import requests

def countries_list():
    """
    :API_description: Retrieve a list of countries categorized into featured and all countries, including their IDs, numbers, short codes, and full names.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "string",
      "description": "Status code indicating the result of the API call."
    },
    "msg": {
      "type": "string",
      "description": "Message describing the status of the API call."
    },
    "info": {
      "type": "object",
      "properties": {
        "country": {
          "type": "object",
          "properties": {
            "hotcountry": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "description": "Unique identifier for the country."
                  },
                  "countrynum": {
                    "type": "string",
                    "description": "Country number or code."
                  },
                  "value": {
                    "type": "string",
                    "description": "Short code or abbreviation for the country."
                  },
                  "country": {
                    "type": "string",
                    "description": "Full name of the country."
                  }
                },
                "required": ["id", "countrynum", "value", "country"]
              },
              "description": "List of hot or featured countries."
            },
            "item_cates": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "description": "Unique identifier for the country."
                  },
                  "countrynum": {
                    "type": "string",
                    "description": "Country number or code."
                  },
                  "value": {
                    "type": "string",
                    "description": "Short code or abbreviation for the country."
                  },
                  "country": {
                    "type": "string",
                    "description": "Full name of the country."
                  }
                },
                "required": ["id", "countrynum", "value", "country"]
              },
              "description": "List of all countries categorized."
            },
            "dc_switch": {
              "type": "integer",
              "description": "Switch indicating the status of the data center or service."
            }
          },
          "required": ["hotcountry", "item_cates", "dc_switch"]
        }
      },
      "required": ["country"]
    }
  },
  "required": ["code", "msg", "info"]
}
```
    """
    url = "https://unofficial-shein.p.rapidapi.com/countries/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "unofficial-shein.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

