import os
import requests

def locations_get_details(placeid, language="en-US"):
    """
    :API_description: Retrieve comprehensive geographical and contextual information about a specific location, including coordinates, administrative details, and time zone.
    :param placeid: The unique identifier for the location(The value of placeid field returned in .../locations/search endpoint).
    :param language: The language in which the weather details should be returned. Default is "en-US".
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "location": {
      "type": "object",
      "properties": {
        "latitude": {
          "type": "number",
          "description": "Latitude of the location."
        },
        "longitude": {
          "type": "number",
          "description": "Longitude of the location."
        },
        "city": {
          "type": "string",
          "description": "Name of the city."
        },
        "locale": {
          "type": "object",
          "properties": {
            "locale1": {
              "type": ["string", "null"],
              "description": "First locale identifier."
            },
            "locale2": {
              "type": ["string", "null"],
              "description": "Second locale identifier."
            },
            "locale3": {
              "type": ["string", "null"],
              "description": "Third locale identifier."
            },
            "locale4": {
              "type": ["string", "null"],
              "description": "Fourth locale identifier."
            }
          },
          "description": "Locale-related identifiers."
        },
        "neighborhood": {
          "type": ["string", "null"],
          "description": "Name of the neighborhood."
        },
        "adminDistrict": {
          "type": "string",
          "description": "Administrative district name."
        },
        "adminDistrictCode": {
          "type": "string",
          "description": "Code for the administrative district."
        },
        "postalCode": {
          "type": "string",
          "description": "Postal code of the location."
        },
        "postalKey": {
          "type": "string",
          "description": "Composite key of postal code and country code."
        },
        "country": {
          "type": "string",
          "description": "Name of the country."
        },
        "countryCode": {
          "type": "string",
          "description": "ISO 3166-1 alpha-2 country code."
        },
        "ianaTimeZone": {
          "type": "string",
          "description": "IANA time zone identifier."
        },
        "displayName": {
          "type": "string",
          "description": "Display name of the location."
        },
        "dstEnd": {
          "type": "string",
          "format": "date-time",
          "description": "End date and time of Daylight Saving Time."
        },
        "dstStart": {
          "type": "string",
          "format": "date-time",
          "description": "Start date and time of Daylight Saving Time."
        },
        "dmaCd": {
          "type": "string",
          "description": "Designated Market Area code."
        },
        "placeId": {
          "type": "string",
          "description": "Unique identifier for the place."
        },
        "disputedArea": {
          "type": "boolean",
          "description": "Indicates if the area is disputed."
        },
        "disputedCountries": {
          "type": ["array", "null"],
          "items": {
            "type": "string"
          },
          "description": "List of countries involved in the dispute."
        },
        "disputedCountryCodes": {
          "type": ["array", "null"],
          "items": {
            "type": "string"
          },
          "description": "List of country codes involved in the dispute."
        },
        "disputedCustomers": {
          "type": ["array", "null"],
          "items": {
            "type": "string"
          },
          "description": "List of customers affected by the dispute."
        },
        "disputedShowCountry": {
          "type": "array",
          "items": {
            "type": "boolean"
          },
          "description": "Indicates if the country should be shown in the dispute context."
        },
        "canonicalCityId": {
          "type": "string",
          "description": "Canonical identifier for the city."
        },
        "countyId": {
          "type": "string",
          "description": "Identifier for the county."
        },
        "locId": {
          "type": "string",
          "description": "Unique identifier for the location."
        },
        "locationCategory": {
          "type": ["string", "null"],
          "description": "Category of the location."
        },
        "pollenId": {
          "type": "string",
          "description": "Identifier for pollen-related data."
        },
        "pwsId": {
          "type": "string",
          "description": "Personal Weather Station identifier."
        },
        "regionalSatellite": {
          "type": "string",
          "description": "Identifier for regional satellite data."
        },
        "tideId": {
          "type": "string",
          "description": "Identifier for tide-related data."
        },
        "type": {
          "type": "string",
          "description": "Type of location (e.g., city)."
        },
        "zoneId": {
          "type": "string",
          "description": "Identifier for the zone."
        },
        "displayContext": {
          "type": "string",
          "description": "Contextual information for display purposes."
        }
      },
      "required": [
        "latitude",
        "longitude",
        "city",
        "locale",
        "adminDistrict",
        "adminDistrictCode",
        "postalCode",
        "postalKey",
        "country",
        "countryCode",
        "ianaTimeZone",
        "displayName",
        "dstEnd",
        "dstStart",
        "dmaCd",
        "placeId",
        "disputedArea",
        "disputedShowCountry",
        "canonicalCityId",
        "countyId",
        "locId",
        "pollenId",
        "pwsId",
        "regionalSatellite",
        "tideId",
        "type",
        "zoneId",
        "displayContext"
      ]
    }
  },
  "required": ["location"]
}
    ```
    """
    url = "https://weather338.p.rapidapi.com/locations/get-details"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"placeid": placeid, "language": language}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weather338.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
