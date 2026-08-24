import os
import requests

def Download_Stream(video_id, country_geo):
    """
    :API_description: The API retrieves comprehensive metadata for a specific YouTube video, including title, description, duration, and channel details.
    :param video_id: The ID of the YouTube video to download.
    :param country_geo: The geo-location code representing the country.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Status of the API response, typically 'OK' for successful responses."
    },
    "id": {
      "type": "string",
      "description": "Unique identifier for the video."
    },
    "title": {
      "type": "string",
      "description": "Title of the video."
    },
    "lengthSeconds": {
      "type": "string",
      "description": "Duration of the video in seconds."
    },
    "keywords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of keywords associated with the video."
    },
    "channelTitle": {
      "type": "string",
      "description": "Title of the channel that uploaded the video."
    },
    "channelId": {
      "type": "string",
      "description": "Unique identifier for the channel."
    },
    "description": {
      "type": "string",
      "description": "Detailed description of the video content."
    },
    "thumbnail": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "URL of the thumbnail image."
          },
          "width": {
            "type": "integer",
            "description": "Width of the thumbnail image in pixels."
          },
          "height": {
            "type": "integer",
            "description": "Height of the thumbnail image in pixels."
          }
        },
        "required": ["url", "width", "height"]
      },
      "description": "List of thumbnail images with different dimensions."
    },
    "allowRatings": {
      "type": "boolean",
      "description": "Indicates whether the video allows user ratings."
    },
    "viewCount": {
      "type": ["string", "null"],
      "description": "Number of views for the video, or null if not available."
    },
    "isPrivate": {
      "type": "boolean",
      "description": "Indicates whether the video is private."
    },
    "isUnpluggedCorpus": {
      "type": "boolean",
      "description": "Indicates whether the video is part of the Unplugged Corpus."
    },
    "isLiveContent": {
      "type": "boolean",
      "description": "Indicates whether the video is live content."
    },
    "isFamilySafe": {
      "type": "boolean",
      "description": "Indicates whether the video is family-safe."
    },
    "availableCountries": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of countries where the video is available."
    },
    "isUnlisted": {
      "type": "boolean",
      "description": "Indicates whether the video is unlisted."
    },
    "category": {
      "type": "string",
      "description": "Category of the video."
    },
    "publishDate": {
      "type": "string",
      "format": "date-time",
      "description": "Date and time when the video was published."
    },
    "uploadDate": {
      "type": "string",
      "format": "date-time",
      "description": "Date and time when the video was uploaded."
    },
    "storyboards": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "width": {
            "type": "string",
            "description": "Width of the storyboard thumbnails."
          },
          "height": {
            "type": "string",
            "description": "Height of the storyboard thumbnails."
          },
          "thumbsCount": {
            "type": "string",
            "description": "Number of thumbnails in the storyboard."
          },
          "columns": {
            "type": "string",
            "description": "Number of columns in the storyboard grid."
          },
          "rows": {
            "type": "string",
            "description": "Number of rows in the storyboard grid."
          },
          "interval": {
            "type": "string",
            "description": "Interval between thumbnails in milliseconds."
          },
          "storyboardCount": {
            "type": "integer",
            "description": "Number of storyboards available."
          },
          "url": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of URLs for the storyboard images."
          }
        },
        "required": ["width", "height", "thumbsCount", "columns", "rows", "interval", "storyboardCount", "url"]
      },
      "description": "List of storyboards with different dimensions and intervals."
    },
    "captions": {
      "type": "object",
      "properties": {
        "captionTracks": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "baseUrl": {
                "type": "string",
                "description": "Base URL for the caption track."
              },
              "name": {
                "type": "string",
                "description": "Name of the caption track."
              },
              "vssId": {
                "type": "string",
                "description": "Unique identifier for the caption track."
              },
              "languageCode": {
                "type": "string",
                "description": "Language code for the caption track."
              },
              "isTranslatable": {
                "type": "boolean",
                "description": "Indicates whether the caption track is translatable."
              }
            },
            "required": ["baseUrl", "name", "vssId", "languageCode", "isTranslatable"]
          }
        }
      },
      "description": "Information about available caption tracks."
    }
  },
  "required": ["status", "id", "title", "lengthSeconds", "keywords", "channelTitle", "channelId", "description", "thumbnail", "allowRatings", "viewCount", "isPrivate", "isUnpluggedCorpus", "isLiveContent", "isFamilySafe", "availableCountries", "isUnlisted", "category", "publishDate", "uploadDate", "storyboards", "captions"]
}
    ```
    """
    url = "https://yt-api.p.rapidapi.com/dl"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": video_id, "cgeo": country_geo}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")