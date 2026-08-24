import os
import requests

def Search_for_a_word_in_Quran():
    """
    :API_description: Retrieve a list of Quranic verses related to a specified search term, including surah number, verse number, and verse content.
    :param: None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "total_matches": {
        "type": "integer",
        "description": "The total number of matches found."
      },
      "surah_no": {
        "type": "string",
        "description": "The number of the surah (chapter) in the Quran."
      },
      "verse_no": {
        "type": "string",
        "description": "The number of the verse within the surah."
      },
      "content": {
        "type": "string",
        "description": "The content of the verse, which includes the text of the verse."
      }
    },
    "required": ["surah_no", "verse_no", "content"]
  }
}
```
    """
    url = "https://al-quran1.p.rapidapi.com/corpus/muhammad"
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
      

