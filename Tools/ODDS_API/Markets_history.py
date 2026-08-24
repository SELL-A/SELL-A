import os
import requests
def Markets_history(market_book_id):
    """
    :API_description: Get historical odds changes for a specific market book.
    :param market_book_id: The unique identifier for the market book whose history is being requested(e.g. 564).
    :response_schema: 
    ```json
{
  "data": [
    {
      "market_book_id": 564,
      "is_open": true,
      "change_at": "2024-08-19 01:12:05",
      "outcome_0": 1.46,
      "outcome_1": 2.47,
      "outcome_2": null,
      "volume_0": null,
      "volume_1": null,
      "volume_2": null
    },
    {
      "market_book_id": 564,
      "is_open": true,
      "change_at": "2024-08-19 01:12:05",
      "outcome_0": 1.46,
      "outcome_1": 2.47,
      "outcome_2": null,
      "volume_0": null,
      "volume_1": null,
      "volume_2": null
    },
    {
      "market_book_id": 564,
      "is_open": true,
      "change_at": "2024-08-19 08:05:51",
      "outcome_0": 1.51,
      "outcome_1": null,
      "outcome_2": null,
      "volume_0": null,
      "volume_1": null,
      "volume_2": null
    },
    {
      "market_book_id": 564,
      "is_open": true,
      "change_at": "2024-08-19 08:07:52",
      "outcome_0": 1.5,
      "outcome_1": null,
      "outcome_2": null,
      "volume_0": null,
      "volume_1": null,
      "volume_2": null
    },
    {
      "market_book_id": 564,
      "is_open": true,
      "change_at": "2024-08-19 08:08:53",
      "outcome_0": null,
      "outcome_1": 2.48,
      "outcome_2": null,
      "volume_0": null,
      "volume_1": null,
      "volume_2": null
    },
    {
      "market_book_id": 564,
      "is_open": true,
      "change_at": "2024-08-19 08:17:53",
      "outcome_0": null,
      "outcome_1": 2.45,
      "outcome_2": null,
      "volume_0": null,
      "volume_1": null,
      "volume_2": null
    }
  ]
}
```
    """
    url = "https://odds-feed.p.rapidapi.com/api/v1/markets/history"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"market_book_id": market_book_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "odds-feed.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

