import os
import requests

def Get_base_information():
    """
    :API_description: Retrieves detailed linguistic metrics and structural information about a text, including chapter counts, verse details, and unique word analysis, categorized by origin.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "total_surahs": {
      "type": "integer",
      "description": "Total number of surahs (chapters) in the text."
    },
    "total_meccan_surahs": {
      "type": "integer",
      "description": "Total number of Meccan surahs in the text."
    },
    "total_medinan_surahs": {
      "type": "integer",
      "description": "Total number of Medinan surahs in the text."
    },
    "total_verses": {
      "type": "integer",
      "description": "Total number of verses in the text."
    },
    "number_of_words": {
      "type": "integer",
      "description": "Total number of words in the text."
    },
    "number_of_unique_words": {
      "type": "integer",
      "description": "Total number of unique words in the text."
    },
    "number_of_stems": {
      "type": "integer",
      "description": "Total number of stems in the text."
    },
    "number_of_lemmas": {
      "type": "integer",
      "description": "Total number of lemmas in the text."
    },
    "number_of_roots": {
      "type": "integer",
      "description": "Total number of roots in the text."
    }
  },
  "required": [
    "total_surahs",
    "total_meccan_surahs",
    "total_medinan_surahs",
    "total_verses",
    "number_of_words",
    "number_of_unique_words",
    "number_of_stems",
    "number_of_lemmas",
    "number_of_roots"
  ]
}
```
    """
    url = "https://al-quran1.p.rapidapi.com/"
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
