# LingoMigo - AI Language Learning Companion
Chat your way to fluency with real-time text or voice interactions, instant transcriptions, and spot-on pronunciations.

## KEY FEATURES
- Multi-Language Support: Arabic, Chinese, French, German, Italian, Japanese, Hindi, Portuguese, Russian, Spanish.
- Real-Time Chat Assistance: Practice through conversational AI.
- Speech-to-Text: Distil-Whisper (distil-large-v3) for quick, accurate transcriptions.
- Language Detection & Pronunciation: XLM-RoBERTa plus Google TTS for clear audio output.
- Interactive Interface: Gradio-powered text and microphone input, plus audio playback.

## PROJECT COMPONENTS
- Language Model: Microsoft Phi-3.5-mini-instruct for lifelike, context-aware responses.
- ASR: Transcribe spoken queries via Distil-Whisper.
- Language Detection: Extract target-language phrases for pronunciation.
- TTS: Google gTTS combines audio segments with silences for clarity.
- Gradio UI: Dropdown for language selection, text/audio chat, and output playback.

## HOW IT WORKS
1. Choose your target language.
2. Type or speak your question or prompt.
3. LingoMigo processes it, detects key phrases, and replies.
4. Pronunciations are generated to reinforce correct speech.

## EXAMPLE USAGE
Selected Language: French
- User Text/Audio Input: How do I say Hello?
- Assistant Text output: "In French, you say "Bonjour".
- Assistant Audio output: (Pronounces "Bonjour" in French.) 