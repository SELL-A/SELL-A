import os
import requests
def Supported_Currencies():
    """
    :API_description: Retrieve a list of supported currencies, including their symbols and full names.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "symbol": {
        "type": "string",
        "description": "The currency symbol (e.g., 'USD', 'EUR')."
      },
      "name": {
        "type": "string",
        "description": "The full name of the currency (e.g., 'United States Dollar', 'Euro Member Countries')."
      }
    },
    "required": ["symbol", "name"]
  }
}
    ```
    """
    url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
