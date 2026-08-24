import os
import requests

def chemical_elements_en():
    """
    :API_description: Retrieves detailed information about a specific chemical element, including its properties and historical data.
    :param None
    :response_schema: 
    ```json
{
  "atomicMass": 268,
  "atomicNumber": 109,
  "ionizationEnergy": 0,
  "elementGroup": "transition-metal",
  "group": 9,
  "name": "Meitnerium",
  "period": 7,
  "symbol": "Mt",
  "electronsPerShell": [
    2,
    8,
    18,
    32,
    32,
    15,
    2
  ],
  "nameLatin": "Meitnerium",
  "nameDE": "Meitnerium"
}
```
    """
    url = "https://daily-knowledge.p.rapidapi.com/chemical-elements-en.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "daily-knowledge.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")