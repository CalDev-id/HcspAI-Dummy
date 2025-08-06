# import streamlit as st
# from LLM.groq_runtime import GroqRunTime 
# from utils.chatbot import ChatBot      

# # Inisialisasi Session State
# if "chatbot" not in st.session_state:
#     st.session_state.chatbot = ChatBot()

# if "chat_sessions" not in st.session_state:
#     st.session_state.chat_sessions = []

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "current_session_name" not in st.session_state:
#     st.session_state.current_session_name = "Chat #1"

# # Dashboard config
# st.set_page_config(
#     page_title="HCSP-AI Dashboard",
#     layout="wide", 
# )

# # Inject CSS
# st.markdown("""
#     <style>
#         .appview-container .main .block-container {
#             background-color: white !important;
#             color: black !important;
#         }

#         section[data-testid="stSidebar"] {
#             background-color: #f9f9f9 !important;
#             border-right: 2px solid #cccccc;
#         }

#         .stTextInput > div > input,
#         .stTextArea > div > textarea,
#         .stChatMessage,
#         .stMarkdown {
#             color: black !important;
#         }

#         [data-testid="stChatMessageContent"] {
#             background-color: #f2f2f2;
#             padding: 1rem;
#             border-radius: 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Sidebar (navigasi + riwayat chat)
# with st.sidebar:
#     st.markdown("## HCSP-AI")

#     menu = st.radio(
#         "Navigasi",
#         ["Home", "Dashboard", "Task", "File", "Meeting"],
#         label_visibility="collapsed"
#     )

#     st.markdown("---")
#     st.markdown("### 💬 Riwayat Chat")

#     # Tombol Mulai Chat Baru
#     if st.button("➕ Mulai Chat Baru"):
#         st.session_state.messages = []
#         st.session_state.current_session_name = f"Chat #{len(st.session_state.chat_sessions) + 1}"


#     # Tampilkan daftar sesi chat sebelumnya

#     if st.session_state.chat_sessions:
#         for i, session in enumerate(st.session_state.chat_sessions):
#             if st.button(session['name'], key=f"session_{i}"):
#                 # Ganti isi chat ke session yang diklik
#                 st.session_state.messages = session["messages"].copy()
#                 st.session_state.current_session_name = session["name"]
#     else:
#         st.markdown("_Belum ada sesi chat._")

# # Redirect otomatis ke halaman Home saat klik sesi chat
# if "Chat #" in st.session_state.current_session_name:
#     menu = "Home"


# # ================================
# # HOME - Chatbot Interface
# # ================================
# if menu == "Home":
#     st.title("🧠 HCSP-AI Chatbot")

#     # Tampilkan riwayat pesan
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     # Input dari user
#     user_input = st.chat_input("Tanyakan sesuatu...")

#     if user_input:
#         # Simpan pesan user
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with st.chat_message("user"):
#             st.markdown(user_input)

#         # Respons dari chatbot
#         with st.chat_message("assistant"):
#             with st.spinner("Sedang berpikir..."):
#                 response = st.session_state.chatbot.generate_response(user_input)
#                 st.markdown(response)

#         # Simpan pesan bot
#         st.session_state.messages.append({"role": "assistant", "content": response})

#         # Simpan sesi ke history
#         if len(st.session_state.messages) == 2:
#             # Ambil beberapa kata pertama dari prompt user sebagai nama sesi
#             preview = user_input.strip().split()
#             session_title = " ".join(preview[:5]) + ("..." if len(preview) > 5 else "")
            
#             st.session_state.current_session_name = session_title
#             st.session_state.chat_sessions.append({
#                 "name": session_title,
#                 "messages": st.session_state.messages.copy()
#             })
#         else:
#             # Update sesi terakhir
#             st.session_state.chat_sessions[-1]["messages"] = st.session_state.messages.copy()


# # ================================
# # Dashboard
# # ================================
# elif menu == "Dashboard":
#     st.write("Ini halaman Dashboard dengan grafik atau ringkasan data.")
#     import pandas as pd
#     import numpy as np
#     import matplotlib.pyplot as plt

#     data = pd.DataFrame({
#         "Hari": pd.date_range(start="2025-08-01", periods=10),
#         "Nilai": np.random.randint(50, 100, 10)
#     })
#     st.line_chart(data.set_index("Hari"))

# # ================================
# # Task
# # ================================
# elif menu == "Task":
#     st.write("Daftar task yang sedang berjalan:")
#     tasks = ["Analisis data meeting", "Training model NLP", "Integrasi API HCSP"]
#     for task in tasks:
#         st.checkbox(task)

# # ================================
# # File
# # ================================
# elif menu == "File":
#     st.write("Upload atau lihat file terkait proyek:")
#     uploaded_file = st.file_uploader("Upload file", type=["pdf", "docx", "txt"])
#     if uploaded_file:
#         st.success(f"Berhasil upload: {uploaded_file.name}")

# # ================================
# # Meeting
# # ================================
# elif menu == "Meeting":
#     st.write("Upload atau lihat file hasil meeting:")
#     uploaded_file = st.file_uploader("Upload file", type=["pdf", "docx", "txt"])
#     if uploaded_file:
#         st.success(f"Berhasil upload: {uploaded_file.name}")

import streamlit as st
from config.dashboard_config import configure_dashboard
from utils.session import initialize_session_state
from components.sidebar import render_sidebar
from components.home import home_page
from components.dashboard import dashboard_page
from components.task import task_page
from components.file import file_page
from components.meeting import meeting_page

# 1. Konfigurasi tampilan dashboard dan state
configure_dashboard()
initialize_session_state()

# 2. Tampilkan sidebar & ambil menu yang dipilih
menu = render_sidebar()

# 3. Cek apakah perlu redirect ke Home
if st.session_state.get("redirect_home", False):
    menu = "Home"
    st.session_state.redirect_home = False  # reset flag

# 4. Routing ke halaman yang sesuai
if menu == "Home":
    home_page()
elif menu == "Dashboard":
    dashboard_page()
elif menu == "Task":
    task_page()
elif menu == "File":
    file_page()
elif menu == "Meeting":
    meeting_page()
