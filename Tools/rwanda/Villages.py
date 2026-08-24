import os
import requests

def Villages(province, district, sector, cell):
    """
    :API_description: Retrieves a list of villages within a specified geographic area, including province, district, sector, and cell. If no parameters are provided, it returns all villages in Rwanda.
    :param province: The province in Rwanda to search within(e.g. east).
    :param district: The district within the specified province(e.g. ngoma).
    :param sector: The sector within the specified district(e.g. kibungo).
    :param cell: The cell within the specified sector(e.g. cyasemakamba).
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
      "description": "A descriptive message providing additional context about the response, often detailing the scope or result of the query."
    },
    "data": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "An array of strings representing the list of villages retrieved based on the specified geographic parameters."
    }
  },
  "required": ["status", "statusCode", "message", "data"]
}
```
    """
    url = "https://rwanda.p.rapidapi.com/villages"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"p": province, "d": district, "s": sector, "c": cell}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "rwanda.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")