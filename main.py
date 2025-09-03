import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    print("Hello from bootaiagent!")

    if len(sys.argv) == 2:
        resp = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents = sys.argv[1]
        )
        print(resp.text)
    else:
        print("Error: Enter a prompt")
        sys.exit(1)
    print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
