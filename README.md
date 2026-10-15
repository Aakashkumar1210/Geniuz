# Geniuz – AI Smart Study Assistant

**Bachelor of Computer Applications (BCA) Project Demonstration**

A modular, student-centric academic productivity application built using Python and Streamlit.

## 🚀 Key Features
1. **Interactive Dashboard**: Study statistics, streak counter, and syllabus completion overview.
2. **Document & PDF Upload**: Extract and analyze academic text using pure Python and PyPDF2.
3. **Smart Notes Generator**: Extracts key concepts, bullet takeaways, and summaries.
4. **Download Notes**: One-click TXT file download for offline study.
5. **MCQ Quiz Engine**: Instant answer checking, score calculation, and conceptual explanations.
6. **Study Planner**: Subject countdowns, daily target hours, and milestone tracker.
7. **Flashcards Revision**: Active recall decks for quick exam preparation.
8. **Chat with PDF**: Ask questions grounded in uploaded lecture notes.

## 💻 How to Run Locally

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

4. Open `http://localhost:8501` in your browser!

---

## 🎓 BCA Viva Preparation Guide (Examiner Q&A)

**Q1: Why did you choose Python and Streamlit for this project?**  
*Answer:* Python offers rich text-processing capabilities and high-level libraries. Streamlit enables rapid prototyping of interactive, reactive web user interfaces with clean state management without requiring complex frontend build chains.

**Q2: How does the offline summarization work without an API key?**  
*Answer:* It uses frequency-based extractive summarization. The algorithm tokenizes text, removes stop words, computes word frequency weights, scores sentences based on keyword density and definition markers, and selects the highest-scoring sentences.

**Q3: How are ACID properties represented in the database quiz engine?**  
*Answer:* The quiz tests students on Atomicity, Consistency, Isolation, and Durability principles, validating user choices and displaying transactional concurrency explanations.

**Q4: What is the benefit of the Flashcard module?**  
*Answer:* It applies the cognitive psychology principles of **Active Recall** and **Spaced Repetition**, proven to significantly boost long-term memory retention before university examinations.
