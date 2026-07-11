# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from config import LLM_MODEL

# # Load environment variables
# load_dotenv()

# # Initialize Gemini LLM
# llm = ChatGoogleGenerativeAI(
#     model=LLM_MODEL,
#     temperature=0
# )


# def get_llm():
#     """
#     Returns the initialized Gemini model.
#     """

#     return llm

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from config import LLM_MODEL

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    temperature=0
)


def get_llm():
    """
    Returns the initialized Gemini model.
    """
    return llm


def generate_answer(question, documents):
    """
    Generates an answer using the retrieved documents.
    """

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the context below.

If the answer is not present in the context,
reply:

"I couldn't find enough information in the uploaded PDF to answer this question."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content