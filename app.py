from utils.pdf_reader import extract_text_from_pdf

pdf_text = extract_text_from_pdf("data/sample.pdf")

print(pdf_text[:1000])