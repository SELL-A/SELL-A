import os
import requests

def list_non_working_days(country_code, start_date, end_date):
    """
    :API_description: Retrieve a list of non-working days between specified dates, categorized by date, description, and type.
    :param country_code: The ISO code of the country for which to retrieve non-working days (e.g., "AU").
    :param start_date: The start date of the range in YYYY-MM-DD format.
    :param end_date: The end date of the range in YYYY-MM-DD format.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "non_working_days": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "date": {
            "type": "string",
            "format": "date"
          },
          "description": {
            "type": "string"
          },
          "type": {
            "type": "integer"
          }
        },
        "required": ["date", "description", "type"]
      }
    }
  },
  "required": ["non_working_days"]
}
```
    """
    url = "https://working-days.p.rapidapi.com/1.3/list_non_working_days"

    querystring = {
        "country_code": country_code,
        "start_date": start_date,
        "end_date": end_date
    }

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "working-days.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
  

