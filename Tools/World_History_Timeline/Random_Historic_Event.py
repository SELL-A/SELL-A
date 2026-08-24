import os
import requests

def Random_Historic_Event():
    """
    :API_description: Retrieves a randomly selected historical event, including its year and a brief description.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "count": {
          "type": "integer",
          "description": "The total number of items available."
        },
        "next": {
          "type": ["null", "string"],
          "description": "URL to the next page of results, or null if there are no more pages."
        },
        "previous": {
          "type": ["null", "string"],
          "description": "URL to the previous page of results, or null if this is the first page."
        },
        "results": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Unique identifier for the event."
              },
              "order": {
                "type": "string",
                "description": "Order of the event, represented as a string to accommodate high precision."
              },
              "Year": {
                "type": "string",
                "description": "Year when the event occurred."
              },
              "Event": {
                "type": "string",
                "description": "Description of the historical event."
              },
              "UID": {
                "type": "string",
                "description": "Unique identifier for the event, possibly redundant with 'id'."
              }
            },
            "required": ["id", "order", "Year", "Event", "UID"]
          },
          "description": "List of historical events."
        }
      },
      "required": ["count", "next", "previous", "results"]
    }
  },
  "required": ["data"]
}
```

    """
    url = "https://world-history-timeline.p.rapidapi.com/History"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "world-history-timeline.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

