import os
import requests

def Search_GST_by_Company_Name(name):
    """
    :API_description: Retrieve GST numbers and corresponding company names that match your search term.
    :param name: The name of the entity to search for GSTIN information(e.g. "ABC Corp").
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
          "name": {
            "type": "string",
            "description": "The name of the entity or business."
          },
          "gstin": {
            "type": "string",
            "description": "The GST Identification Number (GSTIN) of the entity."
          },
          "state": {
            "type": "string",
            "description": "The state where the entity is registered."
          }
        },
        "required": ["name", "gstin", "state"]
      }
    }
  },
  "required": ["data"]
}
```
    """
    url = "https://powerful-gstin-tool.p.rapidapi.com/v1/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"name": name}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "powerful-gstin-tool.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")