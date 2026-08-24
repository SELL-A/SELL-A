import re
import sys
from pathlib import Path

import pandas as pd
import json
import os
import time
import logging
import subprocess
import uuid


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from util.llm_util import LLM_util
from util.code_util import CodeUtil
from prompt.prompt_select import prompt_select
from prompt.prompt_requirement import prompt_requirement
from prompt.prompt_task_plan import prompt_task_plan_only, prompt_pseudocode_from_plan
from prompt.prompt_error_judge import prompt_error_judge
from prompt.prompt_task_plan_error import prompt_pseudocode_error_fix
from approach.retrieval import Retrieval
from prompt.prompt_compiler import prompt_compiler
from prompt.prompt_code_repair import prompt_repair
from config import Config

current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())


BASE_DIR = Path(__file__).resolve().parents[1]
log_dir = BASE_DIR / "logs" / "log_SE_code_gen"
os.makedirs(log_dir, exist_ok=True)
log_filename = str(log_dir / f"log_{current_time}.log")


logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'), 
        logging.StreamHandler()  
    ]
)


class SEFramework:
    def __init__(self):
        openai_api_key = os.getenv('OPENAI_API_KEY')
        self.model = LLM_util()
        self.retrieval = Retrieval()
        self._reset_runtime_state()

        self.requirement_principles = [
            "1.Establish clear, measurable objectives to guide the development process and evaluate success.",
            "2.Involve all relevant stakeholders early in the analysis to gather diverse inputs and maintain alignment throughout the project lifecycle.",
            "3.Prioritize the needs and experiences of end-users to ensure the solution is user-centric and practical.",
            "4.Maintain traceability of requirements from inception through to implementation to ensure all needs are met and changes are managed effectively.",
            "5.Use an iterative approach to refine requirements through continuous feedback and validation.",
            "6.Evaluate the technical feasibility and risks associated with each requirement to ensure realistic planning and execution.",
            "7.Analyze and prioritize requirements based on their potential value to the business or project goals.",
            "8.Design requirements to accommodate changes and future expansions without significant reworks.",
            "9.Detailed use cases are provided, such as a user inputting a theme and receiving a list of movies fitting that theme available on selected streaming platforms.",
            "10.The requirement is broken down into specific functionalities, such as identifying movies based on themes and checking their availability on streaming platforms.",
            "11.User stories are created to capture the perspective of end-users and their interactions with the system, such as planning a movie night.",
            "12.Requirements should be expressed clearly and simply to ensure they are understood by all stakeholders.",
            "13.Ensure all requirements are in alignment with the overarching business strategy to support organizational objectives.",
            "14.Consider the broader system and operational environment when analyzing requirements to understand interdependencies and impacts.",
            "15.Design requirements to accommodate future growth and changes in technology without substantial alterations.",
            "16.Adopt an agile mindset to allow for flexibility in changing requirements as projects evolve and new insights are gained.",
            "17.Each requirement should have a clearly defined purpose that contributes directly to the project goals.",
            "18.Write requirements in a language that is easy to understand for all project stakeholders, avoiding technical jargon where possible.",
            "19.Aim for consensus among all key stakeholders on the importance and interpretation of each requirement.",
            "20.Formulate requirements in a way that their fulfillment can be objectively tested and verified.",
            "21.Each requirement should be unique and avoid overlap with others to prevent duplication and conflicts.",
            "22.Requirements should be concise, providing enough detail without unnecessary verbosity."
        ]

    def _reset_runtime_state(self):
        self.selected_APIs = {}
        self.last_runnable_code = ''
        self.last_stdout = ''
        self.last_stderr = ''
        self.repair_count = 0
        self.design_repair_count = 0
        self.code_repair_count = 0
        self.error_judge_count = 0
        self.repair_path = []
        self.repair_llm_calls = 0
        self.repair_token_cost = 0
        self.repair_time = 0.0
        self.current_run_id = ''


    def _track_repair_llm(self, stage, prompt, is_repair=False):
        self.repair_llm_calls += 1
        try:
            self.repair_token_cost += LLM_util.num_tokens_from_prompt(prompt)
        except Exception:
            pass
        if stage == 'error_judge':
            self.error_judge_count += 1
        if is_repair:
            self.repair_path.append(stage)
            self.repair_count += 1
            if stage == 'pseudocode_repair':
                self.design_repair_count += 1
            elif stage == 'code_repair':
                self.code_repair_count += 1

    @staticmethod
    def _summarize_requirement(user_requirement, max_len=120):
        text = ' '.join(str(user_requirement).split())
        if len(text) <= max_len:
            return text
        return text[:max_len] + '...'

    @staticmethod
    def _truncate_error_message(error_message, max_chars=10000, head_chars=2000, tail_chars=2000):
        text = str(error_message or '')
        if len(text) <= max_chars:
            return text
        head = text[:head_chars].rstrip()
        tail = text[-tail_chars:].lstrip()
        omitted = len(text) - len(head) - len(tail)
        return (
            f"{head}\n\n"
            f"... [truncated {omitted} chars of intermediate output] ...\n\n"
            f"{tail}"
        )


    def select_requirement_principles(self, user_requirement) -> str:
       

        principles_str = "\n        ".join(self.requirement_principles)
        prompt = prompt_select(user_requirement, principles_str)

        logging.info("prompt\n" + prompt)
       
        selected_principles = self.model.model_deepseek_chat(prompt)
        return selected_principles

    def requirement_analysis(self, selected_principles, user_requirement) -> str:
     
        requirement_principles = selected_principles.split("\n")
        requirement_principles = "        \n".join(requirement_principles)
        prompt = prompt_requirement(user_requirement, requirement_principles)
        analyzed_requirements = self.model.model_deepseek_chat(prompt)
        return analyzed_requirements

    def task_plan(self, user_requirement, tool_API_doc):
       
        prompt = prompt_task_plan_only(tool_API_doc, user_requirement)
        logging.info("task plan prompt\n" + prompt)
        task_plan_json = self.model.model_deepseek_chat(prompt)
        return task_plan_json

    def pseudocode_from_plan(self, user_requirement, task_plan_json, error_example=None):
        if error_example is None:
            prompt = prompt_pseudocode_from_plan(task_plan_json, user_requirement)
            logging.info("pseudocode prompt\n" + prompt)
            pseudocode = self.model.model_deepseek_chat(prompt)
            return pseudocode
        else:
            prompt = prompt_pseudocode_error_fix(task_plan_json, user_requirement, error_example)
            self._track_repair_llm('pseudocode_repair', prompt, is_repair=True)
            logging.info("pseudocode fix prompt\n" + prompt)
            pseudocode = self.model.model_deepseek_chat(prompt)
            return pseudocode

    def pseudocode_compiler(self, user_requirement, API_calling_code, pseudocode: str):
       
        prompt = prompt_compiler(API_calling_code, user_requirement, pseudocode)
        runnable_code = self.model.model_deepseek_chat(prompt)
        return runnable_code

    def error_judge(self, error_message, pseudocode, runnable_code, API_documentation, user_requirement):
       
        truncated_error_message = self._truncate_error_message(error_message)
        prompt = prompt_error_judge(API_documentation, pseudocode, runnable_code, truncated_error_message, user_requirement)
        self._track_repair_llm('error_judge', prompt, is_repair=False)
        error_result = self.model.model_deepseek_chat(prompt)
        error_result = CodeUtil.json_string_extract(error_result)
        return error_result

    def code_repair(self, runnable_code, error_message, error_documentation, API_documentation, user_requirement):
       
        prompt = prompt_repair(runnable_code, error_message, error_documentation, API_documentation, user_requirement)
        self._track_repair_llm('code_repair', prompt, is_repair=True)
        repaired_code = self.model.model_deepseek_chat(prompt)
        return repaired_code


    def _is_failure(self, run_result):
        out = (run_result.stdout or '').lower()
        err = (run_result.stderr or '')
        if err.strip():
            return True
        if getattr(run_result, 'returncode', 0) != 0:
            return True

        return False
      

    def _generate_import_lines(self, APIs: dict) -> str:
        header = (
            "import sys\n"
            "from pathlib import Path\n"
            "PROJECT_ROOT = Path(__file__).resolve().parents[1]\n"
            "if str(PROJECT_ROOT) not in sys.path:\n"
            "    sys.path.insert(0, str(PROJECT_ROOT))\n"
        )
        lines = [header]
        for value in APIs.values():
            tool_name = value[1].strip().replace(' ', '_')
            api_name = value[0].strip().replace(' ', '_')
            lines.append(f"from Tools.{tool_name}.{api_name} import {api_name}")
        return "\n".join(lines) + "\n"

    def _inject_import_lines_once(self, runnable_code: str, APIs: dict) -> str:
        header_lines = [
            "import sys",
            "from pathlib import Path",
            "PROJECT_ROOT = Path(__file__).resolve().parents[1]",
            "if str(PROJECT_ROOT) not in sys.path:",
            "    sys.path.insert(0, str(PROJECT_ROOT))",
        ]
        tool_import_lines = []
        for value in APIs.values():
            tool_name = value[1].strip().replace(' ', '_')
            api_name = value[0].strip().replace(' ', '_')
            tool_import_lines.append(f"from Tools.{tool_name}.{api_name} import {api_name}")

        generated_lines = set(header_lines + tool_import_lines)
        cleaned_lines = [line for line in runnable_code.splitlines() if line not in generated_lines]
        cleaned_code = "\n".join(cleaned_lines).lstrip()

        import_lines = self._generate_import_lines(APIs).rstrip()
        if cleaned_code:
            return import_lines + "\n\n" + cleaned_code
        return import_lines + "\n"

    @staticmethod
    def get_API_calling_code(APIs:dict):
       
        API_calling_code = ''
        tools_dir = Path(__file__).resolve().parents[1] / "Tools"
        for value in APIs.values():
            tool_name = value[1].strip().replace(' ', '_')
            API_name = value[0].strip().replace(' ', '_')
            API_code_path = tools_dir / tool_name / f"{API_name}.py"
            try:
                API_calling_code += open(API_code_path, 'r', encoding='utf-8').read()
            except Exception as e:
                logging.error(e, exc_info=True)
        return API_calling_code

    @staticmethod
    def extract_selected_APIs_from_plan(task_plan_json_str: str) -> dict:
      
        try:
            plan = CodeUtil.parse_json_from_text(task_plan_json_str)
        except Exception as e:
            logging.error("json extract failed", exc_info=True)
            raise e

        APIs = {}
        idx = 1
        invalid_tokens = {'', 'null', 'none', 'n/a', 'not available', 'na'}
        for item in plan:
            primary = item.get("Primary API")
            if isinstance(primary, list) and len(primary) >= 2:
                api_name = str(primary[0]).strip()
                tool_name = str(primary[1]).strip()
                if api_name.lower() in invalid_tokens or tool_name.lower() in invalid_tokens:
                    continue
                APIs[f"API{idx}"] = [api_name, tool_name]
                idx += 1
        if not APIs:
            raise ValueError("Task plan did not contain any valid API selections.")
        return APIs

    @staticmethod
    def code_run(runnable_code):
      
        os.makedirs(os.path.dirname(Config.runnable_code_temp_path), exist_ok=True)
        with open(Config.runnable_code_temp_path, 'w', encoding='utf-8') as f:
            f.write(runnable_code)
            f.flush()
            f.close()

      
        env = os.environ.copy()
        if 'RAPID_API_KEY' not in env or not env['RAPID_API_KEY']:
            env['RAPID_API_KEY'] = Config.Rapid_API_key
        env['PYTHONIOENCODING'] = 'utf-8'
        env['PYTHONUTF8'] = '1'

        code_path = Config.runnable_code_temp_path
        result = subprocess.run(
            ["python", code_path],
            stdout=subprocess.PIPE,  
            stderr=subprocess.PIPE,  
            text=True,  
            encoding='utf-8'  
            , env=env
        )
        return result

 
    def SE_framework(self, user_requirement):
     

        self._reset_runtime_state()
        ERROR = True 
        FIRST_RUN = True  
        error_report = ''

        max_design_retries = 2
        max_total_repairs = 2
        design_retries = 0
        budget_exhausted = False
        run_id = uuid.uuid4().hex[:8]
        self.current_run_id = run_id
        requirement_summary = self._summarize_requirement(user_requirement)
        logging.info("[RUN %s] START requirement=%s", run_id, requirement_summary)
       
        df_possible_tools = self.retrieval.tool_retrieval(user_requirement, Config.tool_nums)
        tool_API_doc = CodeUtil.get_api_doc(df_possible_tools)

        logging.info('[RUN %s] possible_tools:\n%s', run_id, tool_API_doc)

        task_plan_json = self.task_plan(user_requirement, tool_API_doc)
        logging.info('[RUN %s] task_plan:\n%s', run_id, task_plan_json)

       
        APIs = self.extract_selected_APIs_from_plan(task_plan_json)
        logging.info('[RUN %s] selected_APIs:\n%s', run_id, json.dumps(APIs, ensure_ascii=False))
        self.selected_APIs = APIs

        while ERROR and design_retries < max_design_retries:
            if FIRST_RUN:
              
                logging.info('[RUN %s] Design Round 0/%s: initial pseudocode generation', run_id, max_design_retries)
                pseudocode = self.pseudocode_from_plan(user_requirement, task_plan_json)
                pseudocode = CodeUtil.string_clean(pseudocode)
                logging.info('[RUN %s] initial pseudocode:\n%s', run_id, pseudocode)
                FIRST_RUN = False
            else:
                if self.repair_count >= max_total_repairs:
                    budget_exhausted = True
                    logging.warning('[RUN %s] Total repair budget exhausted before pseudocode repair (%s/%s)', run_id, self.repair_count, max_total_repairs)
                    break
                if design_retries >= max_design_retries:
                    logging.warning('[RUN %s] Design retries exhausted before pseudocode repair generation (%s/%s)', run_id, design_retries, max_design_retries)
                    break
                design_retries += 1
           
                logging.info('[RUN %s] Design Round %s/%s: pseudocode repair (total repairs used=%s/%s)', run_id, design_retries, max_design_retries, self.repair_count, max_total_repairs)
                error_example = CodeUtil.get_error_example(pseudocode, error_report, tool_API_doc)
                pseudocode = self.pseudocode_from_plan(user_requirement, task_plan_json, error_example)
                pseudocode = CodeUtil.string_clean(pseudocode)
                logging.info('[RUN %s] repair pseudocode:\n%s', run_id, pseudocode)


            
            API_calling_code = self.get_API_calling_code(APIs)
            logging.info('[RUN %s] API_calling_code:\n%s', run_id, API_calling_code)
        
            runnable_code = self.pseudocode_compiler(user_requirement, API_calling_code, pseudocode)
            logging.info('[RUN %s] runnable_code:\n%s', run_id, runnable_code)
    
            runnable_code = CodeUtil.get_code_from_string(runnable_code)
            runnable_code = self._inject_import_lines_once(runnable_code, APIs)
            self.last_runnable_code = runnable_code

       
            logging.info("[RUN %s] Executable Code:\n%s", run_id, runnable_code)
          
            result = self.code_run(runnable_code)
            self.last_stdout = result.stdout
            self.last_stderr = result.stderr

            if self._is_failure(result):
                repair_start = time.perf_counter()
              
                logging.warning('[RUN %s] Code execution failed:\n%s', run_id, result.stdout)
                error_message = result.stderr or result.stdout
                logging.error('[RUN %s] error_message:\n%s', run_id, error_message)
                API_doc = CodeUtil.get_API_doc_for_error_judge(APIs)
                error_result = self.error_judge(error_message, pseudocode, runnable_code, API_doc, user_requirement)
                logging.info('[RUN %s] error_judge:\n%s', run_id, error_result)
                error_result = CodeUtil.parse_json_from_text(error_result)
                error_level = error_result['error_level']
                error_report = error_result['error_report']
              
                if error_level == 'design_level':
                    logging.info('[RUN %s] Switch to design repair with error_level=%s', run_id, error_level)
                    self.repair_time += time.perf_counter() - repair_start
                    continue
                else:
                    max_coding_retries = 2
                    coding_retries = 0
                    while coding_retries < max_coding_retries:
                        if self.repair_count >= max_total_repairs:
                            budget_exhausted = True
                            logging.warning('[RUN %s] Total repair budget exhausted before code repair (%s/%s)', run_id, self.repair_count, max_total_repairs)
                            break
                        coding_retries += 1
                        logging.info('[RUN %s] Code Repair Round %s/%s (total repairs used=%s/%s)', run_id, coding_retries, max_coding_retries, self.repair_count, max_total_repairs)
                        API_documentation = CodeUtil.get_API_doc_foe_code_repair(APIs)
                        runnable_code = self.code_repair(runnable_code, error_message, error_report, API_documentation, user_requirement)
                        runnable_code = CodeUtil.get_code_from_string(runnable_code)
                        runnable_code = self._inject_import_lines_once(runnable_code, APIs)
                        logging.info('[RUN %s] repair runnable_code:\n%s', run_id, runnable_code)
                        logging.info("[RUN %s] Executable Code:\n%s", run_id, runnable_code)
                        run_result = self.code_run(runnable_code)
                        self.last_runnable_code = runnable_code
                        self.last_stdout = run_result.stdout
                        self.last_stderr = run_result.stderr
                        if not self._is_failure(run_result):
                            self.repair_time += time.perf_counter() - repair_start
                            logging.info('[RUN %s] Code execution successful:\n%s', run_id, run_result.stdout)
                            return run_result.stdout
                        else:
                            logging.warning('[RUN %s] Code execution failed:\n%s', run_id, run_result.stdout)
                            error_message = run_result.stderr or run_result.stdout
                            error_result = self.error_judge(error_message, pseudocode, runnable_code, API_doc, user_requirement)
                            error_result = CodeUtil.parse_json_from_text(error_result)
                            logging.info('[RUN %s] error_judge:\n%s', run_id, error_result)
                            error_level = error_result['error_level']
                            error_report = error_result['error_report']
                            if error_level == 'design_level':
                                logging.info('[RUN %s] Code repair escalated to design repair', run_id)
                                self.repair_time += time.perf_counter() - repair_start
                                break
                            else:
                                continue
                    if budget_exhausted:
                        self.repair_time += time.perf_counter() - repair_start
                        break
                    if coding_retries >= max_coding_retries:
                        self.repair_time += time.perf_counter() - repair_start
                        logging.warning("[RUN %s] Coding retries exhausted, forcing design level repair.", run_id)
                        error_report = "Coding retries exhausted. Please rethink the logic design."
                     
            if budget_exhausted:
                break
            if not self._is_failure(result):
               
                logging.info('[RUN %s] Code execution successful:\n%s', run_id, result.stdout)
                return result.stdout
        
        if budget_exhausted:
            logging.error("[RUN %s] Total repair budget exhausted (%s/%s). requirement=%s", run_id, self.repair_count, max_total_repairs, requirement_summary)
        else:
            logging.error("[RUN %s] All retries exhausted. requirement=%s", run_id, requirement_summary)
        return 'fail'
            

if __name__ == '__main__':
    se = SEFramework()
    user_requirement = "movies that fit params like 'Adventure' or 'Animation'. They are looking for three ."
    result = se.run(user_requirement)
    print(result)




