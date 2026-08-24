import os
import requests

def Details_for_IMDb_ID(imdbld):
    """
    :API_description: Retrieves detailed information about movies, TV shows, or other media content using their unique IMDb identifier.
    :param imdbld: The unique identifier for a movie or TV show on IMDb(e.g., "tt0816692").
    :response_schema: 
    ```json
    {
  "id": "tt0816692",
  "url": "https://www.imdb.com/title/tt0816692/",
  "primaryTitle": "Interstellar",
  "originalTitle": "Interstellar",
  "type": "movie",
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
  "trailer": "https://www.youtube.com/watch?v=827FNDpQWrQ",
  "contentRating": "PG-13",
  "startYear": 2014,
  "endYear": null,
  "releaseDate": "2014-11-07",
  "interests": [
    "Adventure Epic",
    "Epic",
    "Quest",
    "Sci-Fi Epic",
    "Space Sci-Fi",
    "Time Travel",
    "Adventure",
    "Drama",
    "Sci-Fi"
  ],
  "countriesOfOrigin": [
    "US",
    "GB",
    "CA"
  ],
  "externalLinks": [
    "https://www.facebook.com/Interstellar",
    "https://twitter.com/Interstellar"
  ],
  "spokenLanguages": [
    "en"
  ],
  "filmingLocations": [
    "Iceland"
  ],
  "productionCompanies": [
    {
      "id": "co0023400",
      "name": "Paramount Pictures"
    },
    {
      "id": "co0002663",
      "name": "Warner Bros."
    },
    {
      "id": "co0159111",
      "name": "Legendary Entertainment"
    }
  ],
  "budget": 165000000,
  "grossWorldwide": 758614115,
  "genres": [
    "Adventure",
    "Drama",
    "Sci-Fi"
  ],
  "isAdult": false,
  "runtimeMinutes": 169,
  "averageRating": 8.7,
  "numVotes": 2356666,
  "metascore": 74,
  "directors": [
    {
      "id": "nm0634240",
      "url": "https://www.imdb.com/name/nm0634240/",
      "fullName": "Christopher Nolan"
    }
  ],
  "writers": [
    {
      "id": "nm0634240",
      "url": "https://www.imdb.com/name/nm0634240/",
      "fullName": "Christopher Nolan"
    },
    {
      "id": "nm0634300",
      "url": "https://www.imdb.com/name/nm0634300/",
      "fullName": "Jonathan Nolan"
    }
  ],
  "cast": [
    {
      "id": "nm0000190",
      "url": "...",
      "fullName": "Matthew McConaughey",
      "primaryImage": "...",
      "thumbnails": [
        {
          "url": "...",
          "width": 140,
          "height": 140
        },
        {
          "url": "...",
          "width": 320,
          "height": 320
        }
      ],
      "job": "actor",
      "characters": [
        "Cooper"
      ]
    },
    {
      "id": "nm0004266",
      "url": "...",
      "fullName": "Anne Hathaway",
      "primaryImage": "...",
      "thumbnails": [
        {
          "url": "...",
          "width": 140,
          "height": 140
        },
        {
          "url": "...",
          "width": 320,
          "height": 320
        }
      ],
      "job": "actress",
      "characters": [
        "Brand"
      ]
    },
    {
      "id": "nm0189769",
      "url": "https://www.imdb.com/name/nm0189769/",
      "fullName": "Nathan Crowley",
      "primaryImage": null,
      "thumbnails": [],
      "job": "production_designer",
      "characters": []
    }
  ]
}
}
```
    """
    url = f"https://imdb236.p.rapidapi.com/api/imdb/{imdbld}"
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")