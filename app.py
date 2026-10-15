"""
Geniuz – AI Smart Study Assistant
BCA Final Year / Semester Mini-Project Demonstration
Target Framework: Python + Streamlit
"""

import streamlit as st
import datetime
from modules.pdf_processor import extract_text_from_pdf, get_document_metrics
from modules.notes_generator import generate_summary_and_notes
from modules.quiz_engine import render_quiz_interface
from modules.study_planner import render_study_planner
from modules.flashcards import render_flashcards
from modules.chat_interface import render_pdf_chat

# Configure Streamlit Page
st.set_page_config(
    page_title="Geniuz – AI Smart Study Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Blue-and-White Professional CSS Styling
st.markdown("""
<style>
    /* Executive Blue-and-White Palette */
    :root {
        --primary-blue: #1e40af;
        --secondary-blue: #2563eb;
        --light-blue-bg: #f0f7ff;
        --card-border: #e2e8f0;
    }
    
    .main {
        background-color: #f8fafc;
    }
    
    .stSidebar {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    .project-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        color: white;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .project-header h1 {
        color: white !important;
        font-size: 28px;
        font-weight: 700;
        margin: 0;
    }
    
    .project-header p {
        color: #dbeafe;
        font-size: 15px;
        margin-top: 6px;
    }
    
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #2563eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .stat-number {
        font-size: 28px;
        font-weight: 800;
        color: #1e3a8a;
    }
    
    .stat-label {
        font-size: 13px;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State Variables
if "current_doc_text" not in st.session_state:
    st.session_state["current_doc_text"] = ""
if "current_doc_name" not in st.session_state:
    st.session_state["current_doc_name"] = "No document selected"
if "generated_notes" not in st.session_state:
    st.session_state["generated_notes"] = None
if "quiz_score" not in st.session_state:
    st.session_state["quiz_score"] = 0

# Sidebar Navigation
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/graduation-cap.png", width=64)
    st.title("Geniuz AI")
    st.caption("Smart Study Assistant | BCA Project")
    st.markdown("---")
    
    menu_choice = st.radio(
        "Navigation Menu",
        [
            "📊 Dashboard",
            "📄 Document / PDF Upload",
            "📝 Notes Generator",
            "🎯 MCQ Quiz Master",
            "📅 Study Planner",
            "🃏 Flashcards",
            "💬 Chat with PDF",
            "📈 Progress & Analytics"
        ]
    )
    
    st.markdown("---")
    st.info("💡 **Engine Status:**\nFree Offline NLP Engine active.\n(Zero API key required)")

# Top Banner
st.markdown("""
<div class="project-header">
    <h1>🎓 Geniuz – AI Smart Study Assistant</h1>
    <p>Automated Notes Generation, Smart MCQ Quizzes, Exam Scheduling & Document Q&A for University Students</p>
</div>
""", unsafe_allow_html=True)

# Route to active module
if menu_choice == "📊 Dashboard":
    st.subheader("Welcome back, Student!")
    st.write("Here is your current academic preparation summary:")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-card"><div class="stat-number">7 Days</div><div class="stat-label">Study Streak</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><div class="stat-number">38.5 hrs</div><div class="stat-label">Total Study Time</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><div class="stat-number">84%</div><div class="stat-label">Avg Quiz Score</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-card"><div class="stat-number">32 / 45</div><div class="stat-label">Flashcards Mastered</div></div>', unsafe_allow_html=True)
        
    st.markdown("### 📌 Active Document Status")
    st.info(f"**Loaded Document:** {st.session_state['current_doc_name']}")
    
elif menu_choice == "📄 Document / PDF Upload":
    st.subheader("Upload Study Material (PDF or TXT)")
    uploaded_file = st.file_uploader("Select PDF or Notes Text File", type=["pdf", "txt", "md"])
    if uploaded_file is not None:
        extracted = extract_text_from_pdf(uploaded_file)
        st.session_state["current_doc_text"] = extracted
        st.session_state["current_doc_name"] = uploaded_file.name
        st.success(f"Successfully processed: {uploaded_file.name}")
        
        metrics = get_document_metrics(extracted)
        m1, m2, m3 = st.columns(3)
        m1.metric("Word Count", metrics["words"])
        m2.metric("Character Count", metrics["chars"])
        m3.metric("Estimated Reading Time", f"{metrics['read_time']} mins")
        
        with st.expander("Preview Extracted Text"):
            st.text_area("Extracted Content", extracted[:2000], height=250)

elif menu_choice == "📝 Notes Generator":
    generate_summary_and_notes()

elif menu_choice == "🎯 MCQ Quiz Master":
    render_quiz_interface()

elif menu_choice == "📅 Study Planner":
    render_study_planner()

elif menu_choice == "🃏 Flashcards":
    render_flashcards()

elif menu_choice == "💬 Chat with PDF":
    render_pdf_chat()

elif menu_choice == "📈 Progress & Analytics":
    st.subheader("Study Progress & Subject Readiness")
    st.info("Demonstrating study metrics, quiz history, and unit completion curves.")
