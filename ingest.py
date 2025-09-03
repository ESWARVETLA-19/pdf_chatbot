# ingest.py
import os
from app.pdf_utils import load_pdfs
from app.vectordb import get_vectordb

def main():
    persist_dir = "db"
    pdf_dir = "pdfs"

    #  Skip if DB already exists and is not empty
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        print(f"⚡ Vector DB already exists in '{persist_dir}', skipping ingestion.")
        return

    # collect all pdf paths
    pdf_paths = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    if not pdf_paths:
        print(" No PDFs found in ./pdfs directory")
        return

    print(f"📄 Found {len(pdf_paths)} PDFs, loading...")
    docs = load_pdfs(pdf_paths)

    print("📚 Building vector database...")
    vectordb = get_vectordb(docs=docs, load_existing=False)
    vectordb.persist()

    print(f"✅ Vector DB built and saved to {persist_dir}")

if __name__ == "__main__":
    main()
