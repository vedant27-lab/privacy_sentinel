from llama_cpp import Llama

llm = Llama(
    model_path="llama.cpp/phi-2.Q8_0.gguf",
    n_gpu_layers=50,  # GPU usage
    n_ctx=1024
)

while True:
    prompt = input("You: ")
    output = llm(prompt, max_tokens=200)
    print("AI:", output["choices"][0]["text"])