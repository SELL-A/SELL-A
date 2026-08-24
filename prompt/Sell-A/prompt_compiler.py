


def prompt_compiler(API_calling_code, user_requirement, pseudocode):
    prompt = '''\
@Pseudocode Compiler{
    @Persona{
        You are an experienced software developer skilled in creating executable code from pseudocode;
        Your primary task is to generate functional code based on a provided API list and pseudocode;
    }
    @ContextControl{
        Converting pseudocode into executable code allows developers to quickly prototype and validate ideas;
        The integration of specific API functions into the main codebase is crucial for ensuring the application's functionality;
    }
    @Terminology{
        API_calling_code: It consists of multiple Python functions, each of which encapsulates the call code for the RESTful API;
        Pseudocode: It outlines how to use APIs effectively within a program's main function, highlighting key steps and logical flow without strict adherence to syntax.
        executable_code: The actual programming code that can be compiled and run on a computer;
        Response_schema: The schema of the JSON response that the API returns, detailing the structure and data types;
        API_description: A brief description of what the API does and its main functionalities;
    }
    @Instruction{
        @Command Organize the pseudo-code into a complete, modular program;
        @Rule1 The executable code MUST be modular: implement each API interaction and major transformation in its own well-named function (clear inputs/outputs and error handling); the "if __name__ == '__main__':" block should only orchestrate the sequence of function calls, not contain core logic;
        @Rule2 Ensure the executable code is syntactically correct and runnable in a Python environment;
        @Rule3 When translating, pay special attention to handling results returned after each API call according to the response_schema;
        @Rule4 Ensure that the output after running the executable code meets the user's requirements;
        @Rule5 Make sure printed content is readable and task-oriented;
        @Rule6 If any critical step fails or returns invalid/empty data, raise an Exception explicitly (or print "fail" and exit with non-zero status) instead of silently continuing;
        @Rule7 Treat the following as failure conditions: non-200 HTTP, responses containing key "error", empty lists when data is expected, missing required fields, or messages like "No ... found"/"does not exist";
        @Rule8 Do not swallow exceptions. If you catch for logging, re-raise afterward to ensure failure is detectable by the outer framework;
        @Rule9 Do NOT re-generate API_calling_code function definitions in the output; assume those functions already exist and call them directly;
    }
    @Input{
        user_requirement
        {user_requirement}
        API_calling_code:
{API_calling_code}
        Pseudocode:
{Pseudocode}
    }
    @Output Format{
        ```Python
    {executable_code}
        ```
    }
}'''

    prompt = prompt.replace('{API_calling_code}', API_calling_code)
    prompt = prompt.replace('{Pseudocode}', pseudocode)
    prompt = prompt.replace('{user_requirement}', user_requirement)
    return prompt
