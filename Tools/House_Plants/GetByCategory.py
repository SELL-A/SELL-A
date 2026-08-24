import os
import requests

def GetByCategory(category):
    """
    :API_description: Retrieve a list of fern species based on the specified category, including detailed information such as common names, image URL, growth zones, and more.
    :param category: The category of house plants to retrieve information for(e.g, "Fern").
    :response_schema: 
    ```json
[
  {
    "Categories": "Fern",
    "Common name (fr.)": "Capilaire",
    "Img": "...",
    "Zone": [
      "10",
      "8"
    ],
    "Family": "Polypodiaceae",
    "Common name": [
      "Maindenhair",
      "Delta maidenhair"
    ],
    "Latin name": "Adiantum raddianum",
    "Other names": "cuneatum",
    "Description": null,
    "Origin": [
      "Brazil"
    ],
    "id": "6fcfb288-5a1f-53aa-ba7d-fcad91b11aab",
    "Climat": "Tropical"
  },
  {
    "Categories": "Fern",
    "Common name (fr.)": "Fougère de Boston",
    "Img": "...",
    "Zone": [
      "11-10"
    ],
    "Family": "Nephrolepidaceae",
    "Common name": [
      "Boston fern",
      "Sword fern"
    ],
    "Latin name": "Nephrolepis exaltata var.",
    "Other names": null,
    "Description": null,
    "Origin": [
      "Cultivar"
    ],
    "id": "171368f9-fff3-5d5a-8bcd-03cd157f32fc",
    "Climat": "Tropical"
  },
  {
    "Categories": "Fern",
    "Common name (fr.)": "Pteris dentelle d'argent",
    "Img": "...",
    "Zone": [
      "10-9"
    ],
    "Family": "Pteridaceae",
    "Common name": [
      "Silver Lace Fern"
    ],
    "Latin name": "Pteris ensiformis 'Evergemiensis'",
    "Other names": null,
    "Description": null,
    "Origin": [
      "Asia"
    ],
    "id": "69bd6c60-3ad9-5a31-8860-25565e374b26",
    "Climat": "Tropical humid"
  }
]
```
    """
    url = f"https://house-plants2.p.rapidapi.com/category/{category}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "house-plants2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
        

