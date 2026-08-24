import os
import requests

def Yarns():
    """
    :API_description: Retrieve detailed information about yarn products, including brand details and colorway availability.
    :param None
    :response_schema: 
    ```json
{
  "meta": {
    "total": 257
  },
  "data": [
    {
      "brandId": "4_seasons",
      "brandName": "4 Seasons",
      "yarnId": "flinders_cotton_8_ply",
      "yarnName": "Flinders Cotton 8 Ply",
      "yarnWeightId": "d",
      "colorways": 23
    },
    {
      "brandId": "4_seasons",
      "brandName": "4 Seasons",
      "yarnId": "marvel_8_ply",
      "yarnName": "Marvel 8 Ply",
      "yarnWeightId": "d",
      "colorways": 60
    },
    {
      "brandId": "4_seasons",
      "brandName": "4 Seasons",
      "yarnId": "marvel_12_ply_bulky",
      "yarnName": "Marvel 12 Ply Bulky",
      "yarnWeightId": "b",
      "colorways": 19
    }
  ]
}
```
    """
    url = "https://yarn-colorways.p.rapidapi.com/v3/yarns"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yarn-colorways.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")