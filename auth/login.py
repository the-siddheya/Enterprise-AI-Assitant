import streamlit as st
import pandas as pd

def login():
    st.title("Login")

    # Create input fields for user login
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        df = pd.read_csv("users.csv")
        user = df[(df["username"] == username) & (df["password"] == password)]
        if len(user) > 0:
            role = user.iloc[0]["role"]
            st.session_state["logged_in"] = True
            st.session_state["role"] = role
            st.session_state["email"] = email

            st.success(f"Login successful! Welcome, {username}.")
        else:
            st.error("Invalid username or password. Please try again.")

