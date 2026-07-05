"""
Application Configuration

This file stores all configurable values used across the project.
Changing values here automatically affects the whole application.
"""

# Google Gemini Models
LLM_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-2"

# Text Splitting
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200