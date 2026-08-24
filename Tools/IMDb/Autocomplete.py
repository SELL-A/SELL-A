import os
import requests

def Autocomplete(query):
    """
    :API_description: Search for various types of movies, short films and animations
    :param query: The search term for which autocomplete suggestions are needed.
    :response_schema: 
    ```json
[
  {
    "id": "tt0903747",
    "primaryTitle": "Breaking Bad",
    "originalTitle": "Breaking Bad",
    "type": "tvSeries",
    "description": "...",
    "primaryImage": "...",
    "contentRating": "TV-MA",
    "isAdult": false,
    "releaseDate": "2008-01-20",
    "startYear": 2008,
    "endYear": 2013,
    "runtimeMinutes": null,
    "genres": [
      "Crime",
      "Drama",
      "Thriller"
    ],
    "interests": [
      "Desert Adventure",
      "Drug Crime",
      "Epic"
    ],
    "countriesOfOrigin": [
      "United States"
    ],
    "externalLinks": [
      "https://www.facebook.com/BreakingBad",
      "https://www.instagram.com/breakingbad/"
    ],
    "spokenLanguages": [
      "English",
      "Spanish"
    ],
    "filmingLocations": [
      "3828 Piermont Dr NE, Albuquerque, New Mexico, USA"
    ],
    "originalLanguage": null,
    "budget": null,
    "grossWorldwide": null,
    "averageRating": 9.5,
    "numVotes": 2266133
  },
  {
    "id": "tt0455275",
    "primaryTitle": "Prison Break",
    "originalTitle": "Prison Break",
    "type": "tvSeries",
    "description": "...",
    "primaryImage": "...",
    "contentRating": "TV-14",
    "isAdult": false,
    "releaseDate": "2005-08-29",
    "startYear": 2005,
    "endYear": 2017,
    "runtimeMinutes": null,
    "genres": [
      "Action",
      "Crime",
      "Drama"
    ],
    "interests": [
      "Conspiracy Thriller",
      "Prison Drama",
      "Action"
    ],
    "countriesOfOrigin": [
      "United Kingdom",
      "United States"
    ],
    "externalLinks": [
      "https://www.hulu.com/series/prison-break-d1d023da-ebb7-474c-b858-c4890e2d5757",
      "https://www.facebook.com/PrisonBreak/"
    ],
    "spokenLanguages": [
      "English",
      "Spanish",
      "Arabic"
    ],
    "filmingLocations": [
      "Joliet Prison - Collins Street, Joliet, Illinois, USA"
    ],
    "originalLanguage": null,
    "budget": null,
    "grossWorldwide": null,
    "averageRating": 8.3,
    "numVotes": 612422
  }
]
```
    """
    url = "https://imdb236.p.rapidapi.com/api/imdb/autocomplete"
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")