import os
import requests
def Flight_number_auto_complete(term):
    """
    :API_description: Search Flight Numbers By Term (lookup available flight numbers by term - useful for implmenting auto-complete features)
    :param term: The search term used to find flights (e.g., flight number or airline code).
    :response_schema: 
    ```json:
{
  "searchBy": "KL30",
  "count": 10,
  "items": [
    {
      "number": "KL 3060"
    },
    {
      "number": "KL 3061"
    },
    {
      "number": "KL 3062"
    },
    {
      "number": "KL 3063"
    },
    {
      "number": "KL 3064"
    },
    {
      "number": "KL 3065"
    },
    {
      "number": "KL 3066"
    },
    {
      "number": "KL 3067"
    },
    {
      "number": "KL 3074"
    },
    {
      "number": "KL 3075"
    }
  ]
}
```
    """
    url = "https://aerodatabox.p.rapidapi.com/flights/search/term"
    querystring = {"q": term}
    headers = {
        "x-rapidapi-key": "9cda500e54mshe688ef1d857bd6bp1f9040jsn59b82e309f42",
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 204:
        return {}
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
