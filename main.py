from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set default model in case it's not specified in .env file
DEFAULT_MODEL = "gemini-2.0-flash-001"

def chat_with_gemini():
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file")
        return
    
    # Set up the Gemini API client
    client = genai.Client(api_key=api_key)
    
    # Get model from environment variable or use default
    model = os.getenv("MODEL", DEFAULT_MODEL)
    
    print("Welcome to Gemini Chat CLI!")
    print(f"Using model: {model}")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("-" * 50)
    
    # Keep track of conversation history (just strings, not structured objects)
    conversation = []
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("\nThank you for chatting with Gemini. Goodbye!")
            break
        
        try:
            # For the first message, we just send the user input
            if not conversation:
                response = client.models.generate_content(
                    model=model,
                    contents=user_input,
                    config=types.GenerateContentConfig(
                        max_output_tokens=1024,
                        temperature=0.7
                    )
                )
            else:
                # For subsequent messages, we need to include the history
                # Format the conversation history as a list of messages
                formatted_history = []
                for i in range(0, len(conversation), 2):
                    # Add user message
                    formatted_history.append({"role": "user", "parts": [{"text": conversation[i]}]})
                    # Add model response if available
                    if i + 1 < len(conversation):
                        formatted_history.append({"role": "model", "parts": [{"text": conversation[i+1]}]})
                
                # Add the current user message
                formatted_history.append({"role": "user", "parts": [{"text": user_input}]})
                
                response = client.models.generate_content(
                    model=model,
                    contents=formatted_history,
                    config=types.GenerateContentConfig(
                        max_output_tokens=1024,
                        temperature=0.7
                    )
                )
            
            # Print Gemini's response
            assistant_message = response.text
            print(f"\nGemini: {assistant_message}")
            
            # Add messages to conversation history as simple strings
            conversation.append(user_input)
            conversation.append(assistant_message)
            
        except Exception as e:
            print(f"\nError: {e}")
            # Optionally remove the last user message if there was an error
            if conversation:
                conversation.pop()

if __name__ == "__main__":
    chat_with_gemini()