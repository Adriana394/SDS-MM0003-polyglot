import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

# Initialize

openai = OpenAI()
MODEL = 'gpt-4o-mini'

system_message = "You are a helpful assistant who is polyglot that can teach many languages like spanish, french, hindi"
prompt = input("You: ")
history = " "
while prompt != "bye":
    messages = [
        {"role": "assistant", "content": system_message},
        {"role": "user", "content":  prompt}
    ]
    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)
    print("AI:", end="")
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    print("\n")
    prompt = input("You: ")