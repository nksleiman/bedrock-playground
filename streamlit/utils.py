import json
import os
import boto3
from langchain.llms.bedrock import Bedrock

os.environ["AWS_PROFILE"] = "nsleim"
region = os.environ["AWS_REGION"] = "us-west-2"

'''
Uses AWS_PROFILE profile string to retrieve API credentials from ~/.aws/credentials
'''
def get_bedrock_client():
    client = boto3.client(service_name='bedrock-runtime', region_name=region)
    return client

'''
Uses LangChain Bedrock wrapper to accomplish a zero shot single prompt response from Llama 2
'''
def send_prompt_langchain(prompt):

    boto3_bedrock = get_bedrock_client()

    body = {
        "prompt": prompt,
        "temperature": 0.2,
        "top_p": 0.9,
        "max_gen_len": 512
    }

    textgen_llm = Bedrock(
        model_id="meta.llama2-70b-chat-v1",
        client=boto3_bedrock,
        model_kwargs=body,
    )

    response = textgen_llm.invoke(prompt)
    return response

'''
Uses Pure Bedrock API to accomplish a zero shot single prompt response from Llama 2
'''
def send_prompt_boto3(prompt):

    bedrock = get_bedrock_client()

    body = json.dumps({
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9,
        "max_gen_len": 512
    })

    modelId = "meta.llama2-70b-chat-v1" 
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    print(response_body)
    return response_body
