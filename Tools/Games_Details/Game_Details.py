import os
import requests

def Game_Details(id):
    """
    :API_description: Retrieves comprehensive metadata for a specific video game, including its title, description, pricing, media assets, system requirements, and publisher information.
    :param id: The unique identifier of the game(eg. "124").
    :response_schema: 
    ```json
{
  "status": 200,
  "message": "success",
  "data": {
    "name": "Counter-Strike 2",
    "desc": "",
    "release_date": "",
    "pricing": [
      {
        "discount": "0%",
        "originalPrice": "free",
        "discountPrice": "free"
      },
      {
        "discount": "0%",
        "originalPrice": "₹1370",
        "discountPrice": "₹1370"
      }
    ],
    "external_links": [
      {
        "name": "website",
        "link": "http://counter-strike.net/"
      }
    ],
    "tags": [
      "FPS",
      "Shooter",
      "Multiplayer",
      "Competitive",
      "Action",
      "Team-Based",
      "eSports",
      "Tactical",
      "First-Person",
      "PvP",
      "Online Co-Op",
      "Co-op",
      "Strategy",
      "Military",
      "War",
      "Difficult",
      "Trading",
      "Realistic",
      "Fast-Paced",
      "Moddable"
    ],
    "lang": [
      "English",
      "Czech",
      "Danish",
      "Dutch",
      "Finnish",
      "French",
      "German",
      "Hungarian",
      "Italian",
      "Japanese",
      "Korean",
      "Norwegian",
      "Polish",
      "Portuguese - Portugal",
      "Portuguese - Brazil",
      "Romanian",
      "Russian",
      "Simplified Chinese",
      "Spanish - Spain",
      "Swedish",
      "Thai",
      "Traditional Chinese",
      "Turkish",
      "Bulgarian",
      "Ukrainian",
      "Greek",
      "Spanish - Latin America",
      "Vietnamese",
      "Indonesian"
    ],
    "dev_details": {
      "developer_name": [
        "Valve"
      ],
      "publisher": [
        "Valve"
      ],
      "franchise": []
    },
    "media": {
      "screenshot": [],
      "videos": []
    },
    "sys_req": {
      "window": {
        "min": [
          "OS: Windows® 10",
          "Processor: 4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "Memory: 8 GB RAM",
          "Graphics: Video card must be 1 GB or more and should be a DirectX 11-compatible with support for Shader Model 5.0",
          "DirectX: Version 11",
          "Storage: 85 GB available space"
        ],
        "recomm": [
          "OS: Windows® 10",
          "Processor: 4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "Memory: 8 GB RAM",
          "Graphics: Video card must be 1 GB or more and should be a DirectX 11-compatible with support for Shader Model 5.0",
          "DirectX: Version 11",
          "Storage: 85 GB available space"
        ]
      },
      "linux": {
        "min": [
          "OS: Ubuntu 20.04",
          "Processor: 4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "Memory: 8 GB RAM",
          "Graphics: AMD GCN+ or NVIDIA Kepler+ with up-to-date Vulkan drivers.  Support for VK_EXT_graphics_pipeline_library highly recommended.",
          "Storage: 85 GB available space",
          "Sound Card: Highly recommended"
        ],
        "recomm": [
          "OS: Ubuntu 20.04",
          "Processor: 4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "Memory: 8 GB RAM",
          "Graphics: AMD GCN+ or NVIDIA Kepler+ with up-to-date Vulkan drivers.  Support for VK_EXT_graphics_pipeline_library highly recommended.",
          "Storage: 85 GB available space",
          "Sound Card: Highly recommended"
        ]
      }
    },
    "about_game": "CS2"
  }
}
    ```
    """
    url = f"https://games-details.p.rapidapi.com/gameinfo/single_game/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        return  {}

