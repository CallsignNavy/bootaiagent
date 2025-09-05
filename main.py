#python
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    print("Hello from bootaiagent!")

    
    #verbose check
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error: Enter a prompt, optionally followed by --verbose")
        sys.exit(1)
    if len(sys.argv) == 3 and sys.argv[2] != "--verbose":
        print("Error: Unknown option. Prompts must be followed with --verbose")
        sys.exit(1)

    user_prompt = sys.argv[1]
    verbose = (len(sys.argv) == 3 and sys.argv[2] == "--verbose")

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print(resp.text)

    if verbose:
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
