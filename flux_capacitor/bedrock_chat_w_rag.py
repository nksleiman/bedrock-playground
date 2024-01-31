from utils.utils import get_bedrock_llm
from IPython import embed
from langchain.retrievers.self_query.base import SelfQueryRetriever

def query_vectordb_directly(vectordb, prompt):

    # docs = vectordb.similarity_search(prompt, k=3)
    docs = vectordb.max_marginal_relevance_search(prompt, k=3, fetch_k=3)

    embed()
    print(docs[0].page_content)

def self_query_retriever(vectordb, prompt):
    llm = get_bedrock_llm()

