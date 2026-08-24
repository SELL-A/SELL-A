import os
import requests

def Get_Game_News(id):
    """
    :API_description: Retrieves a paginated list of news, updates, and patch notes for Counter-Strike 2, including details like publication dates, update descriptions, and community engagement metrics.
    :param id: The unique identifier for the game(eg. "124").
    :response_schema: 
    ```json
{
  "status": 200,
  "message": "success",
  "data": {
    "news": [
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Mar 31",
        "content": " ",
        "like": "5,896"
      },
      {
        "news_title": "Spring Forward",
        "date": "Mar 31",
        "content": "",
        "like": "16,386"
      },
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Mar 20",
        "content": ".",
        "like": "30,788"
      },
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Feb 27",
        "content": ".",
        "like": "64,597"
      },
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Feb 13",
        "content": ".",
        "like": "53,564"
      },
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Feb 6",
        "content": ".",
        "like": "38,381"
      },
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Feb 3",
        "content": ".",
        "like": "27,897"
      },
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Jan 29",
        "content": ".",
        "like": "30,594"
      },
      {
        "news_title": "Season's Greetings",
        "date": "Jan 28",
        "content": ".",
        "like": "40,752"
      },
      {
        "news_title": "Counter-Strike 2 Update",
        "date": "Jan 28",
        "content": ".",
        "like": "13,997"
      }
    ],
    "limit": 10,
    "offset": 0
  }
}
```

    """
    url = f"https://games-details.p.rapidapi.com/news/all/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")