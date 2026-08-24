import os
import requests

def Estimated_Job_Salary(job_title, location):
    """
    :API_description: Retrieve estimated salary data for a specified job title and location, including various salary periods and currency details.
    :param job_title: The title of the job for which the salary is being estimated(e.g., "Data Scientist").
    :param location: The location where the job is based(e.g., "San Francisco").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Status of the API response, typically 'OK' for successful responses."
    },
    "request_id": {
      "type": "string",
      "description": "Unique identifier for the request, typically a UUID."
    },
    "parameters": {
      "type": "object",
      "properties": {
        "job_title": {
          "type": "string",
          "description": "The job title used in the search query."
        },
        "location": {
          "type": "string",
          "description": "The location used in the search query."
        },
        "radius": {
          "type": "integer",
          "description": "The search radius in miles or kilometers."
        }
      },
      "required": ["job_title", "location", "radius"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The location of the job."
          },
          "job_title": {
            "type": "string",
            "description": "The title of the job."
          },
          "publisher_name": {
            "type": "string",
            "description": "The name of the publisher providing the salary data."
          },
          "publisher_link": {
            "type": "string",
            "description": "A URL link to the publisher's source of salary data."
          },
          "min_salary": {
            "type": ["number", "integer"],
            "description": "The minimum salary for the job."
          },
          "max_salary": {
            "type": ["number", "integer"],
            "description": "The maximum salary for the job."
          },
          "median_salary": {
            "type": ["number", "integer"],
            "description": "The median salary for the job."
          },
          "salary_period": {
            "type": "string",
            "description": "The period for which the salary is calculated (e.g., 'HOUR', 'YEAR')."
          },
          "salary_currency": {
            "type": "string",
            "description": "The currency in which the salary is provided."
          }
        },
        "required": ["location", "job_title", "publisher_name", "publisher_link", "min_salary", "max_salary", "median_salary", "salary_period", "salary_currency"]
      }
    }
  },
  "required": ["status", "request_id", "parameters", "data"]
}
```


or
```json
{
  "status": "OK",
  "request_id": "f9d3dbb8-0a9e-42cf-9c0d-7620a1980980",
  "parameters": {
    "job_title": "software engineer",
    "location": "new york",
    "location_type": "ANY",
    "years_of_experience": null
  },
  "data": []
}
```
    """
    url = "https://jsearch.p.rapidapi.com/estimated-salary"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"job_title": job_title, "location": location}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == '__main__':
    print(Estimated_Job_Salary("Data Scientist", "San Francisco"))