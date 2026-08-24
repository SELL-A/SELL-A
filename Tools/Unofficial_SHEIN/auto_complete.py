import os
import requests

def auto_complete(word, language, country, currency):
    """
    :API_description: Retrieve suggestions for related terms and categories based on a given term or phrase, particularly useful for product search in women's swimwear.
    :param word: The search term for which auto-complete suggestions are needed(e.g., "bikini top").
    :param language: The language code for the suggestions(e.g., "en").
    :param country: The country code for the suggestions(e.g., "US").
    :param currency: The currency code for the suggestions(e.g., "USD").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "string",
      "description": "Status code indicating the result of the API call."
    },
    "msg": {
      "type": "string",
      "description": "Message describing the result of the API call."
    },
    "info": {
      "type": "object",
      "properties": {
        "guideWords": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "word": {
                "type": "string",
                "description": "The main word or term."
              },
              "word_id": {
                "type": "string",
                "description": "Unique identifier for the word."
              },
              "wordLabel": {
                "type": ["string", "null"],
                "description": "Label associated with the word, if any."
              },
              "categories": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "cateId": {
                      "type": "string",
                      "description": "Unique identifier for the category."
                    },
                    "cateName": {
                      "type": "string",
                      "description": "Name of the category."
                    }
                  },
                  "required": ["cateId", "cateName"]
                },
                "description": "List of categories associated with the word."
              }
            },
            "required": ["word", "word_id", "categories"]
          },
          "description": "List of guide words with their associated categories."
        },
        "word": {
          "type": "array",
          "items": {
            "type": "string",
            "description": "List of related words or phrases."
          },
          "description": "Array of related words or phrases."
        },
        "is_suggested": {
          "type": "boolean",
          "description": "Flag indicating if the words are suggested."
        },
        "wordsInfo": {
          "type": ["object", "null"],
          "description": "Additional information about the words, if available."
        },
        "catWordInfo": {
          "type": ["object", "null"],
          "description": "Additional information about the categories, if available."
        },
        "trace_id": {
          "type": "string",
          "description": "Unique identifier for tracing the request."
        }
      },
      "required": ["guideWords", "word", "is_suggested", "trace_id"]
    }
  },
  "required": ["code", "msg", "info"]
}
    ```
    """
    url = "https://unofficial-shein.p.rapidapi.com/auto-complete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"word": word, "language": language, "country": country, "currency": currency}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "unofficial-shein.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

