import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def initialize_engine():
    documents = SimpleDirectoryReader("resume").load_data()

    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")

    service_context = ServiceContext.from_defaults(llm=llm)
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)

    return index.as_query_engine(similarity_top_k=3)
