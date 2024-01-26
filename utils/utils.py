import os
import boto3
import yaml

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
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)
