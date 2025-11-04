from groq import Groq
import os
from utils.prompts import KELLY_SYSTEM_PROMPT

def generate_kelly_response(user_query, chat_history):
    """
    Generate a poetic response from Kelly using Groq API
    """
    try:
        # Initialize Groq client with API key from environment
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        # Prepare messages for API call
        messages = [
            {"role": "system", "content": KELLY_SYSTEM_PROMPT}
        ]
        
        # Add recent chat history (last 10 messages for context)
        for msg in chat_history[-10:]:
            if msg["role"] in ["user", "assistant"]:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        # Call Groq API with correct model
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",  # CORRECT MODEL - Currently Available!
            temperature=0.8,  # Higher for creative poetry
            max_tokens=600,
            top_p=0.9
        )
        
        # Extract and return response
        response = chat_completion.choices[0].message.content
        return response
        
    except Exception as e:
        return f"""An error in my verse has appeared,
The connection, it seems, has interfered.
Check your API key with care,
Ensure it's set and properly there.

Error details: {str(e)}"""
