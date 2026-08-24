import os
import requests

def Get_Random_Article():
    """
    :API_description: This endpoint retrieves a random article from the available news articles. You can filter the results by language and topic
    :param None
    :response_schema: 
    ```json
{
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
}
```
    """
    url = "https://news-api14.p.rapidapi.com/v2/article/random"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "news-api14.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")