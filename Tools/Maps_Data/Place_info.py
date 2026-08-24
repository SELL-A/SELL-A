import os
import requests

def Place_info(business_id):
    """
    :API_description: Retrieves comprehensive details about a business, including its name, address, ratings, and operational hours, using its unique identifier or Google Place ID.
    :param business_id: The unique identifier for the business.
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
                "type": "string",
                "description": "Unique identifier for the business"
              },
              "phone_number": {
                "type": ["string", "null"],
                "description": "Phone number of the business"
              },
              "name": {
                "type": "string",
                "description": "Name of the business"
              },
              "full_address": {
                "type": "string",
                "description": "Full address of the business"
              },
              "latitude": {
                "type": "number",
                "description": "Latitude coordinate of the business location"
              },
              "longitude": {
                "type": "number",
                "description": "Longitude coordinate of the business location"
              },
              "review_count": {
                "type": "integer",
                "description": "Number of reviews for the business"
              },
              "rating": {
                "type": "integer",
                "description": "Average rating of the business"
              },
              "timezone": {
                "type": "string",
                "description": "Timezone of the business location"
              },
              "website": {
                "type": ["string", "null"],
                "description": "Website URL of the business"
              },
              "website_full": {
                "type": "string",
                "description": "Full website URL of the business"
              },
              "place_id": {
                "type": "string",
                "description": "Google Place ID for the business"
              },
              "place_link": {
                "type": "string",
                "description": "Link to the business on Google Maps"
              },
              "types": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "Types of the business (e.g., Corporate office)"
              },
              "price_level": {
                "type": ["integer", "null"],
                "description": "Price level of the business"
              },
              "working_hours": {
                "type": "array",
                "items": {},
                "description": "Working hours of the business"
              },
              "is_claimed": {
                "type": "boolean",
                "description": "Indicates if the business is claimed"
              },
              "state": {
                "type": ["string", "null"],
                "description": "State where the business is located"
              },
              "details": {
                "type": "array",
                "items": {},
                "description": "Additional details about the business"
              },
              "photos": {
                "type": "array",
                "items": {},
                "description": "Photos of the business"
              },
              "description": {
                "type": "array",
                "items": {},
                "description": "Description of the business"
              }
            },
            "required": [
              "business_id",
              "name",
              "full_address",
              "latitude",
              "longitude",
              "review_count",
              "rating",
              "timezone",
              "website_full",
              "place_id",
              "place_link",
              "types",
              "working_hours",
              "is_claimed",
              "details",
              "photos",
              "description"
            ]
          }
        }
      },
      "required": ["data"]
    }
    ```
    """
    url = "https://maps-data.p.rapidapi.com/place.php"
    querystring = {
        "business_id": business_id
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