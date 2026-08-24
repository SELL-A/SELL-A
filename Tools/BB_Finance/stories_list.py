import os
import requests

def stories_list(id, template):
    """
    :API_description: Retrieve a list of market-related articles, specifically focusing on currencies, with metadata including title, publication timestamp, and URLs.
    :param id: The currency identifier (e.g., 'usdjpy').
    :param template: The template type for the stories (e.g., 'CURRENCY').
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "stories": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "resourceType": {
            "type": "string",
            "description": "Type of the resource, always 'Story' in this context."
          },
          "card": {
            "type": "string",
            "description": "Type of the card, always 'article' in this context."
          },
          "title": {
            "type": "string",
            "description": "Title of the article."
          },
          "published": {
            "type": "integer",
            "description": "Timestamp indicating when the article was published."
          },
          "internalID": {
            "type": "string",
            "description": "Unique identifier for the article."
          },
          "thumbnailImage": {
            "type": "string",
            "description": "URL to the thumbnail image of the article."
          },
          "primarySite": {
            "type": "string",
            "description": "Primary site or category where the article is published."
          },
          "shortURL": {
            "type": "string",
            "description": "Short URL to the article."
          },
          "longURL": {
            "type": "string",
            "description": "Full URL to the article."
          },
          "label": {
            "type": "string",
            "description": "Optional label categorizing the article, e.g., 'Currencies'."
          }
        },
        "required": [
          "resourceType",
          "card",
          "title",
          "published",
          "internalID",
          "thumbnailImage",
          "primarySite",
          "shortURL",
          "longURL"
        ]
      }
    },
    "title": {
      "type": "string",
      "description": "Title of the collection of stories, e.g., 'Currencies'."
    }
  },
  "required": [
    "stories",
    "title"
  ]
}
```
    """
    url = "https://bb-finance.p.rapidapi.com/stories/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": id, "template": template}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "bb-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")