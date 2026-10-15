"""
Module: chat_interface.py
Local keyword & sentence search for document Q&A without requiring paid API keys
"""

import streamlit as st
import re

def query_text_locally(query: str, text: str) -> str:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    query_words = set(re.findall(r'[a-zA-Z]{3,}', query.lower()))
    
    scored = []
    for s in sentences:
        s_words = set(re.findall(r'[a-zA-Z]{3,}', s.lower()))
        match_count = len(query_words.intersection(s_words))
        if match_count > 0:
            scored.append((match_count, s))
            
    scored.sort(key=lambda x: x[0], reverse=True)
    if scored:
        best = [s for _, s in scored[:2]]
        return "Based on your uploaded study notes:\n\n" + "\n\n".join(best)
    return "I couldn't find a direct match in the current notes for that question. Try asking using related syllabus terms."

def render_pdf_chat():
    st.subheader("💬 Chat with PDF / Study Notes")
    text = st.session_state.get("current_doc_text", "")
    
    if not text:
        st.warning("Please upload a document or notes first in the Document Upload tab.")
        return
        
    query = st.text_input("Ask a question about the document:")
    if query:
        with st.spinner("Searching document context..."):
            ans = query_text_locally(query, text)
            st.markdown(f"**Geniuz:** {ans}")
