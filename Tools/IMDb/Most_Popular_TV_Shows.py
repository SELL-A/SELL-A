import os
import requests

def Most_Popular_TV_Shows():
    """
    :API_description: This API provides comprehensive information about popular television series and films, including detailed metadata such as plot descriptions, ratings, production details, release information, and multimedia links for entertainment discovery.
    :param None
    :response_schema: 
    ```json
[
  {
    "id": "tt27995114",
    "url": "...",
    "primaryTitle": "Dept. Q",
    "originalTitle": "Dept. Q",
    "type": "tvSeries",
    "description": "...",
    "primaryImage": "...",
    "thumbnails": [
      {
        "url": "...",
        "width": 100,
        "height": 148
      },
      {
        "url": "...",
        "width": 280,
        "height": 414
      }
    ],
    "trailer": null,
    "contentRating": "TV-MA",
    "startYear": 2025,
    "endYear": null,
    "releaseDate": "2025-05-29",
    "interests": [
      "Crime",
      "Drama",
      "Thriller"
    ],
    "countriesOfOrigin": [
      "GB"
    ],
    "externalLinks": [
      "https://www.netflix.com/title/81487660"
    ],
    "spokenLanguages": [
      "en"
    ],
    "filmingLocations": [
      "Edinburgh, Scotland, UK"
    ],
    "productionCompanies": [
      {
        "id": "co0826666",
        "name": "Flitcraft"
      },
      {
        "id": "co0208971",
        "name": "Left Bank Pictures"
      }
    ],
    "budget": null,
    "grossWorldwide": null,
    "genres": [
      "Crime",
      "Drama",
      "Thriller"
    ],
    "isAdult": false,
    "runtimeMinutes": null,
    "averageRating": 8.3,
    "numVotes": 29913,
    "metascore": null
  },
  {
    "id": "tt3581920",
    "url": "...",
    "primaryTitle": "The Last of Us",
    "originalTitle": "The Last of Us",
    "type": "tvSeries",
    "description": "...",
    "primaryImage": "...",
    "thumbnails": [
      {
        "url": "...",
        "width": 100,
        "height": 148
      },
      {
        "url": "...",
        "width": 100,
        "height": 414
      }
    ],
    "trailer": "https://www.youtube.com/watch?v=uLtkt8BonwM",
    "contentRating": "TV-MA",
    "startYear": 2023,
    "endYear": null,
    "releaseDate": "2023-01-15",
    "interests": [
      "Dystopian Sci-Fi",
      "Quest",
      "Survival",
      "Zombie Horror",
      "Action",
      "Adventure",
      "Drama",
      "Horror",
      "Sci-Fi",
      "Thriller"
    ],
    "countriesOfOrigin": [
      "CA",
      "US"
    ],
    "externalLinks": [
      "https://www.hbo.com/the-last-of-us",
      "https://www.sky.com/watch/the-last-of-us"
    ],
    "spokenLanguages": [
      "en",
      "id"
    ],
    "filmingLocations": [
      "Calgary, Alberta, Canada"
    ],
    "productionCompanies": [
      {
        "id": "co0016350",
        "name": "Canadian Film or Video Production Tax Credit (CPTC)"
      },
      {
        "id": "co0328593",
        "name": "Government of Alberta"
      },
      {
        "id": "co0135004",
        "name": "Naughty Dog"
      }
    ],
    "budget": null,
    "grossWorldwide": null,
    "genres": [
      "Action",
      "Adventure",
      "Drama"
    ],
    "isAdult": false,
    "runtimeMinutes": null,
    "averageRating": 8.6,
    "numVotes": 674049,
    "metascore": null
  },
  {
    "id": "tt0804503",
    "url": "...",
    "primaryTitle": "Mad Men",
    "originalTitle": "Mad Men",
    "type": "tvSeries",
    "description": "...",
    "primaryImage": "...",
    "thumbnails": [
      {
        "url": "...",
        "width": 100,
        "height": 148
      },
      {
        "url": "...",
        "width": 100,
        "height": 414
      }
    ],
    "trailer": "https://www.youtube.com/watch?v=m7NChV93LBw",
    "contentRating": "TV-MA",
    "startYear": 2007,
    "endYear": 2015,
    "releaseDate": "2007-07-19",
    "interests": [
      "Epic",
      "Period Drama",
      "Workplace Drama",
      "Drama"
    ],
    "countriesOfOrigin": [
      "US"
    ],
    "externalLinks": [
      "https://www.facebook.com/MadMen",
      "https://twitter.com/madmen_amc"
    ],
    "spokenLanguages": [
      "en"
    ],
    "filmingLocations": [
      "New York City, New York, USA"
    ],
    "productionCompanies": [
      {
        "id": "co0026995",
        "name": "Lionsgate Television"
      },
      {
        "id": "co0247554",
        "name": "Weiner Bros."
      },
      {
        "id": "co0019701",
        "name": "American Movie Classics (AMC)"
      }
    ],
    "budget": null,
    "grossWorldwide": null,
    "genres": [
      "Drama"
    ],
    "isAdult": false,
    "runtimeMinutes": null,
    "averageRating": 8.7,
    "numVotes": 276272,
    "metascore": null
  }
]
```
    """
    url = "https://imdb236.p.rapidapi.com/api/imdb/most-popular-tv"

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")