import streamlit as st
import bedrock_basic_prompt


# Function to handle the main logic
def process_input(chef_selection, prompt):
    response = bedrock_basic_prompt.bedrock_chat_w_prompt_template(
        chef_selection, prompt
    )
    st.write(response)


# Set up the Streamlit interface
st.title("Cook With A Famous Chef")

# Dropdown for chef selection
chef_selection = st.sidebar.selectbox(
    "Select Your Chef",
    ["Anthony Bourdain", "Alton Brown", "Gordon Ramsey"],
    index=0,
)

# Text area for user input
prompt_input = st.sidebar.text_area("What is your question?", max_chars=2000)

# Button to trigger the processing
if st.sidebar.button("Submit"):
    process_input(chef_selection, prompt_input)
