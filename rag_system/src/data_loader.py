import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader

# In data_loader.py
from langchain_community.document_loaders import (
    TextLoader,
    PDFPlumberLoader,
    DirectoryLoader
)

def load_and_chunk(directory):
    # Load JS files
    js_loader = DirectoryLoader(directory, glob="*.js", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
    js_docs = js_loader.load()
    
    # Load PDFs
    pdf_loader = DirectoryLoader(directory, glob="*.pdf", loader_cls=PDFPlumberLoader)
    pdf_docs = pdf_loader.load()
    
    # Combine and split
    documents = js_docs + pdf_docs
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)
    return chunks