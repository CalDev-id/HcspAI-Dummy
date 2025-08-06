import streamlit as st

def configure_dashboard():
    st.set_page_config(page_title="HCSP-AI Dashboard", layout="wide")
    st.markdown("""
        <style>
            .appview-container .main .block-container {
                background-color: white !important;
                color: black !important;
            }

            section[data-testid="stSidebar"] {
                background-color: #f9f9f9 !important;
                border-right: 2px solid #cccccc;
            }

            .stTextInput > div > input,
            .stTextArea > div > textarea,
            .stChatMessage,
            .stMarkdown {
                color: black !important;
            }

            [data-testid="stChatMessageContent"] {
                background-color: #f2f2f2;
                padding: 1rem;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
