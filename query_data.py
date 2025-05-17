from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()


API_KEY=os.getenv('API_KEY')
CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are a helpful assistant who answers questions based ONLY on the context below. 
Please provide a concise and clear answer, not just repeat the context.Make sure it is two whole sentences.

Context:
{context}

Question: {question}

Answer:
"""

def main():
    # Hardcoded query text
    query_text = "Who is Alice?"

    # Set up Chroma vector store and embedder
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    print("Relevance score of top result:", results[0][1])

    if len(results) == 0 or results[0][1] < 0.3:
        print("Unable to find matching results.")
        return

    # Prepare prompt using retrieved documents
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    #open router api
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": API_KEY,
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "RAG-App",
        },
        data=json.dumps({
            "model": "qwen/qwen3-0.6b-04-28:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        })
    )

    try:
        response_json = response.json()
        answer = response_json["choices"][0]["message"]["content"]
        print(f"Response: {answer}")
    except Exception as e:
        print("Error parsing response:", e)
        print("Raw response:", response.text)
        return

    # # Print sources
    sources = [doc.metadata.get("source", None) for doc, _ in results]
    print(f"Sources: {sources}")

if __name__ == "__main__":
    main()
