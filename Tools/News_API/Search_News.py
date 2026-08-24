import os
import requests

def Search_News(query):
    """
    :API_description: This endpoint allows you to search for news articles based on keywords, dates, and other filters
    :param query: The search term (e.g., "nasa")
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "url": {
            "type": "string",
            "format": "uri"
          },
          "excerpt": {
            "type": "string"
          },
          "thumbnail": {
            "type": "string",
            "format": "uri"
          },
          "language": {
            "type": "string"
          },
          "paywall": {
            "type": "boolean"
          },
          "contentLength": {
            "type": "integer"
          },
          "date": {
            "type": "string",
            "format": "date-time"
          },
          "authors": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "keywords": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "publisher": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "url": {
                "type": "string",
                "format": "uri"
              },
              "favicon": {
                "type": "string",
                "format": "uri"
              }
            },
            "required": ["name", "url", "favicon"]
          }
        },
        "required": ["title", "url", "excerpt", "thumbnail", "language", "paywall", "contentLength", "date", "authors", "keywords", "publisher"]
      }
    },
    "size": {
      "type": "integer"
    },
    "totalHits": {
      "type": "integer"
    },
    "hitsPerPage": {
      "type": "integer"
    },
    "page": {
      "type": "integer"
    },
    "totalPages": {
      "type": "integer"
    },
    "timeMs": {
      "type": "integer"
    }
  },
  "required": ["success", "data", "size", "totalHits", "hitsPerPage", "page", "totalPages", "timeMs"]
}
    ```
    """
    url = "https://news-api14.p.rapidapi.com/v2/search/articles"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "news-api14.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

