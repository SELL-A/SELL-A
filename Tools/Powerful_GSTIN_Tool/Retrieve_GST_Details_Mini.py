import os
import requests

def Retrieve_GST_Details_Mini(gstin):
    """
    :API_description: Retrieves essential GST registration details for a business entity using their GSTIN, including legal and trade names, registration date, and current status.
    :param gstin: The GSTIN for which the basic information is to be retrieved(e.g. 18AAACR5055K1Z6).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "gstin": {
          "type": "string",
          "description": "Unique identifier for the GST registration"
        },
        "legal_name": {
          "type": "string",
          "description": "Legal name of the business entity"
        },
        "trade_name": {
          "type": "string",
          "description": "Trade name of the business entity"
        },
        "registration_date": {
          "type": "string",
          "format": "date",
          "description": "Date of GST registration"
        },
        "business_constitution": {
          "type": "string",
          "description": "Constitution of the business (e.g., Public Limited Company)"
        },
        "type": {
          "type": "string",
          "description": "Type of GST registration (e.g., Regular)"
        },
        "status": {
          "type": "string",
          "description": "Current status of the GST registration (e.g., Active)"
        },
        "cancellation_date": {
          "type": "string",
          "format": "date",
          "description": "Date of GST cancellation, if applicable"
        },
        "business_activity_nature": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of business activities the entity is involved in"
        }
      },
      "required": [
        "gstin",
        "legal_name",
        "trade_name",
        "registration_date",
        "business_constitution",
        "type",
        "status",
        "business_activity_nature"
      ]
    }
  },
  "required": ["data"]
}
```

    """
    url = f"https://powerful-gstin-tool.p.rapidapi.com/v1/gstin/{gstin}/basic"
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

