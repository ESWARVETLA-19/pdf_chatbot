# import os
# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory
# from langchain.prompts import PromptTemplate
# from langchain_community.llms.ollama import Ollama

# from app.vectordb import get_vectordb
# from app.pdf_utils import load_pdfs


# def build_qa_pipeline():
#     print("🚀 Initializing QA pipeline...")

#     # 🔗 Connect to Ollama service
#     llm = Ollama(
#         model="mistral",
#         base_url="http://ollama:11434",  # ✅ docker-compose service name
#     )

#     persist_dir = "db"

#     # 📦 Load existing DB or build new one
#     if not os.path.exists(persist_dir) or not os.listdir(persist_dir):
#         print("📄 No existing DB found, processing PDFs...")
#         pdf_paths = [f"pdfs/{f}" for f in os.listdir("pdfs") if f.endswith(".pdf")]
#         docs = load_pdfs(pdf_paths)
#         vectordb = get_vectordb(docs=docs, load_existing=False)
#     else:
#         print("📦 Loading existing vector DB...")
#         vectordb = get_vectordb(load_existing=True)

#     # 💬 Memory for chat
#     memory = ConversationBufferMemory(
#         memory_key="chat_history",
#         return_messages=True
#     )

#     # 🧠 Prompt
#     custom_prompt_template = """You are a helpful assistant. Use the following context to answer the question.
# If you don't know the answer, just say you don't know. Be concise.

# Context:
# {context}

# Question: {question}
# Answer:"""

#     prompt = PromptTemplate(
#         input_variables=["context", "question"],
#         template=custom_prompt_template
#     )

#     # 🤖 QA Chain with memory
#     qa_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=vectordb.as_retriever(),
#         memory=memory,
#         combine_docs_chain_kwargs={"prompt": prompt}
#     )

#     return qa_chain


# build_qa_pipeline.py
import os
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama
from app.vectordb import get_vectordb

def build_qa_pipeline():
    print("🚀 Initializing QA pipeline...")

    # 🔗 Connect to Ollama service
    llm = Ollama(
        model="mistral",
        base_url="http://ollama:11434",
    )

    persist_dir = "db"
    if not os.path.exists(persist_dir) or not os.listdir(persist_dir):
        raise RuntimeError("❌ No vector DB found. Run `python ingest.py` first!")

    print("📦 Loading existing vector DB...")
    vectordb = get_vectordb(load_existing=True)

    # 💬 Memory for chat
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # 🧠 Prompt
    custom_prompt_template = """You are a helpful assistant. Use the following context to answer the question.
If you don't know the answer, just say you don't know. Be concise.

Context:
{context}

Question: {question}
Answer:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=custom_prompt_template
    )

    # 🤖 QA Chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(),
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return qa_chain
