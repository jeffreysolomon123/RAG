# RAG Context Answering App

This is a simple Retrieval-Augmented Generation (RAG) Python application that answers questions based on custom markdown files using vector search and OpenRouter LLMs.

It uses:
- `LangChain` for loading, splitting, and searching documents
- `Chroma` for vector storage
- `HuggingFaceEmbeddings` for embeddings
- `OpenRouter` for LLM responses
- `.env` file to manage API keys securely

---

## Result : 
I fed the Alice in Wonderland story in the form of a markdown file and hardcoded a "Who is Alice?" question to test the RAG. This was the response I got using the `qwen/qwen3-0.6b-04-28:free` model from OpenRouter.

![image](https://github.com/user-attachments/assets/320858a3-2291-47fe-bcea-cb25628cc7a5)



## ✅ Setup Instructions

### 1. Install dependencies

```bash
pip install langchain langchain-community chromadb huggingface-hub requests python-dotenv
```

### 2. Add your markdown files
data/books/alice-in-wonderland.md

### 3. .env (Setup your API key)
```bash
API_KEY=your-openrouter-api-key

