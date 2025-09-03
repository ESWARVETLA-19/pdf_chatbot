from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_vectordb(docs=None, load_existing=True):
    embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    persist_dir = "db"
    collection_name = "pdf_documents"

    if load_existing:
        print("🔄 Loading existing vector store...")
        return Chroma(
            persist_directory=persist_dir,
            embedding_function=embed_model,
            collection_name=collection_name
        )

    if docs is None:
        raise ValueError("No documents provided to build vector DB")

    print("📚 Building new vector store...")
    vectordb = Chroma.from_documents(
        docs,
        embedding=embed_model,
        persist_directory=persist_dir,
        collection_name=collection_name
    )
    return vectordb
