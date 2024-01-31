from langchain_community.document_loaders import ConfluenceLoader
from IPython import embed
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.vectorstores import Chroma

import os

import sys
from pathlib import Path

# Assuming vectordb_utils.py is in flux_capacitor and you want to import from utils,
# which is at the same level as flux_capacitor directory.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from utils.utils import load_config, get_bedrock_client

persist_directory = "./flux_capacitor/vector_db/"

config = load_config()

os.environ["AWS_PROFILE"] = "nsleim"
region = os.environ["AWS_REGION"] = "us-west-2"


def document_loader():
    confluence_config = config["confluence"]

    loader = ConfluenceLoader(
        url=confluence_config["url"],
        username=confluence_config["username"],
        api_key=confluence_config["api_key"],
    )

    documents = loader.load(
        space_key=confluence_config["space_key"], include_attachments=True, limit=50
    )
    print(f"Loaded {len(documents)} documents")

    return documents


def document_splitter(documents):
    chunk_size = 500
    chunk_overlap = 100

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "(?<=\. )", " ", ""],
    )

    chunks = splitter.split_documents(documents)
    print(
        f"Splitting {len(documents)} into {len(chunks)} chunks with a chunk size of {chunk_size} and an overlap of {chunk_overlap}"
    )

    return chunks


def create_vectordb(chunks, embeddings):

    print(f"Creating new chroma vectorstore '{persist_directory}'.")
    vectordb = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=persist_directory
    )

    print(f"Generated new vectorstore with {vectordb._collection.count()} entries")

    vectordb.persist()

    return vectordb


def get_vectordb():

    embeddings=BedrockEmbeddings(
        client=get_bedrock_client(),
        model_id="cohere.embed-english-v3",
    )

    if os.path.exists(persist_directory):
        print(
            f"The vectorstore already exists at '{persist_directory}'. To reconstruct, please remove the directory and run again"
        )
        vectordb = Chroma(
            persist_directory=persist_directory, embedding_function=embeddings
        )
    else:
        documents = document_loader()
        chunks = document_splitter(documents)
        vectordb = create_vectordb(chunks, embeddings)
    
    return vectordb    
    