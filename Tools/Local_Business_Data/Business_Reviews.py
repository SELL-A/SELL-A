import os
import requests

def Business_Reviews(business_id):
    """
    :API_description: This API retrieves review data for a specified business from Google Maps.
    :param business_id: The unique identifier for the business.
    :response_schema: 
    ```json
   {
  "status": "OK",
  "request_id": "f8d71514-e254-4674-bf86-d5115d614af4",
  "parameters": {
    "business_id": "0x880fd393d427a591:0x8cba02d713a995ed",
    "language": "en",
    "region": "us",
    "limit": 5,
    "offset": 0,
    "sort_by": "most_relevant",
    "translate_reviews": false
  },
  "data": [
    {
      "review_id": "Ci9DQUlRQUNvZENodHljRjlvT2xKVU9XUnRiSEZNTlZJNWFWOXFWa2x5U1dGc1RsRRAB",
      "review_text": "What a great and fast job they did! We have a bursted pipe and called them. In less than 1 hour Javier and Jimmy showed up.",
      "rating": 5,
      "review_datetime_utc": "2026-01-26T16:35:13.125Z",
      "review_timestamp": 1769445313,
      "review_time": "4 months ago",
      "review_link": "https://www.google.com/maps/reviews/data=!4m8!14m7!1m6!2m5!1sCi9DQUlRQUNvZENodHljRjlvT2xKVU9XUnRiSEZNTlZJNWFWOXFWa2x5U1dGc1RsRRAB",
      "review_photos": [
        "https://lh3.googleusercontent.com/grass-cs/ANxoTn3TW0piw-4A-yttUMOu9bpJEWe3"
      ],
      "review_language": "en",
      "like_count": 0,
      "author_id": "115242819672475376280",
      "author_link": "https://www.google.com/maps/contrib/115242819672475376280?hl=en",
      "author_name": "Andrea Monllau",
      "author_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjUmqXYY6Qa6Q5wXknAubk_Vo0A5tYQ8SDAQhVp8IsASRy33yMUe=s120-c-rp-mo-ba12-br100",
      "author_review_count": 11,
      "author_photo_count": 2,
      "owner_response_datetime_utc": "2026-01-27T15:50:43.000Z",
      "owner_response_timestamp": 1769529043,
      "owner_response_time": "4 months ago",
      "owner_response_text": "Andrea, thank you so much! We're really glad Javier and Jimmy were able to get out to you so quickly.",
      "owner_response_language": "en",
      "author_reviews_link": "https://www.google.com/maps/contrib/115242819672475376280/reviews?hl=en",
      "author_local_guide_level": 4,
      "author_is_local_guide": true,
      "review_form": null,
      "review_source": "Google",
      "review_source_logo": "https://www.gstatic.com/images/branding/product/1x/googleg_48dp.png"
    }
  ]
}
```
    """
    url = "https://api.openwebninja.com/local-business-data/business-reviews"
  
    querystring = {
        "business_id": business_id
    }

    headers = {
        "X-API-Key": "ak_2a42z3zdrr3rnxcapzcpfplyqqohqtgk8n0rsxjtvftpre3"
        }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    business_id = "0x880fd393d427a591:0x8cba02d713a995ed"
    reviews = Business_Reviews(business_id)
    print(reviews)