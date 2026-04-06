import streamlit as st
import pandas as pd

def register():
    st.title("Register")

    # Create input fields for user registration
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        df = pd.read_csv("users.csv")
        new_user = {
            "username": username,
            "email": email,
            "password": password,
            "role": "user"
        }
        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)       
        df.to_csv("users.csv", index=False)
        st.success("Registration successful! You can now log in.")