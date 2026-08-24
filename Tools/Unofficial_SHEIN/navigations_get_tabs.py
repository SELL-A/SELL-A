import os
import requests

def navigations_get_tabs(language, country, currency):
    """
    :API_description: Retrieve a list of navigation tabs with details including ID, name, channel name, and category IDs.
    :param language: The language code for the response (e.g., 'en' for English).
    :param country: The country code for the response (e.g., 'US' for the United States).
    :param currency: The currency code for the response (e.g., 'USD' for US Dollar).
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
        "tabs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the tab."
              },
              "name": {
                "type": "string",
                "description": "Name of the tab."
              },
              "channelName": {
                "type": "string",
                "description": "Name of the channel associated with the tab."
              },
              "cat_id": {
                "type": "string",
                "description": "Comma-separated list of category IDs associated with the tab."
              },
              "tspNodeIds": {
                "type": ["string", "null"],
                "description": "Node IDs related to the tab, if any."
              },
              "abt_pos": {
                "type": ["string", "null"],
                "description": "Position information related to the tab, if any."
              },
              "crowdId": {
                "type": "string",
                "description": "Crowd ID associated with the tab."
              },
              "is_default": {
                "type": "string",
                "description": "Indicates if the tab is the default tab."
              },
              "recommendAbtPos": {
                "type": ["string", "null"],
                "description": "Recommended position for the tab, if any."
              },
              "isAllTab": {
                "type": "string",
                "description": "Indicates if the tab is an 'All' tab."
              },
              "isNew": {
                "type": "string",
                "description": "Indicates if the tab is new."
              },
              "tabData": {
                "type": ["object", "null"],
                "description": "Additional data associated with the tab, if any."
              },
              "newTabData": {
                "type": ["object", "null"],
                "description": "New data associated with the tab, if any."
              }
            },
            "required": ["id", "name", "channelName", "cat_id", "crowdId", "is_default", "isAllTab", "isNew"]
          },
          "description": "List of tabs with their associated data."
        },
        "crowd_abt": {
          "type": ["string", "null"],
          "description": "Crowd ABT information, if any."
        },
        "crowdId": {
          "type": ["string", "null"],
          "description": "Crowd ID, if any."
        },
        "contentCacheEnable": {
          "type": ["string", "null"],
          "description": "Indicates if content caching is enabled, if any."
        }
      },
      "required": ["tabs"]
    }
  },
  "required": ["code", "msg", "info"]
}
    ```
    """
    url = "https://unofficial-shein.p.rapidapi.com/navigations/get-tabs"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"language": language, "country": country, "currency": currency}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "unofficial-shein.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")