import os
import requests

def GetById(plant_id):
    """
    :API_description: Retrieves comprehensive details about a specific plant, including its scientific name, image, growth characteristics, and more.
    :param plant_id: The unique identifier for the house plant (e.g, "53417c12-4824-5995-bce0-b81984ebbd1d").
    :response_schema: 
    ```json
{
  "Categories": "Dracaena",
  "Disease": "N/A",
  "Use": [
    "Potted plant",
    "Secondary"
  ],
  "Latin name": "Dracaena deremensis 'Janet Craig'",
  "Insects": [
    "Mealy bug",
    "Scale"
  ],
  "Avaibility": "Regular",
  "Style": "Bush",
  "Bearing": "Erect",
  "Light tolered": "Diffuse light ( Less than 5,300 lux / 500 fc)",
  "Height at purchase": {
    "M": 0.91,
    "CM": 91
  },
  "Light ideal": "Strong light ( 21,500 to 3,200 lux/2000 to 300 fc)",
  "Width at purchase": {
    "M": 0.91,
    "CM": 91
  },
  "id": "53417c12-4824-5995-bce0-b81984ebbd1d",
  "Appeal": "Robustness",
  "Perfume": null,
  "Growth": "Regular",
  "Width potential": {
    "M": 1.22,
    "CM": 122
  },
  "Common name (fr.)": "Janet Craig",
  "Pruning": "If needed",
  "Family": "Liliaceae",
  "Height potential": {
    "M": 3.66,
    "CM": 366
  },
  "Origin": [
    "Cultivar"
  ],
  "Description": null,
  "Temperature max": {
    "F": 86,
    "C": 30
  },
  "Blooming season": "Winter / Spring",
  "Color of leaf": [
    "Dark green"
  ],
  "Watering": "Keep moist between watering & Can dry between watering",
  "Color of blooms": "Light green",
  "Zone": [
    "11-10"
  ],
  "Common name": [
    "Janet Craig"
  ],
  "Available sizes (Pot)": "4in to 14in / 10cm to 36cm",
  "Other names": null,
  "Temperature min": {
    "F": 50,
    "C": 10
  },
  "Pot diameter (cm)": {
    "M": 0.25,
    "CM": 25
  },
  "Climat": "Tropical",
  "Img": "...",
  "Url": "..."
}
    ```
    """
    url = f"https://house-plants2.p.rapidapi.com/id/{plant_id}"
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

