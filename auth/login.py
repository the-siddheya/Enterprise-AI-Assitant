import streamlit as st
import pandas as pd

def login():

    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        df = pd.read_csv("users.csv")

        found = False
        role = "user"

        for index in df.index:
            row = df.loc[index]
            if row["email"] == email and str(row["password"]) == password:
                found = True
                role = row["role"]
                break
        if found:
            st.session_state["logged_in"] = True
            st.session_state["role"] = role
            st.session_state["email"] = email
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")