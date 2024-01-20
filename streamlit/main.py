# Import necessary libraries
import utils
import streamlit as st

# Set up the Streamlit interface
st.title("Bedrock Portal")

# Create a text area in the sidebar for user input
prompt = st.sidebar.text_area(label="What is your question?", max_chars=2000)

# Check if there is a prompt provided by the user
if prompt:
    # Send the prompt to the utils function and get a response
    # response = utils.send_prompt(prompt)
    response = utils.send_prompt_langchain(prompt)
    
    # Display the response from the support AI in the main page area
    # st.write("Support AI: ", response["generation"])
    st.write(response)
