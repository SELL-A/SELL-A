import os
import requests

def Cells(p, d, s):
    """
    :API_description: Retrieves all cells within a specified province, district, and sector. If no parameters are provided, it returns all cells in Rwanda.
    :param p: Province code (e.g., 'east')
    :param d: District code (e.g., 'ngoma')
    :param s: Sector code (e.g., 'kibungo')
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
      "description": "An array of strings representing the list of cells retrieved based on the specified location."
    }
  },
  "required": ["status", "statusCode", "message", "data"]
}
```
    """
    url = "https://rwanda.p.rapidapi.com/cells"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"p": p, "d": d, "s": s}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "rwanda.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")