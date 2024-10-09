from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

def load_data(file_path):
    """Loads the CSV data for mental health."""
    loader = CSVLoader(
        file_path=file_path,
        csv_args={
            "delimiter": ",",
            "quotechar": '"',
            "fieldnames": ["selftext", "subreddit", "title", "Label"],
        },
    )
    return loader.load()


def split_text_into_chunks(mental_health_data, chunk_size=1000, chunk_overlap=200):
    """Splits text into smaller chunks for processing."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    
    chunks = []
    for doc in mental_health_data:
        chunked_texts = text_splitter.split_text(doc.page_content)
        for chunk_text in chunked_texts:
            chunks.append(Document(page_content=chunk_text))
    return chunks




def generate_embeddings_and_store_faiss(chunks, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """Generates embeddings for the chunks and stores them in a FAISS index."""
    # Initialize the Hugging Face embeddings model
    model = HuggingFaceEmbeddings(model_name=model_name)

    # Convert chunks into plain text for embedding
    texts = [doc.page_content for doc in chunks]

    # Create FAISS vector store using the embeddings model
    db = FAISS.from_texts(texts, model)
    
    return db, texts

