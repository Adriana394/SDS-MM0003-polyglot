from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HUGGINGFACE_API_KEY:
    raise ValueError("HUGGINGFACE_API_KEY not found.")

client = InferenceClient(api_key=HUGGINGFACE_API_KEY)

system_message = """
You are a helpful AI assistant whose job is to help the user learn a new language.

You will begin by asking the user the following:
1. Which language they want to learn?
2. What is their current level of proficiency in that language?
3. What level of proficiency they want to reach?
4. What is their intent for learning the language?

Using all the information above which the user will provide, you are to help guide them in learning the basics of their preferred language.

Please handle these specific types of queries:
- How do you say [word/phrase] in [target language]?
- Teach me a simple sentence in [target language].
- What's the translation of [word/phrase] in [target language]?
- Help me understand basic greetings in [target language].

When providing translations, make sure to explain pronunciation tips when relevant.

Here is an example conversation:
Assistant: Welcome to your personal learning companion. Which language would you like to learn?
User: French
Assistant: Great, let's get started with French. Let me teach you about some basic words and phrases in French.

And then you will proceed to tell the user about some basic words and phrases they can use.
"""

# Initialize conversation history
messages = [{"role": "system", "content": system_message}]

def chat(user_input):
    """
    Process user message and return AI response.
    Args:
        user_input: String containing the user's message
    Returns:
        String containing the AI's response
    """
    global messages
    
    # Add user message to conversation history
    messages.append({"role": "user", "content": user_input})
    
    # Get response from model
    completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=messages,
        max_tokens=500
    )
    response = completion.choices[0].message['content']
    
    # Add AI response to conversation history
    messages.append({"role": "assistant", "content": response})
    
    return response

def main():
    """
    Main function to run the language learning assistant in the terminal.
    """
    print("🌐 Welcome to the AI Language Companion!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.\n")
    
    # Initial greeting
    print("AI: Welcome to your personal learning companion. Which language would you like to learn?\n")
    
    # Main conversation loop
    while True:
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("AI: Thank you for learning with me today! Goodbye!")
            break
        
        # Get and display AI response
        ai_response = chat(user_input)
        print(f"AI: {ai_response}\n")

if __name__ == "__main__":
    main()