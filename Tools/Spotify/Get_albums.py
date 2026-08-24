import os
import requests

def Get_albums(ids):
    """
    :API_description: Retrieve detailed information about one or more albums, including tracks, artists, and release details.
    :param ids: A comma-separated string of album IDs(e.g., "3IBcauSj5M2A6lTeffJzdv,3IBcauSj5M2A6lTeffJzdv").
    :response_schema: 
    ```json
{
  "albums": [
    {
      "album_type": "string",
      "total_tracks": "integer",
      "is_playable": "boolean",
      "external_urls": {
        "spotify": "string"
      },
      "id": "string",
      "images": [
        {
          "url": "string",
          "height": "integer",
          "width": "integer"
        }
      ],
      "name": "string",
      "release_date": "string",
      "release_date_precision": "string",
      "type": "string",
      "uri": "string",
      "artists": [
        {
          "external_urls": {
            "spotify": "string"
          },
          "id": "string",
          "name": "string",
          "type": "string",
          "uri": "string"
        }
      ],
      "tracks": {
        "limit": "integer",
        "next": "string or null",
        "offset": "integer",
        "previous": "string or null",
        "total": "integer",
        "items": [
          {
            "artists": [
              {
                "external_urls": {
                  "spotify": "string"
                },
                "id": "string",
                "name": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "disc_number": "integer",
            "duration_ms": "integer",
            "explicit": "boolean",
            "external_urls": {
              "spotify": "string"
            },
            "id": "string",
            "is_playable": "boolean",
            "name": "string",
            "preview_url": "string",
            "track_number": "integer",
            "type": "string",
            "uri": "string",
            "is_local": "boolean"
          }
        ]
      },
      "copyrights": [
        {
          "text": "string",
          "type": "string"
        }
      ],
      "external_ids": {
        "upc": "string"
      },
      "genres": [
        "string"
      ],
      "label": "string",
      "popularity": "integer"
    }
  ]
}
```
    """
    url = "https://spotify81.p.rapidapi.com/albums/"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"ids": ids}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "spotify81.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")