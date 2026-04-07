import streamlit as st
from auth.login import login
from admin.admin_panel import admin_panel
from auth.register import register

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    page = st.sidebar.selectbox("Select Page", ["Login", "Register"])

    if page == "Login":
        login()   
    else:
        register()  

else:
    if st.session_state["role"] == "admin":
        admin_panel()
    else:
        st.write("user chat")
