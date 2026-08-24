import os
import requests

def wcag_en():
    """
    :API_description: Provides detailed information about audio control criteria for web accessibility, including unique identifiers, version numbers, headlines, descriptions, conformance levels, and notes.
    :param: None
    :response_schema: 
    ```json
{
  "id": "images-of-text",
  "number": "1.4.5",
  "headline": "Images of Text",
  "description": "If the technologies being used can achieve the visual presentation, text is used to convey information rather than images of text except for the following:",
  "level": "AA",
  "details": [
    "<strong>Customizable</strong>: The image of text can be visually customized to the user's requirements;",
    "<strong>Essential</strong>: A particular presentation of text is essential to the information being conveyed.",
    "<strong>Note 1</strong>: Logotypes (text that is part of a logo or brand name) are considered essential."
  ]
}
    ```
    """
    url = "https://daily-knowledge.p.rapidapi.com/wcag-en.json"
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