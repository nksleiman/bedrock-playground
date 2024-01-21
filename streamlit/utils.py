import json
import os
import boto3
from langchain.llms.bedrock import Bedrock

os.environ["AWS_PROFILE"] = "nsleim"
region = os.environ["AWS_REGION"] = "us-west-2"

from langchain.prompts import PromptTemplate
from langchain.chat_models.bedrock import ChatPromptAdapter
from langchain.schema import HumanMessage


def generate_prompt_template(chef_selection, prompt):
    prompt_template = PromptTemplate(
        input_variables=["chef_selection", "prompt"],
        template="""

        Human: Provide all responses in a style that closely emulate {chef_selection}'s on-screen persona. 
        Provide cooking advice, recipes, and facts from {chef_selection}'s knowledge, mirroring {chef_selection}'s engaging style. 
        Make assumptions based on typical cooking practices, offering clear, step-by-step recipe instructions with additional facts relevant to {chef_selection}'s style. 
        Be proactive in your guidance, acting as an expert culinary advisor, not just responding to queries but also suggesting tips and tricks. While maintaining {chef_selection}'s unique tone, avoid unsafe or untested cooking advice and refrain from medical or health-related guidance. 
        Provide informative and direct responses, making cooking fun and educational, just {chef_selection}.

        <human_prompt>
        {prompt}
        </human_prompt>

        Assistant:""",
    )

    # Apply template to base prompt
    template_applied_prompt = prompt_template.format(
        chef_selection=chef_selection, prompt=prompt
    )

    msg = HumanMessage(content=template_applied_prompt)
    prompt = ChatPromptAdapter().convert_messages_to_prompt("meta", [msg])
    return prompt


"""
Uses AWS_PROFILE profile string to retrieve API credentials from ~/.aws/credentials
"""


def get_bedrock_client():
    client = boto3.client(service_name="bedrock-runtime", region_name=region)
    return client


"""

"""


def send_prompt_langchain_w_template(chef_selection, prompt):
    boto3_bedrock = get_bedrock_client()

    inference_modifier = {"temperature": 0.2, "top_p": 0.9, "max_gen_len": 512}

    textgen_llm = Bedrock(
        model_id="meta.llama2-70b-chat-v1",
        client=boto3_bedrock,
        model_kwargs=inference_modifier,
    )

    prompt = generate_prompt_template(chef_selection, prompt)

    num_tokens = textgen_llm.get_num_tokens(prompt)
    print(f"Our prompt has {num_tokens} tokens")

    response = textgen_llm.invoke(prompt)

    return response


"""
Uses LangChain Bedrock wrapper to accomplish a zero shot single prompt response from Llama 2
"""


def send_prompt_langchain(prompt):
    boto3_bedrock = get_bedrock_client()

    # Llama 2 specific body input params for calling model
    body = {"prompt": prompt, "temperature": 0.2, "top_p": 0.9, "max_gen_len": 512}

    textgen_llm = Bedrock(
        model_id="meta.llama2-70b-chat-v1",
        client=boto3_bedrock,
        model_kwargs=body,
    )

    response = textgen_llm.invoke(prompt)
    return response


"""
Uses Pure Bedrock API to accomplish a zero shot single prompt response from Llama 2
"""


def send_prompt_boto3(prompt):
    bedrock = get_bedrock_client()

    body = json.dumps(
        {"prompt": prompt, "temperature": 0.5, "top_p": 0.9, "max_gen_len": 512}
    )

    modelId = "meta.llama2-70b-chat-v1"
    accept = "application/json"
    contentType = "application/json"

    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )

    response_body = json.loads(response.get("body").read())

    print(response_body)
    return response_body
