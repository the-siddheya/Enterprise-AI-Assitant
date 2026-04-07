import streamlit as st
import os

def admin_panel():
    st.title("Admin Panel")

    st.subheader("Upload Files")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:

        # ✅ Ensure directory exists
        os.makedirs("data/documents", exist_ok=True)

        save_path = f"data/documents/{uploaded_file.name}"

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully!")
        st.write("File saved at:", save_path)