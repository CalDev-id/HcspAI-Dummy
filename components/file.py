import streamlit as st

def file_page():
    st.write("Upload atau lihat file terkait proyek:")
    uploaded_file = st.file_uploader("Upload file", type=["pdf", "docx", "txt"])
    if uploaded_file:
        st.success(f"Berhasil upload: {uploaded_file.name}")
