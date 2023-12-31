import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
import openai
import pinecone
from llama_index.vector_stores import PineconeVectorStore

openai.api_key = st.secrets.openai_key
pinecone.init(api_key=st.secrets.pinecone_key, environment="gcp-starter")
st.header("Tailwind GPT")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I'm Tailwind GPT. How can I help you?"}
    ]

pinecone_index = pinecone.Index("tailwind-hugging")
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on TailwindCSS and your job is to answer technical questions only about TailwindCSS. Assume that all questions are related to TailwindCSS. Keep your answers technical and based on facts. Context will be provided in many questions, only use it if it helps you answer the question. DO NOT answer questions that you do not understand or that are not related to TailwindCSS"))
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, service_context=service_context)
chat_engine = index.as_chat_engine(chat_mode="react", verbose=True)

if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
             response = chat_engine.chat(prompt)
             st.write(response.response)
             message = {"role": "assistant", "content": response.response}
             st.session_state.messages.append(message)
            except Exception as inst:
             print(type(inst))    # the exception type
             print(inst.args)     # arguments stored in .args
             print(inst)
            
