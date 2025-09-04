#python
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

def main():
    print("Hello from bootaiagent!")

    if len(sys.argv) == 2:

        resp = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )
        print(resp.text)
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")
    else:
        print("Error: Enter a prompt")
        sys.exit(1)

if __name__ == "__main__":
    main()
