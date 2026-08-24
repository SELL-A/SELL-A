import os
import requests
def Get_Article_Content(url):
    """
    :API_description: This endpoint retrieves the full content of a specific article based on the url
    :param url: The URL of the article to retrieve(come from Search_News.py).
    :response_schema: 
    ```json{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "excerpt": {
          "type": "string"
        },
        "thumbnail": {
          "type": "string"
        },
        "language": {
          "type": "string"
        },
        "paywall": {
          "type": "boolean"
        },
        "content": {
          "type": "string"
        },
        "contentLength": {
          "type": "integer"
        },
        "date": {
          "type": "string"
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
              "type": "string"
            },
            "favicon": {
              "type": "string"
            }
          },
          "required": ["name", "url", "favicon"]
        }
      },
      "required": ["title", "url", "excerpt", "thumbnail", "language", "paywall", "content", "contentLength", "date", "authors", "keywords", "publisher"]
    }
  },
  "required": ["success", "data"]
}```
    """
    endpoint = "https://news-api14.p.rapidapi.com/v2/article"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"url": url}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "news-api14.p.rapidapi.com"
    }
    response = requests.get(endpoint, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")