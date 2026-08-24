import os
import requests
def Similar_titles_to_IMDb_ID(imdbld):
    """
    :API_description: Retrieves similar titles based on movie or other media of IMDb ID
    :param imdbld: The IMDb ID of the movie for which similar movies are to be fetched.
    :response_schema: 
    ```json
[
  {
    "id": "tt1345836",
    "url": "...",
    "primaryTitle": "The Dark Knight Rises",
    "originalTitle": "The Dark Knight Rises",
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
    "trailer": "...",
    "contentRating": "PG-13",
    "isAdult": false,
    "releaseDate": "2012-07-20",
    "startYear": 2012,
    "endYear": null,
    "runtimeMinutes": 164,
    "genres": [
      "Crime",
      "Thriller"
    ],
    "interests": [
      "Action Epic",
      "Epic",
      "Psychological Drama",
      "Superhero",
      "Crime",
      "Thriller"
    ],
    "countriesOfOrigin": [
      "US",
      "GB"
    ],
    "externalLinks": [
      "https://www.facebook.com/darkknighttrilogy",
      "https://www.warnerbros.com/movies/dark-knight-rises"
    ],
    "spokenLanguages": [
      "en",
      "ar"
    ],
    "filmingLocations": [
      "Mehrangarh Fort, Jodhpur, Rajasthan, India"
    ],
    "productionCompanies": [
      {
        "id": "co0002663",
        "name": "Warner Bros."
      },
      {
        "id": "co1041831",
        "name": "Legendary Pictures"
      },
      {
        "id": "co0123927",
        "name": "DC Entertainment"
      }
    ],
    "budget": 250000000,
    "grossWorldwide": 1085429532,
    "averageRating": 8.4,
    "numVotes": 1996742,
    "metascore": 78
  },
  {
    "id": "tt6476140",
    "url": "...",
    "primaryTitle": "Serenity",
    "originalTitle": "Serenity",
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
    "trailer": "...",
    "contentRating": "R",
    "isAdult": false,
    "releaseDate": "2019-01-25",
    "startYear": 2019,
    "endYear": null,
    "runtimeMinutes": 106,
    "genres": [
      "Drama",
      "Mystery",
      "Thriller"
    ],
    "interests": [
      "Drama",
      "Mystery",
      "Thriller"
    ],
    "countriesOfOrigin": [
      "GB",
      "US"
    ],
    "externalLinks": null,
    "spokenLanguages": [
      "en",
      "fr"
    ],
    "filmingLocations": [
      "Mauritius"
    ],
    "productionCompanies": [
      {
        "id": "co0587505",
        "name": "Blue Budgie Films Limited"
      },
      {
        "id": "co0680234",
        "name": "Global Road Entertainment"
      },
      {
        "id": "co0531993",
        "name": "Ingenious"
      }
    ],
    "budget": 25000000,
    "grossWorldwide": 14454622,
    "averageRating": 5.4,
    "numVotes": 49454,
    "metascore": 37
  }
]
```
    """
    url = f"https://imdb236.p.rapidapi.com/api/imdb/{imdbld}/similar"
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
