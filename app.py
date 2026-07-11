# # # # # # from utils.pdf_reader import extract_text_from_pdf

# # # # # # pdf_text = extract_text_from_pdf("data/sample.pdf")

# # # # # # print(pdf_text[:1000])
# # # # # from utils.pdf_reader import extract_text_from_pdf
# # # # # from utils.text_splitter import split_text_into_chunks

# # # # # # Read the PDF
# # # # # pdf_text = extract_text_from_pdf("data/sample.pdf")

# # # # # # Split into chunks
# # # # # chunks = split_text_into_chunks(pdf_text)

# # # # # # Print information
# # # # # print(f"Total Chunks: {len(chunks)}")

# # # # # print("\nFirst Chunk:\n")
# # # # # print(chunks[0])

# # # # # print("\nSecond Chunk:\n")
# # # # # print(chunks[1])
# # # # from utils.pdf_reader import extract_text_from_pdf
# # # # from utils.text_splitter import split_text_into_chunks
# # # # from utils.embeddings import create_embeddings

# # # # # Read PDF
# # # # pdf_text = extract_text_from_pdf("data/sample.pdf")

# # # # # Split into chunks
# # # # chunks = split_text_into_chunks(pdf_text)

# # # # print(f"Total Chunks: {len(chunks)}")

# # # # # Create embeddings
# # # # embeddings = create_embeddings(chunks)

# # # # print(f"\nTotal Embeddings: {len(embeddings)}")

# # # # print("\nDimension of one embedding:")
# # # # print(len(embeddings[0]))

# # # # print("\nFirst 10 values of the first embedding:")
# # # # print(embeddings[0][:10])


# # # from utils.pdf_reader import extract_text_from_pdf
# # # from utils.text_splitter import split_text_into_chunks
# # # from utils.vector_store import (
# # #     create_vector_store,
# # #     search_vector_store,
# # # )

# # # # -------------------------------
# # # # Step 1: Read PDF
# # # # -------------------------------

# # # pdf_text = extract_text_from_pdf("data/sample.pdf")

# # # # -------------------------------
# # # # Step 2: Split Text
# # # # -------------------------------

# # # chunks = split_text_into_chunks(pdf_text)

# # # print(f"\nTotal Chunks : {len(chunks)}")

# # # # -------------------------------
# # # # Step 3: Create Vector Store
# # # # -------------------------------

# # # vector_store = create_vector_store(chunks)

# # # if vector_store is None:
# # #     print("\nFailed to create FAISS Vector Store.")
# # #     exit()

# # # print("\n✅ FAISS Vector Store Created Successfully!")

# # # # -------------------------------
# # # # Step 4: Test Similarity Search
# # # # -------------------------------

# # # query = input("\nEnter your question: ")

# # # results = search_vector_store(vector_store, query)

# # # print("\nTop Matching Chunks\n")

# # # for i, doc in enumerate(results, start=1):
# # #     print(f"Result {i}")
# # #     print("-" * 60)
# # #     print(doc.page_content)
# # #     print()

# # from utils.llm import get_llm

# # llm = get_llm()

# # response = llm.invoke("Say hello in one sentence.")

# # print(response.content)

# from utils.pdf_reader import extract_text_from_pdf
# from utils.text_splitter import split_text_into_chunks
# from utils.vector_store import (
#     create_vector_store,
#     search_vector_store,
# )
# from utils.llm import generate_answer

# # ----------------------------------
# # Step 1: Read PDF
# # ----------------------------------

# pdf_text = extract_text_from_pdf("data/sample.pdf")

# # ----------------------------------
# # Step 2: Split Text
# # ----------------------------------

# chunks = split_text_into_chunks(pdf_text)

# print(f"\nTotal Chunks: {len(chunks)}")

# # ----------------------------------
# # Step 3: Create Vector Store
# # ----------------------------------

# vector_store = create_vector_store(chunks)

# if vector_store is None:
#     print("Failed to create vector store.")
#     exit()

# print("✅ Vector Store Created Successfully!")

# # ----------------------------------
# # Step 4: Ask User Question
# # ----------------------------------

# question = input("\nAsk your question: ")

# # ----------------------------------
# # Step 5: Retrieve Relevant Chunks
# # ----------------------------------

# documents = search_vector_store(
#     vector_store,
#     question
# )

# # ----------------------------------
# # Step 6: Generate Final Answer
# # ----------------------------------

# answer = generate_answer(
#     question,
#     documents
# )

# print("\n" + "=" * 60)
# print("ANSWER")
# print("=" * 60)

# print(answer)

from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import (
    create_vector_store,
    search_vector_store,
)
from utils.llm import generate_answer

# ----------------------------------
# Load PDF
# ----------------------------------

print("Loading PDF...")

pdf_text = extract_text_from_pdf("data/sample.pdf")

# ----------------------------------
# Split Text
# ----------------------------------

chunks = split_text_into_chunks(pdf_text)

# ----------------------------------
# Create Vector Store
# ----------------------------------

print("Creating Vector Store...")

vector_store = create_vector_store(chunks)

if vector_store is None:
    print("Failed to create vector store.")
    exit()

print("\n✅ AI PDF Chatbot is Ready!")
print("Type 'exit' anytime to quit.\n")

# ----------------------------------
# Chat Loop
# ----------------------------------

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    documents = search_vector_store(
        vector_store,
        question
    )

    answer = generate_answer(
        question,
        documents
    )

    print("\nAssistant:")
    print(answer)
    print("-" * 60)