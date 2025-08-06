import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("# HCSP-AI")

        menu = st.radio("Navigasi", ["Home", "Dashboard", "Task", "File", "Meeting"], label_visibility="collapsed")
        st.markdown("---")
        st.markdown("### 💬 Riwayat Chat")

        if st.button("➕ Mulai Chat Baru"):
            st.session_state.messages = []
            st.session_state.current_session_name = f"Chat #{len(st.session_state.chat_sessions) + 1}"

        if st.session_state.chat_sessions:
            for i, session in enumerate(st.session_state.chat_sessions):
                if st.button(session['name'], key=f"session_{i}"):
                    st.session_state.messages = session["messages"].copy()
                    st.session_state.current_session_name = session["name"]
        else:
            st.markdown("_Belum ada sesi chat._")

    return menu
