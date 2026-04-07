import streamlit as st

def user_chat():

    st.title("Enterprise AI Assistant")
    st.write("Ask questions about uploaded documents")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    query = st.chat_input("Ask your question")

    if query:

        st.session_state.messages.append({
            "role": "user", 
            "content": query
        })

        with st.chat_message("user"):
            st.markdown(query)

        answer = "Answer by rag"

        st.session_state.messages.append({
            "role": "assistant", 
            "content": answer
        })

        with st.chat_message("assistant"):
            st.markdown(answer)

        