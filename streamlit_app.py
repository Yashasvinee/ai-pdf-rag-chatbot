import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.vector_store import (
    create_vector_store,
    search_vector_store,
)

from utils.llm import generate_answer

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="AI PDF RAG Chatbot",
    page_icon="📄",
    layout="centered"
)

# ----------------------------------
# Session State
# ----------------------------------

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "messages" not in st.session_state:
    st.session_state.messages = []

    # ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.header("📄 PDF Information")

    if st.session_state.pdf_name:

        st.write(f"**File:** {st.session_state.pdf_name}")
        st.divider()

    if st.button("🧹 Clear Chat"):

        st.session_state.messages = []

        st.success("Chat cleared successfully!")

    else:

        st.write("No PDF uploaded.")

# ----------------------------------
# Title
# ----------------------------------

st.title("📄 AI PDF RAG Chatbot")

st.write(
    "Upload a PDF and ask questions about its contents."
)
# ----------------------------------

# ----------------------------------
# PDF Upload
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

# ----------------------------------
# Question Input
# ----------------------------------

question = st.chat_input(
    "Ask a question about the PDF..." 
)
# ----------------------------------
# Process Uploaded PDF
# ----------------------------------


if uploaded_file is not None:

    # Process only if a different PDF is uploaded
    if uploaded_file.name != st.session_state.pdf_name:

        with st.spinner("Processing PDF..."):

            pdf_text = extract_text_from_pdf(uploaded_file)

            chunks = split_text_into_chunks(pdf_text)

            st.session_state.vector_store = create_vector_store(chunks)

            st.session_state.pdf_name = uploaded_file.name
            st.session_state.messages = []

        st.success("✅ PDF processed successfully!")

        st.write(f"Total Chunks: {len(chunks)}")

    else:

        st.success("✅ PDF already processed.")
    # ----------------------------------
# Answer Question
# ----------------------------------

if question:
    if st.session_state.vector_store is None:
        st.warning("Please upload a PDF first.")

    elif question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):
            # Save user message
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
)

            documents = search_vector_store(
                st.session_state.vector_store,
                question
            )

            answer = generate_answer(
                question,
                documents
            )

            # Save assistant message
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
)
            # Display Chat History
# ----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


        # st.subheader("Answer")

        # st.write(answer)