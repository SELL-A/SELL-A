import os
import requests

def RecordCount(rows="1"):
    """
    :API_description: Retrieves the total number of records available in a work list, including metadata for pagination and filtering.
    :param rows: Number of rows to return (default "1").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Status of the API response, typically 'ok' for successful responses."
    },
    "message-type": {
      "type": "string",
      "description": "Type of message returned by the API, indicating the nature of the response, e.g., 'work-list'."
    },
    "message-version": {
      "type": "string",
      "description": "Version of the message format used in the API response."
    },
    "message": {
      "type": "object",
      "properties": {
        "facets": {
          "type": "object",
          "description": "Facets or filters applied to the query, currently empty."
        },
        "total-results": {
          "type": "integer",
          "description": "Total number of results available for the query."
        },
        "items": {
          "type": "array",
          "items": {
            "type": "object"
          },
          "description": "List of items returned by the query, currently empty."
        },
        "items-per-page": {
          "type": "integer",
          "description": "Number of items returned per page in the response."
        },
        "query": {
          "type": "object",
          "properties": {
            "start-index": {
              "type": "integer",
              "description": "Starting index for the query results."
            },
            "search-terms": {
              "type": ["string", "null"],
              "description": "Search terms used in the query, which can be null if no specific terms were used."
            }
          },
          "description": "Details of the query parameters used in the API request."
        }
      },
      "description": "Main content of the API response, containing details about the query and results."
    }
  },
  "required": ["status", "message-type", "message-version", "message"]
}
```
    """
    url = "https://crossref.p.rapidapi.com/"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"rows": rows}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "crossref.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
  
