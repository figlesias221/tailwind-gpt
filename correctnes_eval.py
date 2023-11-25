import logging
import sys
import os
import openai
from llama_index.llms import OpenAI
import pinecone
from llama_index import ServiceContext, VectorStoreIndex
from llama_index.vector_stores import PineconeVectorStore
from llama_index.evaluation import CorrectnessEvaluator


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

os.environ["PINECONE_API_KEY"] = "2bcecfc8-35f9-44dc-9459-ab0cc2781b29"
os.environ["OPENAI_API_KEY"] = "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"


api_key = "2bcecfc8-35f9-44dc-9459-ab0cc2781b29"
pinecone.init(api_key=api_key, environment="gcp-starter")

pinecone_index = pinecone.Index("tailwind-ada")
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on TailwindCSS and your job is to answer technical questions. Assume that all questions are related to TailwindCSS. Keep your answers technical and based on facts – do not hallucinate features."))
evaluator = CorrectnessEvaluator(service_context=service_context)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, service_context=service_context)


chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
query = "What is border-radius? And how do I use it in TailwindCSS?"
response = chat_engine.chat(query)
reference = "It is a property that allows you to round the corners of an element. You can use it in TailwindCSS by adding the rounded class to an element. For example, rounded-lg will round the corners of an element by 0.5rem."

result = evaluator.evaluate(
    query=query,
    response=response.response,
    reference=reference,
)

print(result)

