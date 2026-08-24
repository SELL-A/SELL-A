import os
import requests

def auto_complete(term, locale):
    """
    :API_description: Provides suggestions for completing a word or phrase, useful for search or content generation.
    :param term: The search term for which auto-complete suggestions are needed.
    :param locale: The locale for the search results, e.g., 'en-US'.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "hints": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "term": {
            "type": "string",
            "description": "A phrase or expression related to a specific topic or theme."
          }
        },
        "required": ["term"]
      }
    }
  },
  "required": ["hints"]
}
    ```
    """
    url = "https://shazam.p.rapidapi.com/v2/auto-complete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"term": term, "locale": locale}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "shazam.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
