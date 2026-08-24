import os
import requests

def Additional_Title_Details(imdbid):
    """
    :API_description: Retrieve comprehensive details about a movie or TV show, including reviews, quotes, plot summaries, cast details, and trailer URLs.
    :param imdbid: The IMDb ID of the movie or TV show for which additional details are requested(e.g. "tt7286456").
    :response_schema: 
    ```json
{
  "imdbid": "tt7286456",
  "numVotes": 849733,
  "people": [
    {
      "category": "producer",
      "characters": null,
      "job": "producer",
      "peopleid": "nm0177896"
    },
    {
      "category": "actor",
      "characters": [
        "Arthur Fleck"
      ],
      "job": null,
      "peopleid": "nm0001618"
    },
    {
      "category": "actress",
      "characters": [
        "Sophie Dumond"
      ],
      "job": null,
      "peopleid": "nm5939164"
    },
    {
      "category": "actress",
      "characters": [
        "Penny Fleck"
      ],
      "job": null,
      "peopleid": "nm0175814"
    },
    {
      "category": "director",
      "characters": null,
      "job": null,
      "peopleid": "nm0680846"
    },
    {
      "category": "writer",
      "characters": null,
      "job": "written by",
      "peopleid": "nm0798788"
    },
    {
      "category": "writer",
      "characters": null,
      "job": "based on characters created by",
      "peopleid": "nm0004170"
    },
    {
      "category": "writer",
      "characters": null,
      "job": "based on characters created by",
      "peopleid": "nm0277730"
    },
    {
      "category": "writer",
      "characters": null,
      "job": "based on characters created by",
      "peopleid": "nm1047603"
    },
    {
      "category": "actor",
      "characters": [
        "Murray Franklin"
      ],
      "job": null,
      "peopleid": "nm0000134"
    }
  ],
  "plotSummary": "",
  "quotes": [
    "\n\nArthur Fleck:\n[written in notebook]\nThe worst part of having a mental illness is people expect you to behave as if you don't.     ",
    "\n\nArthur Fleck:\nI used to think that my life was a tragedy, but now I realize, it's a fucking comedy.     ",
     ],
  "reviews": [
    "I was a person that saw all the hype and claims of masterpiece as overreacting and overblown excitement for another Joker based film. I thought this looked solid at best and even a bit too pretentious in the trailer, but in here to say I was incredibly wrong. This is a massive achievement of cinema that's extremely rare in a day and age of cgi nonsense and reboots. While this is somewhat of a reboot of sorts, the standalone origin tale is impeccable from start to finish and echoes resemblance to the best joker origin comics from the past. Joaquin bleeds, sweats, and cries his every drop into this magnificently dedicated performance. Heath Ledger would be proud. This is undoubtedly the greatest acting performance since Heath's joker. The directing and writing is slickly brilliant and the bleak settings and tones are palpable throughout. When this film was over the place was blown away and every audience member was awestruck that they witnessed a film that could still transport them into a character's world and very existence. Believe the hype. This is going to be revered as a transcending masterpiece of cinema.",
    "Every once in a while a movie comes, that truly makes an impact. Joaquin's performance and scenography in all it's brilliance. Grotesque, haunting and cringy. Hard to watch at times,... but so mesmerizing, you won't blink an eye watching it. Tragic, but with seriously funny moments. Emotional rollercoaster - sometimes, with multiple emotions popping-up at the same time.this is far from a typical action-riddled predictable super-hero movie - it's a proper psychological thriller/drama, with the single best character development I have ever seen.",
    ],
  "title": "Joker",
  "trailerUrl": [
    "https://imdb.com/title/tt7286456/videoplayer/vi1723318041?ref_=tt_pv_vi_aiv_1",
    "https://imdb.com/title/tt7286456/videoplayer/vi2883960089?ref_=tt_pv_vi_aiv_2",
    "https://imdb.com/title/tt7286456/videoplayer/vi2059058969?ref_=tt_pv_vi_aiv_3"
  ]
}
    ```
    """
    url = "https://ott-details.p.rapidapi.com/getadditionalDetails"
    
    querystring = {"imdbid": imdbid}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

