"""
Module: quiz_engine.py
Interactive Multiple Choice Quiz with instant validation and score calculations
"""

import streamlit as st

SAMPLE_QUIZZES = [
    {
        "question": "What is the balance factor constraint for any node in an AVL tree?",
        "options": ["Must be exactly 0", "Must be within {-1, 0, 1}", "Can be between -2 and +2", "Any integer"],
        "answer": 1,
        "explanation": "An AVL tree requires that the height difference between left and right subtrees must be -1, 0, or 1."
    },
    {
        "question": "Which tree traversal visits elements of a Binary Search Tree in sorted ascending order?",
        "options": ["Pre-order", "Post-order", "In-order", "Level-order"],
        "answer": 2,
        "explanation": "In-order traversal visits Left -> Root -> Right, which naturally outputs sorted values in a BST."
    },
    {
        "question": "Which Normal Form specifically eliminates Partial Functional Dependency?",
        "options": ["1NF", "2NF", "3NF", "BCNF"],
        "answer": 1,
        "explanation": "Second Normal Form (2NF) mandates that no non-prime attribute depends on a proper subset of a candidate key."
    },
    {
        "question": "Which ACID property guarantees that all transaction operations commit or none do?",
        "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
        "answer": 0,
        "explanation": "Atomicity enforces all-or-nothing execution."
    }
]

def render_quiz_interface():
    st.subheader("🎯 MCQ Quiz Master")
    st.write("Test your understanding with instant feedback and score evaluation:")
    
    score = 0
    total = len(SAMPLE_QUIZZES)
    
    with st.form("mcq_quiz_form"):
        user_answers = []
        for i, q in enumerate(SAMPLE_QUIZZES):
            st.markdown(f"**Question {i+1}: {q['question']}**")
            choice = st.radio(f"Select answer for Q{i+1}:", q["options"], key=f"q_{i}")
            user_answers.append(choice)
            st.markdown("---")
            
        submitted = st.form_submit_button("Submit Quiz for Evaluation")
        
    if submitted:
        st.subheader("📊 Quiz Results")
        for i, q in enumerate(SAMPLE_QUIZZES):
            chosen = user_answers[i]
            correct = q["options"][q["answer"]]
            if chosen == correct:
                score += 1
                st.success(f"✅ Q{i+1}: Correct!\n*Explanation:* {q['explanation']}")
            else:
                st.error(f"❌ Q{i+1}: Incorrect. Your choice: {chosen} | Correct: {correct}\n*Explanation:* {q['explanation']}")
                
        pct = (score / total) * 100
        st.metric("Final Score", f"{score} / {total}", f"{pct:.1f}%")
        if pct >= 75:
            st.balloons()
