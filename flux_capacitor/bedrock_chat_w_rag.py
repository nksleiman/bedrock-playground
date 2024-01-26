from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.chat_models import BedrockChat
from langchain_community.document_loaders import ConfluenceLoader
from IPython import embed
from utils.utils import load_config
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from utils.utils import get_bedrock_client


def document_loader():

    config = load_config()['confluence']

    loader = ConfluenceLoader(
        url=config['url'],
        username=config['username'],
        api_key=config['api_key']
    )

    documents = loader.load(space_key=config['space_key'], include_attachments=True, limit=50)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", "(?<=\. )", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    embed()

def bedrock_chat_with_rag(prompt):
    document_loader()