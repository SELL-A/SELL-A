import pandas as pd
from config import Config
import numpy as np
import re
from util.llm_util import LLM_util
from prompt.prompt_json_data_extract import prompt_json_data_extract
from prompt.prompt_code_extract import prompt_code_extract
import json
import time
import logging
from pathlib import Path

class CodeUtil:

    @staticmethod
    def _get_api_code_from_tools(tool_API_pairs):
       
        api_code = ''
        tools_dir = Path(__file__).resolve().parents[1] / "Tools"
        for values in tool_API_pairs.values():
            tool_name = str(values[1]).strip().replace(' ', '_')
            api_name = str(values[0]).strip().replace(' ', '_')
            api_code_path = tools_dir / tool_name / f"{api_name}.py"
            try:
                api_code += open(api_code_path, 'r', encoding='utf-8').read() + '\n\n'
            except Exception as e:
                logging.error(e, exc_info=True)
        return api_code

    @staticmethod
    def get_api_doc(df_tools):
       
        df_apis = pd.read_csv(Config.api_path)
        # df_tools = pd.read_csv(Config.tool_path)
        api_doc = ''

        for _, tool_row in df_tools.iterrows():
            tool_name = tool_row['tool_name']
            tool_desc = tool_row['tool_description']
            tool_str = f'''\
        Tool name: {tool_name}
        Tool description: {tool_desc}
'''
            api_doc = api_doc + tool_str
            # url = tool_row['head']
            apis = df_apis.loc[df_apis['tool_name'] == tool_name]
            apis_prefix = ''''''
            for index, api_row in apis.iterrows():
                api_name = api_row['api_name'].strip()
                api_desc = api_row['api_description'].strip()
                scenario = api_row['scenario'].strip()
                API_dependency = api_row['calling_dependency'].strip()
                required_parameters = api_row['required_parameters']
                parameters_lines = []
                if isinstance(required_parameters, float) and np.isnan(required_parameters):
                    parameters_lines = []
                elif isinstance(required_parameters, str):
                    parameters_lines = required_parameters.split('\n')
                else:
                    parameters_lines = []

                # parameters = '            \n'.join(parameters_lines)
                parameters = ''
                for line in parameters_lines:
                    p = f'''\
                {line.strip()}'''
                    parameters = parameters + p + '\n'
                    # parameters = '          ' + parameters.strip() + line + '\n'
                api_str = f'''\
            API name: {api_name}
            API description: {api_desc}
            API_dependency: {API_dependency}
            scenario: {scenario}
            parameters:
{parameters}\n'''
                apis_prefix = apis_prefix + api_str
            api_doc = api_doc + apis_prefix
        return api_doc

    
    @staticmethod
    def get_tool_doc(tool_name):
        """
       
        tool_name: Advanced Movie Search
tool_description:Search for movies via advanced queries like genre, name, etc. And get all their details
    api_name: Search by Genre
    api_description: This API allows users to discover movies by their genre.
    scenario: ...
    parameters:
        with_genres: (String) This is an optional parameter where the user can specify the genre of the movie they are looking for.
        page: (Number) This is an optional parameter where the user can specify the page number of the search results they want to view.

    api_name: Search by Name
    api_description: This API allows users to search for a movie by its name.
    scenario: ...
    parameters:
        query: (String) This is a required parameter where the user can specify the name of the movie they are searching for.
        page: (Number) This is an optional parameter where the user can specify the page number of the search results they want to view.

    api_name: Get Detailed Response
    api_description: This API provides detailed information about a movie based on its ID.
    scenario: ...
    parameters:
        movie_id: (Number) This is a required parameter where the user can specify the ID of the movie they want detailed information about.

        :param tool_name:
        :return:
        """

        df_tools = pd.read_csv(Config.tool_original_path)
        df_apis = pd.read_csv(Config.api_first_expan_path)

        df_selected_tool = df_tools.loc[df_tools['tool_name'] == tool_name]
        tool_description = ''
        for _,row in df_selected_tool.iterrows():
            tool_description = row['tool_description']

        tool_doc = f'''\
tool_name: {tool_name}
tool_description:{tool_description}'''
        apis = df_apis.loc[df_apis['tool_name'] == tool_name]
        api_doc = ''
        for _,row_api in apis.iterrows():
            api_name = row_api['api_name']
            api_description = row_api['api_description']
            response_schema = row_api['json_schema']

            required_parameters = row_api['required_parameters']

            
            if isinstance(required_parameters, float) and np.isnan(required_parameters):
                parameters_lines = []
            elif isinstance(required_parameters, str):
                parameters_lines = required_parameters.split('\n')
            else:
                parameters_lines = []

            parameters = ''
            if parameters_lines == []:
                parameters = 'None'

            for line in parameters_lines:
                p = f'''\
        {line.strip()}'''
                parameters = parameters + p + '\n'
            api_str = f'''
    api_name: {api_name}
    api_description: {api_description}
    scenario: ...
    parameters: 
{parameters}
    response_schema: 
    {response_schema}'''
            api_doc = api_doc + api_str
        tool_doc = tool_doc + api_doc
        return tool_doc

    @staticmethod
    def get_API_doc_for_error_judge(tool_API_pairs):
        
        return CodeUtil._get_api_code_from_tools(tool_API_pairs)


    @staticmethod
    def string_clean(original_string):
       
        text = str(original_string or '').strip()
        fenced_match = re.search(r"```(?:json|python|py)?\s*([\s\S]*?)```", text, re.IGNORECASE)
        if fenced_match:
            return fenced_match.group(1).strip()
        return text

    @staticmethod
    def _extract_balanced_json_substring(text):
        s = str(text or '')
        start = None
        opener = None
        for i, ch in enumerate(s):
            if ch in '{[':
                start = i
                opener = ch
                break
        if start is None:
            return ''
        closer = '}' if opener == '{' else ']'
        depth = 0
        in_string = False
        escape = False
        for i in range(start, len(s)):
            ch = s[i]
            if in_string:
                if escape:
                    escape = False
                elif ch == '\\':
                    escape = True
                elif ch == '"':
                    in_string = False
                continue
            if ch == '"':
                in_string = True
            elif ch == opener:
                depth += 1
            elif ch == closer:
                depth -= 1
                if depth == 0:
                    return s[start:i + 1]
        return ''

    @staticmethod
    def _escape_invalid_backslashes(text):
        return re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', text)

    @staticmethod
    def _repair_task_plan_json_text(text):
        s = CodeUtil.string_clean(text)
        if not s:
            return s
        s = re.sub(r'(^|\n)(\s*)(Primary API|Alternative APIs|task)(\s*):', r'\1\2"\3"\4:', s)
        s = re.sub(r'(^|\n)(\s*)"Primary API\s*:\s*\[', r'\1\2"Primary API": [', s)
        s = re.sub(r'(^|\n)(\s*)"Alternative APIs"\s*:\s*\[\s*\[\s*\[', r'\1\2"Alternative APIs": [[', s)
        s = re.sub(r'\]\s*\]\s*(\n\s*[}\]])', r']\1', s)
        return s

    @staticmethod
    def parse_json_from_text(text):
        candidates = []
        cleaned = CodeUtil.string_clean(text)
        if cleaned:
            candidates.append(cleaned)
        balanced = CodeUtil._extract_balanced_json_substring(text)
        if balanced and balanced not in candidates:
            candidates.append(balanced)
        repaired = CodeUtil._repair_task_plan_json_text(text)
        if repaired and repaired not in candidates:
            candidates.append(repaired)

        last_error = None
        for candidate in candidates:
            for variant in (candidate, CodeUtil._escape_invalid_backslashes(candidate)):
                try:
                    return json.loads(variant)
                except Exception as e:
                    last_error = e
                    continue
        try:
            repaired_by_model = CodeUtil.json_string_extract(text)
            if repaired_by_model:
                return json.loads(CodeUtil._escape_invalid_backslashes(CodeUtil.string_clean(repaired_by_model)))
        except Exception as e:
            last_error = e
        if last_error is not None:
            raise last_error
        raise ValueError("No JSON content found in text")

    @staticmethod
    def remove_docstrings(source_code):
      
        pattern = re.compile(r'""".*?"""', re.DOTALL)

       
        cleaned_code = pattern.sub('', source_code)

        return cleaned_code

    @staticmethod
    def json_string_extract(input_string):
       
        model = LLM_util()
        prompt = prompt_json_data_extract(input_string)
        json_string = model.model_deepseek_chat(prompt)
        extracted = CodeUtil._extract_balanced_json_substring(json_string)
        if extracted:
            return extracted
        return CodeUtil.string_clean(json_string)

    @staticmethod
    def get_error_example(pseudocode,error_report,tool_API_doc):
        error_example = f'''\
        tool_API_documentation:
        {tool_API_doc}
        pseudocode:
        {pseudocode}
        error_report: {error_report}
'''
        return error_example

    @staticmethod
    def configure_logging(log_dir):
    
        current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())

       
        log_filename = f"{log_dir}/log_{current_time}.log"

       
        logging.basicConfig(
            level=logging.INFO,  
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
            handlers=[
                logging.FileHandler(log_filename, encoding='utf-8'),  
                logging.StreamHandler()  
            ]
        )

    @staticmethod
    def get_code_from_string(original_string):
       
        direct_code = CodeUtil.string_clean(original_string)
        if direct_code and ('def ' in direct_code or 'import ' in direct_code or 'if __name__ ==' in direct_code):
            return direct_code

        model = LLM_util()
        prompt = prompt_code_extract(original_string)
        result = model.model_deepseek_coder(prompt)
        direct_result_code = CodeUtil.string_clean(result)
        if direct_result_code and ('def ' in direct_result_code or 'import ' in direct_result_code or 'if __name__ ==' in direct_result_code):
            return direct_result_code

        code = CodeUtil.parse_json_from_text(result)
        if isinstance(code, dict):
            python_code = code.get("Python_code") or code.get("python_code") or code.get("code")
            if python_code:
                return str(python_code)
        if isinstance(code, str):
            return code
        raise ValueError("Failed to extract Python code from model output")


    @staticmethod
    def get_API_doc_foe_code_repair(tool_API_pairs):
       
        return CodeUtil._get_api_code_from_tools(tool_API_pairs)


    @staticmethod
    def get_api_doc_for_codeact(df_tools):
        """
        Tool name: Advanced Movie Search
        Tool description: Search for movies via advanced queries like genre, name, etc. And get all their details
            API name: Search by Genre
            API description: This API allows users to discover movies by their genre.
            scenario: If a user wants to find all movies in the 'Action' genre, they would use this API.
            parameters:
                with_genres: (String) This is an optional parameter where the user can specify the genre of the movie they are looking for.
                page: (Number) This is an optional parameter where the user can specify the page number of the search results they want to view.

            API name: Search by Name
            API description: This API allows users to search for a movie by its name.
            scenario: If a user wants to find a movie named 'Kong', they would use this API.
            parameters:
                query: (String) This is a required parameter where the user can specify the name of the movie they are searching for.
                page: (Number) This is an optional parameter where the user can specify the page number of the search results they want to view.

            API name: Get Detailed Response
            API description: This API provides detailed information about a movie based on its ID.
            scenario: If a user wants to get detailed information about a movie with the ID '399566', they would use this API.
            parameters:
                movie_id: (Number) This is a required parameter where the user can specify the ID of the movie they want detailed information about.
        :return:
        """
        df_apis = pd.read_csv(Config.api_path)
        # df_tools = pd.read_csv(Config.tool_path)
        api_doc = ''

        for _, tool_row in df_tools.iterrows():
            tool_name = tool_row['tool_name']
            tool_desc = tool_row['tool_description']
            tool_str = f'''\
        Tool name: {tool_name}
        Tool description: {tool_desc}
'''
            api_doc = api_doc + tool_str
            # url = tool_row['head']
            apis = df_apis.loc[df_apis['tool_name'] == tool_name]
            apis_prefix = ''''''
            for index, api_row in apis.iterrows():
                api_name = api_row['api_name'].strip()
                response_schema = api_row['json_schema'].strip()
                api_desc = api_row['api_description'].strip()
                scenario = api_row['scenario'].strip()
                API_dependency = api_row['calling_dependency'].strip()
                API_request_code = api_row['example_calling_code'].strip()
                required_parameters = api_row['required_parameters']
                parameters_lines = []
                if isinstance(required_parameters, float) and np.isnan(required_parameters):
                    parameters_lines = []
                elif isinstance(required_parameters, str):
                    parameters_lines = required_parameters.split('\n')
                else:
                    parameters_lines = []

                # parameters = '            \n'.join(parameters_lines)
                parameters = ''
                for line in parameters_lines:
                    p = f'''\
                {line.strip()}'''
                    parameters = parameters + p + '\n'
                    # parameters = '          ' + parameters.strip() + line + '\n'
                api_str = f'''\
            API name: {api_name}
            API description: {api_desc}
            API_dependency: {API_dependency}
            API_request_code:{API_request_code}
            scenario: {scenario}
            parameters:
{parameters}
            respoonse_schema: {response_schema}\n'''
                apis_prefix = apis_prefix + api_str
            api_doc = api_doc + apis_prefix
        return api_doc




