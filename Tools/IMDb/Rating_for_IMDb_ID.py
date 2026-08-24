import os
import requests

def Rating_for_IMDb_ID(imdbid):
    """
    :API_description: Retrieves rating information for movies or TV shows using their IMDb identifier.
    :param imdbid: The IMDb ID of the movie or TV show for which the rating is requested.
    :response_schema: 
    ```json
   {
  "id": "tt0816692",
  "url": "https://www.imdb.com/title/tt0816692/",
  "averageRating": 8.7,
  "numVotes": 2312856
}
```
    """
    url = f"https://imdb236.p.rapidapi.com/api/imdb/{imdbid}/rating"
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")