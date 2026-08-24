import os
import requests

def Convert_three_phase_current_to_power(current, voltage, powerfactor):
    """
    :API_description: This API converts three-phase current in amperes to power in watts, considering optional parameters for voltage and power factor.
    :param current: The electrical current in amperes.
    :param voltage: The voltage in volts.
    :param powerfactor: The power factor of the system.
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
    url = "https://electrical-units.p.rapidapi.com/current_to_power/three_phase"
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