import os
import requests

def Job_Details(job_id):
    """
    :API_description: Retrieve detailed information about a job, including application options, employer reviews, and estimated salaries.
    :param job_id: The unique identifier for the job(e.g., "qIsPjUMr0Em0hqHoAAAAAA==").
  
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Status of the API response, typically 'OK' for successful requests."
    },
    "request_id": {
      "type": "string",
      "description": "Unique identifier for the request, useful for tracking and debugging."
    },
    "parameters": {
      "type": "object",
      "properties": {
        "job_id": {
          "type": "string",
          "description": "Unique identifier for the job associated with the request."
        },
        "extended_publisher_details": {
          "type": "boolean",
          "description": "Flag indicating whether extended details about the publisher are requested."
        }
      },
      "required": ["job_id", "extended_publisher_details"]
    },
    "data": {
      "type": "array",
      "items": {},
      "description": "Array containing the data returned by the API, currently empty."
    }
  },
  "required": ["status", "request_id", "parameters", "data"]
}
```
    """
    url = "https://jsearch.p.rapidapi.com/job-details"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"job_id": job_id}

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
    print(Job_Details("qIsPjUMr0Em0hqHoAAAAAA=="))