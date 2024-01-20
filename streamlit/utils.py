import json
import os
import boto3

# Set AWS environment variables
os.environ["AWS_PROFILE"] = "YOUR_PROFILE"
region = os.environ["AWS_REGION"] = "us-west-2"

def create_llama_body(prompt):

    body = json.dumps({
        "prompt": prompt,
        "temperature": 0.5,
        "top_p": 0.9,
        "max_gen_len": 512
    })
    return body

def send_prompt(prompt):

    bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-west-2')

    prompt_body = create_llama_body(prompt)

    modelId = "meta.llama2-70b-chat-v1" 
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock.invoke_model(body=prompt_body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    print(response_body)
    return response_body
