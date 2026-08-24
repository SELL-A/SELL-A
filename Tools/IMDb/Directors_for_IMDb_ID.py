import os
import requests

def Directors_for_IMDb_ID(imdb_id):
    """
    :API_description: This API retrieves director information from the IMDb database using an IMDb ID, returning basic profile details including name, IMDb identifier, and profile URL.
    :param imdb_id: The IMDb ID of the movie or show for which to retrieve directors(e.g., "tt0816692").
    :response_schema: 
    ```json
[
  {
    "id": "nm0634240",
    "url": "https://www.imdb.com/name/nm0634240/",
    "fullName": "Christopher Nolan"
  }
]
```
    """
    url = f"https://imdb236.p.rapidapi.com/api/imdb/{imdb_id}/directors"
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")