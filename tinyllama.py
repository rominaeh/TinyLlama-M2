import os
import urllib.request
from llama_cpp import Llama

MODEL_URL = "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
MODEL_PATH = "tinyllama.gguf"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Download complete.")
    else:
        print("Model already exists.")

def run_chat():
    print("Loading model…")
    llm = Llama(
        model_path=MODEL_PATH,
        chat_format="chatml",   
    )

    messages = [
        {"role": "user", "content": "Explain how MacBook M2 handles local AI inference."}
    ]

    print("Running inference…")
    response = llm.create_chat_completion(
        messages=messages,
        max_tokens=150,
        stream=False,
    )

    print("\n--- Assistant ---")
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    download_model()
    run_chat()
