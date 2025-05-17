# RAG Context Answering App

This is a simple Retrieval-Augmented Generation (RAG) Python application that answers questions based on custom markdown files using vector search and OpenRouter LLMs.

It uses:
- `LangChain` for loading, splitting, and searching documents
- `Chroma` for vector storage
- `HuggingFaceEmbeddings` for embeddings
- `OpenRouter` for LLM responses
- `.env` file to manage API keys securely

---

## 📁 Project Structure
![image](https://github.com/user-attachments/assets/320858a3-2291-47fe-bcea-cb25628cc7a5)


## 📁 Project Structure
RAG/
├── chroma/ # Auto-generated vector store
├── data/books/ # Folder for markdown files (your data)
├── create_database.py # Script to generate and store vector embeddings
├── query_data.py # Script to query vector DB and get answers via LLM
├── .env # Contains your OpenRouter API key
├── .gitignore
└── README.md


---

## ✅ Setup Instructions

### 1. Install dependencies

```bash
pip install langchain langchain-community chromadb huggingface-hub requests python-dotenv


### 2. Add your markdown files
data/books/
├── alice-in-wonderland.md

### 3. Set your API key
