from src.data_loader import load_and_chunk
from src.summarizer import summarize_chunks
from src.embedder import generate_embeddings
from src.rag_pipeline import setup_rag
from src.evaluator import evaluate_rag

# Load data
chunks = load_and_chunk("data/raw")

# Generate summaries
summaries = summarize_chunks(chunks)

# Generate embeddings and store
vector_store = generate_embeddings(chunks, summaries)

# Setup RAG pipeline
qa_chain = setup_rag(vector_store)

# Evaluate
sample_queries = ["How does the authentication system work?"]
dataset = [{"user_input": q} for q in sample_queries]
results = evaluate_rag(dataset)
print(results)