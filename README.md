# Real-time voice-enabled AI chatbot

<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/groq-FF6600?style=for-the-badge&logo=groq&logoColor=white" alt="Groq">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/deepgram-13EF93?style=for-the-badge&logo=deepgram&logoColor=black" alt="Deepgram">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/asyncio-306998?style=for-the-badge&logo=python&logoColor=white" alt="AsyncIO">
  <img src="https://img.shields.io/badge/requests-FF6B6B?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <img src="https://img.shields.io/badge/dotenv-ECD53F?style=for-the-badge&logo=python&logoColor=black" alt="Python-dotenv">
  <img src="https://img.shields.io/badge/ffmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" alt="FFmpeg">
  <img src="https://img.shields.io/badge/speech--to--text-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Speech-to-Text">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/text--to--speech-FF4B4B?style=for-the-badge&logo=amazon-alexa&logoColor=white" alt="Text-to-Speech">
  <img src="https://img.shields.io/badge/real--time--audio-1DB954?style=for-the-badge&logo=spotify&logoColor=white" alt="Real-time Audio">
  <img src="https://img.shields.io/badge/conversational--ai-FF6F00?style=for-the-badge&logo=chatbot&logoColor=white" alt="Conversational AI">
  <img src="https://img.shields.io/badge/llama3-8B2635?style=for-the-badge&logo=meta&logoColor=white" alt="Llama3">
</p>

<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
<img src="https://img.shields.io/badge/Deepgram-13EF93?style=for-the-badge&logo=deepgram&logoColor=white" alt="Deepgram">
<img src="https://img.shields.io/badge/LangChain-4A90E2?style=for-the-badge&logo=LangChain&logoColor=white" alt="LangChain">
<img src="https://img.shields.io/badge/Groq-0B132B?style=for-the-badge&logoColor=white&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNTYgMjU2Ij48cGF0aCBmaWxsPSIjRkZGIiBkPSJNMjQ3LjcgNjJjMCAxMi4xLTQuNCAyMy40LTEyLjQgMzEuOEwxNjggMTYxLjFjLTguMyA4LjctMTkuNiAxMy41LTMxLjUgMTMuNUgxMDhjLTI1LjIgMC00NS43LTIwLjUtNDUuNy00NS43di05LjFjMC0yNS4yIDIwLjUtNDUuNyA0NS43LTQ1LjdoMjMuOGMxMi4xIDAgMjMuNCA0LjQgMzEuOCAxMi40bDIwLjggMjIuMmM4LjcgOC4zIDEzLjUgMTkuNiAxMy41IDMxLjV2MjMuOGM2LjIgMCAxMi4xLTIuNCAxNi41LTYuOGwzMS44LTMxLjhjNC40LTQuNCA2LjgtMTAuMyA2LjgtMTYuNWMwLTI1LjItMjAuNS00NS43LTQ1LjgtNDUuN2gtOS4xYy0yNS4yIDAtNDUuNyAyMC41LTQ1LjcgNDUuN3YyMy44YzAgMTIuMS00LjQgMjMuNC0xMi40IDMxLjhMNzYuNyAxOTVjLTguMyA4LjctMTkuNiAxMy41LTMxLjUgMTMuNUgzNi4xYy0xOS45IDAtMzYtMTYuMS0zNi0zNlY2Mi4xYzAtMTkuOSAxNi4xLTM2IDM2LTMzaDE4My44YzE5LjkgMCAzNiAxNi4xIDM2IDM2djB6Ii8+PC9zdmc+" alt="Groq">
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
</p>

🔊 Real-Time Voice AI Assistant using Groq LLaMA3 + Deepgram + LangChain .

This project is a real-time voice-based conversational AI assistant that integrates:

   🧠 Groq’s LLaMA3 (via LangChain) for ultra-fast, high-quality conversational intelligence
   
   🎙️ Deepgram STT (Speech-to-Text) for real-time transcription from microphone input
   
   🗣️ Deepgram TTS (Text-to-Speech) for fast and natural voice responses using ffplay
   
Core components such as LLM, STT, TTS, and the overall chatbot architecture have been documented to support comprehensive understanding and customization.

