import streamlit as st
import bedrock_chat_w_rag


# Function to handle the main logic
def process_input(prompt):
    response = bedrock_chat_w_rag.bedrock_chat_with_rag(prompt)
    st.write(response)


# Set up the Streamlit interface
st.title("Flux Capacitor Chat")

# Text area for user input
prompt_input = st.sidebar.text_area("What is your question?", max_chars=2000)

# Button to trigger the processing
if st.sidebar.button("Submit"):
    process_input(prompt_input)
