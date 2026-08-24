import os
import requests

def auto_complete(locationPrefix: str):
    """
    :API_description: Retrieves locationPrefix of the query
    :param locationPrefix: The prefix of the location to search for suggestions(e.g., "greenwich").
    :response_schema: 
    ```json
    {
  "data": {
    "geoSuggestion": [
      {
        "geoIdentifier": "greenwich",
        "geoLabel": "Greenwich, London",
        "geoSubLabel": null,
        "__typename": "GeoSuggestion"
      },
      {
        "geoIdentifier": "greenwich-royal-borough",
        "geoLabel": "Greenwich (Royal Borough), London",
        "geoSubLabel": null,
        "__typename": "GeoSuggestion"
      },
      {
        "geoIdentifier": "station/greenwich",
        "geoLabel": "Greenwich Station, London",
        "geoSubLabel": null,
        "__typename": "GeoSuggestion"
      },
      {
        "geoIdentifier": "schools/secondary/greenwich-community-college",
        "geoLabel": "Greenwich Community College, London, SE18",
        "geoSubLabel": null,
        "__typename": "GeoSuggestion"
      },
      {
        "geoIdentifier": "schools/primary/greenwich-community-college-at-plumstead-centre",
        "geoLabel": "Greenwich Community College at Plumstead Centre, London, SE18",
        "geoSubLabel": null,
        "__typename": "GeoSuggestion"
      },
      {
        "geoIdentifier": "schools/primary/greenwich-house-independent-school",
        "geoLabel": "Greenwich House Independent School, Lincolnshire, LN11",
        "geoSubLabel": null,
        "__typename": "GeoSuggestion"
      },
      {
        "geoIdentifier": "schools/primary/greenwich-steiner-school",
        "geoLabel": "Greenwich Steiner School, London, SE3",
        "geoSubLabel": null,
        "__typename": "GeoSuggestion"
      }
    ]
  },
  "extensions": {
    "requestId": "aa3a606e-a7b2-46e8-985b-bc639ef92b14"
  }
}
```

    """
    url = "https://zoopla.p.rapidapi.com/v2/auto-complete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"locationPrefix": locationPrefix}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "zoopla.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

