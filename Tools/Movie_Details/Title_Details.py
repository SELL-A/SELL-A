import os
import requests

def Title_Details(imdbid):
    """
    :API_description: Retrieve comprehensive data on movies, including genre, image URLs, IMDb ID, rating, languages, release year, runtime, and streaming availability.
    :param imdbid: The IMDb ID of the title for which details are to be fetched(e.g. "tt0148600").
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "genre": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of genres associated with the movie."
        },
        "imageurl": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "URLs of images associated with the movie."
        },
        "imdbid": {
          "type": "string",
          "description": "Unique IMDb ID of the movie."
        },
        "imdbrating": {
          "type": "number",
          "description": "IMDb rating of the movie."
        },
        "language": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of languages in which the movie is available."
        },
        "released": {
          "type": "integer",
          "description": "Year the movie was released."
        },
        "runtime": {
          "type": "string",
          "description": "Duration of the movie."
        },
        "streamingAvailability": {
          "type": "object",
          "properties": {
            "country": {
              "type": "object",
              "properties": {
                "US": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "platform": {
                        "type": "string",
                        "description": "Name of the streaming platform."
                      },
                      "url": {
                        "type": "string",
                        "description": "URL to watch the movie on the platform."
                      }
                    },
                    "required": ["platform", "url"]
                  },
                  "description": "List of streaming platforms and URLs where the movie is available in the US."
                }
              }
            }
          },
          "required": ["country"]
        },
        "synopsis": {
          "type": "string",
          "description": "Brief summary of the movie's plot."
        },
        "title": {
          "type": "string",
          "description": "Title of the movie."
        },
        "type": {
          "type": "string",
          "description": "Type of the media (e.g., 'movie')."
        }
      },
      "required": ["genre", "imageurl", "imdbid", "imdbrating", "language", "released", "runtime", "streamingAvailability", "synopsis", "title", "type"]
    }
    ```
    """
    url = "https://ott-details.p.rapidapi.com/gettitleDetails"
  
    querystring = {"imdbid": imdbid}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")