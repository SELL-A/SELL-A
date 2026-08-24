import os
import requests

def Search(q, type="multi", offset=0, limit=10, numberOfTopResults=5):
    """
    :API_description: The Search API provides detailed information on various media items like albums, artists, and episodes available on Spotify, including their metadata and cover art.
    :param q: The search query.
    :param type: The type of content to search for. Valid types are: 'multi', 'albums', 'artists', 'episodes', 'genres', 'playlists', 'podcasts', 'tracks', 'users'".
    :param offset: The index of the first result to return.
    :param limit: The maximum number of results to return.
    :param numberOfTopResults: The number of top results to prioritize in the response.
    :response_schema: 
    ```json
{
  "albums": {
    "totalCount": "integer",
    "items": [
      {
        "data": {
          "uri": "string",
          "name": "string",
          "artists": {
            "items": [
              {
                "uri": "string",
                "profile": {
                  "name": "string"
                }
              }
            ]
          },
          "coverArt": {
            "sources": [
              {
                "url": "string",
                "width": "integer",
                "height": "integer"
              }
            ]
          },
          "date": {
            "year": "integer"
          }
        }
      }
    ]
  },
  "artists": {
    "totalCount": "integer",
    "items": [
      {
        "data": {
          "uri": "string",
          "profile": {
            "name": "string"
          },
          "visuals": {
            "avatarImage": {
              "sources": [
                {
                  "url": "string",
                  "width": "integer",
                  "height": "integer"
                }
              ]
            }
          }
        }
      }
    ]
  },
  "episodes": {
    "totalCount": "integer",
    "items": [
      {
        "data": {
          "uri": "string",
          "name": "string",
          "coverArt": {
            "sources": [
              {
                "url": "string",
                "width": "integer",
                "height": "integer"
              }
            ]
          },
          "duration": {
            "totalMilliseconds": "integer"
          },
          "releaseDate": {
            "isoString": "string"
          },
          "podcast": {
            "coverArt": {
              "sources": [
                {
                  "url": "string",
                  "width": "integer",
                  "height": "integer"
                }
              ]
            }
          },
          "description": "string",
          "contentRating": {
            "label": "string"
          }
        }
      }
    ]
  }
}
    ```
    """
    url = "https://spotify81.p.rapidapi.com/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "q": q,
        "type": type,
        "offset": offset,
        "limit": limit,
        "numberOfTopResults": numberOfTopResults
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "spotify81.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
