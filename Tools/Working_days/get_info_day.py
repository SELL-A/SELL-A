import os
import requests

def get_info_day(country_code, date, configuration):
    """
    :API_description: Retrieve comprehensive details about a specific day, including work hours, wages, and holiday information.
    :param country_code: The code representing the country (e.g., 'US' for the United States).
    :param date: The date for which information is requested, formatted as 'YYYY-MM-DD'.
    :param configuration: The configuration setting, such as 'Federal holidays',Australian Capital Territory,Ontario.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "working_day": {
      "type": "integer",
      "description": "Indicates whether the day is a working day (1 for yes, 0 for no)."
    },
    "work_hours": {
      "type": "integer",
      "description": "Total number of work hours for the day."
    },
    "wages": {
      "type": "integer",
      "description": "Total wages for the day based on work hours."
    },
    "morning_start": {
      "type": "string",
      "format": "time",
      "description": "Start time of the morning work session."
    },
    "morning_end": {
      "type": "string",
      "format": "time",
      "description": "End time of the morning work session."
    },
    "afternoon_start": {
      "type": "string",
      "format": "time",
      "description": "Start time of the afternoon work session."
    },
    "afternoon_end": {
      "type": "string",
      "format": "time",
      "description": "End time of the afternoon work session."
    },
    "public_holiday": {
      "type": "string",
      "description": "Indicates whether the day is a public holiday ('1' for yes, '0' for no)."
    },
    "public_holiday_description": {
      "type": "string",
      "description": "Description of the public holiday if applicable."
    },
    "public_holiday_short_description": {
      "type": "string",
      "description": "Short description of the public holiday if applicable."
    },
    "weekend_day": {
      "type": "integer",
      "description": "Indicates whether the day is a weekend day (1 for yes, 0 for no)."
    },
    "custom_date": {
      "type": "integer",
      "description": "Indicates whether the date is a custom date (1 for yes, 0 for no)."
    },
    "custom_date_description": {
      "type": "string",
      "description": "Description of the custom date if applicable."
    },
    "custom_date_color": {
      "type": "string",
      "description": "Color code for the custom date if applicable."
    },
    "teleworking": {
      "type": "object",
      "properties": {
        "days": {
          "type": "integer",
          "description": "Number of teleworking days."
        },
        "hours": {
          "type": "integer",
          "description": "Number of teleworking hours."
        }
      },
      "description": "Details about teleworking for the day."
    },
    "type": {
      "type": "integer",
      "description": "Type identifier for the day."
    },
    "type_comment": {
      "type": "string",
      "description": "Comment explaining the type identifier."
    }
  },
  "required": [
    "working_day",
    "work_hours",
    "wages",
    "morning_start",
    "morning_end",
    "afternoon_start",
    "afternoon_end",
    "public_holiday",
    "public_holiday_description",
    "public_holiday_short_description",
    "weekend_day",
    "custom_date",
    "custom_date_description",
    "custom_date_color",
    "teleworking",
    "type",
    "type_comment"
  ]
}
    ```
    """
    url = "https://working-days.p.rapidapi.com/1.3/get_info_day"
    querystring = {"country_code": country_code, "date": date, "configuration": configuration}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "working-days.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")