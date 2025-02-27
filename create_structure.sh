#!/bin/bash

# Define the base directory
BASE_DIR="rag_system"

# Create the directory structure
folders=(
    "$BASE_DIR/data/raw"
    "$BASE_DIR/data/processed"
    "$BASE_DIR/models/bge-m3"
    "$BASE_DIR/vector_db/faiss_index"
    "$BASE_DIR/src"
)

# Create the files with initial content if any
files=(
    "$BASE_DIR/src/data_loader.py"
    "$BASE_DIR/src/summarizer.py"
    "$BASE_DIR/src/embedder.py"
    "$BASE_DIR/src/rag_pipeline.py"
    "$BASE_DIR/src/evaluator.py"
    "$BASE_DIR/src/main.py"
    "$BASE_DIR/requirements.txt"
    "$BASE_DIR/config.yaml"
)

# Create directories
for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
        echo "Created folder: $folder"
    else
        echo "Folder already exists: $folder"
    fi
done

# Create files
for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        touch "$file"
        echo "Created file: $file"
    else
        echo "File already exists: $file"
    fi
done

echo "All folders and files have been created successfully."
