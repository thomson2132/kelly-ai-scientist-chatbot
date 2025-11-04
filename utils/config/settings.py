import os

# Groq API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-70b-versatile"

# Alternative Groq models you can use:
# - "llama-3.1-8b-instant" (faster, less capable)
# - "mixtral-8x7b-32768" (good alternative)
# - "gemma2-9b-it" (another option)

# Model parameters
TEMPERATURE = 0.8  # Higher = more creative
MAX_TOKENS = 600
TOP_P = 0.9
