import os
import requests

def Anual():
    """
    :API_description: Provides a chronological list of daily values from October 23, 2023, to January 23, 2024, likely representing financial metrics or sales data.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "date": {
        "type": "string",
        "description": "Date in the format 'dd-MM-yyyy'"
      },
      "value": {
        "type": "integer",
        "description": "Numerical value associated with the date"
      }
    },
    "required": ["date", "value"]
  }
}
    ```
    """
    url = "https://riesgo-pais.p.rapidapi.com/api/riesgopais/anual"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "riesgo-pais.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

