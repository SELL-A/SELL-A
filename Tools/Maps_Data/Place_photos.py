import os
import requests

def Place_photos(business_id: str, lang: str, country: str):
    """
    :API_description: Retrieve detailed information about a specific business or location, including images, address, and operational details.
    :param business_id: The unique identifier of the business for which photos are being retrieved.
    :param lang: The language code for the response (e.g., 'en' for English).
    :param country: The country code for the response (e.g., 'us' for the United States).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "business_id": {
          "type": "string"
        },
        "phone_number": {
          "type": ["null", "string"]
        },
        "name": {
          "type": "string"
        },
        "full_address": {
          "type": "string"
        },
        "latitude": {
          "type": "number"
        },
        "longitude": {
          "type": "number"
        },
        "review_count": {
          "type": "integer"
        },
        "rating": {
          "type": "number"
        },
        "timezone": {
          "type": "string"
        },
        "website": {
          "type": "string"
        },
        "website_full": {
          "type": "string"
        },
        "place_id": {
          "type": "string"
        },
        "reviews_id1": {
          "type": "string"
        },
        "reviews_id2": {
          "type": "string"
        },
        "place_link": {
          "type": "string"
        },
        "types": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "price_level": {
          "type": ["null", "integer"]
        },
        "working_hours": {
          "type": "object",
          "properties": {
            "Wednesday": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "Thursday": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "Friday": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "Saturday": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "Sunday": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "Monday": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "Tuesday": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "state": {
          "type": "string"
        },
        "photos": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "description": {
          "type": "array",
          "items": {
            "type": ["string", "null"]
          }
        },
        "cursor": {
          "type": "string"
        }
      }
    }
  }
}
```
    """
    url = "https://maps-data.p.rapidapi.com/photos.php"
    querystring = {"business_id": business_id, "lang": lang, "country": country}

    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "maps-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")