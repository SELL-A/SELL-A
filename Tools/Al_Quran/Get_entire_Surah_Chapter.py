import os
import requests

def Get_entire_Surah_Chapter(surah_number):
    """
    :API_description: Retrieve detailed information about a specific surah (chapter) from the Quran, including its name, translation, type, verses, and more.
    :param surah_number: The number of the Surah to retrieve.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "Unique identifier for the surah."
    },
    "surah_name": {
      "type": "string",
      "description": "Name of the surah in English."
    },
    "surah_name_ar": {
      "type": "string",
      "description": "Name of the surah in Arabic."
    },
    "translation": {
      "type": "string",
      "description": "Translation of the surah name in English."
    },
    "type": {
      "type": "string",
      "description": "Type of the surah (e.g., 'meccan')."
    },
    "total_verses": {
      "type": "integer",
      "description": "Total number of verses in the surah."
    },
    "description": {
      "type": "string",
      "description": "Detailed description of the surah."
    },
    "verses": {
      "type": "object",
      "description": "Collection of verses in the surah.",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number",
            "description": "Unique identifier for the verse."
          },
          "content": {
            "type": "string",
            "description": "Content of the verse in Arabic."
          },
          "translation_eng": {
            "type": "string",
            "description": "Translation of the verse in English."
          },
          "transliteration": {
            "type": "string",
            "description": "Transliteration of the verse in English."
          }
        },
        "required": ["id", "content", "translation_eng", "transliteration"]
      }
    }
  },
  "required": ["id", "surah_name", "surah_name_ar", "translation", "type", "total_verses", "description", "verses"]
}
    ```
    """
    url = f"https://al-quran1.p.rapidapi.com/{surah_number}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "al-quran1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")