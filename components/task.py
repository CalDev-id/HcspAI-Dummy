# import streamlit as st

# def task_page():
#     st.title("Browse Tasks")
#     st.write("Discover and create premade tasks that combine multiple instructions and specific knowledge.")

#     search_query = st.text_input("Search tasks", placeholder="Search tasks")

#     tasks = [
#         {"title": "Profile Matchup Promosi", "opened": 5, "description": "Template for Profile Matchup Promosi"},
#         {"title": "Learning Recommendation", "opened": 31, "description": "Template for Learning Recommendation"},
#         {"title": "Skill-Based Talent Matching", "opened": 12, "description": "Template for Talent Matching"},
#         {"title": "Mandatory Training Completion Tracker", "opened": 22, "description": "Template for Training Tracker"},
#         {"title": "Candidate Sourcing Promosi", "opened": 5, "description": "Template for Sourcing Promosi"},
#         {"title": "Candidate Sourcing Promosi", "opened": 45, "description": "Updated template for Sourcing Promosi"},
#         {"title": "Drop-off Analysis Report Employee Transfer Program", "opened": 21, "description": "Report for drop-off & transfer"},
#         {"title": "Promotion Eligibility Listing", "opened": 11, "description": "Check employee eligibility for promotion"},
#     ]

#     # Filter by search query
#     if search_query:
#         tasks = [task for task in tasks if search_query.lower() in task["title"].lower()]

#     # Layout: display 2 cards per row
#     cols = st.columns(2)
#     for i, task in enumerate(tasks):
#         col = cols[i % 2]
#         with col:
#             with st.container(border=True):
#                 st.caption(f"Opened {task['opened']} times")
#                 if st.button(task["title"], key=f"task_{i}"):
#                     with st.modal(task["title"]):
#                         st.subheader(task["title"])
#                         st.write(task["description"])
#                         st.button("Close", key=f"close_{i}")

import streamlit as st

def task_page():
    st.title("Browse Tasks")
    st.write("Discover and create premade tasks that combine multiple instructions and specific knowledge.")

    search_query = st.text_input("Search tasks", placeholder="Search tasks")

    tasks = [
        {"title": "Profile Matchup Promosi", "opened": 5, "description": "Template for Profile Matchup Promosi"},
        {"title": "Learning Recommendation", "opened": 31, "description": "Template for Learning Recommendation"},
        {"title": "Skill-Based Talent Matching", "opened": 12, "description": "Template for Talent Matching"},
        {"title": "Mandatory Training Completion Tracker", "opened": 22, "description": "Template for Training Tracker"},
        {"title": "Candidate Sourcing Promosi", "opened": 5, "description": "Template for Sourcing Promosi"},
        {"title": "Candidate Sourcing Promosi", "opened": 45, "description": "Updated template for Sourcing Promosi"},
        {"title": "Drop-off Analysis Report Employee Transfer Program", "opened": 21, "description": "Report for drop-off & transfer"},
        {"title": "Promotion Eligibility Listing", "opened": 11, "description": "Check employee eligibility for promotion"},
    ]

    if search_query:
        tasks = [task for task in tasks if search_query.lower() in task["title"].lower()]

    # Initialize state
    if "selected_task" not in st.session_state:
        st.session_state.selected_task = None

    cols = st.columns(2)
    for i, task in enumerate(tasks):
        col = cols[i % 2]
        with col:
            with st.container(border=True):
                st.caption(f"Opened {task['opened']} times")
                if st.button(task["title"], key=f"task_{i}"):
                    st.session_state.selected_task = task

    # Simulate modal with expanded section
    if st.session_state.selected_task:
        st.markdown("---")
        with st.expander(f"📝 {st.session_state.selected_task['title']}", expanded=True):
            st.write(st.session_state.selected_task["description"])
            if st.button("Close", key="close_task"):
                st.session_state.selected_task = None
