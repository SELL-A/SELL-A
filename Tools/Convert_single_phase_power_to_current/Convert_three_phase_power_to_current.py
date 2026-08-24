import os
import requests

def Convert_three_phase_power_to_current(power, voltage, powerfactor):
    """
    :API_description: This API converts three-phase power in watts to current in amperes, considering optional parameters for power factor and voltage.
    :param power: The power in watts.
    :param voltage: The voltage in volts.
    :param powerfactor: The power factor (dimensionless).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "current": {
      "type": "number",
      "description": "The current value, represented as a floating-point number."
    }
  },
  "required": ["current"]
}
```
    """
    url = "https://electrical-units.p.rapidapi.com/power_to_current/three_phase"
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

