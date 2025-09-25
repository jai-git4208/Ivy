import ollama
import json
from datetime import datetime
from actions import open_app  # your offline app executor

MODEL_NAME = "ivy"
LOG_FILE = "ivy_outputs.json"

def clean_output(raw_output: str) -> str:
    """
    Remove ```json and ``` wrappers if present, leaving pure JSON.
    """
    text = raw_output.strip()

    # Remove ```json at start
    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    # Remove ``` at start or end
    if text.startswith("```"):
        text = text[3:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()

    return text

def query_ivy(prompt: str):
    # Send prompt to Ivy via Ollama
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response["message"]["content"].strip()
    cleaned_output = clean_output(raw_output)

    try:
        parsed = json.loads(cleaned_output)  # parse cleaned JSON
    except json.JSONDecodeError:
        parsed = {
            "action": "none",
            "params": {},
            "response": cleaned_output
        }

    # Immediately execute open_app if requested
    if parsed.get("action") == "open_app":
        app_name = parsed.get("params", {}).get("app_name")
        if app_name:
            result_msg = open_app(app_name)
            print(f"\nIvy executed open_app: {result_msg}\n")
        else:
            print("\nNo app_name provided for open_app.\n")

    # Save the latest output exactly as parsed
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "output": parsed
    }
    with open(LOG_FILE, "w") as f:
        json.dump(log_entry, f, indent=2)

    return parsed


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        result = query_ivy(user_input)
        print(f"\nIvy: {json.dumps(result, indent=2)}\n")
