import os
import requests

def Get_specific_Ayah_Verse(chapter, verse):
    """
    :API_description: Retrieve detailed information about a specific verse from the Quran, including its Arabic text, English translation, and transliteration.
    :param chapter: The chapter number in the Quran.
    :param verse: The verse number within the specified chapter.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "number",
      "description": "A numerical identifier for the content."
    },
    "content": {
      "type": "string",
      "description": "The original text in Arabic."
    },
    "translation_eng": {
      "type": "string",
      "description": "The English translation of the original Arabic text."
    },
    "transliteration": {
      "type": "string",
      "description": "The transliteration of the original Arabic text into Latin script."
    }
  },
  "required": ["id", "content", "translation_eng", "transliteration"]
}
```
    """
    url = f"https://al-quran1.p.rapidapi.com/{chapter}/{verse}"
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