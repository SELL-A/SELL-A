import os
import requests

def Get_Player_Advance_Stats(playerid):
    """
    :API_description: Retrieves comprehensive advanced statistics for a specific NBA player across multiple seasons, including performance metrics per 40 minutes, shooting percentages, and usage rates.
    :param playerid: The unique identifier for the NBA player whose advanced statistics are being requested.
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "advancestats": {
      "teams": {
        "atlanta-hawks": {
          "id": "1",
          "uid": "s:40~l:46~t:1",
          "guid": "15096a54-f015-c987-5ec8-55afedf6272f",
          "slug": "atlanta-hawks",
          "location": "Atlanta",
          "name": "Hawks",
          "abbreviation": "ATL",
          "displayName": "Atlanta Hawks",
          "shortDisplayName": "Hawks",
          "color": "c8102e",
          "alternateColor": "fdb927",
          "isActive": true,
          "isAllStar": false,
          "logos": [
            {
              "href": "https://a.espncdn.com/i/teamlogos/nba/500/atl.png",
              "width": 500,
              "height": 500,
              "rel": [
                "full",
                "default"
              ]
            },
            {
              "href": "https://a.espncdn.com/i/teamlogos/nba/500-dark/atl.png",
              "width": 500,
              "height": 500,
              "rel": [
                "full",
                "dark"
              ]
            }
          ],
          "links": [
            {
              "language": "en-US",
              "rel": [
                "clubhouse",
                "desktop",
                "team"
              ],
              "href": "https://www.espn.com/nba/team/_/name/atl/atlanta-hawks",
              "text": "Clubhouse",
              "shortText": "Clubhouse",
              "isExternal": false,
              "isPremium": false
            },
            {
              "language": "en-US",
              "rel": [
                "roster",
                "desktop",
                "team"
              ],
              "href": "https://www.espn.com/nba/team/roster/_/name/atl/atlanta-hawks",
              "text": "Roster",
              "shortText": "Roster",
              "isExternal": false,
              "isPremium": false
            }
          ],
          "groups": {},
          "coaches": {},
          "venue": {
            "id": "1827",
            "fullName": "State Farm Arena",
            "shortName": "State Farm Arena",
            "address": {
              "city": "Atlanta",
              "state": "GA"
            },
            "grass": false,
            "indoor": true,
            "images": [
              {
                "href": "https://a.espncdn.com/i/venues/nba/day/1827.jpg",
                "width": 2000,
                "height": 1125,
                "rel": [
                  "full",
                  "day"
                ]
              }
            ]
          },
          "record": {},
          "againstTheSpreadRecords": {},
          "ranks": {},
          "franchise": {}
        },
        "new-orleans-pelicans": {
          "id": "3",
          "uid": "s:40~l:46~t:3",
          "guid": "9461f397-7882-94c0-c18c-e89bdc9e570e",
          "slug": "new-orleans-pelicans",
          "location": "New Orleans",
          "name": "Pelicans",
          "abbreviation": "NO",
          "displayName": "New Orleans Pelicans",
          "shortDisplayName": "Pelicans",
          "color": "0a2240",
          "alternateColor": "b4975a",
          "isActive": true,
          "isAllStar": false,
          "logos": [
            {
              "href": "https://a.espncdn.com/i/teamlogos/nba/500/no.png",
              "width": 500,
              "height": 500,
              "rel": [
                "full",
                "default"
              ]
            },
            {
              "href": "https://a.espncdn.com/i/teamlogos/nba/500-dark/no.png",
              "width": 500,
              "height": 500,
              "rel": [
                "full",
                "dark"
              ]
            }
          ],
          "links": [
            {
              "language": "en-US",
              "rel": [
                "clubhouse",
                "desktop",
                "team"
              ],
              "href": "https://www.espn.com/nba/team/_/name/no/new-orleans-pelicans",
              "text": "Clubhouse",
              "shortText": "Clubhouse",
              "isExternal": false,
              "isPremium": false
            }
          ],
          "groups": {},
          "coaches": {},
          "venue": {
            "id": "985",
            "fullName": "Smoothie King Center",
            "shortName": "Smoothie King Center",
            "address": {
              "city": "New Orleans",
              "state": "LA"
            },
            "grass": false,
            "indoor": true,
            "images": [
              {
                "href": "https://a.espncdn.com/i/venues/nba/day/985.jpg",
                "width": 2000,
                "height": 1125,
                "rel": [
                  "full",
                  "day"
                ]
              }
            ]
          },
          "record": {},
          "againstTheSpreadRecords": {},
          "ranks": {},
          "franchise": {}
        }
      },
      "categories": [
        {
          "name": "advanced",
          "displayName": "Regular Season ",
          "labels": [
            "P/40",
            "R/40",
            "A/40",
            "TS%",
            "AST",
            "TO",
            "USG",
            "REBR"
          ],
          "names": [
            "p40",
            "r40",
            "a40",
            "trueShootingPct",
            "assistRatio",
            "turnoverRatio",
            "usageRate",
            "reboundRate"
          ],
          "displayNames": [
            "P/40",
            "R/40",
            "A/40",
            "True Shooting Percentage",
            "Assist Ratio",
            "Turnover Ratio",
            "Usage Rate",
            "Rebound Rate"
          ],
          "descriptions": [
            "Points Per 40 Minutes.",
            "Rebounds Per 40 Minutes.",
            "Assists Per 40 Minutes."
            ],
          "statistics": [
            {
              "teamId": "3",
              "teamSlug": "new-orleans-pelicans",
              "season": {
                "year": 2023,
                "displayName": "2022-23"
              },
              "stats": [
                "8.7",
                "7.2",
                "5.1",
                "50.3",
                "32.2",
                "13.7",
                "12.6",
                "10.2"
              ],
              "position": "G"
            },
            {
              "teamId": "3",
              "teamSlug": "new-orleans-pelicans",
              "season": {
                "year": 2024,
                "displayName": "2023-24"
              },
              "stats": [
                "10.4",
                "6.9",
                "4.8",
                "52.9",
                "29.4",
                "10.6",
                "13.3",
                "9.7"
              ],
              "position": "G"
            },
            {
              "teamId": "1",
              "teamSlug": "atlanta-hawks",
              "season": {
                "year": 2025,
                "displayName": "2024-25"
              },
              "stats": [
                "16.7",
                "7.0",
                "5.2",
                "54.5",
                "22.6",
                "10.5",
                "18.7",
                "9.6"
              ],
              "position": "G"
            },
            {
              "teamId": "1",
              "teamSlug": "atlanta-hawks",
              "season": {
                "year": 2026,
                "displayName": "2025-26"
              },
              "stats": [
                "14.3",
                "8.3",
                "7.1",
                "54.2",
                "31.7",
                "9.5",
                "17.3",
                "11.2"
              ],
              "position": "G"
            }
          ],
          "totals": [
            "13.6",
            "7.4",
            "5.8",
            "0.0",
            "0.0",
            "0.0",
            "0.0",
            "0.0"
          ],
          "sortKey": "advanced"
        }
      ],
      "glossary": [
        {
          "abbreviation": "A/40",
          "displayName": "Assists Per 40 Minutes."
        },
        {
          "abbreviation": "AST",
          "displayName": "..."
        }
      ]
    }
  }
}
    ```
    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-player-advancestats"
    
    querystring = {"playerid": playerid}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")