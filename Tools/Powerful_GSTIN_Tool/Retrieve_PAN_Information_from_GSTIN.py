import os
import requests

def Retrieve_PAN_Information_from_GSTIN(gstin):
    """
    :API_description: Retrieve the PAN (Permanent Account Number) linked to a given GSTIN (Goods and Services Tax Identification Number) for tax verification purposes.
    :param gstin: The GSTIN for which PAN information is to be retrieved(e.g. 18AAACR5055K1Z6).
    :response_schema: 
    ```json
{
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "gstin": {
                    "type": "string",
                    "description": "The GST Identification Number (GSTIN) of the entity."
                },
                "pan_num": {
                    "type": "string",
                    "description": "The Permanent Account Number (PAN) of the entity."
                }
            },
            "required": ["gstin", "pan_num"]
        }
    },
    "required": ["data"]
}
```
    """
    url = f"https://powerful-gstin-tool.p.rapidapi.com/v1/gstin/{gstin}/pan-info"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "powerful-gstin-tool.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
