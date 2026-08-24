import os
import requests

def Trending_News(topic, language):
    """
    :API_description: Retrieves trending news articles based on both live and historical topics across 61 categories
    :param topic: The topic of news to fetch The topic of interest, example: General, Politics, Sports, or a subtopic Soccer. Check out the Supported Topics endpoint to see a list of all the topics you can search for.
    :param language: Language code for the news (e.g., "en" for English).
    :response_schema:
    ```json
{
"type": "object",
"properties": {
"success": {
"type": "boolean"
},
"data": {
"type": "array",
"items": {
"type": "object",
"properties": {
"title": {
"type": "string"
},
"url": {
"type": "string",
"format": "uri"
},
"excerpt": {
"type": "string"
},
"thumbnail": {
"type": "string",
"format": "uri"
},
"language": {
"type": "string"
},
"paywall": {
"type": "boolean"
},
"contentLength": {
"type": "integer"
},
"date": {
"type": "string",
"format": "date-time"
},
"authors": {
"type": "array",
"items": {
"type": "string"
}
},
"keywords": {
"type": "array",
"items": {
"type": "string"
}
},
"publisher": {
"type": "object",
"properties": {
"name": {
"type": "string"
},
"url": {
"type": "string",
"format": "uri"
},
"favicon": {
"type": "string",
"format": "uri"
}
},
"required": ["name", "url", "favicon"]
}
},
"required": ["title", "url", "excerpt", "thumbnail", "language", "paywall", "contentLength", "date", "authors", "keywords", "publisher"]
}
},
"size": {
"type": "integer"
},
"totalHits": {
"type": "integer"
},
"hitsPerPage": {
"type": "integer"
},
"page": {
"type": "integer"
},
"totalPages": {
"type": "integer"
},
"timeMs": {
"type": "integer"
}
},
"required": ["success", "data", "size", "totalHits", "hitsPerPage", "page", "totalPages", "timeMs"]
}
    ```
    """
    url = "https://news-api14.p.rapidapi.com/v2/trendings"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "topic": topic,
        "language": language
    }
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "news-api14.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == '__main__':
    print(Trending_News("Sports", "en"))