from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

class ModelHandler:
    def __init__(self, data_path, faiss_index_path=None):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.data = pd.read_csv(data_path)
        self.index = None
        if faiss_index_path:
            self.load_faiss_index(faiss_index_path)

    def load_faiss_index(self, index_path):
        """Loads the FAISS index from disk."""
        self.index = faiss.read_index(index_path)
        print(f"Loaded FAISS index from {index_path}")

    def embed_text(self, texts):
        """Generates embeddings for the input texts."""
        return self.model.encode(texts, convert_to_tensor=False)

    def search_similar(self, query_embedding, top_k=5):
        """Searches the FAISS index for similar documents."""
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        return self.data.iloc[indices[0]].to_dict('records')

    def process_query(self, query):
        """Processes a query and returns the nearest documents."""
        query_embedding = self.embed_text([query])[0]
        return self.search_similar(query_embedding)