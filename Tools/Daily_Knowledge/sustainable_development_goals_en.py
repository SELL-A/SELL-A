import os
import requests

def sustainable_development_goals_en():
    """
    :API_description: Provides comprehensive details about the 'Life on Land' goal, including its objectives, targets, and actionable tips for sustainable land management and biodiversity conservation.
    :param None
    :response_schema: 
    ```json
{
  "title": "Climate Action",
  "slug": "climate-action",
  "number": 13,
  "backgroundColor": "#3f7e44",
  "image": "...",
  "introduction": "Take urgent action to combat climate change and its impacts.",
  "manifest": "...",
  "targets": [
    {
      "title": "Strengthen resilience and Adaptive Capacity to Climate Related Disasters",
      "body": "Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries.",
      "pictogram": "https://prismic-io.s3.amazonaws.com/globalgoals%2F8f2d59b3-fbb1-4c33-9bfd-333b15b6cf9d_goal_13.1_rgb_ng.svg"
    },
    {
      "title": "...",
      "body": "...",
      "pictogram": "..."
    }
  ],
  "tips": [
    "Find a Goal 13 charity you want to support. Any donation, big or small, can make a difference! See the \"Get Involved\" section above.",
    "Recycle paper, glass, plastic, metal and old electronics."
    ]
}
```
    """
    url = "https://daily-knowledge.p.rapidapi.com/sustainable-development-goals-en.json"
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
