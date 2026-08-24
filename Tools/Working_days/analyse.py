import os
import requests

def analyse(start_date, end_date, country_code, start_time, end_time):
    """
    :API_description: Analyze a specified date range to provide detailed breakdowns of days, working days, weekend days, public holidays, and custom dates, including counts, hours, and wages.
    :param start_date: The start date for the analysis in YYYY-MM-DD format.
    :param end_date: The end date for the analysis in YYYY-MM-DD format.
    :param country_code: The country code for which the working days are to be analyzed(e.g., "US").
    :param start_time: The start time of the working day in HH:MM format.
    :param end_time: The end time of the working day in HH:MM format.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "days": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of days in the year"
        },
        "mondays": {
          "type": "integer",
          "description": "Number of Mondays in the year"
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of Tuesdays in the year"
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of Wednesdays in the year"
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of Thursdays in the year"
        },
        "fridays": {
          "type": "integer",
          "description": "Number of Fridays in the year"
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of Saturdays in the year"
        },
        "sundays": {
          "type": "integer",
          "description": "Number of Sundays in the year"
        },
        "hours": {
          "type": "number",
          "description": "Total number of hours in the year"
        }
      }
    },
    "working_days": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of working days in the year"
        },
        "mondays": {
          "type": "integer",
          "description": "Number of working Mondays in the year"
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of working Tuesdays in the year"
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of working Wednesdays in the year"
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of working Thursdays in the year"
        },
        "fridays": {
          "type": "integer",
          "description": "Number of working Fridays in the year"
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of working Saturdays in the year"
        },
        "sundays": {
          "type": "integer",
          "description": "Number of working Sundays in the year"
        },
        "work_hours": {
          "type": "integer",
          "description": "Total number of working hours in the year"
        },
        "wages": {
          "type": "integer",
          "description": "Total wages for the year"
        },
        "teleworking": {
          "type": "object",
          "properties": {
            "days": {
              "type": "integer",
              "description": "Number of teleworking days in the year"
            },
            "hours": {
              "type": "integer",
              "description": "Number of teleworking hours in the year"
            }
          }
        }
      }
    },
    "weekend_days": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of weekend days in the year"
        },
        "mondays": {
          "type": "integer",
          "description": "Number of weekend Mondays in the year"
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of weekend Tuesdays in the year"
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of weekend Wednesdays in the year"
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of weekend Thursdays in the year"
        },
        "fridays": {
          "type": "integer",
          "description": "Number of weekend Fridays in the year"
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of weekend Saturdays in the year"
        },
        "sundays": {
          "type": "integer",
          "description": "Number of weekend Sundays in the year"
        }
      }
    },
    "public_holidays": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of public holidays in the year"
        },
        "mondays": {
          "type": "integer",
          "description": "Number of public holidays falling on Mondays in the year"
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of public holidays falling on Tuesdays in the year"
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of public holidays falling on Wednesdays in the year"
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of public holidays falling on Thursdays in the year"
        },
        "fridays": {
          "type": "integer",
          "description": "Number of public holidays falling on Fridays in the year"
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of public holidays falling on Saturdays in the year"
        },
        "sundays": {
          "type": "integer",
          "description": "Number of public holidays falling on Sundays in the year"
        },
        "list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of the public holiday"
              },
              "description": {
                "type": "string",
                "description": "Description of the public holiday"
              }
            }
          },
          "description": "List of public holidays with their dates and descriptions"
        }
      }
    },
    "custom_dates": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of custom dates in the year"
        },
        "mondays": {
          "type": "integer",
          "description": "Number of custom dates falling on Mondays in the year"
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of custom dates falling on Tuesdays in the year"
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of custom dates falling on Wednesdays in the year"
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of custom dates falling on Thursdays in the year"
        },
        "fridays": {
          "type": "integer",
          "description": "Number of custom dates falling on Fridays in the year"
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of custom dates falling on Saturdays in the year"
        },
        "sundays": {
          "type": "integer",
          "description": "Number of custom dates falling on Sundays in the year"
        },
        "list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of the custom date"
              },
              "description": {
                "type": "string",
                "description": "Description of the custom date"
              }
            }
          },
          "description": "List of custom dates with their dates and descriptions"
        }
      }
    }
  }
}
```
    """
    url = "https://working-days.p.rapidapi.com/1.3/analyse"
    querystring = {
        "start_date": start_date,
        "end_date": end_date,
        "country_code": country_code,
        "start_time": start_time,
        "end_time": end_time
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

