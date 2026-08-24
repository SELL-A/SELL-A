import os
import requests

def Search_Autocomplete_API(query):
    """
    :API_description: The Search/Autocomplete API retrieves detailed information about specific locations, including their unique identifiers, names, regions, countries, and geographical coordinates.
    :param query: The search query string, typically a location name.
    :response_schema: 
    ```json
[
  {
    "id": 2801268,
    "name": "London",
    "region": "City of London, Greater London",
    "country": "United Kingdom",
    "lat": 51.52,
    "lon": -0.11,
    "url": "london-city-of-london-greater-london-united-kingdom"
  },
  {
    "id": 315398,
    "name": "London",
    "region": "Ontario",
    "country": "Canada",
    "lat": 42.98,
    "lon": -81.25,
    "url": "london-ontario-canada"
  },
  {
    "id": 2610925,
    "name": "Londonderry",
    "region": "New Hampshire",
    "country": "United States of America",
    "lat": 42.86,
    "lon": -71.37,
    "url": "londonderry-new-hampshire-united-states-of-america"
  }
]
```
    """
    url = "https://weatherapi-com.p.rapidapi.com/search.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"q": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
if __name__ == "__main__":
    query = "New York"
    result = Search_Autocomplete_API(query)
    print(result)
