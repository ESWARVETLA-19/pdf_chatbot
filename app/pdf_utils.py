from langchain.text_splitter import RecursiveCharacterTextSplitter
import fitz  # PyMuPDF

def load_pdfs(pdf_paths):
    print("📄 Loading and parsing PDFs...")
    documents = []
    for path in pdf_paths:
        doc = fitz.open(path)
        text = "\n".join([page.get_text() for page in doc])
        documents.append(text)
        doc.close()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = text_splitter.create_documents(documents)
    print(f"✅ Split into {len(chunks)} chunks.")
    return chunks
