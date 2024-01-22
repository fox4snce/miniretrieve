import os
import faiss
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

os.environ["OPENAI_API_KEY"] = ""

def initialize_models_and_embeddings():
    embeddings = OpenAIEmbeddings(
        
    )
    return embeddings

def initialize_vector_store(embeddings, document_path):
    loader = PyPDFLoader(document_path)  
    pages = loader.load_and_split()

    vectorstore = FAISS.from_documents(
        pages, embedding=embeddings
    )
    return vectorstore.as_retriever()

def retrieve_documents(query, retriever):
    records = retriever.get_relevant_documents(query)
    return ' '.join(record.page_content for record in records)