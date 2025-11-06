import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

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

# Clear chat history button below chat box
st.divider()
if st.button("🗑️ Clear Chat History", use_container_width=True):
    st.session_state.messages = []
    st.rerun()
