import os
import requests

def Search_By_Name(query):
    """
    :API_description: This API allows users to search for movies by name, providing detailed information including title, overview, release date, popularity, and ratings.
    :param query: The search term for the movie.
    :response_schema: 
    ```json
{'page': 1, 'results': [{'adult': False, 'backdrop_path': 'https://image.tmdb.org/t/p/original/c3OHQncTAnKFhdOTX7D3LTW6son.jpg', 'genre_ids': [28, 80, 18, 53], 'id': 49026, 'title': 'The Dark Knight Rises', 'original_language': 'en', 'original_title': 'The Dark Knight Rises', 'overview': "...", 'popularity': 23.6114, 'poster_path': '...', 'release_date': '2012-07-17', 'softcore': False, 'video': False, 'vote_average': 7.796, 'vote_count': 24342}, {'adult': False, 'backdrop_path': None, 'genre_ids': [99], 'id': 243238, 'title': 'The Fire Rises: The Creation and Impact of The Dark Knight Trilogy', 'original_language': 'en', 'original_title': 'The Fire Rises: The Creation and Impact of The Dark Knight Trilogy', 'overview': '...', 'popularity': 1.8171, 'poster_path': '...', 'release_date': '2013-09-24', 'softcore': False, 'video': False, 'vote_average': 6.8, 'vote_count': 27}, {'adult': False, 'backdrop_path': None, 'genre_ids': [99], 'id': 1178799, 'title': 'E:60 - Matt Harvey: The Dark Knight Rises', 'original_language': 'en', 'original_title': 'E:60 - Matt Harvey: The Dark Knight Rises', 'overview': '...', 'popularity': 0.0286, 'poster_path': 'https://image.tmdb.org/t/p/original/2Ufw1MLUxbu5FuMmfO08lut6NWa.jpg', 'release_date': '2015-04-04', 'softcore': False, 'video': False, 'vote_average': 0, 'vote_count': 0}], 'total_pages': 1, 'total_results': 3}
```
    """
    url = "https://advanced-movie-search.p.rapidapi.com/api/search/movie"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "advanced-movie-search.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    query = "The Dark Knight Rises"
    results = Search_By_Name(query)
    print(results)