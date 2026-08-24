import os
import requests

def schools_list(lat, lon):
    """
    :API_description: Retrieve a list of schools categorized by type (all, primary, secondary) near a specified GEO location, including detailed school information.
    :param lat: Latitude of the location to search for schools.
    :param lon: Longitude of the location to search for schools.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "all": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "url": { "type": ["string", "null"] },
          "sector": { "type": "string" },
          "year_range": { "type": ["string", "null"] },
          "school_type": { "type": "string" },
          "address": {
            "type": "object",
            "properties": {
              "street": { "type": "string" },
              "suburb": { "type": "string" },
              "state": { "type": "string" },
              "postcode": { "type": "string" }
            },
            "required": ["street", "suburb", "state", "postcode"]
          },
          "location": {
            "type": "object",
            "properties": {
              "latitude": { "type": "number" },
              "longitude": { "type": "number" },
              "accuracy": { "type": "string" }
            },
            "required": ["latitude", "longitude", "accuracy"]
          },
          "distance": {
            "type": "object",
            "properties": {
              "value": { "type": "number" },
              "unit": { "type": "string" }
            },
            "required": ["value", "unit"]
          }
        },
        "required": ["name", "url", "sector", "year_range", "school_type", "address", "location", "distance"]
      }
    },
    "primary": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "url": { "type": ["string", "null"] },
          "sector": { "type": "string" },
          "year_range": { "type": ["string", "null"] },
          "school_type": { "type": "string" },
          "address": {
            "type": "object",
            "properties": {
              "street": { "type": "string" },
              "suburb": { "type": "string" },
              "state": { "type": "string" },
              "postcode": { "type": "string" }
            },
            "required": ["street", "suburb", "state", "postcode"]
          },
          "location": {
            "type": "object",
            "properties": {
              "latitude": { "type": "number" },
              "longitude": { "type": "number" },
              "accuracy": { "type": "string" }
            },
            "required": ["latitude", "longitude", "accuracy"]
          },
          "distance": {
            "type": "object",
            "properties": {
              "value": { "type": "number" },
              "unit": { "type": "string" }
            },
            "required": ["value", "unit"]
          }
        },
        "required": ["name", "url", "sector", "year_range", "school_type", "address", "location", "distance"]
      }
    },
    "secondary": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "url": { "type": ["string", "null"] },
          "sector": { "type": "string" },
          "year_range": { "type": ["string", "null"] },
          "school_type": { "type": "string" },
          "address": {
            "type": "object",
            "properties": {
              "street": { "type": "string" },
              "suburb": { "type": "string" },
              "state": { "type": "string" },
              "postcode": { "type": "string" }
            },
            "required": ["street", "suburb", "state", "postcode"]
          },
          "location": {
            "type": "object",
            "properties": {
              "latitude": { "type": "number" },
              "longitude": { "type": "number" },
              "accuracy": { "type": "string" }
            },
            "required": ["latitude", "longitude", "accuracy"]
          },
          "distance": {
            "type": "object",
            "properties": {
              "value": { "type": "number" },
              "unit": { "type": "string" }
            },
            "required": ["value", "unit"]
          }
        },
        "required": ["name", "url", "sector", "year_range", "school_type", "address", "location", "distance"]
      }
    }
  },
  "required": ["all", "primary", "secondary"]
}
    ```
    """
    url = "https://realty-in-au.p.rapidapi.com/schools/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"lat": lat, "lon": lon}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "realty-in-au.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


