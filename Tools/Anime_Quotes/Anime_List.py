import os
import requests

def Anime_List():
    """
    :API_description: Retrieve a list of anime titles, each with associated character and quote counts.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "string"
  },
  "description": "An array of anime titles as strings."
}
    ```
    """
    url = "https://anime-quotes5.p.rapidapi.com/anime-list"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-quotes5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")