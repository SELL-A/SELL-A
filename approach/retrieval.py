
import pandas as pd
from config import Config
from ast import literal_eval
import numpy as np
from util.llm_util import LLM_util
from util.code_util import CodeUtil
from pathlib import Path
import json
import re




class Retrieval:
    def __init__(self):
        self.llm_util = LLM_util()

    @staticmethod
    def _keyword_fallback_retrieval(df_tools, user_requirement, top_k):
        requirement = str(user_requirement or '').lower()
        req_tokens = set(re.findall(r'[a-zA-Z0-9_]+', requirement))
        if not req_tokens:
            return df_tools.iloc[0:0]

        scored_rows = []
        for idx, row in df_tools.iterrows():
            tool_name = str(row.get("tool_name", "")).strip()
            tool_type = str(row.get("type", "")).strip()
            tool_desc = str(row.get("tool_description", "")).strip()
            text = f"{tool_name} {tool_type} {tool_desc}".lower()
            score = 0
            for token in req_tokens:
                if len(token) < 3:
                    continue
                if token in text:
                    score += 1
            if score > 0:
                scored_rows.append((idx, score))

        if not scored_rows:
            return df_tools.iloc[0:0]

        ranked_index = [idx for idx, _ in sorted(scored_rows, key=lambda x: x[1], reverse=True)[:top_k]]
        return df_tools.loc[ranked_index].copy()

    def consine_similarity(self, vec1, vec2):
     
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    def tool_retrieval(self, user_requirement, top_k=3):
      

        df_tools = pd.read_csv(Path(__file__).resolve().parents[1] / 'data' / 'tools.csv')
        candidate_lines = []
        for _, row in df_tools.iterrows():
            tool_name = str(row.get("tool_name", "")).strip()
            tool_type = str(row.get("type", "")).strip()
            candidate_lines.append(f'- tool_name: "{tool_name}", type: "{tool_type}"')

        prompt = f'''\
@Tool Retriever{{
    @Persona{{
        You are a strict tool selector for API orchestration.
    }}
    @Goal{{
        Select the {top_k} tools that are most useful for actually solving the user's requirement.
    }}
    @Instruction{{
        @Rule1 You MUST only choose from the provided candidate tools;
        @Rule2 Judge relevance mainly based on tool_name and type, but focus on whether the tool can directly help accomplish the user's task;
        @Rule3 Candidate order has NO meaning. Do NOT prefer tools just because they appear earlier in the list;
        @Rule4 Prefer tools whose domain clearly matches the user requirement. Reject tools from unrelated domains even if their names look generic;
        @Rule5 If the requirement needs multiple steps, choose tools that are most central to completing the whole task, not loosely related tools;
        @Rule6 Return ONLY a valid JSON array of tool_name strings, ordered from most relevant to less relevant;
        @Rule7 Return at most {top_k} tool_name values. If fewer than {top_k} tools are genuinely relevant, return fewer;
    }}
    @Input{{
        user_requirement: {user_requirement}
        candidate_tools:
{chr(10).join(candidate_lines)}
    }}
    @Output{{
        ["tool_name_1", "tool_name_2"]
    }}
}}'''

        try:
            selected = self.llm_util.model_deepseek_chat(prompt)
            selected = CodeUtil.parse_json_from_text(selected)
        except Exception:
            selected = []

        if not isinstance(selected, list):
            selected = []

        selected = [str(x).strip() for x in selected if str(x).strip()]
        df_tools_retrieved = df_tools[df_tools["tool_name"].isin(selected)].copy()
        if not df_tools_retrieved.empty:
            order_map = {name: idx for idx, name in enumerate(selected)}
            df_tools_retrieved["llm_rank"] = df_tools_retrieved["tool_name"].map(order_map)
            df_tools_retrieved = df_tools_retrieved.sort_values("llm_rank").head(top_k).drop(columns=["llm_rank"])
            return df_tools_retrieved

        

        fallback_df = self._keyword_fallback_retrieval(df_tools, user_requirement, top_k)
        if not fallback_df.empty:
            return fallback_df

        return df_tools.iloc[0:0]



