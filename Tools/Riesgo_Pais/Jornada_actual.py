import os
import requests

def Jornada_actual():
    """
    :API_description: Provides financial or economic data, including the latest value, date, variation, and associated country.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "ultimo": {
      "type": "string",
      "description": "The latest value or data point, represented as a string."
    },
    "fecha": {
      "type": "string",
      "description": "The date associated with the data, formatted as DD-MM-YYYY."
    },
    "variacion": {
      "type": "string",
      "description": "The variation or change in value, represented as a string with a comma as the decimal separator."
    },
    "class-variacion": {
      "type": "string",
      "description": "A class or category indicating the nature of the variation, possibly related to visual representation (e.g., 'up-rp' could indicate an upward trend with a specific representation)."
    },
    "value": {
      "type": "string",
      "description": "The value of the data point, represented as a string."
    },
    "country": {
      "type": "string",
      "description": "The country associated with the data."
    }
  },
  "required": ["ultimo", "fecha", "variacion", "class-variacion", "value", "country"]
}
```
    """
    url = "https://riesgo-pais.p.rapidapi.com/api/riesgopais"
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

