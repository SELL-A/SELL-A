import time
from openai import OpenAI
import os
import httpx
from config import Config
import tiktoken

class LLM_util:
    def __init__(self):
        # openai_api_key = os.getenv('OPENAI_API_KEY')
        openai_api_key = Config.openai_api_key
        # print(openai_api_key)
        # Ignore stale system proxy env vars by default; they often cause TLS failures.
        self.client_gpt = OpenAI(
            api_key=openai_api_key,
            base_url="https://api.rcouyi.com/v1",
            http_client=httpx.Client(timeout=60.0, trust_env=False)
        )
        # self.client_gpt = OpenAI(api_key=openai_api_key)
        self.client_deepseek = OpenAI(
            api_key=Config.deepseek_key,
            base_url="https://api.deepseek.com",
            http_client=httpx.Client(timeout=60.0, trust_env=False)
        )
        self.client_nvidia = OpenAI(
            api_key=Config.nvidia_api_key,
            base_url=Config.nvidia_url,
            http_client=httpx.Client(timeout=500.0, trust_env=False)
        )

    def call_LLM(self, prompt, llm_name, client):
        message = [
            {"role": "user", "content": prompt}
        ]
        last_error = None
        for attempt in range(3):
            try:
                response = client.chat.completions.create(
                    model=llm_name,
                    messages=message,
                    temperature=0
                )
                # return response.choices[0].message['content']
                # print(response)
                return response.choices[0].message.content
            except Exception as e:
                print(e)
                last_error = e
                print(f"[LLM attempt {attempt + 1}/3] {type(e).__name__}: {e}")

        raise RuntimeError(f"LLM request failed after 3 attempts for model {llm_name}: {last_error}")

    def model_gpt35(self, prompt):
        model = "gpt-3.5-turbo"
        return self.call_LLM(prompt, model,self.client_gpt)

    def model_gpt4o(self, prompt):
        model = "gpt-5.4-mini"
        return self.call_LLM(prompt, model,self.client_gpt)


    def model_deepseek_chat(self, prompt):
        model = "gpt-5.4-mini"
        return self.call_LLM(prompt, model,self.client_gpt)

    def model_deepseek_coder(self, prompt):
        model = "gpt-5.4-mini"
        return self.call_LLM(prompt, model,self.cclient_gpt)

    def model_gpt4(self,prompt):
        model = "gpt-4"
        return self.call_LLM(prompt, model, self.client_gpt)

    def model_gpt4o_mini(self, prompt):
        model = "gpt-4o-mini"
        return self.call_LLM(prompt, model, self.client_gpt)

    def model_embedding(self, text):
    
        model = Config.model_embedding
        text = text.replace("\n", " ")
        try:
      
            response = self.client_gpt.embeddings.create(
            input=[text], 
            model=model
        )
      
            return response.data[0].embedding
        
        except Exception as e:
       
            print(f"{e}")
            raise

    @staticmethod
    def num_tokens_from_prompt(prompt):
       
        prompt = str(prompt)
        encoding = tiktoken.get_encoding(Config.encoding_name)
        num_tokens = len(encoding.encode(prompt))
        return num_tokens

    @staticmethod
    def get_top_k_tokens(prompt, k:int):
        
        embedding_encoding = Config.encoding_name
        encoding = tiktoken.get_encoding(embedding_encoding)
        tokens = encoding.encode(prompt, disallowed_special=())
        return tokens[:k]

    @staticmethod
    def tokens_to_text(tokens):
      
        embedding_encoding = Config.encoding_name
        encoding = tiktoken.get_encoding(embedding_encoding)
        return encoding.decode(tokens)



