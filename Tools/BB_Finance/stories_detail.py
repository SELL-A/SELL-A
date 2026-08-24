import os
import requests

def stories_detail(internalID):
    """
    :API_description: Retrieve comprehensive details about a specific article, including metadata and content information.
    :param internalID: The unique identifier for the story.
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "Unique identifier for the article, including the date and a brief description."
        },
        "title": {
          "type": "string",
          "description": "Title of the article."
        },
        "summary": {
          "type": "string",
          "description": "Summary of the article."
        },
        "secondaryBrands": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of secondary brands associated with the article."
        },
        "internalID": {
          "type": "string",
          "description": "Internal identifier for the article."
        },
        "byline": {
          "type": "string",
          "description": "Author of the article."
        },
        "archived": {
          "type": "boolean",
          "description": "Indicates if the article is archived."
        },
        "longURL": {
          "type": "string",
          "description": "Full URL to the article."
        },
        "shortURL": {
          "type": "string",
          "description": "Shortened URL to the article."
        },
        "authoredRegion": {
          "type": "string",
          "description": "Region where the article was authored."
        },
        "primarySite": {
          "type": "string",
          "description": "Primary site where the article is published."
        },
        "brand": {
          "type": "string",
          "description": "Brand associated with the article."
        },
        "primaryCategory": {
          "type": "string",
          "description": "Primary category of the article."
        },
        "attributor": {
          "type": "string",
          "description": "Attributor of the article."
        },
        "published": {
          "type": "integer",
          "description": "Timestamp when the article was published."
        },
        "updatedAt": {
          "type": "integer",
          "description": "Timestamp when the article was last updated."
        },
        "resourceType": {
          "type": "string",
          "description": "Type of resource (e.g., Story)."
        },
        "resourceId": {
          "type": "string",
          "description": "Unique identifier for the resource."
        },
        "wordCount": {
          "type": "integer",
          "description": "Number of words in the article."
        },
        "premium": {
          "type": "boolean",
          "description": "Indicates if the article is premium content."
        },
        "readings": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "url": {
                "type": "string",
                "description": "URL to the audio reading of the article."
              },
              "voice": {
                "type": "string",
                "description": "Voice used for the audio reading."
              },
              "durationMs": {
                "type": "integer",
                "description": "Duration of the audio reading in milliseconds."
              }
            }
          },
          "description": "List of audio readings associated with the article."
        },
        "type": {
          "type": "string",
          "description": "Type of the article (e.g., article)."
        },
        "card": {
          "type": "string",
          "description": "Type of card used for the article (e.g., article)."
        },
        "abstract": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Abstract or summary points of the article."
        },
        "adParams": {
          "type": "object",
          "properties": {
            "dfpTarget": {
              "type": "object",
              "properties": {
                "ni": {
                  "type": "string",
                  "description": "Targeting information for ad placement."
                },
                "kwl": {
                  "type": "string",
                  "description": "Keyword list for ad targeting."
                },
                "sites": {
                  "type": "string",
                  "description": "Sites where the ad is targeted."
                },
                "url": {
                  "type": "string",
                  "description": "URL for ad targeting."
                },
                "adCode": {
                  "type": "string",
                  "description": "Ad code for the article."
                },
                "record": {
                  "type": "string",
                  "description": "Record information for ad targeting."
                },
                "isWeekend": {
                  "type": "boolean",
                  "description": "Indicates if the ad is targeted for weekends."
                }
              }
            }
          },
          "description": "Parameters for ad targeting."
        },
        "ledeImage": {
          "type": "object",
          "properties": {
            "imageURLs": {
              "type": "object",
              "properties": {
                "default": {
                  "type": "string",
                  "description": "Default URL for the lead image."
                },
                "large": {
                  "type": "string",
                  "description": "URL for the large version of the lead image."
                }
              }
            },
            "caption": {
              "type": "string",
              "description": "Caption for the lead image."
            },
            "credit": {
              "type": "string",
              "description": "Credit for the lead image."
            },
            "ledeImageAspectRatio": {
              "type": "number",
              "description": "Aspect ratio of the lead image."
            }
          },
          "description": "Lead image details for the article."
        },
        "securityIDs": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of security identifiers associated with the article."
        },
        "topics": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the topic."
              },
              "name": {
                "type": "string",
                "description": "Name of the topic."
              },
              "referringId": {
                "type": "string",
                "description": "Referring identifier for the topic."
              }
            }
          },
          "description": "List of topics associated with the article."
        },
        "components": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "role": {
                "type": "string",
                "description": "Role of the component (e.g., paragraph)."
              },
              "parts": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "role": {
                      "type": "string",
                      "description": "Role of the part (e.g., anchor, text)."
                    },
                    "parts": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "role": {
                            "type": "string",
                            "description": "Role of the nested part."
                          },
                          "text": {
                            "type": "string",
                            "description": "Text content of the nested part."
                          },
                          "security": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "string",
                                "description": "Text representation of the security."
                              },
                              "ticker": {
                                "type": "string",
                                "description": "Ticker symbol for the security."
                              },
                              "template": {
                                "type": "string",
                                "description": "Template used for the security."
                              },
                              "name": {
                                "type": "string",
                                "description": "Name of the security."
                              },
                              "tickerName": {
                                "type": "string",
                                "description": "Ticker name for the security."
                              },
                              "watchlist": {
                                "type": "boolean",
                                "description": "Indicates if the security is on a watchlist."
                              },
                              "symbol": {
                                "type": "string",
                                "description": "Symbol for the security."
                              },
                              "eqtIndex": {
                                "type": "boolean",
                                "description": "Indicates if the security is part of an equity index."
                              }
                            }
                          }
                        }
                      },
                      "description": "Nested parts within the component."
                    }
                  }
                },
                "description": "Parts of the component."
              }
            }
          },
          "description": "Components of the article, such as paragraphs and headers."
        },
        "themedImages": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "description": "Themed images associated with the article."
        },
        "newsletterToutLabel": {
          "type": "string",
          "description": "Label for newsletter tout."
        },
        "isMetered": {
          "type": "boolean",
          "description": "Indicates if the article is metered."
        },
        "disableAds": {
          "type": "boolean",
          "description": "Indicates if ads are disabled for the article."
        },
        "contentTags": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the content tag."
              },
              "type": {
                "type": "string",
                "description": "Type of the content tag (e.g., Company, Location)."
              },
              "derivedScore": {
                "type": "number",
                "description": "Derived score for the content tag."
              },
              "directScore": {
                "type": "number",
                "description": "Direct score for the content tag."
              }
            }
          },
          "description": "Content tags associated with the article."
        },
        "followAuthorDetails": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "boolean",
              "description": "Indicates if following the author is enabled."
            },
            "authorId": {
              "type": "string",
              "description": "Unique identifier for the author."
            },
            "authorName": {
              "type": "string",
              "description": "Name of the author."
            }
          },
          "description": "Details for following the author."
        }
      }
    }
    ```
    """
    url = "https://bb-finance.p.rapidapi.com/stories/detail"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"internalID": internalID}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "bb-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")