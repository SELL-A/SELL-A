import os
import requests

def Retrieve_Address_Information_from_GSTIN(gstin):
    """
    :API_description: Retrieve detailed address information for a given GSTIN, including both principal and additional business locations.
    :param gstin: The GSTIN for which the address is to be retrieved(e.g. 18AAACR5055K1Z6).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "place_of_business_additional": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "address": {
                "type": "object",
                "properties": {
                  "building_name": { "type": "string" },
                  "street": { "type": "string" },
                  "location": { "type": "string" },
                  "door_num": { "type": "string" },
                  "state": { "type": "string" },
                  "floor_num": { "type": "string" },
                  "lattitude": { "type": "string" },
                  "longitude": { "type": "string" },
                  "district": { "type": "string" },
                  "city": { "type": "string" },
                  "pin_code": { "type": "string" }
                },
                "required": [
                  "building_name",
                  "street",
                  "location",
                  "door_num",
                  "state",
                  "floor_num",
                  "lattitude",
                  "longitude",
                  "district",
                  "city",
                  "pin_code"
                ]
              },
              "nature": {
                "type": "array",
                "items": { "type": "string" }
              }
            },
            "required": ["address", "nature"]
          }
        },
        "place_of_business_principal": {
          "type": "object",
          "properties": {
            "address": {
              "type": "object",
              "properties": {
                "building_name": { "type": "string" },
                "street": { "type": "string" },
                "location": { "type": "string" },
                "door_num": { "type": "string" },
                "state": { "type": "string" },
                "floor_num": { "type": "string" },
                "lattitude": { "type": "string" },
                "longitude": { "type": "string" },
                "district": { "type": "string" },
                "city": { "type": "string" },
                "pin_code": { "type": "string" }
              },
              "required": [
                "building_name",
                "street",
                "location",
                "door_num",
                "state",
                "floor_num",
                "lattitude",
                "longitude",
                "district",
                "city",
                "pin_code"
              ]
            },
            "nature": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["address", "nature"]
        }
      },
      "required": ["place_of_business_additional", "place_of_business_principal"]
    }
  },
  "required": ["data"]
}
```
    """
    url = f"https://powerful-gstin-tool.p.rapidapi.com/v1/gstin/{gstin}/address"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "powerful-gstin-tool.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

