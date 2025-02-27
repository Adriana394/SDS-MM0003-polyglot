import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
from subprocess import call

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

openai = OpenAI()
MODEL = 'gpt-4o-mini'

system_message = "You are a helpful assistant who is polyglot that can teach many languages like spanish, french, hindi"



def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response
    call(["python3", "tts.py", response])

gr.ChatInterface(fn=chat, type="messages").launch()
