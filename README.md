⚙️ Setup & Usage
1️⃣ Clone Repository
```
git clone https://github.com/ESWARVETLA-19/pdf_chatbot.git
cd pdf_chatbot
```
2️⃣ Add PDFs

Place your PDF files in the pdfs/ folder.

3️⃣ Build Vector DB
```docker-compose run app python app/ingest.py```

4️⃣ Start Services
```docker-compose up```


This will start:

Ollama service (LLM runtime)

App service (RAG pipeline + streamlit)

5️⃣ Chat with PDFs

Access the app in your browser (depends on Streamlit/React config).
Ask questions and get contextual answers from your documents.



**🧩 How It Works**

PDF Ingestion → Extract text → Split into chunks.

Embedding → Convert text chunks into vectors using HuggingFace MiniLM.

Storage → Save embeddings into ChromaDB (persistent).

Retrieval → At query time, fetch the most relevant chunks.

Generation → Mistral LLM (via Ollama) generates answers using retrieved context.
