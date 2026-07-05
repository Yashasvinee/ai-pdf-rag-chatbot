# # # from utils.pdf_reader import extract_text_from_pdf

# # # pdf_text = extract_text_from_pdf("data/sample.pdf")

# # # print(pdf_text[:1000])
# # from utils.pdf_reader import extract_text_from_pdf
# # from utils.text_splitter import split_text_into_chunks

# # # Read the PDF
# # pdf_text = extract_text_from_pdf("data/sample.pdf")

# # # Split into chunks
# # chunks = split_text_into_chunks(pdf_text)

# # # Print information
# # print(f"Total Chunks: {len(chunks)}")

# # print("\nFirst Chunk:\n")
# # print(chunks[0])

# # print("\nSecond Chunk:\n")
# # print(chunks[1])
# from utils.pdf_reader import extract_text_from_pdf
# from utils.text_splitter import split_text_into_chunks
# from utils.embeddings import create_embeddings

# # Read PDF
# pdf_text = extract_text_from_pdf("data/sample.pdf")

# # Split into chunks
# chunks = split_text_into_chunks(pdf_text)

# print(f"Total Chunks: {len(chunks)}")

# # Create embeddings
# embeddings = create_embeddings(chunks)

# print(f"\nTotal Embeddings: {len(embeddings)}")

# print("\nDimension of one embedding:")
# print(len(embeddings[0]))

# print("\nFirst 10 values of the first embedding:")
# print(embeddings[0][:10])


from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import (
    create_vector_store,
    search_vector_store,
)

# -------------------------------
# Step 1: Read PDF
# -------------------------------

pdf_text = extract_text_from_pdf("data/sample.pdf")

# -------------------------------
# Step 2: Split Text
# -------------------------------

chunks = split_text_into_chunks(pdf_text)

print(f"\nTotal Chunks : {len(chunks)}")

# -------------------------------
# Step 3: Create Vector Store
# -------------------------------

vector_store = create_vector_store(chunks)

if vector_store is None:
    print("\nFailed to create FAISS Vector Store.")
    exit()

print("\n✅ FAISS Vector Store Created Successfully!")

# -------------------------------
# Step 4: Test Similarity Search
# -------------------------------

query = input("\nEnter your question: ")

results = search_vector_store(vector_store, query)

print("\nTop Matching Chunks\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}")
    print("-" * 60)
    print(doc.page_content)
    print()