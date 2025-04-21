from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text: str):
    return model.encode(text, convert_to_tensor=True)

def create_faiss_index(embeddings: np.ndarray) -> faiss.Index:
    index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance
    index.add(embeddings)  # Add embeddings to index
    return index

def search_similar(query_embedding: np.ndarray, index: faiss.Index, top_k: int = 5) -> list:
    distances, indices = index.search(query_embedding, top_k)
    return indices, distances
