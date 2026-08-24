
def prompt_task_plan_only(API_doc, user_requirement) -> str:
    prompt = '''\
@Task Planner{
    @Persona{
        You are an API planner who breaks a user requirement into actionable sub-tasks and assigns suitable APIs.
    }
    @ContextControl{
        Given a set of available APIs with descriptions and a user requirement,
        Break down user requirement into a list of clear, actionable sub-tasks.
        For each sub-task, identify one "Primary API" and multiple "Alternative APIs" that can fulfill the same or similar functionality.
        Only select APIs from the provided list of APIs. Do not invent or assume APIs.
    }
    @Terminology{
        Alternative ToolAPI List: Tools and their APIs with descriptions and parameters;
        Primary API: The most suitable API to complete the step;
        Alternative APIs: Backup APIs that can also fulfill the step;
    }
    @Instruction{
        @Command Break down the user requirement into concise steps;
        @Rule1 Each step MUST include "Primary API" as [API_name, Tool_name];
        @Rule2 Each step MAY include "Alternative APIs" as a list of [API_name, Tool_name];
        @Rule3 Use a SINGLE Tool_name across ALL steps whenever feasible; avoid switching tools unless no endpoint in the chosen tool can fulfill the step WITHOUT requiring unavailable specific identifiers (e.g., internal id fields);
        @Rule5 When multiple candidates exist, PRIORITIZE endpoints that do not depend on pre-obtained ids, and prefer query-based endpoints;
        @Rule4 Return ONLY valid JSON (no comments, no code fences);
    }
    @Knowledge{
        Alternative ToolAPI List:
{API_list}
    }
    @Input{
        user requirement:
{user_requirement}
    }
    @Output format[
        [
          {
            "task": "description of subtask",
            "Primary API": ["API_name", "Tool_name"],
            "Alternative APIs": [["API_name", "Tool_name"]]
          }
        ]
    ]
}'''
    prompt = prompt.replace('{API_list}', API_doc, 1)
    prompt = prompt.replace('{user_requirement}', user_requirement, 1)
    return prompt

def prompt_pseudocode_from_plan(task_plan_json, user_requirement) -> str:
    prompt = '''\
@Pseudocode Author{
    @Persona{
        You generate Python-like pseudocode that orchestrates API calls to satisfy the requirement.
    }
    @ContextControl{
       Your task is to generate clear, high-level pseudocode that logically fulfills the user's requirement using only the provided RESTful APIs.
    }
    @Instruction{
        @Command Use ONLY the "Primary API" entries from the provided task plan to build the pseudocode;
        @Rule1 Encapsulate the logic in an "if __name__ == '__main__':" block;
        @Rule2 The pseudocode must be modular: define multiple high-level abstract functions,each representing an API interaction or logical step;
        @Rule3 Do NOT output any JSON or selected API list; output ONLY the pseudocode;
    }
    @Input{
        user requirement:
{user_requirement}
        task plan (JSON):
{task_plan}
    }
    @Output{
    def Step_A:
        perform an API operation
    def Step_B:
        perform another API operation
    def Step_C():
        perform additional API operation or transformation
    def __main__():
            """Key Steps to accomplish the user requirement"""
    }
}'''
    prompt = prompt.replace('{user_requirement}', user_requirement, 1)
    prompt = prompt.replace('{task_plan}', task_plan_json, 1)
    return prompt
