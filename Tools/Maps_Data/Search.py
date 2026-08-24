import os
import requests

def Search(query):
    """
    :API_description: Retrieve detailed information about local businesses, including IDs, contact details, location, ratings, and operational hours.
    :param query: The search term, e.g., 'restaurant'.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "business_id": {
            "type": "string"
          },
          "phone_number": {
            "type": "string"
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
            "type": ["string", "null"]
          },
          "place_id": {
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
            "type": ["string", "null"]
          },
          "working_hours": {
            "type": ["object", "array"],
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
          "city": {
            "type": "string"
          },
          "is_claimed": {
            "type": "boolean"
          },
          "verified": {
            "type": "boolean"
          },
          "photos": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "src": {
                  "type": "string"
                },
                "max_size": {
                  "type": ["array", "null"],
                  "items": {
                    "type": "integer"
                  }
                },
                "min_size": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  }
                }
              }
            }
          },
          "state": {
            "type": ["string", "null"]
          },
          "description": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "business_id",
          "phone_number",
          "name",
          "full_address",
          "latitude",
          "longitude",
          "review_count",
          "rating",
          "timezone",
          "website",
          "place_id",
          "place_link",
          "types",
          "price_level",
          "working_hours",
          "city",
          "is_claimed",
          "verified",
          "photos",
          "state",
          "description"
        ]
      }
    }
  },
  "required": ["data"]
}
```
    """
    url = "https://maps-data.p.rapidapi.com/searchmaps.php"
    querystring = {
        "query": query
    }

    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "maps-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")