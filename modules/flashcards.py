"""
Module: flashcards.py
Interactive flashcards with active recall testing and reveal mechanism
"""

import streamlit as st

FLASHCARDS = [
    {
        "topic": "AVL Trees",
        "question": "What is the balance factor formula in an AVL Tree?",
        "answer": "Balance Factor = Height(Left Subtree) - Height(Right Subtree). Must be {-1, 0, +1}."
    },
    {
        "topic": "Graph Algorithms",
        "question": "Which data structure is used in Breadth-First Search (BFS)?",
        "answer": "A First-In-First-Out (FIFO) Queue."
    },
    {
        "topic": "Database Normalization",
        "question": "What is the primary condition for a relation to be in 3NF?",
        "answer": "Must be in 2NF and have NO Transitive Dependencies (non-key determining non-key)."
    }
]

def render_flashcards():
    st.subheader("🃏 Flashcards Revision Deck")
    st.write("Flip cards to test your active recall memory before exams:")
    
    for i, card in enumerate(FLASHCARDS):
        with st.expander(f"Card {i+1}: {card['topic']} (Click to Reveal Answer)"):
            st.markdown(f"### ❓ **Question:**\n{card['question']}")
            st.markdown(f"### 💡 **Answer:**\n{card['answer']}")
