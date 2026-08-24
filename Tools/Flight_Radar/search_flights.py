import os
import requests
def search_flights(query):
    """
    :API_description: Search for individual flights using query
    :param query: A string representing the search term (e.g., Aircraft number, flight code, airline code, etc...).
    :response_schema: 
    ```json:
{
  "type": "object",
  "properties": {
    "results": {
      "type": "array",
      "description": "List of search results matching the query.",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the result item."
          },
          "label": {
            "type": "string",
            "description": "Display label for the result item."
          },
          "detail": {
            "type": "object",
            "description": "Additional details specific to the result type.",
            "properties": {
              "operator_id": {
                "type": "integer",
                "description": "Numeric ID of the airline operator. Present in 'operator' type results."
              },
              "iata": {
                "type": "string",
                "description": "IATA airline code. Present in 'operator' type results."
              },
              "logo": {
                "type": "string",
                "description": "URL to the operator's logo image."
              },
              "callsign": {
                "type": "string",
                "description": "Flight callsign. Present in 'schedule' type results."
              },
              "flight": {
                "type": "string",
                "description": "Flight number. Present in 'schedule' type results."
              },
              "operator": {
                "type": "string",
                "description": "Operator code. Present in 'schedule' type results."
              }
            },
            "required": ["logo"],
            "additionalProperties": false
          },
          "type": {
            "type": "string",
            "description": "Type of the result (e.g., 'operator', 'schedule')."
          },
          "match": {
            "type": "string",
            "description": "Describes how the result matched the search query (e.g., 'iata', 'begins')."
          },
          "name": {
            "type": "string",
            "description": "Full name of the entity. Present in 'operator' type results."
          }
        },
        "required": ["id", "label", "detail", "type", "match"],
        "additionalProperties": false
      }
    },
    "info": {
      "type": "object",
      "description": "API service information.",
      "properties": {
        "grpcEnabled": {
          "type": "boolean",
          "description": "Indicates if gRPC is enabled for the service."
        }
      },
      "required": ["grpcEnabled"],
      "additionalProperties": false
    },
    "stats": {
      "type": "object",
      "description": "Statistical summary of the search results.",
      "properties": {
        "total": {
          "type": "object",
          "description": "Total counts across all categories.",
          "properties": {
            "all": { "type": "integer" },
            "airport": { "type": "integer" },
            "operator": { "type": "integer" },
            "live": { "type": "integer" },
            "schedule": { "type": "integer" },
            "aircraft": { "type": "integer" }
          },
          "required": ["all", "airport", "operator", "live", "schedule", "aircraft"],
          "additionalProperties": false
        },
        "count": {
          "type": "object",
          "description": "Counts of returned items per category.",
          "properties": {
            "airport": { "type": "integer" },
            "operator": { "type": "integer" },
            "live": { "type": "integer" },
            "schedule": { "type": "integer" },
            "aircraft": { "type": "integer" }
          },
          "required": ["airport", "operator", "live", "schedule", "aircraft"],
          "additionalProperties": false
        }
      },
      "required": ["total", "count"],
      "additionalProperties": false
    }
  },
  "required": ["results", "info", "stats"],
  "additionalProperties": false
}
```
    """
    url = "https://flight-radar1.p.rapidapi.com/flights/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "flight-radar1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

