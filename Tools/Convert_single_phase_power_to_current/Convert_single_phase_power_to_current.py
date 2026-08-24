import os
import requests

def Convert_single_phase_power_to_current(power, voltage, powerfactor):
    """
    :API_description: This API converts a given power in watts to current in amperes, considering optional voltage and power factor inputs.
    :param power: The electrical power in watts.
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
    url = "https://electrical-units.p.rapidapi.com/power_to_current/single_phase"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"power": power, "voltage": voltage, "powerfactor": powerfactor}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "electrical-units.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        
