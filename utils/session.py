import streamlit as st
from utils.chatbot import ChatBot

def initialize_session_state():
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBot()
    if "chat_sessions" not in st.session_state:
        st.session_state.chat_sessions = []
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_session_name" not in st.session_state:
        st.session_state.current_session_name = "Chat #1"
    if "pdf_text" not in st.session_state:
        st.session_state.pdf_text = ""
    if "pdf_file" not in st.session_state:
        st.session_state.pdf_file = None
