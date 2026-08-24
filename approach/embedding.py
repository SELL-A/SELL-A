import openai
import numpy as np
import pandas as pd
import os
from util import Util

class Embedding:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.util = Util()
        self.client = openai.OpenAI(api_key=api_key)
        self.model = 'text-embedding-3-small'


    def get_embedding(self, input):

        embedding = self.client.embeddings.create(
            model=self.model,
            input=input,
            encoding_format='float'
        )
        return embedding.data[0].embedding

    def consine_similarity(self, vec1, vec2):
   
        return np.dot(vec1,vec2) / (np.linalg.norm(vec1)*np.linalg.norm(vec2))

    def find_top_similar_texts(self,input_text,top_n=4):
   
        df = self.util.get_api_df()
        api_dict = {}
        for _, row in df.iterrows():
            api_vec = self.str2list(row['embedding'])
            api_dict[row['api_description']] = api_vec

        input_vec = self.get_embedding(input_text)
        similarities = []
        for key in api_dict.keys():
            vec = api_dict.get(key)
            similarity = self.consine_similarity(input_vec,vec)
            similarities.append((key,similarity))

 
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_n]

    def str2list(self,api_embedding_str:str):
        
        str_list = api_embedding_str.strip('[]').split(',')
        float_list = [float(i) for i in str_list]
        return float_list
