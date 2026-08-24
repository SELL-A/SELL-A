import os
import requests

def Markets_feed(event_id):
    """
    :API_description: Get markets for multiple events.
    :param event_id: The ID of the event for which market feed data is requested.
    :response_schema: 
    ```json
{
  "total": 107,
  "per_page": 100,
  "current_page": 0,
  "last_page": 1,
  "data": [
    {
      "id": 8089,
      "event_id": 845,
      "period": "FULL_TIME",
      "bet_type": "BACK",
      "placing": "PREMATCH",
      "market_name": "ASIAN_HANDICAP",
      "value": 0.25,
      "value_type": null,
      "market_books": [
        {
          "market_book_id": 20456,
          "market_id": 8089,
          "is_open": true,
          "book": "UNIBET",
          "outcome_0": 2.35,
          "outcome_1": 1.58,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20412,
          "market_id": 8089,
          "is_open": true,
          "book": "1XBET",
          "outcome_0": 2.25,
          "outcome_1": 1.63,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20396,
          "market_id": 8089,
          "is_open": true,
          "book": "BET_IN_ASIA",
          "outcome_0": 2.37,
          "outcome_1": 1.65,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20439,
          "market_id": 8089,
          "is_open": true,
          "book": "BET365",
          "outcome_0": 2.29,
          "outcome_1": 1.6,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20383,
          "market_id": 8089,
          "is_open": true,
          "book": "PINNACLE",
          "outcome_0": 2.37,
          "outcome_1": 1.64,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20426,
          "market_id": 8089,
          "is_open": false,
          "book": "WILLIAM_HILL",
          "outcome_0": 2.02,
          "outcome_1": 1.74,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20483,
          "market_id": 8089,
          "is_open": true,
          "book": "DAFABET",
          "outcome_0": 2.35,
          "outcome_1": 1.66,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20467,
          "market_id": 8089,
          "is_open": true,
          "book": "BETFAIR_EXCH",
          "outcome_0": 2.49,
          "outcome_1": 1.65,
          "outcome_2": null,
          "volume_0": 330,
          "volume_1": 630,
          "volume_2": null
        },
        {
          "market_book_id": 20498,
          "market_id": 8089,
          "is_open": true,
          "book": "MATCHBOOK",
          "outcome_0": 2.42,
          "outcome_1": 1.64,
          "outcome_2": null,
          "volume_0": 40,
          "volume_1": 90,
          "volume_2": null
        }
      ]
    },
    {
      "id": 8062,
      "event_id": 845,
      "period": "FULL_TIME",
      "bet_type": "BACK",
      "placing": "PREMATCH",
      "market_name": "ASIAN_HANDICAP",
      "value": -0.5,
      "value_type": null,
      "market_books": [
        {
          "market_book_id": 20303,
          "market_id": 8062,
          "is_open": true,
          "book": "PINNACLE",
          "outcome_0": 4.74,
          "outcome_1": 1.21,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20286,
          "market_id": 8062,
          "is_open": true,
          "book": "BET_AT_HOME",
          "outcome_0": 4.5,
          "outcome_1": 1.15,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20330,
          "market_id": 8062,
          "is_open": true,
          "book": "BET365",
          "outcome_0": 4.4,
          "outcome_1": 1.2,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20345,
          "market_id": 8062,
          "is_open": true,
          "book": "UNIBET",
          "outcome_0": 4.8,
          "outcome_1": 1.19,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20317,
          "market_id": 8062,
          "is_open": true,
          "book": "BET_IN_ASIA",
          "outcome_0": 4.74,
          "outcome_1": 1.21,
          "outcome_2": null,
          "volume_0": null,
          "volume_1": null,
          "volume_2": null
        },
        {
          "market_book_id": 20360,
          "market_id": 8062,
          "is_open": true,
          "book": "BETFAIR_EXCH",
          "outcome_0": 5,
          "outcome_1": 1.24,
          "outcome_2": null,
          "volume_0": 120,
          "volume_1": 10,
          "volume_2": null
        }
      ]
    }
    
  ]
}
```
    """
    url = "https://odds-feed.p.rapidapi.com/api/v1/markets/feed"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"event_id": event_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "odds-feed.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")