import streamlit as st
import os
import pandas as pd

DOCUMENTS_FILE = "documents.csv"

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
        
        df = pd.read_csv(DOCUMENTS_FILE)
        new_doc = {
            "filename": uploaded_file.name,
            "status": "pending"
        }

        df = pd.concat([df, pd.DataFrame([new_doc])], ignore_index=True)
        df.to_csv(DOCUMENTS_FILE, index=False)

        st.success("File uploaded successfully!")
        st.write("File saved at:", save_path)