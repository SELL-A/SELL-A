import os
import requests

def Colorways():
    """
    :API_description: Retrieve a list of yarn colors with details like color name, hexadecimal code, brand, yarn type, and product page link. The response is paginated with metadata for limit, offset, and total items.
    :param None
    :response_schema: 
    ```json
{
  "meta": {
    "limit": 50,
    "offset": 0,
    "total": 6743
  },
  "data": [
    {
      "brandId": "bernat",
      "brandName": "Bernat",
      "dateAccessed": "2024-01-19",
      "hex": "#665e3f",
      "href": "https://www.yarnspirations.com/products/bernat-blanket-yarn-300g-10-5oz-1",
      "name": "Olive",
      "yarnId": "blanket",
      "yarnName": "Blanket",
      "yarnWeightId": "sb"
    }
  ]
}
```
    """
    url = "https://yarn-colorways.p.rapidapi.com/v3/colorways"
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