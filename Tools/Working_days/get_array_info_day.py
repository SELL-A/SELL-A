import os
import requests

def get_array_info_day(start_date, end_date, country_code):
    """
    :API_description: Retrieve a detailed schedule for a specified period, including daily status, work hours, wages, and teleworking details.
    :param start_date: The start date of the range in 'YYYY-MM-DD' format.
    :param end_date: The end date of the range in 'YYYY-MM-DD' format.
    :param country_code: The country code for which the working days information is requested(e.g., "US").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "days": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "date": {
            "type": "string",
            "format": "date"
          },
          "working_day": {
            "type": "integer"
          },
          "work_hours": {
            "type": "integer"
          },
          "wages": {
            "type": "integer"
          },
          "morning_start": {
            "type": "string",
            "format": "time"
          },
          "morning_end": {
            "type": "string",
            "format": "time"
          },
          "afternoon_start": {
            "type": "string",
            "format": "time"
          },
          "afternoon_end": {
            "type": "string",
            "format": "time"
          },
          "public_holiday": {
            "type": "string"
          },
          "public_holiday_description": {
            "type": "string"
          },
          "public_holiday_short_description": {
            "type": "string"
          },
          "weekend_day": {
            "type": "integer"
          },
          "custom_date": {
            "type": "integer"
          },
          "custom_date_description": {
            "type": "string"
          },
          "custom_date_color": {
            "type": "string"
          },
          "teleworking": {
            "type": "object",
            "properties": {
              "days": {
                "type": "integer"
              },
              "hours": {
                "type": "integer"
              }
            }
          },
          "type": {
            "type": "integer"
          },
          "type_comment": {
            "type": "string"
          }
        },
        "required": [
          "date",
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
    }
  },
  "required": [
    "days"
  ]
}
    ```
    """
    url = "https://working-days.p.rapidapi.com/1.3/get_array_info_day"
    querystring = {"start_date": start_date, "end_date": end_date, "country_code": country_code}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "working-days.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")