import os
import requests

def Social_Media_News_in_Russian():
    """
    :API_description: Retrieve a list of social media news articles in Russian, including details like publication date, title, and URL.
    :param: None
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
                  "type": "string"
                },
                "publishedat": {
                  "type": "string",
                  "format": "date-time"
                },
                "title": {
                  "type": "string"
                },
                "url": {
                  "type": "string",
                  "format": "uri"
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
    url = "https://onelike1.p.rapidapi.com/serviceru/news"
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