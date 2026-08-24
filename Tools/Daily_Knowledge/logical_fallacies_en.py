import os
import requests

def logical_fallacies_en():
    """
    :API_description: Retrieve detailed information about the 'black-or-white' logical fallacy, including its definition, example, and SEO metadata.
    :param None
    :response_schema: 
    ```json
{
  "name": "tu-quoque",
  "title": "tu quoque",
  "slug": "tu-quoque",
  "head": "...",
  "first": "...",
  "description": "...",
  "example": "...",
  "pageTitle": "Your logical fallacy is tu quoque",
  "exampleText": "...",
  "meta": {
    "seo": {
      "title": "Your logical fallacy is tu quoque",
      "description": "You avoided having to engage with criticism by turning it back on the accuser - you answered criticism with criticism."
    },
    "og": {
      "og:title": "Your logical fallacy is tu quoque",
      "og:description": "You avoided having to engage with criticism by turning it back on the accuser - you answered criticism with criticism.",
      "og:image": "https://yourlogicalfallacyis.com/system/App/Meta/og_images/000/000/028/original/07-tu-quoque.png",
      "og:image:width": 150,
      "og:image:height": 150
    }
  }
}
```
    """
    url = "https://daily-knowledge.p.rapidapi.com/logical-fallacies-en.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "daily-knowledge.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")