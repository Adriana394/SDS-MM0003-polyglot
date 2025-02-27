from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import gradio as gr
from openai import OpenAI
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HUGGINGFACE_API_KEY:
    raise ValueError("HUGGINGFACE_API_KEY not found.")

client = InferenceClient(api_key=HUGGINGFACE_API_KEY)
openai_client = OpenAI()

system_message = """
You are a helpful AI assistant whose job is to help the user learn a new language.

You will begin by asking the user the following:
1. Which language they want to learn?
2. What is their current level of proficiency in that language?
3. What level of proficiency they want to reach?
4. What is their intent for learning the language?

Using all the information above which the user will provide, you are to help guide them in learning the basics of their preferred language.

Here is an example conversation:
Assistant: Welcome to your personal learning companion. Which language would you like to learn?
User: French
Assistant: Great, let's get started with French. Let me teach you about some basic words and phrases in French.

And then you will proceed to tell the user about some basic words and phrases they can use.
"""

messages = [{"role": "system", "content": system_message}]

def chat(messages):
    logging.info("Sending messages to the chat model.")
    completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=messages,
        max_tokens=500
    )
    response = completion.choices[0].message['content']
    logging.info("Received response from the chat model.")
    return response

def generate_audio(text, lang):
    logging.info("Generating audio for the text.")
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = openai_client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    response.stream_to_file(speech_file_path)
    logging.info("Audio file saved.")
    return str(speech_file_path)

def transcribe_audio(audio_file):
    logging.info("Transcribing audio file.")
    audio_path = Path(audio_file)
    response = openai_client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_path
    )
    transcription = response.text
    logging.info("Transcription completed.")
    return transcription

def respond(selected_prompt, language, audio_input=None):
    logging.info("User input received: %s", selected_prompt)
    if audio_input:
        user_input = transcribe_audio(audio_input)
        logging.info("Transcribed audio input: %s", user_input)
    else:
        user_input = selected_prompt
    
    messages.append({"role": "user", "content": user_input})
    response = chat(messages)
    messages.append({"role": "assistant", "content": response})
    audio_file = generate_audio(response, language)
    logging.info("Response generated and audio file created.")
    return response, audio_file

def gradio_interface():
    prompt_templates = [
        "Teach me how to greet someone formally.",
        "How do I say 'Thank you'?",
        "What is the translation of 'Good morning'?",
        "Teach me some basic phrases"
    ]

    with gr.Blocks(css=".btn-primary {background-color: green;}") as demo:
        gr.Markdown("## Language Learning Assistant")
        
        with gr.Row():
            with gr.Column(scale=1):
                language = gr.Dropdown(choices=["French", "Spanish", "Dutch"], label="What language would you like to learn?")
                selected_prompt = gr.Dropdown(choices=prompt_templates, label="What would you like to learn?")
                audio_input = gr.Audio(sources=["upload","microphone"], type="filepath", label="Or speak your query")
            with gr.Column(scale=1):
                text_output = gr.Textbox(label="AI Response")
                audio_output = gr.Audio(label="AI Response (Audio)")
        
        submit_button = gr.Button("Submit", variant="primary")
        
        submit_button.click(respond, inputs=[selected_prompt, language, audio_input], outputs=[text_output, audio_output])

    logging.info("Launching Gradio interface.")
    demo.launch()

if __name__ == "__main__":
    logging.info("Starting the application.")
    gradio_interface()