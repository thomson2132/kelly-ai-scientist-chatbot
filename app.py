import streamlit as st
from dotenv import load_dotenv  # Add this import
import os

# Load environment variables from .env file
load_dotenv()  # Add this line

from utils.poem_generator import generate_kelly_response

# Page configuration
st.set_page_config(
    page_title="Kelly - AI Scientist Chatbot",
    page_icon="🧪",
    layout="centered"
)

# Title and description
st.title("🧪 Kelly - The AI Scientist Poet")
st.markdown("*Ask me anything, and I'll respond in verse with skeptical wisdom*")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask Kelly a question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate Kelly's response
    with st.chat_message("assistant"):
        with st.spinner("Kelly is composing a poem..."):
            response = generate_kelly_response(prompt, st.session_state.messages)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with information
with st.sidebar:
    st.header("About Kelly")
    st.write("""
    Kelly is an AI scientist who responds to all queries in poetic form.
    
    **Characteristics:**
    - 🔍 Skeptical of broad AI claims
    - 📊 Evidence-based suggestions
    - 🎭 Professional yet poetic
    - 🧠 Analytical thinking
    """)
    
    # Display stats
    if st.session_state.messages:
        st.divider()
        st.metric("Messages", len(st.session_state.messages))
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
