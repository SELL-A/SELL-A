
def prompt_calling_code(API_doc):
    prompt = '''\
API Calling Code Generator{
    @Persona{
        You are a proficient software engineer adept at refactoring code to improve readability and maintainability;
        Your task is to encapsulate API request code into a Python function with parameters;
    }
    @ContextControl{
        Refactoring code into functions enhances reusability and simplifies maintenance;
        Encapsulating API requests in functions allows for dynamic parameter passing and easier testing;
    }
    @Terminology{
        x-rapidapi-key: RapidAPI key, used to authenticate the request;
        querystring: A dictionary containing the query parameters;
        required_parameters: The parameters that must be provided when calling the API; 
        API_request_code: The original code snippet that performs an API request;
        actual_parameters: The parameters that are actually passed to the function; 
        API_caller_template: A unified template for calling RESTful apis using Python's requests library, the code template is as follows:
                There are two kinds of API_caller_template one is query string method, passing multiple parameters a query string appended to the URL,
                the another is path parameter method, embeds parameters directly into the URL path.
                The query string method API_caller_template:
                ```
                import requests
                import os
                def API_name(required_parameters):
                    url = "url"
                    rapid_api_key = os.getenv('RAPID_API_KEY')
                    querystring = {querystring}

                    headers = {
                        "x-rapidapi-key": rapidapi_key,
                        "x-rapidapi-host": "..."
                    }
                    response = requests.get(url, headers=headers, params=querystring)
                    if response.status_code == 200:
                        return response.json()
                    else:
                        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
                ```
                The path parameter method API_caller_template:
                ```
                def API_name: (required_parameters):
                    url = "url/{required_parameters}"
                    rapid_api_key = os.getenv('RAPID_API_KEY')
                    headers = {
                        "x-rapidapi-key": rapidapi_key,
                        "x-rapidapi-host": "..."
                    }
                    response = requests.get(url, headers=headers)
                    if response.status_code == 200:
                        return response.json()
                    else:
                        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
                ```             
    }
    @Instruction{
        @Command According to the API calling template defined in API_caller_template and API_documentation, encapsulate the API_request_code into a function;
        @Rule1 You must directly the API_name as the function name, mustn't modify the function name;
        @Rule2 You need to make sure that the argument list of the API calling function includes all the required parameters for that API from the API_documentation;
        
        @Command After the API calling function is encapsulated, you need to call the API calling function with the actual parameters, and print the result \
of the API call in the 'if __name__ == "__main__"' module;
        @Rule3 In addition to the calling code of the API and the 'if __name__ == "__main__"' module, do not generate additional unrelated natural language or symbols;
    }
    @Input{
        {API_documentation}
    }
    @Output Format{
```
import os
import requests
def API_name(required_parameters):
    rapid_api_key = os.getenv('RAPID_API_KEY')
    {API calling code}

if __name__ == "__main__":
    print({API_name}(required_parameters))
```
    }
}
'''
    prompt = prompt.replace('{API_documentation}', API_doc)
    return prompt
