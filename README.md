# AI Voice Assistant

An AI-powered voice assistant built with LiveKit that interacts with users through voice. The assistant listens to user commands, processes them using AI, and responds with concise, natural voice replies.

### Features
- Real-time voice interaction.
- Short, concise, and natural responses.
- Processes user commands using advanced AI tools.
- Speech-to-text and text-to-speech capabilities for seamless communication.

### Technologies 
- Python: Core programming language.
- LiveKit Agents: For building and managing the voice assistant.
- Silero: For voice activity detection.
- OpenAI Plugins: For natural language understanding, speech-to-text, and text-to-speech.

### Prerequisites
- Python 3.8+
- Pip (Python Package Manager)
- A .env file with required configurations (e.g., API keys for LiveKit and OpenAI).
- LiveKit Playground: A web-based interface to interact with the voice assistant in real-time

### Installation 
1. Clone 
```bash
git clone https://github.com/Ben-Arlanda/AI-Voice-Assistant.git
```
2. Create and activate a virtual environment
```bash 
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Create a .env file in the root directory and add the necessary API keys
```bash
LIVEKIT_API_KEY=
OPENAI_API_KEY=
LIVEKIT_API_SECRET=
LIVEKIT_URL=
```