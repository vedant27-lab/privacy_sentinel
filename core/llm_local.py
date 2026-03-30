#import subprocess

#MODEL_PATH = "llama.cpp/models/phi-2.gguf"
#LLAMA_BIN = "llama.cpp/build/bin/main"


import requests

URL = "http://localhost:8080/completion"

def run_llm(prompt):
    response = requests.post(URL, json={
        "prompt": prompt,
        "n_predict": 200,
        "temperature": 0.7,
        "stop": ["</s>"]
    })

    return response.json()["content"]