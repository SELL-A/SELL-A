import os
import requests

def Raid_Exclusive_Pokemon():
    """
    :API_description: Retrieves a JSON object containing details of exclusive raid Pokémon, including their unique ID, name, and associated raid level.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "144": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "145": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "146": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "150": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "243": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "244": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "245": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "249": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "250": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "377": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "378": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "379": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "380": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "381": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "382": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "383": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "384": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "386": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "480": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "481": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "482": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "483": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "484": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "485": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "486": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "487": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "488": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "491": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    },
    "638": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "description": "Unique identifier for the Pokémon."
        },
        "name": {
          "type": "string",
          "description": "Name of the Pokémon."
        },
        "raid_level": {
          "type": "integer",
          "description": "Level of the raid associated with the Pokémon."
        }
      },
      "required": ["id", "name", "raid_level"]
    }
  }
}
    ```
    """
    url = "https://pokemon-go1.p.rapidapi.com/raid_exclusive_pokemon.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "pokemon-go1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")