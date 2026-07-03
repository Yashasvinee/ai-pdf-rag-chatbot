# from utils.pdf_reader import extract_text_from_pdf

# pdf_text = extract_text_from_pdf("data/sample.pdf")

# print(pdf_text[:1000])
from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks

# Read the PDF
pdf_text = extract_text_from_pdf("data/sample.pdf")

# Split into chunks
chunks = split_text_into_chunks(pdf_text)

# Print information
print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])
