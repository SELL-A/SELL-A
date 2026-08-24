import os
import requests

def Events_list(name: str, status: str, tournament_id: str, sports_id: str):
    """
    :API_description: Get a list of events with extensive filtering options.
    :param name: The name of the sport (e.g., "soccer").
    :param status: The status of the event (e.g., FINISHED,LIVE,SCHEDULED,CANCELLED,DELAYED,INTERRUPTED,POSTPONED,ABANDONED: FINISHED,LIVE,SCHEDULED,CANCELLED,DELAYED,INTERRUPTED,POSTPONED,ABANDONED)
    :param tournament_id: The ID of the tournament.
    :param sports_id: The ID of the sport.
    :response_schema: 
    ```json:
{
  "total": 6,
  "per_page": 100,
  "current_page": 0,
  "last_page": 0,
  "data": [
    {
      "id": 22,
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      },
      "category": {
        "id": 22,
        "name": "Bolivia",
        "slug": "bolivia",
        "code": "bo"
      },
      "tournament": {
        "id": 189,
        "name": "Division Profesional",
        "slug": "football-bolivia-division-profesional"
      },
      "season": {
        "id": 88,
        "slug": "2024",
        "year_start": 2024,
        "year_end": null
      },
      "team_home": {
        "id": 43,
        "name": "Nacional Potosi",
        "slug": "football-nacional-potosi",
        "team_type": "TEAM"
      },
      "team_away": {
        "id": 44,
        "name": "GV San Jose",
        "slug": "football-gv-san-jose",
        "team_type": "TEAM"
      },
      "status": "FINISHED",
      "status_details": null,
      "start_at": "2024-08-17 21:30:00",
      "winner": "HOME_WIN",
      "score_home": 2,
      "score_away": 1,
      "score_details": "0:1, 2:0",
      "comments": null,
      "final_result_only": false,
      "main_outcome_0": null,
      "main_outcome_1": null,
      "main_outcome_2": null,
      "main_volume_1": null,
      "main_volume_2": null
    },
    {
      "id": 123,
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      },
      "category": {
        "id": 155,
        "name": "Taiwan",
        "slug": "taiwan",
        "code": "tw"
      },
      "tournament": {
        "id": 1222,
        "name": "Premier League",
        "slug": "football-taiwan-premier-league"
      },
      "season": {
        "id": 222,
        "slug": "2024",
        "year_start": 2024,
        "year_end": null
      },
      "team_home": {
        "id": 245,
        "name": "Taichung",
        "slug": "football-taichung",
        "team_type": "TEAM"
      },
      "team_away": {
        "id": 246,
        "name": "Taiwan Steel",
        "slug": "football-taiwan-steel",
        "team_type": "TEAM"
      },
      "status": "FINISHED",
      "status_details": null,
      "start_at": "2024-08-18 08:00:00",
      "winner": "HOME_WIN",
      "score_home": 1,
      "score_away": 0,
      "score_details": "1:0, 0:0",
      "comments": null,
      "final_result_only": false,
      "main_outcome_0": null,
      "main_outcome_1": null,
      "main_outcome_2": null,
      "main_volume_1": null,
      "main_volume_2": null
    },
    {
      "id": 435,
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      },
      "category": {
        "id": 41,
        "name": "Czech Republic",
        "slug": "czech-republic",
        "code": "cz"
      },
      "tournament": {
        "id": 368,
        "name": "4. liga - Group C",
        "slug": "football-czech-republic-4-liga-group-c"
      },
      "season": {
        "id": 1669,
        "slug": "2024-2025",
        "year_start": 2024,
        "year_end": 2025
      },
      "team_home": {
        "id": 875849,
        "name": "Horni Redice",
        "slug": "football-horni-redice-bw1j9",
        "team_type": "TEAM"
      },
      "team_away": {
        "id": 875850,
        "name": "Velke Hamry",
        "slug": "football-velke-hamry-z8574",
        "team_type": "TEAM"
      },
      "status": "FINISHED",
      "status_details": null,
      "start_at": "2024-08-18 15:00:00",
      "winner": "AWAY_WIN",
      "score_home": 0,
      "score_away": 5,
      "score_details": "0:3, 0:2",
      "comments": null,
      "final_result_only": false,
      "main_outcome_0": null,
      "main_outcome_1": null,
      "main_outcome_2": null,
      "main_volume_1": null,
      "main_volume_2": null
    },
    {
      "id": 842,
      "sport": {
        "id": 1,
        "name": "Football",
        "slug": "football"
      },
      "category": {
        "id": 120,
        "name": "Norway",
        "slug": "norway",
        "code": "no"
      },
      "tournament": {
        "id": 920,
        "name": "OBOS-ligaen",
        "slug": "football-norway-obos-ligaen"
      },
      "season": {
        "id": 1785,
        "slug": "2024",
        "year_start": 2024,
        "year_end": null
      },
      "team_home": {
        "id": 876302,
        "name": "Ranheim",
        "slug": "football-ranheim-1hph3",
        "team_type": "TEAM"
      },
      "team_away": {
        "id": 876303,
        "name": "Mjondalen",
        "slug": "football-mjondalen-1my85",
        "team_type": "TEAM"
      },
      "status": "FINISHED",
      "status_details": null,
      "start_at": "2024-08-19 17:00:00",
      "winner": "AWAY_WIN",
      "score_home": 0,
      "score_away": 1,
      "score_details": "0:0, 0:1",
      "comments": "0:1 (0:0, 0:1)",
      "final_result_only": false,
      "main_outcome_0": 1.53,
      "main_outcome_1": 4.09,
      "main_outcome_2": 4.75,
      "main_volume_1": 20,
      "main_volume_2": 70
    }
    }
  ]
}
```
    """
    url = "https://odds-feed.p.rapidapi.com/api/v1/events"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "name": name,
        "status": status,
        "tournament_id": tournament_id,
        "sports_id": sports_id
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "odds-feed.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


