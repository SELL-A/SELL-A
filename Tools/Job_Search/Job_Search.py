import os
import requests

def Job_Search(query,page=1, num_pages=1, date_posted="all"):
    """
    :API_description: Search for jobs across various platforms with extensive filtering options, including job title, location, and employer details.
    :param query: The job title and location to search for (e.g., "Node.js developer in New-York, USA").
    :param page: The page number of the results to retrieve(optional, default is 1).
    :param num_pages: The number of pages of results to retrieve(optional, default is 1).
    :param date_posted: The time frame for when the jobs were posted (e.g., "all").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "request_id": {
      "type": "string"
    },
    "parameters": {
      "type": "object",
      "properties": {
        "query": {
          "type": "string"
        },
        "page": {
          "type": "integer"
        },
        "num_pages": {
          "type": "integer"
        },
        "date_posted": {
          "type": "string"
        }
      },
      "required": ["query", "page", "num_pages", "date_posted"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "job_id": {
            "type": "string"
          },
          "employer_name": {
            "type": "string"
          },
          "employer_logo": {
            "type": "string"
          },
          "employer_website": {
            "type": "string"
          },
          "employer_company_type": {
            "type": "string"
          },
          "employer_linkedin": {
            "type": ["string", "null"]
          },
          "job_publisher": {
            "type": "string"
          },
          "job_employment_type": {
            "type": "string"
          },
          "job_title": {
            "type": "string"
          },
          "job_apply_link": {
            "type": "string"
          },
          "job_apply_is_direct": {
            "type": "boolean"
          },
          "job_apply_quality_score": {
            "type": "number"
          },
          "apply_options": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "publisher": {
                  "type": "string"
                },
                "apply_link": {
                  "type": "string"
                },
                "is_direct": {
                  "type": "boolean"
                }
              },
              "required": ["publisher", "apply_link", "is_direct"]
            }
          },
          "job_description": {
            "type": "string"
          },
          "job_is_remote": {
            "type": "boolean"
          },
          "job_posted_at_timestamp": {
            "type": "integer"
          },
          "job_posted_at_datetime_utc": {
            "type": "string"
          },
          "job_city": {
            "type": "string"
          },
          "job_state": {
            "type": "string"
          },
          "job_country": {
            "type": "string"
          },
          "job_latitude": {
            "type": "number"
          },
          "job_longitude": {
            "type": "number"
          },
          "job_benefits": {
            "type": ["array", "null"],
            "items": {
              "type": "string"
            }
          },
          "job_google_link": {
            "type": "string"
          },
          "job_offer_expiration_datetime_utc": {
            "type": ["string", "null"]
          },
          "job_offer_expiration_timestamp": {
            "type": ["integer", "null"]
          },
          "job_required_experience": {
            "type": "object",
            "properties": {
              "no_experience_required": {
                "type": "string"
              },
              "required_experience_in_months": {
                "type": ["integer", "null"]
              },
              "experience_mentioned": {
                "type": "string"
              },
              "experience_preferred": {
                "type": "string"
              }
            },
            "required": ["no_experience_required", "required_experience_in_months", "experience_mentioned", "experience_preferred"]
          },
          "job_required_skills": {
            "type": ["array", "null"],
            "items": {
              "type": "string"
            }
          },
          "job_required_education": {
            "type": "object",
            "properties": {
              "postgraduate_degree": {
                "type": "boolean"
              },
              "professional_certification": {
                "type": "boolean"
              },
              "high_school": {
                "type": "boolean"
              },
              "associates_degree": {
                "type": "boolean"
              },
              "bachelors_degree": {
                "type": "boolean"
              },
              "degree_mentioned": {
                "type": "boolean"
              },
              "degree_preferred": {
                "type": "boolean"
              },
              "professional_certification_mentioned": {
                "type": "boolean"
              }
            },
            "required": ["postgraduate_degree", "professional_certification", "high_school", "associates_degree", "bachelors_degree", "degree_mentioned", "degree_preferred", "professional_certification_mentioned"]
          },
          "job_experience_in_place_of_education": {
            "type": "boolean"
          },
          "job_min_salary": {
            "type": ["integer", "null"]
          },
          "job_max_salary": {
            "type": ["integer", "null"]
          },
          "job_salary_currency": {
            "type": ["string", "null"]
          },
          "job_salary_period": {
            "type": ["string", "null"]
          },
          "job_highlights": {
            "type": "object",
            "properties": {
              "Qualifications": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Responsibilities": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "Benefits": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          },
          "job_job_title": {
            "type": ["string", "null"]
          },
          "job_posting_language": {
            "type": "string"
          },
          "job_onet_soc": {
            "type": "string"
          },
          "job_onet_job_zone": {
            "type": "string"
          },
          "job_occupational_categories": {
            "type": ["array", "null"],
            "items": {
              "type": "string"
            }
          },
          "job_naics_code": {
            "type": ["string", "null"]
          },
          "job_naics_name": {
            "type": ["string", "null"]
          }
        },
        "required": [
          "job_id",
          "employer_name",
          "employer_logo",
          "employer_website",
          "employer_company_type",
          "employer_linkedin",
          "job_publisher",
          "job_employment_type",
          "job_title",
          "job_apply_link",
          "job_apply_is_direct",
          "job_apply_quality_score",
          "apply_options",
          "job_description",
          "job_is_remote",
          "job_posted_at_timestamp",
          "job_posted_at_datetime_utc",
          "job_city",
          "job_state",
          "job_country",
          "job_latitude",
          "job_longitude",
          "job_benefits",
          "job_google_link",
          "job_offer_expiration_datetime_utc",
          "job_offer_expiration_timestamp",
          "job_required_experience",
          "job_required_skills",
          "job_required_education",
          "job_experience_in_place_of_education",
          "job_min_salary",
          "job_max_salary",
          "job_salary_currency",
          "job_salary_period",
          "job_highlights",
          "job_job_title",
          "job_posting_language",
          "job_onet_soc",
          "job_onet_job_zone",
          "job_occupational_categories",
          "job_naics_code",
          "job_naics_name"
        ]
      }
    }
  },
  "required": ["status", "request_id", "parameters", "data"]
}
    ```
    """
    url = "https://jsearch.p.rapidapi.com/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query, "page": page, "num_pages": num_pages, "date_posted": date_posted}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


