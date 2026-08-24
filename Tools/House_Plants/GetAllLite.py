import os
import requests

def GetAllLite():
    """
    :API_description: Retrieves basic information about various house plants, including categories, common names, scientific names, and unique identifiers, without additional details.
    :param None
    :response_schema: 
    ```json
[
  {
    "Categories": "Dracaena",
    "Common name (fr.)": "Janet Craig",
    "Img": "...",
    "Zone": [
      "11-10"
    ],
    "Family": "Liliaceae",
    "Common name": [
      "Janet Craig"
    ],
    "Latin name": "Dracaena deremensis 'Janet Craig'",
    "Other names": null,
    "Description": null,
    "Origin": [
      "Cultivar"
    ],
    "id": "53417c12-4824-5995-bce0-b81984ebbd1d",
    "Climat": "Tropical"
  },
  {
    "Categories": "Palm",
    "Common name (fr.)": null,
    "Img": "...",
    "Zone": [
      "11",
      "9"
    ],
    "Family": "Arecaceae",
    "Common name": [
      "Lady palm"
    ],
    "Latin name": "Rhapis excelsa",
    "Other names": "Rhapis flabelliformis",
    "Description": null,
    "Origin": [
      "China"
    ],
    "id": "9b97aef1-20a4-5620-af90-7d64dadb414e",
    "Climat": "Subtropical"
  },
  {
    "Categories": "Anthurium",
    "Common name (fr.)": "Flamant rose, Langue de feu",
    "Img": "...",
    "Zone": [
      "11"
    ],
    "Family": "Araceae",
    "Common name": [
      "Tailflower",
      "Wax flower"
    ],
    "Latin name": "Anthurium X",
    "Other names": null,
    "Description": null,
    "Origin": [
      "Cultivar"
    ],
    "id": "215b33f4-66d2-5601-b776-4501f2bd50b7",
    "Climat": "Tropical"
  },
  {
    "Categories": "Other",
    "Common name (fr.)": "Oreille d'lphant",
    "Img": "...",
    "Zone": [
      "11"
    ],
    "Family": "Araceae",
    "Common name": [
      "Elephant ear"
    ],
    "Latin name": "Alocasia X amazonica",
    "Other names": "(A. sanderiana x A. lowii grandis)",
    "Description": null,
    "Origin": [
      "Hybrid"
    ],
    "id": "55a0e4fa-0717-521d-9671-0fc9095f2055",
    "Climat": "Tropical humid"
  },
  {
    "Categories": "Dracaena",
    "Common name (fr.)": "Dracaena de Malaisie",
    "Img": "...",
    "Zone": [
      "11-10"
    ],
    "Family": "Liliaceae",
    "Common name": [
      "Malaysian Dracaena"
    ],
    "Latin name": "Dracaena reflexa 'Song of Jamaica'",
    "Other names": "Pleomele reflexa",
    "Description": null,
    "Origin": [
      "Cultivar"
    ],
    "id": "99596292-0712-5d51-8b94-669d621c504a",
    "Climat": "Tropical"
  },
  {
    "Categories": "Aglaonema",
    "Common name (fr.)": "Aglaonema",
    "Img": "http://www.tropicopia.com/house-plant/thumbnails/5466.jpg",
    "Zone": [
      "11"
    ],
    "Family": "Araceae",
    "Common name": [
      "Chinese Evergreen"
    ],
    "Latin name": "Aglaonema 'Jubilee'",
    "Other names": null,
    "Description": null,
    "Origin": [
      "Hybrid"
    ],
    "id": "894d8453-28a0-59d1-ac0a-132dff7ee7a5",
    "Climat": "Tropical"
  }
]
```

    """
    url = "https://house-plants2.p.rapidapi.com/all-lite"
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
        
if __name__ == "__main__":
    print(GetAllLite())
