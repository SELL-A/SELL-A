import os
import requests

def Album_tracks(id, offset=0, limit=300):
    """
    :API_description: Retrieve detailed information about an album, including its playability status and a list of tracks with metadata such as URI, name, play count, and duration.
    :param id: The Spotify album ID(e.g., "3IBcauSj5M2A6lTeffJzdv").
    :param offset: The index of the first track to return (default is 0).
    :param limit: The maximum number of tracks to return (default is 300).
    :response_schema: 
    ```json
{
  "data": {
    "album": {
      "playability": {
        "playable": true
      },
      "tracks": {
        "totalCount": 10,
        "items": [
          {
            "uid": "3d026f76adb5928f0e59",
            "track": {
              "uri": "spotify:track:5jvhTc0g18kwYQNUJM5C4e",
              "name": "Makina",
              "playcount": "151563089",
              "discNumber": 1,
              "trackNumber": 1,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 211016
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "419656ce995b7d2148d1",
            "track": {
              "uri": "spotify:track:72t3CRd8YEFrlc3x0OVaob",
              "name": "Umrumda Değil",
              "playcount": "187477300",
              "discNumber": 1,
              "trackNumber": 2,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 185458
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "dbfa6b79b176daea3899",
            "track": {
              "uri": "spotify:track:5TkQatzJqKafPgHQerZ0dL",
              "name": "Gecenin Içine Gir",
              "playcount": "36886810",
              "discNumber": 1,
              "trackNumber": 3,
              "contentRating": {
                "label": "NONE"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 200000
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:3BVPc9s4JXzM6O1InlLxED",
                    "profile": {
                      "name": "Mavi"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "58f3989f6fdefaf1c9be",
            "track": {
              "uri": "spotify:track:6IW5ocUH5DRWagxkLTlbUS",
              "name": "Nedenini Sorma",
              "playcount": "92804195",
              "discNumber": 1,
              "trackNumber": 4,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 243205
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "15dadc3ce6fa19b40977",
            "track": {
              "uri": "spotify:track:1ijjjMFlM3Pe8t3ykXBzxk",
              "name": "Mahalle",
              "playcount": "27039442",
              "discNumber": 1,
              "trackNumber": 5,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 152301
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:7GaMopkesD4KK9dNbgyO5D",
                    "profile": {
                      "name": "Eko Fresh"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "d465e72cf8573ced392a",
            "track": {
              "uri": "spotify:track:4a1WLOoydq7u011UG9jjC9",
              "name": "Krvn",
              "playcount": "146698773",
              "discNumber": 1,
              "trackNumber": 6,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 171880
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "b13b0f5f5cc4e9cb104a",
            "track": {
              "uri": "spotify:track:4hy4nY2PiYWx8qVXjpky3P",
              "name": "Vur",
              "playcount": "78647451",
              "discNumber": 1,
              "trackNumber": 7,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 155010
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "cc1f597105ee3f74e5ef",
            "track": {
              "uri": "spotify:track:4PpYi6USHlY7OhOcDASnD3",
              "name": "Davetiye",
              "playcount": "36445082",
              "discNumber": 1,
              "trackNumber": 8,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 223608
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:6dOAGo4z0syiCjbnlh4VSO",
                    "profile": {
                      "name": "Critical"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "a65e4830380ecca8e75e",
            "track": {
              "uri": "spotify:track:5gx3dMxQGJ1JDw5qHarRqp",
              "name": "Elhamdulillah",
              "playcount": "20115757",
              "discNumber": 1,
              "trackNumber": 9,
              "contentRating": {
                "label": "EXPLICIT"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 196682
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  },
                  {
                    "uri": "spotify:artist:3R27mVPp04i87RNmvysZfY",
                    "profile": {
                      "name": "Stap"
                    }
                  }
                ]
              }
            }
          },
          {
            "uid": "e540efaba938853ed3b6",
            "track": {
              "uri": "spotify:track:4PUniKS3Cywu23xjdtoji5",
              "name": "Outro",
              "playcount": "112555931",
              "discNumber": 1,
              "trackNumber": 10,
              "contentRating": {
                "label": "NONE"
              },
              "relinkingInformation": null,
              "duration": {
                "totalMilliseconds": 192694
              },
              "playability": {
                "playable": true
              },
              "artists": {
                "items": [
                  {
                    "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
                    "profile": {
                      "name": "UZI"
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  }
}
```
    """
    url = "https://spotify81.p.rapidapi.com/album_tracks"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": id, "offset": offset, "limit": limit}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "spotify81.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

