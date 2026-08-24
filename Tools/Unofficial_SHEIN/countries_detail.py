import os
import requests

def countries_detail(region):
    """
    :API_description: Retrieve detailed information about a country, including supported languages, currency settings, and the country's full name.
    :param region: The region code for which the country details are to be retrieved(e.g., "US").
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
      "description": "Message describing the result of the API call."
    },
    "info": {
      "type": "object",
      "properties": {
        "support_language_list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "language": {
                "type": "string",
                "description": "Language code."
              },
              "languageTip": {
                "type": "string",
                "description": "Language name in the specified language."
              }
            },
            "required": ["language", "languageTip"]
          },
          "description": "List of supported languages."
        },
        "language_full_name_in_header": {
          "type": "object",
          "properties": {
            "language": {
              "type": "string",
              "description": "Language code for the header."
            },
            "languageTip": {
              "type": "string",
              "description": "Language name in the specified language for the header."
            }
          },
          "required": ["language", "languageTip"],
          "description": "Language settings for the header."
        },
        "suppport_currency_list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string",
                "description": "Currency code."
              },
              "symbol_left": {
                "type": "string",
                "description": "Symbol displayed on the left side of the currency."
              },
              "symbol_right": {
                "type": "string",
                "description": "Symbol displayed on the right side of the currency."
              },
              "value": {
                "type": "string",
                "description": "Exchange rate value."
              },
              "country_flag": {
                "type": "string",
                "description": "Path to the country flag image."
              },
              "default": {
                "type": "string",
                "description": "Indicates if this is the default currency."
              },
              "decimal_place": {
                "type": "string",
                "description": "Number of decimal places for the currency."
              },
              "dec_point": {
                "type": "string",
                "description": "Decimal point character."
              },
              "thousands_sep": {
                "type": "string",
                "description": "Thousands separator character."
              }
            },
            "required": ["code", "symbol_left", "symbol_right", "value", "country_flag", "default", "decimal_place", "dec_point", "thousands_sep"]
          },
          "description": "List of supported currencies."
        },
        "current_country_full_name": {
          "type": "string",
          "description": "Full name of the current country."
        }
      },
      "required": ["support_language_list", "language_full_name_in_header", "suppport_currency_list", "current_country_full_name"]
    }
  },
  "required": ["code", "msg", "info"]
}
    ```
    """
    url = "https://unofficial-shein.p.rapidapi.com/countries/detail"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"region": region}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "unofficial-shein.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")