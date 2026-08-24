import os
import requests

def locations_search(query, language="en-US"):
    """
    :API_description: Retrieve detailed location data including addresses, coordinates, and time zones based on a city name or postal code.
    :param query: The search query for the location (e.g., city name).
    :param language: The language code for the response (default is "en-US").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "location": {
      "type": "object",
      "properties": {
        "address": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "adminDistrict": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "adminDistrictCode": {
          "type": "array",
          "items": {
            "type": ["string", "null"]
          }
        },
        "city": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "country": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "countryCode": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "displayName": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "displayContext": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "ianaTimeZone": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "latitude": {
          "type": "array",
          "items": {
            "type": "number"
          }
        },
        "locale": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "locale1": {
                "type": ["string", "null"]
              },
              "locale2": {
                "type": ["string", "null"]
              },
              "locale3": {
                "type": ["string", "null"]
              },
              "locale4": {
                "type": ["string", "null"]
              }
            }
          }
        },
        "longitude": {
          "type": "array",
          "items": {
            "type": "number"
          }
        },
        "neighborhood": {
          "type": "array",
          "items": {
            "type": ["string", "null"]
          }
        },
        "placeId": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "postalCode": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "postalKey": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "disputedArea": {
          "type": "array",
          "items": {
            "type": "boolean"
          }
        },
        "disputedCountries": {
          "type": "array",
          "items": {
            "type": ["string", "null"]
          }
        },
        "disputedCountryCodes": {
          "type": "array",
          "items": {
            "type": ["string", "null"]
          }
        },
        "disputedCustomers": {
          "type": "array",
          "items": {
            "type": ["string", "null"]
          }
        },
        "disputedShowCountry": {
          "type": "array",
          "items": {
            "type": "array",
            "items": {
              "type": "boolean"
            }
          }
        },
        "iataCode": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "icaoCode": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "locId": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "locationCategory": {
          "type": "array",
          "items": {
            "type": ["string", "null"]
          }
        },
        "pwsId": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "type": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    }
  }
}
    ```
    """
    url = "https://weather338.p.rapidapi.com/locations/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query, "language": language}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weather338.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

