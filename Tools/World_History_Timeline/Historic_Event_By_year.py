import os
import requests

def Historic_Event_By_year(year):
    """
    :API_description: Retrieve a list of historical events from a specific year, including event descriptions and unique identifiers.
    :param year: The year for which historical events are to be retrieved(Example: "2023").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the event"
          },
          "order": {
            "type": "string",
            "description": "Order of the event, represented as a string with high precision"
          },
          "Year": {
            "type": "string",
            "description": "Year of the event, represented as a string"
          },
          "Event": {
            "type": "string",
            "description": "Description of the historical event"
          },
          "UID": {
            "type": "string",
            "description": "Unique identifier for the event, represented as a string"
          }
        },
        "required": ["id", "order", "Year", "Event", "UID"]
      }
    }
  },
  "required": ["results"]
}
```
    """
    url = "https://world-history-timeline.p.rapidapi.com/History-By-Year"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"year": year}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "world-history-timeline.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    year = "2023"
    print(Historic_Event_By_year(year))