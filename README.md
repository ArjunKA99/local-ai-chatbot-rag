# 🤖 Local AI Chatbot with Retrieval-Augmented Generation (RAG)
A local AI chatbot built with Python, Streamlit, Ollama, and FAISS featuring Retrieval-Augmented Generation (RAG), semantic search, conversation memory, and streaming responses.

# 🤖 Local AI Chatbot with Retrieval-Augmented Generation (RAG)

A local AI chatbot built using **Python**, **Streamlit**, **Ollama**, and **FAISS** that answers questions using both an LLM and information retrieved from uploaded PDF documents.

The application runs completely on your local machine and supports streaming responses, conversation memory, semantic search, and Retrieval-Augmented Generation (RAG).

---

## 📌 Features

- 💬 Interactive chatbot using Streamlit
- ⚡ Real-time streaming responses
- 🧠 Conversation memory with automatic summarization
- 📄 PDF document ingestion
- ✂️ Intelligent text chunking with overlap
- 🔍 Semantic search using embeddings
- 📦 FAISS vector database for fast retrieval
- 🤖 Retrieval-Augmented Generation (RAG)
- 🏠 Runs completely locally using Ollama (No OpenAI API required)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| Ollama | Local LLM Runtime |
| Phi-3 Mini | Language Model |
| Nomic Embed Text | Embedding Model |
| FAISS | Vector Database |
| PyPDF | PDF Processing |
| NumPy | Vector Operations |

---

# 🏗️ System Architecture

```
                         PDF Documents
                               │
                               ▼
                     Read PDF Documents
                               │
                               ▼
                     Split into Chunks
                               │
                               ▼
                   Generate Embeddings
                               │
                               ▼
                     Create FAISS Index
                               │
──────────────────────────────────────────────────────

                        User Question
                               │
                               ▼
                  Generate Query Embedding
                               │
                               ▼
                     Search FAISS Index
                               │
                               ▼
                 Retrieve Relevant Chunks
                               │
                               ▼
          Build Prompt (Context + Chat Memory)
                               │
                               ▼
                   Ollama (Phi-3 Mini)
                               │
                               ▼
                    Streaming Response
```

---

# 📂 Project Structure

```
local-ai-chatbot-rag/

│
├── app.py
├── ollama_client.py
├── rag.py
├── embeddings.py
├── vector_store.py
├── build_vector_db.py
│
├── pdf_docs/
│
├── vector_db/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/ArjunKA99/local-ai-chatbot-rag.git

cd local-ai-chatbot-rag
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama

https://ollama.com/download

Verify installation

```bash
ollama --version
```

---

## 5. Download Required Models

LLM

```bash
ollama pull phi3:mini
```

Embedding Model

```bash
ollama pull nomic-embed-text
```

---

# 📄 Add Documents

Place your PDF files inside

```
pdf_docs/
```

Example

```
pdf_docs/

Resume.pdf

Python.pdf

SQL Notes.pdf
```

---

# 🧠 Build Vector Database

Run

```bash
python build_vector_db.py
```

This performs:

- Reads all PDF documents
- Extracts text
- Splits text into chunks
- Generates embeddings
- Creates FAISS vector database
- Stores metadata

Generated files

```
vector_db/

index.faiss

metadata.pkl
```

---

# 🚀 Run the Chatbot

```bash
streamlit run app.py
```

The chatbot opens automatically in your browser.

---

# 💬 Example

### User

```
What Python projects has Arjun worked on?
```

### Assistant

```
According to the uploaded documents,

Arjun worked on an IMDb Movie Analysis project using Python,
Pandas, NumPy and Matplotlib.

The project involved data cleaning, exploratory analysis,
and visualization of movie datasets.
```

---

# 🔍 How Retrieval-Augmented Generation (RAG) Works

1. User asks a question.

2. The question is converted into an embedding.

3. FAISS searches for the most relevant chunks.

4. Retrieved chunks are added to the prompt.

5. Conversation summary and recent chat history are appended.

6. The prompt is sent to Phi-3 Mini through Ollama.

7. The assistant streams the response back to the user.

---

# 🧠 Conversation Memory

To reduce prompt size while preserving context:

- Older conversations are summarized.
- Recent messages are retained.
- Summary + recent chat are sent to the LLM.

This enables longer conversations without exceeding the model's context window.

---

# 📸 Screenshots

## Chat Interface



```
<img width="1913" height="926" alt="image" src="https://github.com/user-attachments/assets/53768c4e-f45f-42e1-9e38-a86bcc99ba2b" />

```

---

## Streaming Response

> Add screenshot here

```
screenshots/streaming_response.png
```

---

## Debug Sidebar

> Add screenshot here

```
screenshots/sidebar_debug.png
```

---

## RAG Response

> Add screenshot here

```
screenshots/rag_response.png
```

---

# 📈 Future Improvements

- Upload PDFs directly from the UI
- Support Word (.docx) and Text (.txt) files
- Display document citations
- Hybrid Search (Keyword + Semantic Search)
- Persistent conversation history
- Docker support
- Deploy on cloud platforms
- Multi-user support

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Embeddings
- Vector Databases (FAISS)
- Prompt Engineering
- Conversation Memory
- Streamlit Development
- Local AI using Ollama

---

# 📄 Requirements

```
streamlit
requests
pypdf
faiss-cpu
numpy
```

Install with

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

**Arjun K A**

GitHub: https://github.com/ArjunKA99/

LinkedIn: https://www.linkedin.com/in/arjun-ka/



---

# ⭐ If you found this project useful

Feel free to star ⭐ the repository.
