import os
import requests

def add_working_days(country_code, start_date, increment):
    """
    :API_description: Calculate a new date by adding or subtracting a specified number of working days from a given start date, considering country-specific holidays and working days.
    :param country_code: The code of the country for which the working days are calculated(The ISO country code (2 letters) e.g. "US").
    :param start_date: The start date from which the working days are added(The start date (YYYY-MM-DD)).
    :param increment: The number of working days to add(The number of working days you want to add to your start date (positive or negative integer but not zero) Default: 10).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "end_date": {
      "type": "string",
      "format": "date",
      "description": "The end date of the period being analyzed."
    },
    "days": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of days in the period."
        },
        "mondays": {
          "type": "integer",
          "description": "Number of Mondays in the period."
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of Tuesdays in the period."
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of Wednesdays in the period."
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of Thursdays in the period."
        },
        "fridays": {
          "type": "integer",
          "description": "Number of Fridays in the period."
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of Saturdays in the period."
        },
        "sundays": {
          "type": "integer",
          "description": "Number of Sundays in the period."
        },
        "hours": {
          "type": "integer",
          "description": "Total number of hours in the period."
        }
      },
      "description": "Details about the days in the period."
    },
    "working_days": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of working days in the period."
        },
        "mondays": {
          "type": "integer",
          "description": "Number of working Mondays in the period."
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of working Tuesdays in the period."
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of working Wednesdays in the period."
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of working Thursdays in the period."
        },
        "fridays": {
          "type": "integer",
          "description": "Number of working Fridays in the period."
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of working Saturdays in the period."
        },
        "sundays": {
          "type": "integer",
          "description": "Number of working Sundays in the period."
        },
        "work_hours": {
          "type": "integer",
          "description": "Total number of working hours in the period."
        },
        "wages": {
          "type": "integer",
          "description": "Total wages earned in the period."
        },
        "teleworking": {
          "type": "object",
          "properties": {
            "days": {
              "type": "integer",
              "description": "Number of teleworking days in the period."
            },
            "hours": {
              "type": "integer",
              "description": "Number of teleworking hours in the period."
            }
          },
          "description": "Details about teleworking in the period."
        }
      },
      "description": "Details about working days in the period."
    },
    "weekend_days": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of weekend days in the period."
        },
        "mondays": {
          "type": "integer",
          "description": "Number of weekend Mondays in the period."
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of weekend Tuesdays in the period."
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of weekend Wednesdays in the period."
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of weekend Thursdays in the period."
        },
        "fridays": {
          "type": "integer",
          "description": "Number of weekend Fridays in the period."
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of weekend Saturdays in the period."
        },
        "sundays": {
          "type": "integer",
          "description": "Number of weekend Sundays in the period."
        }
      },
      "description": "Details about weekend days in the period."
    },
    "public_holidays": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of public holidays in the period."
        },
        "mondays": {
          "type": "integer",
          "description": "Number of public holiday Mondays in the period."
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of public holiday Tuesdays in the period."
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of public holiday Wednesdays in the period."
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of public holiday Thursdays in the period."
        },
        "fridays": {
          "type": "integer",
          "description": "Number of public holiday Fridays in the period."
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of public holiday Saturdays in the period."
        },
        "sundays": {
          "type": "integer",
          "description": "Number of public holiday Sundays in the period."
        },
        "list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of the public holiday."
              },
              "description": {
                "type": "string",
                "description": "Description of the public holiday."
              }
            }
          },
          "description": "List of public holidays in the period."
        }
      },
      "description": "Details about public holidays in the period."
    },
    "custom_dates": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "description": "Total number of custom dates in the period."
        },
        "mondays": {
          "type": "integer",
          "description": "Number of custom Mondays in the period."
        },
        "tuesdays": {
          "type": "integer",
          "description": "Number of custom Tuesdays in the period."
        },
        "wednesdays": {
          "type": "integer",
          "description": "Number of custom Wednesdays in the period."
        },
        "thursdays": {
          "type": "integer",
          "description": "Number of custom Thursdays in the period."
        },
        "fridays": {
          "type": "integer",
          "description": "Number of custom Fridays in the period."
        },
        "saturdays": {
          "type": "integer",
          "description": "Number of custom Saturdays in the period."
        },
        "sundays": {
          "type": "integer",
          "description": "Number of custom Sundays in the period."
        },
        "list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date of the custom date."
              },
              "description": {
                "type": "string",
                "description": "Description of the custom date."
              }
            }
          },
          "description": "List of custom dates in the period."
        }
      },
      "description": "Details about custom dates in the period."
    }
  },
  "required": ["end_date", "days", "working_days", "weekend_days", "public_holidays", "custom_dates"]
}
    ```
    """
    url = "https://working-days.p.rapidapi.com/1.3/add_working_days"
    querystring = {
        "country_code": country_code,
        "start_date": start_date,
        "increment": increment
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
