import ollama
import json
from datetime import datetime

MODEL_NAME = "ivy"  # the name of your custom Modelfile build

LOG_FILE = "ivy_outputs.jsonl"

def query_ivy(prompt: str):
    # Send prompt to Ivy via Ollama
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    
    raw_output = response["message"]["content"].strip()
    
    try:
        parsed = json.loads(raw_output)  # force parse JSON
    except json.JSONDecodeError:
        parsed = {
            "action": "none",
            "params": {},
            "response": raw_output
        }
    
    # Save to file (JSON lines format)
    with open(LOG_FILE, "a") as f:
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "output": parsed
        }
        f.write(json.dumps(log_entry) + "\n")
    
    return parsed


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        result = query_ivy(user_input)
        print(f"\nIvy: {result['response']}")
        print(f"Action: {result['action']} | Params: {result.get('params', {})}\n")
