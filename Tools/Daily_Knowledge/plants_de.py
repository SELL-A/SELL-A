import os
import requests

def plants_de():
    """
    :API_description: Provides comprehensive details about a specific plant, including identification, scientific names, habitat, growth characteristics, and appearance.
    :param: None
    :response_schema: 
    ```json
{
  "id": "alpenfett",
  "name": "Alpen-Fettkraut",
  "basicData": {
    "id": "alpenfett",
    "name": "Alpen-Fettkraut",
    "scName": "Pinguícula alpína",
    "altNames": "",
    "search": "Pinguicula alpina",
    "gatId": "ping",
    "famId": "lenti",
    "home": "17",
    "climate": "4",
    "life": "4",
    "grow": "8",
    "bloomCol": "1",
    "pollen": "0",
    "nectar": "0",
    "props": "0",
    "shows": "0",
    "height": "15",
    "dist": "0",
    "light": "1",
    "ground": "14",
    "imgType": "2",
    "imgNotes": "© Griensteidl, Wikimedia Commons",
    "imgLic": null,
    "imgData": [
      "https://www.smagy.de/images/plantsOther/lenti/ping/alpenfett_01.jpg"
    ],
    "timeSeeds1": "0",
    "timeSeeds2": "0",
    "timeBloom1": "4",
    "timeBloom2": "7",
    "timeFruit1": "7",
    "timeFruit2": "9",
    "timeSeeds": "",
    "timeBloom": "Apr - Jul",
    "timeFruit": "Jul - Sep",
    "gatName": "",
    "gatScName": "Pinguícula",
    "famName": "Wasserschlauchgewächse",
    "famScName": "Lentibulariáceae"
  },
  "descrData": {
    "infoShort": "...",
    "infoGrow": "...",
    "infoAppear": "...",
    "infoBloom": "...",
    "infoRepro": "Nach der Befruchtung werden Kapselfrüchte gebildet, die winzige Samen enthalten. Manche Pflanzen vermehren sich auch vegetativ durch Brutzwiebeln, die nach der Blüte in den Blattachseln gebildet werden.",
    "infoMisc": "",
    "infoUse": ""
  },
  "medData": [],
  "insectData": []
}
    ```
    """
    url = "https://daily-knowledge.p.rapidapi.com/plants-de.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "daily-knowledge.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

