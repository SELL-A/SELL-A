import os
import requests
def Tournaments_list(name):
    """
    :API_description: Retrieves a list of active soccer tournaments, including their names, categories, and unique identifiers.
    :param name: The name of the sport (e.g., "soccer").
    :response_schema: 
    ```json
{
  "total": 8,
  "per_page": 500,
  "current_page": 0,
  "last_page": 0,
  "data": [
    {
      "id": 198,
      "name": "Serie B",
      "slug": "football-brazil-serie-b",
      "category": {
        "id": 25,
        "name": "Brazil",
        "slug": "brazil",
        "code": "br"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    },
    {
      "id": 417,
      "name": "Serie B",
      "slug": "football-ecuador-serie-b",
      "category": {
        "id": 46,
        "name": "Ecuador",
        "slug": "ecuador",
        "code": "ec"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    },
    {
      "id": 720,
      "name": "Serie B",
      "slug": "football-italy-serie-b",
      "category": {
        "id": 77,
        "name": "Italy",
        "slug": "italy",
        "code": "it"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    },
    {
      "id": 758,
      "name": "Serie B Women",
      "slug": "football-italy-serie-b-women",
      "category": {
        "id": 77,
        "name": "Italy",
        "slug": "italy",
        "code": "it"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    },
    {
      "id": 838,
      "name": "Liga Premier Serie B",
      "slug": "football-mexico-liga-premier-serie-b",
      "category": {
        "id": 104,
        "name": "Mexico",
        "slug": "mexico",
        "code": "mx"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    },
    {
      "id": 13242,
      "name": "Serie B Superbet",
      "slug": "football-brazil-serie-b-superbet",
      "category": {
        "id": 25,
        "name": "Brazil",
        "slug": "brazil",
        "code": "br"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    },
    {
      "id": 24180,
      "name": "Serie B Femminile",
      "slug": "football-italy-serie-b-femminile",
      "category": {
        "id": 77,
        "name": "Italy",
        "slug": "italy",
        "code": "it"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    },
    {
      "id": 48640,
      "name": "Serie B Femenina",
      "slug": "football-italy-serie-b-femenina",
      "category": {
        "id": 77,
        "name": "Italy",
        "slug": "italy",
        "code": "it"
      },
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      }
    }
  ]
}
```
    """
    url = "https://odds-feed.p.rapidapi.com/api/v1/tournaments"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"name": name}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "odds-feed.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")