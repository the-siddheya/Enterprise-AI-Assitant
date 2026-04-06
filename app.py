import streamlit as st
import auth.login as login
import auth.register as register

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
        st.write("admin panel")
    else:
        st.write("user chat")
