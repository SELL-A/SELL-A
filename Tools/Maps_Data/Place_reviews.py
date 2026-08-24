import os
import requests

def Place_reviews(business_id, country):
    """
    :API_description: Retrieves detailed reviews and information about a specific business, including its operating status, customer feedback, and contact details.
    :param business_id: The unique identifier for the business.
    :param country: The country code for filtering reviews(e.g., 'us').

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
          "type": "integer"
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
          "type": "string"
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
            "type": "object",
            "properties": {
              "url": {
                "type": "string"
              },
              "description": {
                "type": "string"
              }
            }
          }
        },
        "description": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "reviews": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "user_name": {
                "type": "string"
              },
              "user_avatar": {
                "type": "string"
              },
              "user_link": {
                "type": "string"
              },
              "review_id": {
                "type": "string"
              },
              "review_time": {
                "type": "string"
              },
              "review_timestamp": {
                "type": "integer"
              },
              "review_link": {
                "type": "string"
              },
              "review_text": {
                "type": "string"
              },
              "review_photos": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "business_response_text": {
                "type": ["string", "null"]
              },
              "review_services": {
                "type": "object",
                "properties": {
                  "Service": {
                    "type": "integer"
                  },
                  "Meal type": {
                    "type": "string"
                  },
                  "Food": {
                    "type": "integer"
                  },
                  "Atmosphere": {
                    "type": "integer"
                  }
                }
              },
              "translations": {
                "type": "object",
                "properties": {
                  "en": {
                    "type": "string"
                  }
                }
              },
              "review_rate": {
                "type": "integer"
              },
              "review_cursor": {
                "type": "string"
              }
            }
          }
        }
      }
    }
  }
}
```
    """
    url = "https://maps-data.p.rapidapi.com/reviews.php"
    querystring = {
        "business_id": business_id,
        "country": country
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