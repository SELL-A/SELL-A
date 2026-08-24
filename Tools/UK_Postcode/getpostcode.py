import os
import requests
from urllib.parse import quote

def getpostcode(postcode):
    """
    :API_description: Retrieve detailed location information including postal code, street name, geographic coordinates, and additional metadata.
    :param postcode: The UK postcode to retrieve information for.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates whether the API request was successful."
    },
    "result": {
      "type": "object",
      "properties": {
        "postCode": {
          "type": "string",
          "description": "The full postal code including spaces."
        },
        "postCodeTrimmed": {
          "type": "string",
          "description": "The postal code without spaces."
        },
        "streetName": {
          "type": "string",
          "description": "The name of the street."
        },
        "longitude": {
          "type": "number",
          "description": "The longitude coordinate of the location."
        },
        "latitude": {
          "type": "number",
          "description": "The latitude coordinate of the location."
        },
        "plusCode": {
          "type": "string",
          "description": "The Plus Code for the location, a geocoding system developed by Google."
        },
        "region": {
          "type": "string",
          "description": "The region or administrative area."
        },
        "locality": {
          "type": "string",
          "description": "The locality or city."
        },
        "area": {
          "type": "string",
          "description": "The larger area or country."
        },
        "numUPRNs": {
          "type": "integer",
          "description": "The number of Unique Property Reference Numbers (UPRNs) associated with the location."
        }
      },
      "required": [
        "postCode",
        "postCodeTrimmed",
        "streetName",
        "longitude",
        "latitude",
        "plusCode",
        "region",
        "locality",
        "area",
        "numUPRNs"
      ]
    }
  },
  "required": [
    "success",
    "result"
  ]
}
```

    """
    url = f"https://uk-postcode.p.rapidapi.com/getpostcode"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    params = {
        "postCode": postcode
    }
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "uk-postcode.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


        
