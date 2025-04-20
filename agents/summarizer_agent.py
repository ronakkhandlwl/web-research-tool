from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os


def summarize_links(links):
    loader = WebBaseLoader([link["link"] for link in links])
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2")
    vectordb = FAISS.from_documents(split_docs, embedding)

    retriever = vectordb.as_retriever()

    groq_api_key = os.getenv('GROQ_API_KEY')
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="meta-llama/llama-4-scout-17b-16e-instruct")

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    summary = qa.invoke("Summarize key insights from the above research data.")
    return summary
