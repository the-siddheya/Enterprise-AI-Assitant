import streamlit as st
import pandas as pd
import os

def register():
    st.title("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        if not username or not email or not password:
            st.warning("Please fill all fields")
            return

        if os.path.exists("users.csv"):
            df = pd.read_csv("users.csv")
        else:
            df = pd.DataFrame(columns=["username", "email", "password", "role"])

        # Check duplicate username
        if (df["username"] == username).any():
            st.error("Username already exists")
            return

        new_user = {
            "username": username,
            "email": email,
            "password": password,
            "role": "user"
        }

        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        df.to_csv("users.csv", index=False)

        st.success("Registration successful! You can now log in.")