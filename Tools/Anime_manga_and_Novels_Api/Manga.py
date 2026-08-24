import os
import requests

def Manga(page_size, page):
    """
    :API_description: Retrieve detailed information about manga titles, including their unique identifiers, names, publication status, and related metadata.
    :param page_size: The number of items per page (default: 2).
    :param page: The page number to retrieve (default: 1).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "mangaId": {
            "type": "integer",
            "description": "Unique identifier for the manga."
          },
          "name": {
            "type": "string",
            "description": "Name of the manga."
          },
          "slug": {
            "type": "string",
            "description": "URL-friendly version of the manga name."
          },
          "alternativeNames": {
            "type": "object",
            "properties": {
              "japanese": {
                "type": "string",
                "description": "Alternative Japanese name for the manga."
              }
            },
            "description": "Alternative names for the manga in different languages."
          },
          "description": {
            "type": "string",
            "description": "Description of the manga."
          },
          "status": {
            "type": "string",
            "description": "Publication status of the manga (e.g., 'Finished')."
          },
          "locale": {
            "type": "string",
            "description": "Locale setting for the manga (e.g., 'en_US')."
          },
          "volumes": {
            "type": "integer",
            "description": "Number of volumes in the manga."
          },
          "chapters": {
            "type": "integer",
            "description": "Number of chapters in the manga."
          },
          "published": {
            "type": "string",
            "description": "Publication date or date range of the manga."
          },
          "demographic": {
            "type": "string",
            "description": "Target demographic of the manga."
          },
          "related": {
            "type": "object",
            "description": "Related manga or series."
          }
        },
        "required": ["mangaId", "name", "slug", "alternativeNames", "description", "status", "locale", "volumes", "chapters", "published", "demographic", "related"]
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "totalItems": {
          "type": "integer",
          "description": "Total number of manga items available."
        },
        "itemCount": {
          "type": "integer",
          "description": "Number of manga items in the current response."
        },
        "itemsPerPage": {
          "type": "integer",
          "description": "Number of manga items per page."
        },
        "totalPages": {
          "type": "integer",
          "description": "Total number of pages available."
        },
        "currentPage": {
          "type": "integer",
          "description": "Current page number."
        }
      },
      "required": ["totalItems", "itemCount", "itemsPerPage", "totalPages", "currentPage"]
    }
  },
  "required": ["items", "meta"]
}
```
    """
    url = "https://anime-manga-and-novels-api.p.rapidapi.com/manga"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"pageSize": page_size, "page": page}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-manga-and-novels-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")