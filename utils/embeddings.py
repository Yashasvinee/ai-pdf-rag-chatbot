from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import EMBEDDING_MODEL

# Load environment variables
load_dotenv()

# Create embedding model
embedding_model = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL
)


def create_embeddings(text_chunks):
    """
    Converts text chunks into vector embeddings.

    Args:
        text_chunks (list): List of text chunks.

    Returns:
        list: List of embedding vectors.
    """

    embeddings = embedding_model.embed_documents(text_chunks)

    return embeddings

def get_embedding_model():
      
    return embedding_model