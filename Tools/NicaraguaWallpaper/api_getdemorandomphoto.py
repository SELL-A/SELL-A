import os
import requests

def api_getdemorandomphoto():
    """
    :API_description: Retrieves metadata for a randomly selected popular photo, including its unique identifier, URL, and uploader details.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates whether the API request was successful."
    },
    "dataResponse": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "Unique identifier for the photo."
        },
        "imageUrl": {
          "type": "string",
          "format": "uri",
          "description": "URL of the photo."
        },
        "photoLink": {
          "type": "string",
          "format": "uri",
          "description": "Link to the photo on the platform."
        },
        "username": {
          "type": "string",
          "description": "Username of the photo uploader."
        },
        "platform": {
          "type": "string",
          "description": "Platform where the photo is hosted."
        },
        "profile_url": {
          "type": "string",
          "format": "uri",
          "description": "URL to the user's profile on the platform."
        }
      },
      "required": ["id", "imageUrl", "photoLink", "username", "platform", "profile_url"]
    }
  },
  "required": ["success", "dataResponse"]
}
```
    """
    url = "https://nicaraguawallpaper.p.rapidapi.com/api/getdemorandomphoto"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "nicaraguawallpaper.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

