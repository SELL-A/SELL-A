import os
import requests

def Get_Review_scores_of_the_hotel(hotel_id):
    """
    :API_description: Retrieves detailed review scores and rating distributions for a specified hotel, including breakdowns by customer type, category ratings, and score percentages across quality bands.
    :param hotel_id: The unique identifier for the hotel.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "hotel_id": {
      "type": "integer",
      "description": "Unique identifier for the hotel"
    },
    "score_breakdown": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "average_score": {
            "type": ["string", "number"],
            "description": "Average score for this customer type, can be string or number"
          },
          "from_year": {
            "type": "integer",
            "description": "Starting year for the data collection"
          },
          "question": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "score_comparison_to_ufi_average": {
                  "type": "integer",
                  "description": "Comparison score to UFI average (0 = same, positive/negative = above/below)"
                },
                "question": {
                  "type": "string",
                  "description": "Question identifier/code"
                },
                "score": {
                  "type": ["number", "string"],
                  "description": "Score value, can be numeric or string"
                },
                "localized_question": {
                  "type": "string",
                  "description": "Localized/translated question text"
                },
                "count": {
                  "type": "integer",
                  "description": "Number of responses for this question"
                }
              },
              "required": ["score_comparison_to_ufi_average", "question", "score", "localized_question", "count"]
            }
          },
          "count": {
            "type": "integer",
            "description": "Total number of responses for this customer type"
          },
          "customer_type": {
            "type": "string",
            "description": "Type of customer/traveler (e.g., solo_traveller, couple, family, etc.)"
          }
        },
        "required": ["average_score", "from_year", "question", "count", "customer_type"]
      }
    },
    "score_distribution": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "percent": {
            "type": ["string", "number"],
            "description": "Percentage of total reviews for this score"
          },
          "count": {
            "type": "integer",
            "description": "Number of reviews with this score"
          },
          "score": {
            "type": "integer",
            "description": "Review score (1-10 scale)"
          }
        },
        "required": ["percent", "count", "score"]
      }
    },
    "score_percentage": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "score_word": {
            "type": "string",
            "description": "Descriptive label for score range (e.g., Superb, Good, Okay)"
          },
          "percent": {
            "type": "integer",
            "description": "Percentage of reviews in this score category"
          },
          "score_start": {
            "type": "integer",
            "description": "Starting value of score range"
          },
          "score_end": {
            "type": "number",
            "description": "Ending value of score range (inclusive)"
          },
          "count": {
            "type": "integer",
            "description": "Number of reviews in this score category"
          }
        },
        "required": ["score_word", "percent", "score_start", "score_end", "count"]
      }
    }
  },
  "required": ["hotel_id", "score_breakdown", "score_distribution", "score_percentage"]
}
    ```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/review-scores"
    querystring = {
        "hotel_id": hotel_id,
        "locale": "en-us"
    }

    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "booking-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

