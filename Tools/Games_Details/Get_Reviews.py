import os
import requests

def Get_Reviews(id):
    """
    :API_description: Retrieves user reviews for a specific game, such as Counter-Strike: Global Offensive, from a gaming platform. The response includes an array of review objects containing recommendation status, publication date, review content, and reviewer details.
    :param id: The unique identifier for the game whose top-rated reviews are to be fetched(eg. "124").
    :response_schema: 
    ```json
{
  "status": 200,
  "message": "success",
  "data": {
    "reviews": [
      {
        "review_id": "1NZwwzGKr8oVP12WCXx9sI8aTNIuTxxcWPWvZK1Y0SqVN",
        "title": "Not Recommended",
        "date": "Posted: March 9, 2025",
        "content": "...",
        "user_profile": "...",
        "user_name": "Yulian"
      },
      {
        "review_id": "gSrK8NvsytMjQNRFnIJ3nMJaHEKoqc6Uqc5Wgv7DTAZCQ132rJB",
        "title": "Recommended",
        "date": "Posted: April 8",
        "content": "...",
        "user_profile": "...",
        "user_name": "one gallon of milk"
      },
      {
        "review_id": "hStU1GiKWg7db1YNAkNVdVtEKwXjZ9J0xr2rlZKmcB1",
        "title": "Not Recommended",
        "date": "Posted: March 4, 2025",
        "content": "...",
        "user_profile": "...",
        "user_name": "KeithTheBat"
      },
      {
        "review_id": "gSrK8NvsytIGMGqtEqTWpmTBFnL7hrOfxSH6W4OYFbM4snznU8f",
        "title": "Not Recommended",
        "date": "Posted: March 7, 2025",
        "content": "...",
        "user_profile": "...",
        "user_name": "MrMorganfarts"
      },
      {
        "review_id": "ehr7FoS9jswpkzhag0ISUIZYGeUcoinCqjOZl7p",
        "title": "Not Recommended",
        "date": "Posted: March 5, 2025",
        "content": "...",
        "user_profile": "...",
        "user_name": "Da_Gecko"
      },
      {
        "review_id": "4EQwj8IpF9PnIQGnk7xoKbymIJFPtehTwxyPY0u1NZuWr5",
        "title": "Not Recommended",
        "date": "Posted: March 9, 2025",
        "content": "...",
        "user_profile": "...",
        "user_name": "- Element -"
      }
    ],
    "limit": "6",
    "offset": "0"
  }
}
```
    """
    url = f"https://games-details.p.rapidapi.com/reviews/toprated/{id}"
    params = {
        "limit": "10",
        "offset": "0"
    }
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
