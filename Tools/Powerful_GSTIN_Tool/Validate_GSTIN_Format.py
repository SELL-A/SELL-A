import os
import requests

def Validate_GSTIN_Format(gstin):
    """
    :API_description: This API verifies if a provided GSTIN (Goods and Services Tax Identification Number) is in a valid format, conforming to established standards.
    :param gstin: The GSTIN number to be validated(e.g. 18AAACR5055K1Z6).
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
                "is_valid": {
                    "type": "boolean",
                    "description": "Indicates whether the provided GSTIN is valid."
                }
            },
            "required": ["gstin", "is_valid"]
        }
    },
    "required": ["data"]
}
    ```
    """
    url = f"https://powerful-gstin-tool.p.rapidapi.com/v1/gstin/{gstin}/is-valid"
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