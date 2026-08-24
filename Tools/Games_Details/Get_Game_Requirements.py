import os
import requests

def Get_Game_Requirements(id):
    """
    :API_description: Retrieves detailed minimum and recommended system requirements for a specified game, including specifications for operating systems, processors, memory, graphics, and storage.
    :param id: The unique identifier for the game whose requirements are being requested(eg. "124").
    :response_schema: 
    ```json
{
  "status": 200,
  "message": "success",
  "data": {
    "sys_req": {
      "window": {
        "min": {
          "os": "Windows® 10 ",
          "processor": "4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "memory": "8 GB RAM",
          "graphics": "Video card must be 1 GB or more and should be a DirectX 11-compatible with support for Shader Model 5.0",
          "directx": "Version 11",
          "storage": "85 GB available space"
        },
        "recomm": {
          "os": "Windows® 10 ",
          "processor": "4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "memory": "8 GB RAM",
          "graphics": "Video card must be 1 GB or more and should be a DirectX 11-compatible with support for Shader Model 5.0",
          "directx": "Version 11",
          "storage": "85 GB available space"
        }
      },
      "linux": {
        "min": {
          "os": "Ubuntu 20.04",
          "processor": "4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "memory": "8 GB RAM",
          "graphics": "AMD GCN+ or NVIDIA Kepler+ with up-to-date Vulkan drivers.  Support for VK_EXT_graphics_pipeline_library highly recommended.",
          "storage": "85 GB available space",
          "sound card": "Highly recommended"
        },
        "recomm": {
          "os": "Ubuntu 20.04",
          "processor": "4 hardware CPU threads - Intel® Core™ i5 750 or higher",
          "memory": "8 GB RAM",
          "graphics": "AMD GCN+ or NVIDIA Kepler+ with up-to-date Vulkan drivers.  Support for VK_EXT_graphics_pipeline_library highly recommended.",
          "storage": "85 GB available space",
          "sound card": "Highly recommended"
        }
      }
    }
  }
}
    ```
    """
    url = f"https://games-details.p.rapidapi.com/gameinfo/requirements/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")