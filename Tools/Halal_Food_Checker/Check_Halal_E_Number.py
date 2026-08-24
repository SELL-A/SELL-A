import os
import requests

def Check_Halal_E_Number(e_number):
    """
    :API_description: Determine if a given E number is considered halal, providing details such as the E number and its common name.
    :param e_number: The E-number to be checked(eg. "E101").
    :response_schema: 
    ```json
{
    "type": "object",
    "properties": {
        "is_halal": {
            "type": "boolean",
            "description": "Indicates whether the food additive is considered halal."
        },
        "e_number": {
            "type": "string",
            "description": "The E number assigned to the food additive, which is a unique identifier in the European Union."
        },
        "name": {
            "type": "string",
            "description": "The common name or names of the food additive, including any alternative names or synonyms."
        }
    },
    "required": ["is_halal", "e_number", "name"]
}
    ```
    """
    url = f"https://halal-food-checker.p.rapidapi.com/check-halal-number/{e_number}"
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