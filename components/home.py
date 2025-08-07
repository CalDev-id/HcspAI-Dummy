# import streamlit as st

# def home_page():
#     st.title("🧠 HCSP-AI Chatbot")

#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     user_input = st.chat_input("Tanyakan sesuatu...")

#     if user_input:
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with st.chat_message("user"):
#             st.markdown(user_input)

#         with st.chat_message("assistant"):
#             with st.spinner("Sedang berpikir..."):
#                 response = st.session_state.chatbot.generate_response(user_input)
#                 st.markdown(response)

#         st.session_state.messages.append({"role": "assistant", "content": response})

#         if len(st.session_state.messages) == 2:
#             preview = user_input.strip().split()
#             session_title = " ".join(preview[:5]) + ("..." if len(preview) > 5 else "")
#             st.session_state.current_session_name = session_title
#             st.session_state.chat_sessions.append({
#                 "name": session_title,
#                 "messages": st.session_state.messages.copy()
#             })
#         else:
#             st.session_state.chat_sessions[-1]["messages"] = st.session_state.messages.copy()


#---------------------------------------------------------------------------
# import streamlit as st
# import fitz  # PyMuPDF untuk ekstraksi PDF

# def extract_text_from_pdf(uploaded_file):
#     """Ekstrak teks dari PDF dengan PyMuPDF"""
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     return text.strip()

# def home_page():
#     st.title("🧠 HCSP-AI Chatbot")

#     # Bagian unggah PDF
#     uploaded_pdf = st.file_uploader("Unggah dokumen PDF", type="pdf")
#     extracted_text = ""

#     if uploaded_pdf:
#         with st.spinner("Mengekstrak teks dari PDF..."):
#             extracted_text = extract_text_from_pdf(uploaded_pdf)
#             st.success("Teks berhasil diekstrak dari PDF!")

#             # Tampilkan pratinjau teks PDF
#             with st.expander("📄 Pratinjau Teks dari PDF"):
#                 st.write(extracted_text[:1000] + ("..." if len(extracted_text) > 1000 else ""))

#     # Tampilkan riwayat chat
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     # Input pengguna
#     user_input = st.chat_input("Tanyakan sesuatu...")

#     if user_input:
#         # Gabungkan input user dengan teks dari PDF jika tersedia
#         full_prompt = extracted_text + "\n\n" + user_input if extracted_text else user_input

#         # Simpan pesan user
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with st.chat_message("user"):
#             st.markdown(user_input)

#         # Respons dari chatbot
#         with st.chat_message("assistant"):
#             with st.spinner("Sedang berpikir..."):
#                 response = st.session_state.chatbot.generate_response(full_prompt)
#                 st.markdown(response)

#         st.session_state.messages.append({"role": "assistant", "content": response})

#         # Simpan sesi jika baru
#         if len(st.session_state.messages) == 2:
#             preview = user_input.strip().split()
#             session_title = " ".join(preview[:5]) + ("..." if len(preview) > 5 else "")
#             st.session_state.current_session_name = session_title
#             st.session_state.chat_sessions.append({
#                 "name": session_title,
#                 "messages": st.session_state.messages.copy()
#             })
#         else:
#             st.session_state.chat_sessions[-1]["messages"] = st.session_state.messages.copy()

#---------------------------------------------------------------------------

# import streamlit as st
# import fitz  # PyMuPDF untuk ekstraksi PDF

# def extract_text_from_pdf(uploaded_file):
#     """Ekstrak teks dari PDF dengan PyMuPDF"""
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     return text.strip()

# def home_page():
#     st.title("🧠 HCSP-AI Chatbot")

#     # Inisialisasi state jika belum ada
#     if "pdf_text" not in st.session_state:
#         st.session_state.pdf_text = ""
#     if "pdf_file" not in st.session_state:
#         st.session_state.pdf_file = None
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#     if "chat_sessions" not in st.session_state:
#         st.session_state.chat_sessions = []
#     if "current_session_name" not in st.session_state:
#         st.session_state.current_session_name = "Chat #1"

#     # CSS untuk mengecilkan jarak antara uploader dan input
#     st.markdown("""
#         <style>
#             div[data-testid="stFileUploader"] {
#                 margin-bottom: -15px;
#                 padding-top: 0px;
#                 padding-bottom: 0px;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     # Upload file PDF tepat di atas input chat
#     uploaded_pdf = st.file_uploader(
#         label="📎",  # ikon klip
#         type="pdf",
#         label_visibility="collapsed",
#         key="pdf_upload"
#     )

