from groq import Groq
from langchain.chains import RetrievalQA

def setup_rag(vector_store):
    llm = Groq(model_name="mixtral-8x7b-32768", temperature=0.7)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    return qa_chain