from ddgs import DDGS

def Search(query):
    """
    :API_description: Perform a web search using DuckDuckGo and return the top search results.
    :param query: The search query.
    :response_schema:
    ```json
[
  {
    "title": "Python Release Python 3.11.0 | Python.org",
    "href": "https://www.python.org/downloads/release/python-3110/",
    "body": "Mar 11 , 2015 · Python 3.11.0 is the newest major release of the Python programming language, with many new features and optimizations. It was released on Oct. 24, 2022, and is up to 10-60% faster than Python 3.10."
  },
  {
    "title": "Python 3.11 - What's New, Support Lifecycle & EOL Python - endoflife.date Python 3.11 Release Schedule — Python versions Python 3.11 Released - I Programmer Python 3.11 released - LWN.net PEP 664 – Python 3.11 Release Schedule | peps.python.org",
    "href": "https://versionlog.com/python/3.11/",
    "body": "..."
  },
  {
    "title": "Python - endoflife.date Python 3.11 Release Schedule — Python versions Python 3.11 Released - I Programmer Python 3.11 released - LWN.net PEP 664 – Python 3.11 Release Schedule | peps.python.org",
    "href": "https://endoflife.date/python",
    "body": "..."
  },
  {
    "title": "Python 3.11 Release Schedule — Python versions",
    "href": "https://gdevops.frama.io/python/versions/3.11.0/releases/releases.html",
    "body": "Jun 15, 2018 · Subsequent bugfix releases every two months."
  },
  {
    "title": "Python 3.11 Released - I Programmer",
    "href": "https://www.i-programmer.info/news/216-python/15824-python-311-released.html",
    "body": "..."
   
  }
]
    ```
    """
    try:
        results = DDGS(timeout=20).text(query, max_results=5)

        if hasattr(results, '__iter__') and not isinstance(results, (list, dict)):
            results = list(results)

        if not isinstance(results, list):
            raise Exception("Search returned an unexpected result type.")

        return results
    except Exception as e:
        raise Exception(f"Search request failed: {str(e)}")


if __name__ == "__main__":
    print(Search("Python 3.11 release"))

