import os
import requests

def Get_Reviews_of_the_hotel(hotel_id):
    """
    :API_description: Retrieves a comprehensive collection of customer reviews for a specified hotel, including detailed ratings, reviewer information, stay details, and feedback.
    :param hotel_id: The unique identifier for the hotel.
    :response_schema: 
    ```json
{
  "result": [
    {
      "is_incentivised": "integer",
      "user_new_badges": "array",
      "anonymous": "string",
      "title": "string",
      "hotelier_response": "string",
      "countrycode": "string",
      "hotel_id": "integer",
      "review_id": "integer",
      "average_score": "float",
      "stayed_room_info": {
        "checkin": "string",
        "checkout": "string",
        "room_name": "string",
        "room_id": "integer",
        "photo": {
          "photo_id": "integer",
          "url_square60": "string",
          "ratio": "float",
          "url_640x200": "string",
          "url_max300": "string",
          "url_original": "string"
        },
        "num_nights": "integer"
      },
      "is_moderated": "integer",
      "travel_purpose": "string",
      "date": "string",
      "reviewer_photos": "array",
      "pros": "string",
      "is_trivial": "integer",
      "reviewng": "integer",
      "tags": "array",
      "title_translated": "string",
      "cons": "string",
      "hotelier_name": "string",
      "pros_translated": "string",
      "cons_translated": "string",
      "review_hash": "string",
      "author": {
        "city": "string",
        "type": "string",
        "helpful_vote_count": "integer",
        "user_id": "integer",
        "nr_reviews": "integer",
        "name": "string",
        "age_group": "string",
        "countrycode": "string",
        "type_string": "string",
        "avatar": "string (optional)"
      },
      "languagecode": "string",
      "helpful_vote_count": "integer"
    }
  ]
}
    ```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/reviews"
    querystring = {
        "locale": "en-us",
        "sort_type": "SORT_MOST_RELEVANT",
        "hotel_id": hotel_id
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