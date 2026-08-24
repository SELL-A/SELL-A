import os
import requests

def Retrieve_GST_Details(gstin):
    """
    :API_description: Retrieves comprehensive GST details including business registration, addresses, and activities for a specified GSTIN.
    :param gstin: The GSTIN for which details are to be fetched.
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
        "gstin": { "type": "string" },
        "legal_name": { "type": "string" },
        "state_jurisdiction": { "type": "string" },
        "centre_jurisdiction": { "type": "string" },
        "registration_date": { "type": "string" },
        "business_constitution": { "type": "string" },
        "type": { "type": "string" },
        "business_activity_nature": {
          "type": "array",
          "items": { "type": "string" }
        },
        "status": { "type": "string" },
        "cancellation_date": { "type": "string" },
        "trade_name": { "type": "string" },
        "state_jurisdiction_code": { "type": "string" },
        "centre_jurisdiction_code": { "type": "string" },
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
      "required": [
        "place_of_business_additional",
        "gstin",
        "legal_name",
        "state_jurisdiction",
        "centre_jurisdiction",
        "registration_date",
        "business_constitution",
        "type",
        "business_activity_nature",
        "status",
        "cancellation_date",
        "trade_name",
        "state_jurisdiction_code",
        "centre_jurisdiction_code",
        "place_of_business_principal"
      ]
    }
  },
  "required": ["data"]
}
```
    """
    url = f"https://powerful-gstin-tool.p.rapidapi.com/v1/gstin/{gstin}/details"
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