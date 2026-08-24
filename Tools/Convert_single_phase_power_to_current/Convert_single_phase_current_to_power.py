import os
import requests

def Convert_single_phase_current_to_power(current, voltage, powerfactor):
    """
    :API_description: This API converts a given current in amperes to power in watts, considering optional voltage and power factor inputs.
    :param current: The electrical current in amperes.
    :param voltage: The voltage in volts (optional).
    :param powerfactor: The power factor, a dimensionless number between 0 and 1 (optional).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "power": {
      "type": "number",
      "description": "Represents the power value, likely in a unit such as watts."
    }
  },
  "required": ["power"]
}
```
    """
    url = "https://electrical-units.p.rapidapi.com/current_to_power/single_phase"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"current": current, "voltage": voltage, "powerfactor": powerfactor}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "electrical-units.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