#     if uploaded_pdf:
#         with st.spinner("📄 Mengekstrak teks dari PDF..."):
#             extracted_text = extract_text_from_pdf(uploaded_pdf)
#             st.session_state.pdf_file = uploaded_pdf
#             st.session_state.pdf_text = extracted_text
#             st.success("Teks berhasil diekstrak dari PDF!")

#     # Tampilkan riwayat chat
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     # Input pengguna
#     user_input = st.chat_input("Tanyakan sesuatu...")

#     if user_input:
#         # Gabungkan teks PDF dengan pertanyaan user
#         full_prompt = st.session_state.pdf_text + "\n\n" + user_input if st.session_state.pdf_text else user_input

#         # Simpan dan tampilkan pesan user
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with st.chat_message("user"):
#             st.markdown(user_input)

#         # Dapatkan respons dari chatbot
#         with st.chat_message("assistant"):
#             with st.spinner("Sedang berpikir..."):
#                 response = st.session_state.chatbot.generate_response_global(full_prompt)
#                 st.markdown(response)

#         # Simpan respons
#         st.session_state.messages.append({"role": "assistant", "content": response})

#         # Jika ini adalah chat baru, simpan sesi dan reset PDF
#         if len(st.session_state.messages) == 2:
#             preview = user_input.strip().split()
#             session_title = " ".join(preview[:5]) + ("..." if len(preview) > 5 else "")
#             st.session_state.current_session_name = session_title

#             # Simpan sesi baru
#             st.session_state.chat_sessions.append({
#                 "name": session_title,
#                 "messages": st.session_state.messages.copy()
#             })

#             # RESET PDF saat buka chat baru
#             st.session_state.pdf_text = ""
#             st.session_state.pdf_file = None

#         else:
#             # Update isi sesi chat terakhir
#             st.session_state.chat_sessions[-1]["messages"] = st.session_state.messages.copy()


#------------------------------------------------------------
import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    """Ekstrak teks dari 1 file PDF"""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def home_page():
    st.title("🧠 HCSP-AI Chatbot")

    # Inisialisasi state
    if "pdf_text" not in st.session_state:
        st.session_state.pdf_text = ""
    if "pdf_files" not in st.session_state:
        st.session_state.pdf_files = []
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_sessions" not in st.session_state:
        st.session_state.chat_sessions = []
    if "current_session_name" not in st.session_state:
        st.session_state.current_session_name = "Chat #1"

    # Styling
    st.markdown("""
        <style>
            div[data-testid="stFileUploader"] {
                margin-bottom: -15px;
                padding-top: 0px;
                padding-bottom: 0px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Multi-upload PDF
    uploaded_pdfs = st.file_uploader(
        label="📎",
        type="pdf",
        label_visibility="collapsed",
        accept_multiple_files=True,
        key="pdf_upload"
    )

    # Proses semua file PDF
    if uploaded_pdfs:
        full_text = ""
        with st.spinner(f"Mengekstrak teks dari {len(uploaded_pdfs)} file..."):
            for pdf_file in uploaded_pdfs:
                extracted_text = extract_text_from_pdf(pdf_file)
                full_text += f"\n\n====[ {pdf_file.name} ]====\n\n{extracted_text}"
        st.session_state.pdf_files = uploaded_pdfs
        st.session_state.pdf_text = full_text
        st.success(f"Teks berhasil diekstrak dari {len(uploaded_pdfs)} file PDF!")

    # Tampilkan chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input pengguna
    user_input = st.chat_input("Tanyakan sesuatu...")

    if user_input:
        # Gabungkan teks PDF dengan pertanyaan user
        full_prompt = st.session_state.pdf_text + "\n\n" + user_input if st.session_state.pdf_text else user_input

        # Simpan dan tampilkan pesan user
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Dapatkan respons dari chatbot
        with st.chat_message("assistant"):
            with st.spinner("Sedang berpikir..."):
                response = st.session_state.chatbot.generate_response_global(full_prompt)
                st.markdown(response)

        # Simpan respons
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Sesi baru
        if len(st.session_state.messages) == 2:
            preview = user_input.strip().split()
            session_title = " ".join(preview[:5]) + ("..." if len(preview) > 5 else "")
            st.session_state.current_session_name = session_title

            # Simpan sesi
            st.session_state.chat_sessions.append({
                "name": session_title,
                "messages": st.session_state.messages.copy()
            })

            # Reset PDF saat sesi baru
            st.session_state.pdf_text = ""
            st.session_state.pdf_files = []

        else:
            # Update sesi terakhir
            st.session_state.chat_sessions[-1]["messages"] = st.session_state.messages.copy()
