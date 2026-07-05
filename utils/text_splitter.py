from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

def split_text_into_chunks(text):
    """
    Splits extracted PDF text into smaller overlapping chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False,
    )

    chunks = text_splitter.split_text(text)

    return chunks