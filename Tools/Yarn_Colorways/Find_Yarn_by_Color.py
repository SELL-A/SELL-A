import os
import requests

def Find_Yarn_by_Color(color_code):
    """
    :API_description: Retrieve a list of yarn colorways that best match a specified color, with optional filters for brand, yarn type, weight, and match threshold.
    :param color_code: The color code to match against yarn colorways.
    :response_schema: 
    ```json
{
  "meta": {
    "limit": 50,
    "offset": 0,
    "total": 951
  },
  "data": [
    {
      "name": "Purple",
      "hex": "#701cf0",
      "brandId": "loops_and_threads",
      "brandName": "Loops & Threads",
      "yarnId": "soft_and_shiny_solid",
      "yarnName": "Soft & Shiny Solid",
      "yarnWeightId": "a",
      "dateAccessed": "2023-01-25",
      "href": "https://www.michaels.com/soft-and-shiny-solid-yarn-by-loops-and-threads/M20000268.html",
      "delta": 5.898893653493999,
      "percentMatch": 94
    }
  ]
}
```
    """
    url = f"https://yarn-colorways.p.rapidapi.com/v3/match/{color_code}"
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