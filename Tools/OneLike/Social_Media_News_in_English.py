import os
import requests

def Social_Media_News_in_English():
    """
    :API_description: Retrieve a list of news articles from various English social media platforms, including details like publication time, title, and URL.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "socialmedias": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "news": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "timeago": {
                  "type": "string",
                  "description": "Time elapsed since the news was published, e.g., '5 h' for 5 hours."
                },
                "publishedat": {
                  "type": "string",
                  "description": "Date and time when the news was published, in a specific timezone format."
                },
                "title": {
                  "type": "string",
                  "description": "Title of the news article."
                },
                "url": {
                  "type": "string",
                  "description": "URL link to the full news article."
                }
              },
              "required": ["timeago", "publishedat", "title", "url"]
            }
          }
        },
        "required": ["news"]
      }
    }
  },
  "required": ["socialmedias"]
}
```
    """
    url = "https://onelike1.p.rapidapi.com/service/news"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "onelike1.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
