import os
import requests
def Search(q):
    """
    :API_description: It can be used to look up the details of a given address from a search query. The search query will match against the post code, street name, region, locality or area.
    :param q: The query string to search for (e.g., a location or address).
    :response_schema: 
    ```json
JSON_schema
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates whether the API request was successful."
    },
    "results": {
      "type": "array",
      "description": "An array of location objects matching the query.",
      "items": {
        "type": "object",
        "properties": {
          "postCode": {
            "type": "string",
            "description": "The full postal code, typically including a space."
          },
          "postCodeTrimmed": {
            "type": "string",
            "description": "The postal code without spaces, often used for machine processing."
          },
          "streetName": {
            "type": "string",
            "description": "The name of the street or thoroughfare."
          },
          "longitude": {
            "type": "number",
            "description": "The geographic longitude coordinate (WGS84)."
          },
          "latitude": {
            "type": "number",
            "description": "The geographic latitude coordinate (WGS84)."
          },
          "plusCode": {
            "type": "string",
            "description": "A Google Plus Code representing the location as an alphanumeric code."
          },
          "region": {
            "type": "string",
            "description": "The administrative region (e.g., county or metropolitan area)."
          },
          "locality": {
            "type": "string",
            "description": "The city or town locality."
          },
          "area": {
            "type": "string",
            "description": "The broader area or country subdivision (e.g., England)."
          },
          "numUPRNs": {
            "type": "integer",
            "description": "The count of Unique Property Reference Numbers associated with this postal code."
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
    }
  },
  "required": ["success", "results"]
}
```
    """
    url = "https://uk-postcode.p.rapidapi.com/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"q": q}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "uk-postcode.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

