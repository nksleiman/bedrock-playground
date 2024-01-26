from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.chat_models import BedrockChat
from utils import get_bedrock_client, get_llama_model_id

def bedrock_chat_w_prompt_template(chef_selection, prompt):

    '''
    Use LangChain's 3rd Party implementation wrapper for BedrockChat, specifying our client containing our credentials,
    the model to use (llama 2 70B in this case), and the option to append kwargs specific to the model. Note that other models
    have different kwargs structure
    '''
    chat_model = BedrockChat(
        model_id=get_llama_model_id(),
        client=get_bedrock_client(),
        model_kwargs={"temperature": 0.2, "top_p": 0.9, "max_gen_len": 512},
    )

    # Creating variables for clarity here, these can be passed in directly
    instructions_template = "Provide step by step cooking advice to the best of your ability in the style of {chef_selection}'s on screen persona"
    human_template = "{text}"

    # Using langchain's tuple structure here, I was unable to explicitly get the HumanMessage to convert when passing prompt in directly, so something happens under the hood
    # SystemMessage will tell the chat model how to behave behind the scenes
    # HumanMessage is the user input to the prompt
    chat_prompt = ChatPromptTemplate.from_messages(
        [("system", instructions_template), ("human", human_template)]
    )

    # Apply the variables to the ChatPromptTemplate
    formatted_messages = chat_prompt.format_messages(
        chef_selection=chef_selection, text=prompt
    )

    # Using invoke(), as other methods are being deprecated in LangChain 0.2.0
    result = chat_model.invoke(formatted_messages)

    # Extract content section from result before returning to streamlit app
    return result.content
