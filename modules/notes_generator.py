"""
Module: notes_generator.py
Generates Executive Summaries, Bullet Points, and exports notes as TXT files
"""

import streamlit as st
import re
from collections import Counter

STOP_WORDS = {
    'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'with', 'by',
    'is', 'are', 'was', 'were', 'it', 'this', 'that', 'from', 'as', 'be', 'of'
}

def clean_and_tokenize(text: str):
    words = re.findall(r'[a-zA-Z]{3,}', text.lower())
    return [w for w in words if w not in STOP_WORDS]

def extract_key_points_local(text: str, max_points=6):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 25]
    
    tokens = clean_and_tokenize(text)
    freq = Counter(tokens)
    
    scored = []
    for s in sentences:
        s_tokens = clean_and_tokenize(s)
        score = sum(freq[t] for t in s_tokens)
        if re.search(r'is defined as|refers to|consists of|guarantees|properties', s, re.I):
            score *= 1.5
        scored.append((score, s))
        
    scored.sort(key=lambda x: x[0], reverse=True)
    return [s for _, s in scored[:max_points]]

def generate_summary_and_notes():
    st.subheader("📝 Smart Notes Generator")
    
    text = st.session_state.get("current_doc_text", "")
    doc_name = st.session_state.get("current_doc_name", "Untitled Notes")
    
    if not text:
        st.warning("Please upload a document first or paste text below.")
        text = st.text_area("Or paste course notes directly:", height=200)
        if st.button("Use Pasted Text"):
            st.session_state["current_doc_text"] = text
            st.rerun()
        return

    st.success(f"Ready to synthesize notes for: {doc_name}")
    
    if st.button("⚡ Generate Structured Notes"):
        with st.spinner("Analyzing text using NLP frequency scoring..."):
            key_points = extract_key_points_local(text, max_points=7)
            summary = " ".join(key_points[:2])
            
            st.session_state["generated_notes"] = {
                "title": doc_name,
                "summary": summary,
                "key_points": key_points
            }
            
    notes = st.session_state.get("generated_notes")
    if notes:
        st.markdown("### 📌 Executive Summary")
        st.info(notes["summary"])
        
        st.markdown("### 💡 Key High-Yield Points")
        for i, pt in enumerate(notes["key_points"]):
            st.markdown(f"**{i+1}.** {pt}")
            
        # Download Note as TXT File (Feature #9)
        export_text = f"GENIUZ STUDY NOTES - {notes['title']}\n"
        export_text += "="*60 + "\n\n"
        export_text += "EXECUTIVE SUMMARY:\n" + notes["summary"] + "\n\n"
        export_text += "KEY POINTS:\n"
        for i, pt in enumerate(notes["key_points"]):
            export_text += f"{i+1}. {pt}\n"
            
        st.download_button(
            label="📥 Download Notes as .txt File",
            data=export_text,
            file_name=f"{notes['title']}_notes.txt",
            mime="text/plain"
        )
