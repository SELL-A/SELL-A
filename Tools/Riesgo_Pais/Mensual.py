import os
import requests

def Mensual():
    """
    :API_description: Retrieves a time series of monthly data, including dates and corresponding integer values.
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
        "description": "A date in the format DD-MM-YYYY"
      },
      "value": {
        "type": "integer",
        "description": "An integer value associated with the date"
      }
    },
    "required": ["date", "value"]
  }
}
    ```
    """
    url = "https://riesgo-pais.p.rapidapi.com/api/riesgopais/mensual"
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

