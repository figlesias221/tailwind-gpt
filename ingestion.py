import logging
import sys
import os
import pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import ServiceContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.storage_context import StorageContext

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment="gcp-starter")

pinecone_index = pinecone.Index("tailwind-hugging")

reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
docs = reader.load_data()

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
embed_model = (
  HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
)
service_context = ServiceContext.from_defaults(embed_model=embed_model)
index = VectorStoreIndex.from_documents(
    docs, storage_context=storage_context
)

query_engine = index.as_query_engine()
response = query_engine.query("What is border-radius?")


