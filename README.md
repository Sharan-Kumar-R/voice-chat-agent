# Voice Bot Project

A voice-enabled AI chatbot that uses Deepgram for speech-to-text conversion and Groq for natural language processing.

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

1. Visit [Deepgram Console]([https://console.deepgram.com/])
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
   python QVoiceAgent.py
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
├── QuickAgent.py            # Main voice bot application
├── README.md                # This documentation
├── requirements.txt         # Python dependencies
├── speech_to_text.py        # Speech-to-text streaming functionality
├── system_prompt.txt        # System prompt configuration
├── text_to_speech.py        # Text-to-speech functionality
└── myenv/                   # Virtual environment folder (created during setup)
```
