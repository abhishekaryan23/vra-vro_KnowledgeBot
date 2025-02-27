import litellm
from typing import List
import os

litellm.set_verbose = True
litellm.api_key = os.getenv("GROQ_API_KEY")

def summarize_chunks(chunks: List[str]) -> List[str]:
    summaries = []
    for chunk in chunks:
        prompt = f"Summarize the following in 2 lines:\n{chunk}\nSummary:"
        response = litellm.completion(
            model="groq",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        summaries.append(response["choices"][0]["message"]["content"].strip())
    return summaries