import os
import requests

def Provinces():
    """
    :API_description: Retrieves a list of all provinces in Rwanda.
    :param None
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
      "description": "A descriptive message providing additional context about the response."
    },
    "data": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "An array of strings representing the provinces of Rwanda."
    }
  },
  "required": ["status", "statusCode", "message", "data"]
}
```
    """
    url = "https://rwanda.p.rapidapi.com/provinces"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "rwanda.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")