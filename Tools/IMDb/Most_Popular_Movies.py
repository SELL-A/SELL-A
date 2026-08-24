import os
import requests

def Most_Popular_Movies():
    """
    :API_description: This API retrieves comprehensive movie metadata from an IMDB-like database, including detailed information about upcoming 2025 releases with production details, ratings, financial data, and multimedia content.
    :param None
    :response_schema: 
    ```json
[
  {
    "id": "tt7068946",
    "url": "...",
    "primaryTitle": "The Accountant 2",
    "originalTitle": "The Accountant 2",
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
    "startYear": 2025,
    "endYear": null,
    "releaseDate": "2025-04-25",
    "interests": [
      "Whodunnit",
      "Action",
      "Crime",
      "Drama",
      "Mystery",
      "Thriller"
    ],
    "countriesOfOrigin": [
      "US"
    ],
    "externalLinks": [],
    "spokenLanguages": [
      "en"
    ],
    "filmingLocations": [
      "Cowboy Palace Saloon - 21635 Devonshire St, Chatsworth, Los Angeles, California, USA"
    ],
    "productionCompanies": [
      {
        "id": "co1025982",
        "name": "Amazon MGM Studios"
      },
      {
        "id": "co0961831",
        "name": "Artists Equity"
      },
      {
        "id": "co0655304",
        "name": "51 Entertainment"
      }
    ],
    "budget": 80000000,
    "grossWorldwide": 102123366,
    "genres": [
      "Action",
      "Crime",
      "Drama"
    ],
    "isAdult": false,
    "runtimeMinutes": 132,
    "averageRating": 6.8,
    "numVotes": 57821,
    "metascore": 58
  },
  {
    "id": "tt7181546",
    "url": "...",
    "primaryTitle": "From the World of John Wick: Ballerina",
    "originalTitle": "Ballerina",
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
    "trailer": "https://www.youtube.com/watch?v=0FSwsrFpkbw",
    "contentRating": "R",
    "startYear": 2025,
    "endYear": null,
    "releaseDate": "2025-06-06",
    "interests": [
      "Gun Fu",
      "Martial Arts",
      "One-Person Army Action",
      "Action",
      "Thriller"
    ],
    "countriesOfOrigin": [
      "US"
    ],
    "externalLinks": [
      "https://ballerinamovie2025.com/"
    ],
    "spokenLanguages": [
      "en"
    ],
    "filmingLocations": [
      "Hungary"
    ],
    "productionCompanies": [
      {
        "id": "co0006881",
        "name": "Lionsgate"
      },
      {
        "id": "co0172670",
        "name": "Thunder Road Pictures"
      },
      {
        "id": "co0836036",
        "name": "87Eleven Entertainment"
      }
    ],
    "budget": 90000000,
    "grossWorldwide": 58432471,
    "genres": [
      "Action",
      "Thriller"
    ],
    "isAdult": false,
    "runtimeMinutes": 124,
    "averageRating": 7.3,
    "numVotes": 22807,
    "metascore": 59
  },
  {
    "id": "tt5040012",
    "url": "...",
    "primaryTitle": "Nosferatu",
    "originalTitle": "Nosferatu",
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
    "startYear": 2024,
    "endYear": null,
    "releaseDate": "2024-12-25",
    "interests": [
      "Dark Fantasy",
      "Supernatural Horror",
      "Vampire Horror",
      "Fantasy",
      "Horror",
      "Mystery"
    ],
    "countriesOfOrigin": [
      "US"
    ],
    "externalLinks": [
      "https://amzn.to/4g55ALC",
      "https://www.focusfeatures.com/nosferatu/"
    ],
    "spokenLanguages": [
      "en",
      "ro",
      "ru",
      "la",
      "de"
    ],
    "filmingLocations": [
      "Corvin Castle, Transylvania region, Romania"
    ],
    "productionCompanies": [
      {
        "id": "co0042399",
        "name": "Focus Features"
      },
      {
        "id": "co0442328",
        "name": "Maiden Voyage Pictures"
      },
      {
        "id": "co0329296",
        "name": "Studio 8"
      }
    ],
    "budget": 50000000,
    "grossWorldwide": 181270493,
    "genres": [
      "Fantasy",
      "Horror",
      "Mystery"
    ],
    "isAdult": false,
    "runtimeMinutes": 132,
    "averageRating": 7.2,
    "numVotes": 207918,
    "metascore": 78
  }
]
```
    """
    url = "https://imdb236.p.rapidapi.com/api/imdb/most-popular-movies"
 

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")