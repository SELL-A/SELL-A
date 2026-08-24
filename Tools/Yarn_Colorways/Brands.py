import os
import requests

def Brands():
    """
    :API_description: Retrieve a list of yarn brands, including their names, unique identifiers, and product details such as the number of yarns and colorways available.
    :param None
    :response_schema: 
    ```json
{
  "meta": {
    "total": 3
  },
  "data": [
    {
      "brandName": "4 Seasons",
      "brandId": "4_seasons",
      "yarns": 3,
      "colorways": 102
    },
    {
      "brandName": "Aunt Lydia's",
      "brandId": "aunt_lydias",
      "yarns": 1,
      "colorways": 42
    },
    {
      "brandName": "Alize",
      "brandId": "alize",
      "yarns": 3,
      "colorways": 151
    }
  ]
}
```
    """
    url = "https://yarn-colorways.p.rapidapi.com/v3/brands"
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