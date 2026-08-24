import os
import requests

def Novels(page_size, page):
    """
    :API_description: Retrieve detailed information about novels, including their ID, name, description, and status, along with pagination metadata.
    :param page_size: The number of novels to return per page (default: 2).
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
          "textDetailId": {
            "type": "integer",
            "description": "Unique identifier for the text detail."
          },
          "name": {
            "type": "string",
            "description": "Name of the text detail."
          },
          "slug": {
            "type": "string",
            "description": "URL-friendly version of the name."
          },
          "description": {
            "type": "string",
            "description": "Detailed description of the text detail."
          },
          "status": {
            "type": "string",
            "description": "Status of the text detail (e.g., 'Completed', 'Ongoing')."
          },
          "locale": {
            "type": "string",
            "description": "Locale or language of the text detail."
          },
          "alternativeNames": {
            "type": ["null", "string"],
            "description": "Alternative names for the text detail, if any."
          }
        },
        "required": ["textDetailId", "name", "slug", "description", "status", "locale", "alternativeNames"]
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "totalItems": {
          "type": "integer",
          "description": "Total number of items available."
        },
        "itemCount": {
          "type": "integer",
          "description": "Number of items in the current response."
        },
        "itemsPerPage": {
          "type": "integer",
          "description": "Number of items per page."
        },
        "totalPages": {
          "type": "integer",
          "description": "Total number of pages."
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
    url = "https://anime-manga-and-novels-api.p.rapidapi.com/novels"
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