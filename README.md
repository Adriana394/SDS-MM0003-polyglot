# 🌐 Operation Polyglot: AI Language Companion

## Mission Brief
Agents, your new mission is here!

You are tasked with developing an **AI Language Companion** to revolutionize language learning. This intelligent assistant must harness the power of LLMs to guide users in mastering new languages by providing translations, interactive lessons, and pronunciation guidance.

The objective? To create an engaging, personalized, and multimodal language learning experience that breaks traditional barriers and empowers users to become fluent in the languages of their dreams.

This mission will challenge your creativity, technical expertise, and attention to detail. Should you succeed, you will arm language learners with the ultimate AI-powered companion to conquer communication across borders.

Good luck, Agent. The clock is ticking. 🕒

## Core Objectives
- Develop a language-learning AI assistant using open-source LLMs.
- Support text translation and interactive learning for selected languages.
- Enable multimodal capabilities (audio output) at advanced levels.
- Ensure a natural and engaging user experience.

## Assignment Levels

### Level 1: The Initiate
**Requirements:**
- Use a model capable of multilingual chats and text translations.
- Focus on **text-only** interactions.
- Implement basic conversation history in order to keep chatting with the model.
- Handle basic prompts like:  
  - How do you say [word/phrase] in [target language]?  
  - Teach me a simple sentence in [target language].

**Technical Stack:**
- Python
- HuggingFace/Transformers or OpenAI API

**Example Scenario:**  
- **User:** *How do you say "Good Morning" in Spanish?*  
- **AI:** *"Good Morning" in Spanish is "Buenos días."*

### Level 2: The Specialist
**Requirements:**
- Build a simple **user interface** for text-based interactions using a framework like Gradio or Streamlit.
- Add **multimodal capabilities**, allowing the assistant to respond to users via audio in the selected language using a text-to-speech (TTS) engine (e.g., Google TTS, Coqui TTS).
- Handle more advanced prompts like:  
  - Teach me how to greet someone formally in [target language].  
  - Pronounce this word: [word].

**Technical Stack:**
- All Initiate tools plus:  
  - Gradio/Streamlit for UI  
  - TTS library for audio output

**Example Scenario:**  
- **User:** *How do I say "Thank you" in French?*  
- **AI (text):** *"Thank you" in French is "Merci."*  
- **AI (audio):** *(Plays audio: "Merci")*

### Level 3: The Operative
**Requirements:**
- Implement advanced multimodal features:  
  - Support two-way audio communication (speech-to-text + text-to-speech).  
  - Integrate pronunciation assessment and feedback for users. (optional)
- Deploy the final app to a cloud-based platform (e.g., HuggingFace Spaces).

**Technical Stack:**
- All Specialist tools plus:  
  - Speech-to-text libraries (e.g., Whisper, Vosk)  
  - Vector database (e.g., Weaviate, Pinecone)

**Example Scenario:**  
- **User (speaks):** *How do I ask for directions in German?*  
- **AI (text):** *"How do I get to [destination]?" in German is "Wie komme ich nach [destination]?"*  
- **AI (audio):** *(Plays audio: "Wie komme ich nach [destination]?")*

## Evaluation Criteria
- Accuracy of translations and language guidance
- Code quality and modularity
- Usability and responsiveness of the interface
- Quality and clarity of audio output
- Documentation and deployment readiness

## Submission Guidelines
1. Fork the repository.
2. Create a folder in `submissions/[your-name]` (please follow the example in the submissions folder).
3. Include:
   - Source code
   - Requirements file
   - Setup instructions
   - Documentation explaining your solution

## Getting Started

Follow these steps to set up the project locally:

### 1. Fork the Repository
To work on your own copy of this project:
1. Navigate to the GitHub repository for this project.  
2. Click the **Fork** button in the top-right corner of the repository page.  
3. This will create a copy of the repository under your GitHub account.

### 2. Clone the Repository
After forking the repository:
1. Open a terminal on your local machine.  
2. Clone your forked repository by running:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   ```
3. Navigate to the project directory:
    ```bash
    cd <repository-name>
    ```

### 3. Create a virtual environment
Setup a virtual environment to isolate project dependancies
1. Run the following command in the terminal to create a virtual environment
    ```bash
    python3 -m venv .venv
    ```
2. Activate the virtual environment
  - On a mac/linux:
    ```bash
    source .venv/bin/activate
    ```
  - On a windows:
    ```
    .venv\Scripts\activate
    ```
3. Verify the virtual environment is active (the shell prompt should show (.venv))

### 4. Install dependancies
Install the required libraries for the project
1. Run the following command in the terminal to isntall dependancies from the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```
Once the setup is complete, you can proceed with building your project


## Resources
- HuggingFace documentation: https://huggingface.co/docs/transformers/index
- Gradio documentation: https://www.gradio.app/docs
- LangChain documentation: https://python.langchain.com/docs/introduction/
- Huggingface Spaces documentation: https://huggingface.co/docs/hub/en/index#spaces