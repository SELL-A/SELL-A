import os
import requests

def Pokemon_Power_Up_Requirements():
    """
    :API_description: This API provides the necessary resources (candy, stardust, and XL candy) required to power up a Pokemon at various levels, up to a maximum of level 40.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "1": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "1.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "2": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "2.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "3": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "3.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "4": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "4.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "5.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "6": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "6.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "7": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "7.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "8": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "8.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "9": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "9.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "10": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "10.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "11": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "11.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "12": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "12.5": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "13": {
      "type": "object",
      "properties": {
        "candy_to_upgrade": { "type": "integer" },
        "current_level": { "type": "number" },
        "level_after_powering": { "type": "number" },
        "stardust_to_upgrade": { "type": "integer" },
        "xl_candy_to_upgrade": { "type": "integer" }
      },
      "required": ["candy_to_upgrade", "current_level", "level_after_powering", "stardust_to_upgrade", "xl_candy_to_upgrade"]
    },
    "13.5": {
      "type": "object",
      "properties":
    ```
    """
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_powerup_requirements.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "pokemon-go1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")