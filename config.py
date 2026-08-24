import os


class Config:
 
    openai_api_key = ''
 
    model_embedding = "text-embedding-ada-002"
    deepseek_key = ""
    Rapid_API_key = ""
    nvidia_url = ""
    nvidia_api_key = ""
  
    react_model = ''
    react_max_turn = 20

    encoding_name = "cl100k_base"

    tool_nums = 3


    api_path = os.path.join(BASE_DIR, "data", "apis.csv") 
    tool_path = os.path.join(BASE_DIR, "data", "tools.csv")
    

   