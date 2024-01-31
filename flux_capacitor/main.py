import streamlit as st
from vectordb_utils import get_vectordb
from bedrock_chat_w_rag import query_vectordb_directly

# Set up the Streamlit interface
st.title("Flux Capacitor Chat")

# Text area for user input
prompt_input = st.sidebar.text_area("What is your question?", max_chars=2000)

# Button to trigger the processing
if st.sidebar.button("Submit"):
    vectordb = get_vectordb()
    response = query_vectordb_directly(vectordb, prompt_input)
    st.write(response)
