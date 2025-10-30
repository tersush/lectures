from openai import OpenAI
from multiprocessing import Lock
from dotenv import load_dotenv, find_dotenv
import numpy as np

load_dotenv(dotenv_path=find_dotenv("key.env"))

def get_embeddings(texts: list[str]):
    client: OpenAI = OpenAI()
    
    embeddings: Any = client.embeddings.create(
        model = "Qwen/Qwen3-Embedding-0.6B",
        input=texts
    )
    return embeddings

if __name__=="__main__":
    embeddings = get_embeddings(texts=["мужчина","женщина"])
    print(embeddings[0])
    print(len(embeddings.data[0].embedding))