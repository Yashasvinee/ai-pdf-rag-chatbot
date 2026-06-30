from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF and returns all text as one string.
    """

    reader = PdfReader(pdf_path)

    complete_text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            complete_text += page_text + "\n"

    return complete_text