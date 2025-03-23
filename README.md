# Google Gemini API - CLI Chat

This repository demonstrates a simple command-line chat implementation using the Google API for access to the Gemini family of models. It demonstrates a simple command-line chat implementation using the Google Generative AI API. It serves as a foundational building block for developers looking to integrate advanced AI capabilities into their Python applications.

## Overview

The Google Generative AI API provides access to Google's powerful Gemini models, enabling developers to build applications with state-of-the-art generative AI capabilities. This repository implements a simple command-line chat interface that maintains conversation history and shows the basic patterns that can be extended for more complex use cases.

## Features

- Simple CLI-based chat interface
- Conversation history management
- Environment variable configuration
- Error handling and graceful degradation

## Getting Started

### Prerequisites

- Google API key for Gemini (get yours at [Google AI Studio](https://makersuite.google.com/app/apikey))
- Python 3.7 or later
- Required packages: `google-genai`, `python-dotenv`

### Installation

1. Clone this repository
2. Install dependencies: 
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   MODEL=gemini-2.0-flash-001  # Optional, will use default if not specified
   ```
4. Run the example: 
   ```
   python main.py
   ```

## Building More Advanced Applications

This simple example can be extended in numerous ways:

### 1. Enhanced Context Management

The current implementation already handles basic conversation history, but you can extend it to include:

```python
# Example of more sophisticated context management
def manage_context(conversation, max_tokens=8000):
    """Manage conversation context to prevent exceeding token limits"""
    # Estimate token count (rough approximation)
    total_tokens = sum(len(message.split()) * 1.3 for message in conversation)
    
    # If approaching limit, remove oldest exchanges while preserving most recent context
    while total_tokens > max_tokens and len(conversation) > 2:
        # Remove oldest exchange (user message and model response)
        conversation.pop(0)
        if conversation:
            conversation.pop(0)
        # Recalculate token estimate
        total_tokens = sum(len(message.split()) * 1.3 for message in conversation)
    
    return conversation
```

### 2. Domain-Specific Applications

Leverage Gemini's capabilities for specialized use cases:

- **Custom Instruction Agent**: Create a specialized assistant with system prompts
- **Content Generation**: Blog posts, marketing copy, product descriptions
- **Code Generation and Explanation**: Programming assistance and code documentation
- **Educational Tools**: Interactive tutoring systems, quiz generators
- **Data Analysis**: Natural language interfaces for data exploration

### 3. Multimodal Capabilities

Extend beyond text to leverage Gemini's multimodal abilities:

```python
# Example of handling image inputs with Gemini
from PIL import Image
import base64
import io

def analyze_image(image_path, prompt):
    """Analyze an image with Gemini Pro Vision"""
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    # Load and encode the image
    image = Image.open(image_path)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image_data = buffer.getvalue()
    
    # Create the image part
    image_part = types.Part.from_data(data=image_data, mime_type="image/png")
    
    # Create the text part
    text_part = types.Part.from_text(prompt)
    
    # Generate content with both text and image
    response = client.models.generate_content(
        model="gemini-pro-vision",
        contents=[text_part, image_part],
        config=types.GenerateContentConfig(
            max_output_tokens=1024,
            temperature=0.7
        )
    )
    
    return response.text
```

### 4. Structured Output

Request and process structured data from Gemini:

```python
import json

def get_structured_output(prompt, schema):
    """Get structured JSON output from Gemini based on a schema"""
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    # Create a prompt that requests structured output
    full_prompt = f"""
    {prompt}
    
    Return your response as a JSON object with the following schema:
    {json.dumps(schema, indent=2)}
    
    Only return valid JSON with no additional explanation.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-pro",
        contents=full_prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=1024,
            temperature=0.2
        )
    )
    
    # Parse the JSON response
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        print("Failed to parse response as JSON")
        return None
```

### 5. Integration with Other Services

Combine with other APIs and services for end-to-end solutions:

- Database integration (SQLAlchemy, MongoDB) for persistent storage
- Web frameworks (Flask, FastAPI) for creating API endpoints
- Vector databases (Pinecone, Chroma) for retrieval-augmented generation (RAG)
- Speech-to-text and text-to-speech for voice interfaces

### 6. Deployment Options

Scale your application with different deployment strategies:

- Containerization with Docker
- Cloud Functions or AWS Lambda for serverless deployment
- Traditional web hosting with Gunicorn/WSGI
- Schedule batch processing with tools like Airflow

## Best Practices

When extending this example, consider these best practices:

- Implement proper error handling and retry mechanisms
- Use streaming for better user experience with long responses
- Add rate limiting to manage API usage and costs
- Implement content moderation for user inputs
- Consider ethical implications of AI-generated content
- Store sensitive credentials securely (not in code)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Google Generative AI team for providing the API
- Open source community for supporting AI development