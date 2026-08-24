import os
import requests

def Supported_Topics():
    """
    :API_description: Retrieve specific supported Topics.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the API request was successful."
    },
    "data": {
      "type": "array",
      "description": "List of news categories.",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the category."
          },
          "name": {
            "type": "string",
            "description": "Display name of the category."
          },
          "subtopics": {
            "type": "array",
            "description": "List of subtopics within the category.",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string",
                  "description": "Unique identifier for the subtopic."
                },
                "name": {
                  "type": "string",
                  "description": "Display name of the subtopic."
                }
              },
              "required": ["id", "name"]
            }
          }
        },
        "required": ["id", "name", "subtopics"]
      }
    }
  },
  "required": ["success", "data"]
}
```
    """
    url = "https://news-api14.p.rapidapi.com/v2/info/topics"
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

if __name__ == '__main__':
    print(Supported_Topics())