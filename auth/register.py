import streamlit as st
import pandas as pd

def register():
    st.title("Register")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        df = pd.read_csv("users.csv")
        new_user = {
            "name":name,
            "email":email,
            "password":password,
            "role":"user"
        }
        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        df.to_csv("users.csv", index=False)

        st.success("User Registered")
