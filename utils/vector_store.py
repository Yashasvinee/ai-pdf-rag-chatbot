# # from langchain_community.vectorstores import FAISS

# # from utils.embeddings import get_embedding_model


# # def create_vector_store(chunks):
# #     embedding_model = get_embedding_model()

# #     vector_store = FAISS.from_texts(
# #         texts=chunks,
# #         embedding=embedding_model
# #     )

# #     return vector_store


# # def search_vector_store(vector_store, query, k=3):
# #     results = vector_store.similarity_search(
# #         query=query,
# #         k=k
# #     )

# #     return results

# from langchain_community.vectorstores import FAISS
# from utils.embeddings import get_embedding_model


# def create_vector_store(text_chunks):
#     """
#     Creates a FAISS vector store from text chunks.

#     Args:
#         text_chunks (list): List of text chunks.

#     Returns:
#         FAISS: Vector store containing embeddings.
#     """

#     embedding_model = get_embedding_model()

#     vector_store = FAISS.from_texts(
#         texts=text_chunks,
#         embedding=embedding_model
#     )

#     return vector_store


# def search_vector_store(vector_store, query, k=3):
#     """
#     Searches the FAISS vector store.

#     Args:
#         vector_store: FAISS vector database.
#         query (str): User question.
#         k (int): Number of similar chunks.

#     Returns:
#         list: Most relevant documents.
#     """

#     results = vector_store.similarity_search(
#         query=query,
#         k=k
#     )

#     return results

from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model


def create_vector_store(text_chunks):
    """
    Creates a FAISS vector store from text chunks.

    Args:
        text_chunks (list): List of text chunks.

    Returns:
        FAISS: Vector store object.
    """

    try:
        embedding_model = get_embedding_model()

        vector_store = FAISS.from_texts(
            texts=text_chunks,
            embedding=embedding_model
        )

        return vector_store

    except Exception as e:
        print(f"Error creating vector store: {e}")
        return None


def search_vector_store(vector_store, query, k=3):
    """
    Searches the vector store.

    Args:
        vector_store : FAISS vector store
        query (str)  : User question
        k (int)      : Number of results

    Returns:
        list
    """

    try:
        results = vector_store.similarity_search(
            query=query,
            k=k
        )

        return results

    except Exception as e:
        print(f"Error searching vector store: {e}")
        return []