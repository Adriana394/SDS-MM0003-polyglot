# AI Language Companion

The **AI Language Companion** is an interactive language learning application that uses Gradio as a web interface and OpenAI's ChatGPT API. The assistant helps you learn new languages by:
- Providing translations into the chosen target language
- Offering grammar explanations and example sentences
- Delivering small exercises for language practice

The assistant responds in the language you write in, while always providing translations and examples in the selected target language.


## Features
- **Interactive Translations:** Translate words or phrases into the target language with appropriate examples.
- **Grammar Explanations:** Receive detailed explanations of grammatical rules for the target language.
- **Exercises and Examples:** Engage in small exercises and practice with example sentences to enhance your language skills.
- **Chat History:** Keep track of the conversation history and continue dialogues seamlessly.
- **Streaming Responses:** Enjoy real-time streaming responses from the assistant.
- **Multi-Language Support**: Currently supports English, German, Spanish, French, and Italian.

## Installation

### Requirements
- **Python 3.7** or higher
- **OpenAI API Key** (register at [OpenAI](https://openai.com/) if you haven't yet)
- **Jupyter Notebook** (if running the .ipynb version)


### Installing Dependencies
Install the necessary packages using:

```bash
pip install python-dotenv openai gradio
```

### Setting Up Environment Variables
Create a .env file in your project directory and add your OpenAI API Key:

```
OPENAI_API_KEY=your_openai_api_key 
```

## Usage
Start the application by running the script or notebook:

```
jupyter notebook language_assisstant_level1.ipynb
```
This will launch a Gradio web interface in your browser where you can:

1. Enter your query in the text box.
2. Choose the desired target language from the dropdown menu.
3. Submit your query using the "Submit" button to interact with the language assistant.
4. Reset the chat history using the "Clear" button.

### Example Queries
```
"How do you say 'hello' in Spanish?"
"What is the past tense of 'to go' in French?"
"Teach me basic greetings in German"
"Can you create a simple exercise for Italian numbers?"
```

## Project Structure
- AI_Language_Companion-Level1.ipynb: Main notebook containing the application code
- .env: Stores your OpenAI API Key (this file should not be uploaded to public repositories)
- README.md: Project documentation

## Customization
The AI Language Companion can be customized by modifying the system message in the code. The system message defines how the assistant behaves and responds to queries.
### Modifying the System Message
The system message can be found in the code as the *system_message* variable:
```
system_message = """You are an intelligent language learning assistant specialized in helping users learn new languages...
"""
```
You can modify this message to:

- Change the assistant's behavior
- Add new types of responses
- Implement different teaching methods
- Adjust the format of translations and examples
- Add specific rules for certain languages
- Customize error handling and corrections

### Example Modifications
1. **For more formal language teaching**:
```
system_message = """You are a formal language instructor. Always provide:
- Detailed grammatical explanations
- Academic terminology
- Formal language examples
- Structured exercises with clear learning objectives
"""
```
2. ** For conversation-focuses learning**:

```
system_message = """You are a conversational language partner. Focus on:
- Casual, everyday expressions
- Common phrases and idioms
- Cultural context and usage
- Natural conversation flow
"""
```

3. **For business language learning**:
```
system_message = """You are a business language specialist. Emphasize:
- Professional vocabulary
- Business communication examples
- Formal email and presentation phrases
- Industry-specific terminology
"""
```
### Important Considerations when Modifying
Important Considerations When Modifying

- Maintain the core translation and language handling rules
- Keep the instruction to respond in the user's input language
- Ensure clear formatting for translations and examples
- Test your modifications thoroughly
- Keep the instructions clear and unambiguous


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Notes
- **API Key**: Ensure that your OpenAI API Key is correctly set in the .env file for the application to work.
- **System Message**: The instructions defined in the system message control the behavior of the language assistant. Adjustments to these instructions may affect the quality of responses.
- **Rate Limits**: Be aware of OpenAI API rate limits and usage costs


Enjoy experimenting and happy language learning with AI Language Companion!



