import os
import requests

def Sectors(region, district):
    """
    :API_description: Retrieves all sectors within a specified district and province, or all sectors in Rwanda if no parameters are provided.
    :param region: The region in Rwanda to query (e.g., 'east').
    :param district: The district within the region to query (e.g., 'ngoma').
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Indicates the status of the API response, typically 'success' or 'error'."
    },
    "statusCode": {
      "type": "integer",
      "description": "HTTP status code indicating the result of the API call, e.g., 200 for success."
    },
    "message": {
      "type": "string",
      "description": "A descriptive message providing additional context about the response, often detailing the parameters used or the result."
    },
    "data": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "An array of strings representing the sectors within a specified province and district."
    }
  },
  "required": ["status", "statusCode", "message", "data"]
}
```
    """
    url = "https://rwanda.p.rapidapi.com/sectors"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"p": region, "d": district}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "rwanda.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")