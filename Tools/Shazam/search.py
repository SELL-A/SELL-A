import os
import requests

def search(term, locale="en-US", offset=0, limit=5):
    """
    :API_description: Search for tracks and artists based on a given term, returning detailed metadata including track title, artist, and shareable links suitable for integration with music streaming platforms.
    :param term: The search term for the music track.
    :param locale: The locale for the search results, default is "en-US".
    :param offset: The offset for pagination, default is 0.
    :param limit: The maximum number of results to return, default is 5.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "tracks": {
      "type": "object",
      "properties": {
        "hits": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "track": {
                "type": "object",
                "properties": {
                  "layout": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string"
                  },
                  "key": {
                    "type": "string"
                  },
                  "title": {
                    "type": "string"
                  },
                  "subtitle": {
                    "type": "string"
                  },
                  "share": {
                    "type": "object",
                    "properties": {
                      "subject": {
                        "type": "string"
                      },
                      "text": {
                        "type": "string"
                      },
                      "href": {
                        "type": "string"
                      },
                      "image": {
                        "type": "string"
                      },
                      "twitter": {
                        "type": "string"
                      },
                      "html": {
                        "type": "string"
                      },
                      "avatar": {
                        "type": "string"
                      },
                      "snapchat": {
                        "type": "string"
                      }
                    },
                    "required": ["subject", "text", "href", "image", "twitter", "html", "avatar", "snapchat"]
                  },
                  "images": {
                    "type": "object",
                    "properties": {
                      "background": {
                        "type": "string"
                      },
                      "coverart": {
                        "type": "string"
                      },
                      "coverarthq": {
                        "type": "string"
                      },
                      "joecolor": {
                        "type": "string"
                      }
                    },
                    "required": ["background", "coverart", "coverarthq", "joecolor"]
                  },
                  "hub": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string"
                      },
                      "image": {
                        "type": "string"
                      },
                      "actions": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "string"
                            },
                            "type": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "uri": {
                              "type": "string"
                            }
                          },
                          "required": ["name", "type"]
                        }
                      },
                      "options": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "caption": {
                              "type": "string"
                            },
                            "actions": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "name": {
                                    "type": "string"
                                  },
                                  "type": {
                                    "type": "string"
                                  },
                                  "uri": {
                                    "type": "string"
                                  }
                                },
                                "required": ["name", "type", "uri"]
                              }
                            },
                            "beacondata": {
                              "type": "object",
                              "properties": {
                                "type": {
                                  "type": "string"
                                },
                                "providername": {
                                  "type": "string"
                                }
                              },
                              "required": ["type", "providername"]
                            },
                            "image": {
                              "type": "string"
                            },
                            "type": {
                              "type": "string"
                            },
                            "listcaption": {
                              "type": "string"
                            },
                            "overflowimage": {
                              "type": "string"
                            },
                            "colouroverflowimage": {
                              "type": "boolean"
                            },
                            "providername": {
                              "type": "string"
                            }
                          },
                          "required": ["caption", "actions", "beacondata", "image", "type", "listcaption", "overflowimage", "colouroverflowimage", "providername"]
                        }
                      },
                      "providers": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "caption": {
                              "type": "string"
                            },
                            "images": {
                              "type": "object",
                              "properties": {
                                "overflow": {
                                  "type": "string"
                                },
                                "default": {
                                  "type": "string"
                                }
                              },
                              "required": ["overflow", "default"]
                            },
                            "actions": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "name": {
                                    "type": "string"
                                  },
                                  "type": {
                                    "type": "string"
                                  },
                                  "uri": {
                                    "type": "string"
                                  }
                                },
                                "required": ["name", "type", "uri"]
                              }
                            },
                            "type": {
                              "type": "string"
                            }
                          },
                          "required": ["caption", "images", "actions", "type"]
                        }
                      },
                      "explicit": {
                        "type": "boolean"
                      },
                      "displayname": {
                        "type": "string"
                      }
                    },
                    "required": ["type", "image", "actions", "options", "providers", "explicit", "displayname"]
                  },
                  "artists": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "adamid": {
                          "type": "string"
                        }
                      },
                      "required": ["id", "adamid"]
                    }
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "required": ["layout", "type", "key", "title", "subtitle", "share", "images", "hub", "artists", "url"]
              }
            },
            "required": ["track"]
          }
        }
      },
      "required": ["hits"]
    }
  },
  "required": ["tracks"]
}
```
    """
    url = "https://shazam.p.rapidapi.com/v2/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"term": term, "locale": locale, "offset": str(offset), "limit": str(limit)}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "shazam.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
if __name__ == "__main__":
    results = search(term="Hello", locale="en-US", offset=0, limit=10)
    print(results)