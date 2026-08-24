import os
import requests

def Get_Popular_Leagues():
    """
    :API_description: This API retrieves a comprehensive list of popular football competitions, including major domestic leagues, international tournaments, and cup competitions, providing essential details like ID, name, country, and logo for each.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "popular": [
      {
        "id": 77,
        "name": "World Cup",
        "localizedName": "FIFA World Cup",
        "ccode": "INT",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/77.png"
      },
      {
        "id": 47,
        "name": "Premier League",
        "localizedName": "Premier League",
        "ccode": "ENG",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/47.png"
      },
      {
        "id": 42,
        "name": "Champions League",
        "localizedName": "Champions League",
        "ccode": "INT",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/42.png"
      },
      {
        "id": 87,
        "name": "LaLiga",
        "localizedName": "LaLiga",
        "ccode": "ESP",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/87.png"
      },
      {
        "id": 54,
        "name": "Bundesliga",
        "localizedName": "Bundesliga",
        "ccode": "GER",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/54.png"
      },
      {
        "id": 73,
        "name": "Europa League",
        "localizedName": "Europa League",
        "ccode": "INT",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/73.png"
      },
      {
        "id": 53,
        "name": "Ligue 1",
        "localizedName": "Ligue 1",
        "ccode": "FRA",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/53.png"
      },
      {
        "id": 55,
        "name": "Serie A",
        "localizedName": "Serie A",
        "ccode": "ITA",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/55.png"
      },
      {
        "id": 138,
        "name": "Copa del Rey",
        "localizedName": "Copa del Rey",
        "ccode": "ESP",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/138.png"
      },
      {
        "id": 132,
        "name": "FA Cup",
        "localizedName": "FA Cup",
        "ccode": "ENG",
        "logo": "https://images.fotmob.com/image_resources/logo/leaguelogo/dark/132.png"
      }
    ]
  }
}
```
    """
    url = "https://free-api-live-football-data.p.rapidapi.com/football-popular-leagues"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
