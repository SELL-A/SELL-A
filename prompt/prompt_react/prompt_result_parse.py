

def prompt_result_parse(query, json_response):

    prompt = f'''\
Here is a JSON format API response. 
Your task is to extract the key information required by the query from the JSON-formatted data, and the extracted content is described in a natural language. Please don't\
generate other unrelated content.
query:
{query}
JSON response:
{json_response}
'''
    return prompt