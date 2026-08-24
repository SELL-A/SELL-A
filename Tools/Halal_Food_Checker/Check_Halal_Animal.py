import os
import requests

def Check_Halal_Animal(animal):
    """
    :API_description: Determine if a specified animal is considered halal, returning its name and halal status.
    :param animal: The name of the animal to check(eg "Dog").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "animal": {
      "type": "string",
      "description": "The name of the animal."
    },
    "is_halal": {
      "type": "boolean",
      "description": "Indicates whether the animal is considered halal."
    }
  },
  "required": ["animal", "is_halal"]
}
```
    """
    url = f"https://halal-food-checker.p.rapidapi.com/check-halal-animal/{animal}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "halal-food-checker.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")