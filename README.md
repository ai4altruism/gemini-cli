# Gemini CLI Chat

A simple command-line interface for chatting with Google's Gemini AI model.

## Features

- Interactive command-line chat with Gemini
- Maintains conversation context for natural dialogue
- Configurable model selection via environment variables
- Simple exit commands ("exit" or "quit")

## Prerequisites

- Python 3.8+
- Google AI Gemini API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/gemini-cli-chat.git
   cd gemini-cli-chat
   ```

2. Install required packages:
   ```bash
   pip install google-generativeai python-dotenv
   ```

3. Create a `.env` file in the project directory:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   MODEL=gemini-2.0-flash-001
   ```

## Usage

Run the application:
```bash
python gemini_chat.py
```

Type your messages at the prompt and press Enter. Gemini will respond in the terminal.

To end the conversation, type `exit` or `quit` at the prompt.

## Available Models

You can change the model by updating the MODEL variable in your `.env` file:

- `gemini-2.0-flash-001` - Fast, efficient model (default)
- `gemini-2.0-pro-001` - More capable model for complex tasks
- `gemini-1.5-flash-001` - Previous generation, faster model
- `gemini-1.5-pro-001` - Previous generation, more capable model

## Troubleshooting

- If you encounter import errors, ensure you're using the correct import statements:
  ```python
  from google import genai
  from google.genai import types
  ```

- The Gemini API requires specific formatting for conversation history. This application handles that automatically, but if you're modifying the code, refer to the [Google Generative AI documentation](https://ai.google.dev/docs/gemini_api_overview).

## Getting a Gemini API Key

1. Go to the [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Navigate to "Get API key" in the menu
4. Create a new API key and copy it to your .env file

## License

N/A

## Contributing

N/A