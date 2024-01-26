import os
import boto3

os.environ["AWS_PROFILE"] = "nsleim"
region = os.environ["AWS_REGION"] = "us-west-2"

"""
Uses AWS_PROFILE profile string to retrieve API credentials from ~/.aws/credentials
"""
def get_bedrock_client():
    client = boto3.client(service_name="bedrock-runtime", region_name=region)
    return client

def get_llama_model_id():
    return "meta.llama2-70b-chat-v1"


