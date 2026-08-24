import os
import requests

def People_Details_for_IMDb_ID(imdbld):
    """
    :API_description: Retrieves detailed information about a person in the entertainment industry using their IMDb identifier.
    :param imdbld: The IMDb ID of the person whose information is to be retrieved(e.g., "nm0000001").
    :response_schema: 
    ```json
   {
  "id": "nm0000001",
  "url": "https://www.imdb.com/name/nm0000001/",
  "name": "Fred Astaire",
  "birthName": "Frederic Austerlitz Jr.",
  "primaryImage": "...",
  "thumbnails": [
    {
      "url": "...",
      "width": 140,
      "height": 140
    },
    {
      "url": "...",
      "width": 140,
      "height": 320
    }
  ],
  "biography": "...",
  "primaryProfessions": [
    "actor",
    "miscellaneous",
    "producer"
  ],
  "knownForTitles": [
    "tt0072308",
    "tt0050419",
    "tt0053137",
    "tt0027125"
  ],
  "height": 175,
  "birthDate": "1899-05-10",
  "deathDate": "1987-06-22",
  "birthLocation": "Omaha, Nebraska, USA",
  "deathLocation": "Los Angeles, California, USA"
}
    ```
    """
    url = f"https://imdb236.p.rapidapi.com/api/imdb/name/{imdbld}"
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")