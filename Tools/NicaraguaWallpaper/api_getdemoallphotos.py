import os
import requests

def api_getdemoallphotos():
    """
    :API_description: Fetches a curated list of promoted and popular photos from Flickr, including details like photo ID, image URL, photographer's username, and last update times for both sections.
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
        "dataResponse": {
          "type": "object",
          "properties": {
            "promotion": {
              "type": "object",
              "properties": {
                "items": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "Unique identifier for the promotion item."
                      },
                      "imageUrl": {
                        "type": "string",
                        "description": "URL of the image associated with the promotion item."
                      },
                      "photoLink": {
                        "type": "string",
                        "description": "Link to the photo on the platform."
                      },
                      "username": {
                        "type": "string",
                        "description": "Username of the user who posted the photo."
                      },
                      "profile_url": {
                        "type": "string",
                        "description": "URL to the user's profile on the platform."
                      },
                      "platform": {
                        "type": "string",
                        "description": "Name of the platform where the photo is hosted."
                      }
                    },
                    "required": ["id", "imageUrl", "photoLink", "username", "profile_url", "platform"]
                  }
                },
                "lastUpdated": {
                  "type": "string",
                  "format": "date-time",
                  "description": "Timestamp indicating the last update to the promotion items."
                }
              },
              "required": ["items", "lastUpdated"]
            },
            "popular": {
              "type": "object",
              "properties": {
                "items": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "Unique identifier for the popular item."
                      },
                      "imageUrl": {
                        "type": "string",
                        "description": "URL of the image associated with the popular item."
                      },
                      "photoLink": {
                        "type": "string",
                        "description": "Link to the photo on the platform."
                      },
                      "username": {
                        "type": "string",
                        "description": "Username of the user who posted the photo."
                      },
                      "profile_url": {
                        "type": "string",
                        "description": "URL to the user's profile on the platform."
                      },
                      "platform": {
                        "type": "string",
                        "description": "Name of the platform where the photo is hosted."
                      }
                    },
                    "required": ["id", "imageUrl", "photoLink", "username", "profile_url", "platform"]
                  }
                },
                "lastUpdated": {
                  "type": "string",
                  "format": "date-time",
                  "description": "Timestamp indicating the last update to the popular items."
                }
              },
              "required": ["items", "lastUpdated"]
            }
          },
          "required": ["promotion", "popular"]
        }
      },
      "required": ["dataResponse"]
    }
  },
  "required": ["success", "dataResponse"]
}
    """
    url = "https://nicaraguawallpaper.p.rapidapi.com/api/getdemoallphotos"
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

