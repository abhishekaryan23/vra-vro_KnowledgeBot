import os
import litellm
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

litellm.set_verbose = True
litellm.api_key = os.getenv("GROQ_API_KEY")

class GroqEmbeddings:
    def __init__(self):
        self.model = "bge-base-en-v1.5"  # Use Groq-compatible model

    def embed(self, text):
        response = litellm.completion(
            model="groq",
            messages=[{"role": "user", "content": f"Embed: {text}"}],
            max_tokens=10
        )
        return response["choices"][0]["message"]["embedding"]

def generate_embeddings(chunks):
    embeddings = GroqEmbeddings()
    texts = [chunk.page_content for chunk in chunks]
    embeddings_list = [embeddings.embed(text) for text in texts]
    
    # Store in FAISS
    vector_store = FAISS.from_embeddings(texts, embeddings_list)
    return vector_store