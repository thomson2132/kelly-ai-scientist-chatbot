import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()

from utils.poem_generator import generate_kelly_response


st.set_page_config(
    page_title="Kelly - AI Scientist Chatbot",
    page_icon="🧪",
    layout="centered"
)


st.title("Kelly - The AI Scientist Poet")
st.markdown("*Ask me anything, and I'll respond in verse with skeptical wisdom*")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask Kelly a question..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    
    with st.chat_message("assistant"):
        with st.spinner("Kelly is composing a poem..."):
            response = generate_kelly_response(prompt, st.session_state.messages)
            st.markdown(response)
    
   
    st.session_state.messages.append({"role": "assistant", "content": response})


st.divider()
if st.button("🗑️ Clear Chat History", use_container_width=True):
    st.session_state.messages = []
    st.rerun()