## Features

- Real-time voice recognition using Deepgram
- AI-powered responses via Groq LLM
- Easy setup with virtual environment
- Cross-platform compatibility

## Prerequisites

- Python 3.7 or higher
- Visual Studio Code (recommended)
- Internet connection for API services
- FFmpeg (required for audio processing)

## API Setup

### 1. Groq API Key

1. Visit [Groq Console](https://console.groq.com/keys)
2. Create an account or sign in
3. Generate a new API key
4. Copy the API key for later use

### 2. Deepgram API Key

1. Visit [Deepgram Console](https://console.deepgram.com/)
2. Create an account or sign in
3. Generate a new API key
4. Copy the API key for later use

### 3. Environment Configuration

Create a `.env` file in the project root directory and add your API keys (replace if already exists):

```env
GROQ_API_KEY=your_groq_api_key_here
DEEPGRAM_API_KEY=your_deepgram_api_key_here
```

**Important:** Replace `your_groq_api_key_here` and `your_deepgram_api_key_here` with your actual API keys.

## Installation

### Step 1: Clone the Repository

**Option A: Using VS Code Terminal**
1. Open Visual Studio Code
2. Open a new terminal (Terminal → New Terminal or `Ctrl+Shift+`` )
3. Navigate to your desired directory:
   ```bash
   cd path/to/your/desired/folder
   ```
4. Clone the repository:
   ```bash
   git clone https://github.com/Sharan-Kumar-R/voice-chat-agent.git
   ```
5. Open the project folder:
   ```bash
   cd voice-chat-agent
   ```
6. Open the project in VS Code:
   ```bash
   code .
   ```

**Option B: Using VS Code Git Integration**
1. Open Visual Studio Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "Git: Clone" and select it
4. Paste the repository URL: `https://github.com/Sharan-Kumar-R/voice-chat-agent.git`
5. Choose a folder location and click "Select Repository Location"
6. Click "Open" when prompted

### Step 2: Install FFmpeg

1. Visit [FFmpeg Download Page](https://www.ffmpeg.org/download.html)
2. Download the appropriate version for your operating system
3. Follow the installation instructions for your platform
4. Verify the installation by opening a terminal/command prompt and typing:
   ```bash
   ffmpeg --version
   ```
   If FFmpeg is properly installed, you should see version information displayed.

### Step 3: Create Virtual Environment

Open a terminal in Visual Studio Code and run:

```bash
python -m venv myenv
```

### Step 3: Activate Virtual Environment

**For Windows:**
```bash
myenv\Scripts\activate
```

**For macOS/Linux:**
```bash
source myenv/bin/activate
```

After activation, you should see something like this in your terminal:
```
(myenv) PS C:\Users\username\path\to\project>
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Voice Bot

1. Make sure your virtual environment is activated:
   ```bash
   myenv\Scripts\activate
   ```

2. Run the main voice bot application:
   ```bash
   python VoiceAgent.py
   ```

### Customizing the Bot

To customize the bot's behavior, such as naming the model and defining its function, edit the `system_prompt.txt` file or modify the `system_prompt` variable in the code.

### Running Other Scripts

To run any other Python file in the project:
```bash
python <filename>.py
```

## Deactivating the Environment

When you're done working with the project, deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

- Ensure your API keys are correctly set in the `.env` file
- Make sure your virtual environment is activated before running any scripts
- Check that all dependencies are installed with `pip list`
- Verify your internet connection for API services
- **FFmpeg Issues**: If you encounter audio-related errors, verify FFmpeg installation with `ffmpeg --version`

## Project Structure

```
voice-bot-project/
├── .env                     # Environment variables (API keys)
├── Chat_Bot.py              # Chat bot implementation
├── llm.py                   # Language model integration
├── VoiceAgent.py            # Main voice bot application
├── README.md                # This documentation
├── requirements.txt         # Python dependencies
├── speech_to_text.py        # Speech-to-text streaming functionality
├── system_prompt.txt        # System prompt configuration
├── text_to_speech.py        # Text-to-speech functionality
└── myenv/                   # Virtual environment folder (created during setup)
```
