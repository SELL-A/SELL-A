import os
import requests

def Get_Language_details_by_Language_ID(lang_id):
    """
    :API_description: Retrieve detailed information about a specific language using its unique identifier.
    :param lang_id: The ID of the language to retrieve information for.
    :response_schema: 
    ```json
{
  "lngId": "4",
  "lngIso2": "en",
  "lngDescription": "English (GB)"
}
```
    """
    url = f"https://auto-parts-catalog.p.rapidapi.com/languages/get-language/lang-id/{lang_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "auto-parts-catalog.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")