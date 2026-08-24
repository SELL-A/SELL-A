import os
import requests

def Get_All_Seasons():
    """
    :API_description: Retrieves a chronological list of available season identifiers, typically for systems tracking annual cycles like sports leagues or academic years. The response includes seasons from 2010/2011 to 2024/2025 in descending order.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "seasons": [
      "2024/2025",
      "2023/2024",
      "2022/2023",
      "2021/2022",
      "2020/2021",
      "2019/2020",
      "2018/2019",
      "2017/2018",
      "2016/2017",
      "2015/2016",
      "2014/2015",
      "2013/2014",
      "2012/2013",
      "2011/2012",
      "2010/2011"
    ]
  }
}
    ```
    """
    url = "https://free-api-live-football-data.p.rapidapi.com/football-league-all-seasons"
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