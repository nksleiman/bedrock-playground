import os
import boto3
import yaml
from langchain_community.chat_models import BedrockChat

os.environ["AWS_PROFILE"] = "nsleim"
region = os.environ["AWS_REGION"] = "us-west-2"

"""
Uses AWS_PROFILE profile string to retrieve API credentials from ~/.aws/credentials
"""

def get_bedrock_client():
    client = boto3.client(service_name="bedrock-runtime", region_name=region)
    return client


# Function to load the YAML configuration file
def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

def get_bedrock_llm():
    config = load_config()["models"]
    
    chat_model = BedrockChat(
        model_id=config["llama"],
        client=get_bedrock_client(),
        model_kwargs={"temperature": 0.2, "top_p": 0.9, "max_gen_len": 512},
    )
    return chat_model