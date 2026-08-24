import os
import requests

def countries_en():
    """
    :API_description: Provides comprehensive details about a country, including its name, capital, currency, languages, and flag.
    :param None
    :response_schema: 
    ```json
{
  "name": "Zambia",
  "capital": "Lusaka",
  "countryCode": "ZM",
  "currency": "Zambian Kwacha",
  "languages": "English",
  "tld": ".zm",
  "flag": "base64 encoded SVG image representing the country's flag."
}
```
    """
    url = "https://daily-knowledge.p.rapidapi.com/countries-en.json"
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

if __name__ == "__main__":
    print(countries_en())