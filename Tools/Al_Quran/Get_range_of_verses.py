import os
import requests

def Get_range_of_verses(chapter_number, verse_range):
    """
    :API_description: Retrieves a collection of verses from a specific chapter, including Arabic text, translation, transliteration, and verse IDs.
    :param chapter_number: The chapter number in the Quran.
    :param verse_range: The range of verses to retrieve, formatted as 'start-end'.
    :response_schema: 
    ```json
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string",
            "description": "A message indicating the status or error related to the API key."
        }
    },
    "required": ["message"]
}
    ```
    """
    url = f"https://al-quran1.p.rapidapi.com/{chapter_number}/{verse_range}"
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