import os
import requests

def Album_metadata(id):
    """
    :API_description: Retrieve comprehensive details about a specific album, including its URI, name, artists, cover art, tracks, and additional metadata.
    :param id: The unique identifier for the album(e.g., "3IBcauSj5M2A6lTeffJzdv").
    :response_schema: 
    ```json
{
  "data": {
    "album": {
      "uri": "spotify:album:3IBcauSj5M2A6lTeffJzdv",
      "name": "Kan",
      "artists": {
        "totalCount": 1,
        "items": [
          {
            "id": "51DevdOxIJin6DB1FXJpD1",
            "uri": "spotify:artist:51DevdOxIJin6DB1FXJpD1",
            "profile": {
              "name": "UZI"
            },
            "visuals": {
              "avatarImage": {
                "sources": [
                  {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebfa27f66f319b25d81452b876",
                    "width": 640,
                    "height": 640
                  },
                  {
                    "url": "https://i.scdn.co/image/ab6761610000f178fa27f66f319b25d81452b876",
                    "width": 160,
                    "height": 160
                  },
                  {
                    "url": "https://i.scdn.co/image/ab67616100005174fa27f66f319b25d81452b876",
                    "width": 320,
                    "height": 320
                  }
                ]
              }
            },
            "sharingInfo": {
              "shareUrl": "https://open.spotify.com/artist/51DevdOxIJin6DB1FXJpD1?si=TIWmsSW0RvCxl9E2j18wxQ"
            }
          }
        ]
      },
      "coverArt": {
        "extractedColors": {
          "colorRaw": {
            "hex": "#404040"
          },
          "colorLight": {
            "hex": "#767676"
          },
          "colorDark": {
            "hex": "#404040"
          }
        },
        "sources": [
          {
            "url": "https://i.scdn.co/image/ab67616d00001e0267c738a703dc979f5c3c52ef",
            "width": 300,
            "height": 300
          },
          {
            "url": "https://i.scdn.co/image/ab67616d0000485167c738a703dc979f5c3c52ef",
            "width": 64,
            "height": 64
          },
          {
            "url": "https://i.scdn.co/image/ab67616d0000b27367c738a703dc979f5c3c52ef",
            "width": 640,
            "height": 640
          }
        ]
      },
      "discs": {
        "totalCount": 1,
        "items": [
          {
            "number": 1,
            "tracks": {
              "totalCount": 10
            }
          }
        ]
      },
      "tracks": {
        "totalCount": 10,
        "items": [
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 211016
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 185458
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 200000
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 243205
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 152301
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 171880
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 155010
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 223608
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 196682
              }
            }
          },
          {
            "track": {
              "playability": {
                "playable": true,
                "reason": "PLAYABLE"
              },
              "duration": {
                "totalMilliseconds": 192694
              }
            }
          }
        ]
      },
      "releases": {
        "totalCount": 0,
        "items": []
      },
      "type": "ALBUM",
      "date": {
        "isoString": "2021-03-19T00:00:00Z",
        "precision": "DAY"
      },
      "playability": {
        "playable": true,
        "reason": "PLAYABLE"
      },
      "label": "M.O.B. Entertainment",
      "copyright": {
        "totalCount": 2,
        "items": [
          {
            "type": "C",
            "text": "2021 M.O.B Entertainment Associated Label Of Govinet"
          },
          {
            "type": "P",
            "text": "2021 M.O.B Entertainment Associated Label Of Govinet"
          }
        ]
      },
      "courtesyLine": "",
      "sharingInfo": {
        "shareUrl": "https://open.spotify.com/album/3IBcauSj5M2A6lTeffJzdv?si=i9HB47guQxmY-ASxRMhr0A",
        "shareId": "i9HB47guQxmY-ASxRMhr0A"
      },
      "moreAlbumsByArtist": {
        "items": [
          {
            "discography": {
              "popularReleases": {
                "items": [
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "7wOVZ7Rjv27Gl0kuMhEAyS",
                          "uri": "spotify:album:7wOVZ7Rjv27Gl0kuMhEAyS",
                          "name": "Mortal Kombat",
                          "date": {
                            "year": 2026
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e02f28269ed4bbcd8ebc756d198",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d00004851f28269ed4bbcd8ebc756d198",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b273f28269ed4bbcd8ebc756d198",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "fKSY7O6rQd-rSqJe2gxbCg",
                            "shareUrl": "https://open.spotify.com/album/7wOVZ7Rjv27Gl0kuMhEAyS?si=fKSY7O6rQd-rSqJe2gxbCg"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "7GTNIfApsUZTP72J4r7Pv8",
                          "uri": "spotify:album:7GTNIfApsUZTP72J4r7Pv8",
                          "name": "NEON",
                          "date": {
                            "year": 2025
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e02f2ea9ce778b215eec5cb8bff",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d00004851f2ea9ce778b215eec5cb8bff",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b273f2ea9ce778b215eec5cb8bff",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "NIXjeEnvTwCEU7W5vn8IUQ",
                            "shareUrl": "https://open.spotify.com/album/7GTNIfApsUZTP72J4r7Pv8?si=NIXjeEnvTwCEU7W5vn8IUQ"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "3IBcauSj5M2A6lTeffJzdv",
                          "uri": "spotify:album:3IBcauSj5M2A6lTeffJzdv",
                          "name": "Kan",
                          "date": {
                            "year": 2021
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e0267c738a703dc979f5c3c52ef",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000485167c738a703dc979f5c3c52ef",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b27367c738a703dc979f5c3c52ef",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "aJZpKF21R1eNvdKPHc0IfQ",
                            "shareUrl": "https://open.spotify.com/album/3IBcauSj5M2A6lTeffJzdv?si=aJZpKF21R1eNvdKPHc0IfQ"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "4Y85xXiGtuA1moIlx5JMZV",
                          "uri": "spotify:album:4Y85xXiGtuA1moIlx5JMZV",
                          "name": "9",
                          "date": {
                            "year": 2025
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e0211e86ccf18877dc571196ad4",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000485111e86ccf18877dc571196ad4",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b27311e86ccf18877dc571196ad4",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "DJ-8HKbmStCBNai2AQPGjg",
                            "shareUrl": "https://open.spotify.com/album/4Y85xXiGtuA1moIlx5JMZV?si=DJ-8HKbmStCBNai2AQPGjg"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "6nmFMrH9R3JpIgxtiJq3hY",
                          "uri": "spotify:album:6nmFMrH9R3JpIgxtiJq3hY",
                          "name": "EL CHAVO",
                          "date": {
                            "year": 2022
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e02f50cb65de3d91c7f4ac5c0af",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d00004851f50cb65de3d91c7f4ac5c0af",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b273f50cb65de3d91c7f4ac5c0af",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "hGo3zp2FRgeJF8U0cnOjpw",
                            "shareUrl": "https://open.spotify.com/album/6nmFMrH9R3JpIgxtiJq3hY?si=hGo3zp2FRgeJF8U0cnOjpw"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "65dEDwbxXWzx93f6Vs5A0Q",
                          "uri": "spotify:album:65dEDwbxXWzx93f6Vs5A0Q",
                          "name": "YOUNGSTA",
                          "date": {
                            "year": 2023
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e02330ca5eddb76b12294837a51",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d00004851330ca5eddb76b12294837a51",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b273330ca5eddb76b12294837a51",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "QxIsovNsQRWEmS4hqsO6lQ",
                            "shareUrl": "https://open.spotify.com/album/65dEDwbxXWzx93f6Vs5A0Q?si=QxIsovNsQRWEmS4hqsO6lQ"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "34hptGPWx0q7xhZ4AXJPzg",
                          "uri": "spotify:album:34hptGPWx0q7xhZ4AXJPzg",
                          "name": "Şarkılar Sokaklara Ait",
                          "date": {
                            "year": 2025
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e0237f584dbc35b376b0407884f",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000485137f584dbc35b376b0407884f",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b27337f584dbc35b376b0407884f",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "kwS7P_lMS7OZefBjcTWXqQ",
                            "shareUrl": "https://open.spotify.com/album/34hptGPWx0q7xhZ4AXJPzg?si=kwS7P_lMS7OZefBjcTWXqQ"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "2dcyBRt4q4QJBaujkdIb2X",
                          "uri": "spotify:album:2dcyBRt4q4QJBaujkdIb2X",
                          "name": "Output Nr.1",
                          "date": {
                            "year": 2019
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e02ced57207fd5ba0a724dd9c3d",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d00004851ced57207fd5ba0a724dd9c3d",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b273ced57207fd5ba0a724dd9c3d",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "eQonku50TXq13kobY4gE9g",
                            "shareUrl": "https://open.spotify.com/album/2dcyBRt4q4QJBaujkdIb2X?si=eQonku50TXq13kobY4gE9g"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "5mWXaZ7MlKvbdnLPZ1UlOs",
                          "uri": "spotify:album:5mWXaZ7MlKvbdnLPZ1UlOs",
                          "name": "Yaşıyoken Anla",
                          "date": {
                            "year": 2026
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e021bc39f52aa4390d0d1144a9e",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d000048511bc39f52aa4390d0d1144a9e",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b2731bc39f52aa4390d0d1144a9e",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "lpSPQTVLSwOMDeAngFMPIg",
                            "shareUrl": "https://open.spotify.com/album/5mWXaZ7MlKvbdnLPZ1UlOs?si=lpSPQTVLSwOMDeAngFMPIg"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "releases": {
                      "items": [
                        {
                          "id": "2jCg9W89pwMWmawyBUTm3d",
                          "uri": "spotify:album:2jCg9W89pwMWmawyBUTm3d",
                          "name": "Paranoya",
                          "date": {
                            "year": 2020
                          },
                          "coverArt": {
                            "sources": [
                              {
                                "url": "https://i.scdn.co/image/ab67616d00001e02bb8696887be536014ab5ec62",
                                "width": 300,
                                "height": 300
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d00004851bb8696887be536014ab5ec62",
                                "width": 64,
                                "height": 64
                              },
                              {
                                "url": "https://i.scdn.co/image/ab67616d0000b273bb8696887be536014ab5ec62",
                                "width": 640,
                                "height": 640
                              }
                            ]
                          },
                          "playability": {
                            "playable": true,
                            "reason": "PLAYABLE"
                          },
                          "sharingInfo": {
                            "shareId": "pygIT3GYRPC_WRDvJhjiJw",
                            "shareUrl": "https://open.spotify.com/album/2jCg9W89pwMWmawyBUTm3d?si=pygIT3GYRPC_WRDvJhjiJw"
                          }
                        }
                      ]
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
    url = "https://spotify81.p.rapidapi.com/album_metadata"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "spotify81.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

