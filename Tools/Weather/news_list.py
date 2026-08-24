import os
import requests

def news_list(offset: int, limit: int):
    """
    :API_description: Retrieve detailed articles about weather events, focusing on specific incidents like Hurricane Milton and its impact.
    :param offset: The starting point for the list of news articles(default is 0).
    :param limit: The maximum number of news articles to retrieve(default is 10).
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string",
        "description": "Unique identifier for the article."
      },
      "assetName": {
        "type": "string",
        "description": "Path or name of the asset."
      },
      "type": {
        "type": "string",
        "description": "Type of the asset, e.g., 'article'."
      },
      "locale": {
        "type": "string",
        "description": "Locale of the article, e.g., 'en_US'."
      },
      "schema_version": {
        "type": "string",
        "description": "Version of the schema used."
      },
      "title": {
        "type": "string",
        "description": "Title of the article."
      },
      "teaserTitle": {
        "type": "string",
        "description": "Teaser title of the article."
      },
      "mobileHeadline": {
        "type": "string",
        "description": "Headline for mobile devices."
      },
      "author": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of authors of the article."
      },
      "author_bio_link": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Links to author bios."
      },
      "pcollid": {
        "type": "string",
        "description": "Collection ID of the article."
      },
      "url": {
        "type": "string",
        "description": "URL of the article."
      },
      "description": {
        "type": "string",
        "description": "Description of the article."
      },
      "createdate": {
        "type": "string",
        "format": "date-time",
        "description": "Creation date of the article."
      },
      "publishdate": {
        "type": "string",
        "format": "date-time",
        "description": "Publication date of the article."
      },
      "lastmodifieddate": {
        "type": "string",
        "format": "date-time",
        "description": "Last modification date of the article."
      },
      "adsmetrics": {
        "type": "object",
        "properties": {
          "adconfigid": {
            "type": "string"
          },
          "adzone": {
            "type": "string"
          },
          "pagecode": {
            "type": "string"
          }
        },
        "description": "Metrics related to ads."
      },
      "providerid": {
        "type": "string",
        "description": "ID of the provider."
      },
      "providername": {
        "type": "string",
        "description": "Name of the provider."
      },
      "distro": {
        "type": "boolean",
        "description": "Flag indicating if the article is distributed."
      },
      "premium": {
        "type": "boolean",
        "description": "Flag indicating if the article is premium content."
      },
      "seometa": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "keywords": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "og:image": {
            "type": "string"
          },
          "og:description": {
            "type": "string"
          },
          "canonical": {
            "type": ["string", "null"]
          }
        },
        "description": "SEO metadata for the article."
      },
      "interests": {
        "type": "object",
        "properties": {
          "categoryName": {
            "type": "string"
          },
          "categoryId": {
            "type": "string"
          },
          "backgroundColorName": {
            "type": "string"
          },
          "backgroundColorCode": {
            "type": "string"
          }
        },
        "description": "Interest categories and background colors."
      },
      "tags": {
        "type": "object",
        "properties": {
          "geo": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "keyword": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "iab": {
            "type": "object",
            "properties": {
              "v1": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "v2": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "v3": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          },
          "ai": {
            "type": "object",
            "properties": {
              "v1": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "v2": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "v3": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          },
          "storm": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "entitlements": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "description": "Tags related to geography, keywords, IAB categories, AI categories, storm, and entitlements."
      },
      "variants": {
        "type": "object",
        "additionalProperties": {
          "type": "string"
        },
        "description": "Variants of images or other assets."
      },
      "body": {
        "type": "string",
        "description": "Body content of the article."
      },
      "flags": {
        "type": "object",
        "additionalProperties": {
          "type": "boolean"
        },
        "description": "Flags indicating various properties or states."
      },
      "wxnodes": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "schema_version": {
              "type": "string"
            },
            "options": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "assetid": {
              "type": "string"
            },
            "clipid": {
              "type": "string"
            },
            "collection": {
              "type": "string"
            },
            "collection_name": {
              "type": "string"
            },
            "playlist_type": {
              "type": "string"
            },
            "links": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "align": {
              "type": "string"
            },
            "sizecode": {
              "type": "string"
            },
            "credit": {
              "type": "string"
            },
            "linkurl": {
              "type": "string"
            },
            "synopsis": {
              "type": "string"
            },
            "twitter_widget": {
              "type": "object",
              "properties": {
                "embed_text": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "embed_options": {
                  "type": "object",
                  "properties": {
                    "handle": {
                      "type": "string"
                    },
                    "tweet_id": {
                      "type": "string"
                    }
                  }
                }
              }
            },
            "caption": {
              "type": "string"
            }
          }
        },
        "description": "Nodes related to weather content."
      },
      "source_guid": {
        "type": "string",
        "description": "Source GUID of the article."
      },
      "source_name": {
        "type": "string",
        "description": "Name of the source."
      },
      "story_brief": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Brief summary of the story."
      },
      "partner_byline": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Bylines from partners."
      },
      "page_template": {
        "type": "string",
        "description": "Template used for the article page."
      }
    },
    "required": [
      "id",
      "assetName",
      "type",
      "locale",
      "schema_version",
      "title",
      "teaserTitle",
      "mobileHeadline",
      "author",
      "author_bio_link",
      "pcollid",
      "url",
      "description",
      "createdate",
      "publishdate",
      "lastmodifieddate",
      "adsmetrics",
      "providerid",
      "providername",
      "distro",
      "premium",
      "seometa",
      "interests",
      "tags",
      "variants",
      "body",
      "flags",
      "wxnodes",
      "source_guid",
      "source_name",
      "story_brief",
      "partner_byline",
      "page_template"
    ]
  }
}
```
    """
    url = "https://weather338.p.rapidapi.com/news/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"offset": offset, "limit": limit}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weather338.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

