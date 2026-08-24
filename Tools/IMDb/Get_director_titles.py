import os
import requests

def Get_director_titles(imdbld):
    """
    :API_description: Retrieves film titles directed by a specific person using their IMDb identifier.
    :param imdbld: The IMDb ID of the director whose titles are to be retrieved(e.g., "nm0634240").
    :response_schema: 
    ```json
  [
  {
    "id": "tt33764258",
    "url": "...",
    "primaryTitle": "The Odyssey",
    "originalTitle": "The Odyssey",
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
      },
      {
        "url": "...",
        "width": 380,
        "height": 562
      }
    ],
    "trailer": null,
    "contentRating": null,
    "isAdult": false,
    "releaseDate": "2026-07-17",
    "startYear": 2026,
    "endYear": null,
    "runtimeMinutes": null,
    "genres": [
      "Action",
      "Adventure",
      "Fantasy"
    ],
    "interests": [
      "Action Epic",
      "Adventure Epic",
      "Fantasy Epic",
      "Historical Epic",
      "Action",
      "Adventure",
      "Fantasy",
      "History"
    ],
    "countriesOfOrigin": [
      "US",
      "GB"
    ],
    "externalLinks": null,
    "spokenLanguages": [
      "en"
    ],
    "filmingLocations": [
      "Messinia, Peloponnese region, Greece"
    ],
    "productionCompanies": [
      {
        "id": "co0147954",
        "name": "Syncopy"
      },
      {
        "id": "co0005073",
        "name": "Universal Pictures"
      }
    ],
    "budget": 250000000,
    "grossWorldwide": null,
    "averageRating": null,
    "numVotes": null,
    "metascore": null
  },
  {
    "id": "tt15398776",
    "url": "...",
    "primaryTitle": "Oppenheimer",
    "originalTitle": "Oppenheimer",
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
        "width": 100,
        "height": 414
      },
      {
        "url": "...",
        "width": 380,
        "height": 562
      }
    ],
    "trailer": "https://www.youtube.com/watch?v=bK6ldnjE3Y0",
    "contentRating": "R",
    "isAdult": false,
    "releaseDate": "2023-07-21",
    "startYear": 2023,
    "endYear": null,
    "runtimeMinutes": 180,
    "genres": [
      "Biography",
      "Drama",
      "History"
    ],
    "interests": [
      "Docudrama",
      "Epic",
      "Historical Epic",
      "Period Drama",
      "Psychological Drama",
      "Biography",
      "Drama",
      "History"
    ],
    "countriesOfOrigin": [
      "US",
      "GB"
    ],
    "externalLinks": [
      "https://www.facebook.com/OppenheimerMovie/",
      "https://www.instagram.com/oppenheimermovie/"
    ],
    "spokenLanguages": [
      "en",
      "de",
      "it",
      "nl"
    ],
    "filmingLocations": [
      "Los Alamos, New Mexico, USA"
    ],
    "productionCompanies": [
      {
        "id": "co0005073",
        "name": "Universal Pictures"
      },
      {
        "id": "co0147954",
        "name": "Syncopy"
      },
      {
        "id": "co0028338",
        "name": "Atlas Entertainment"
      }
    ],
    "budget": 100000000,
    "grossWorldwide": 975811333,
    "averageRating": 8.3,
    "numVotes": 938548,
    "metascore": 90
  },
  {
    "id": "tt28642224",
    "url": "https://www.imdb.com/title/tt28642224/",
    "primaryTitle": "Larry Mahoney",
    "originalTitle": "Larry Mahoney",
    "type": "movie",
    "description": "A student angst story.",
    "primaryImage": null,
    "thumbnails": [],
    "trailer": null,
    "contentRating": null,
    "isAdult": false,
    "releaseDate": null,
    "startYear": 1996,
    "endYear": null,
    "runtimeMinutes": null,
    "genres": null,
    "interests": [
      "Drama"
    ],
    "countriesOfOrigin": [
      "GB"
    ],
    "externalLinks": null,
    "spokenLanguages": [
      "en"
    ],
    "filmingLocations": [
      "London, England, UK"
    ],
    "productionCompanies": [],
    "budget": null,
    "grossWorldwide": null,
    "averageRating": null,
    "numVotes": null,
    "metascore": null
  }
]
```
    """
    url = f"https://imdb236.p.rapidapi.com/api/imdb/director/{imdbld}/titles"
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")