import os
import requests

def Get_Novel_By_Id(novel_id):
    """
    :API_description: Retrieve detailed metadata about a specific text or content, identified by its unique ID.
    :param novel_id: The ID of the novel to retrieve information for.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "textDetailId": {
      "type": "integer",
      "description": "Unique identifier for the text detail."
    },
    "name": {
      "type": "string",
      "description": "Name of the text or title."
    },
    "slug": {
      "type": "string",
      "description": "URL-friendly version of the name."
    },
    "description": {
      "type": "string",
      "description": "Detailed description of the text or content."
    },
    "status": {
      "type": "string",
      "description": "Status of the text, e.g., 'Completed'."
    },
    "locale": {
      "type": "string",
      "description": "Locale or language setting for the text."
    },
    "alternativeNames": {
      "type": ["null", "string"],
      "description": "Alternative names for the text, if any."
    }
  },
  "required": ["textDetailId", "name", "slug", "description", "status", "locale", "alternativeNames"]
}
    ```
    """
    url = f"https://anime-manga-and-novels-api.p.rapidapi.com/novels/{novel_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "anime-manga-and-novels-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")