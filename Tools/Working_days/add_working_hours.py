import os
import requests

def add_working_hours(start_date, country_code, start_time, increment_time, configuration):
    """
    :API_description: Add a specified amount of working time to a given start date and time, considering regional configurations and optional custom calendars.
    :param start_date: The start date from which to begin adding working hours (format: YYYY-MM-DD).
    :param country_code: The country code to consider for working days and holidays(e.g., "US").
    :param start_time: The start time from which to begin adding working hours (format: HH:MM).
    :param increment_time: The amount of time to add in working hours (format: HH:MM).
    :param configuration: The specific configuration to use for calculating working days (e.g., a state or region within the country "California").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "end_date": {
      "type": "string",
      "format": "date",
      "description": "The date when an event or activity ends, formatted as YYYY-MM-DD."
    },
    "end_time": {
      "type": "string",
      "format": "time",
      "description": "The time when an event or activity ends, formatted as HH:MM."
    }
  },
  "required": ["end_date", "end_time"]
}
    ```
    """
    url = "https://working-days.p.rapidapi.com/1.3/add_working_hours"
    querystring = {
        "start_date": start_date,
        "country_code": country_code,
        "start_time": start_time,
        "increment_time": increment_time,
        "configuration": configuration
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