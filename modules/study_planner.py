"""
Module: study_planner.py
Manages subjects, target exam dates, and daily study hours calculation
"""

import streamlit as st
import datetime

def render_study_planner():
    st.subheader("📅 Study Planner & Exam Timetable")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Add / Schedule New Subject")
        subject = st.text_input("Subject Name", "Data Structures & Algorithms")
        code = st.text_input("Course Code", "BCA-201")
        exam_date = st.date_input("Target Exam Date", datetime.date(2026, 11, 15))
        hours = st.slider("Target Daily Study Hours", 0.5, 6.0, 2.5, 0.5)
        
        if st.button("Add to Timetable"):
            st.success(f"Added {subject} ({code}) with daily target {hours} hours!")

    with col2:
        st.markdown("### ⏳ Active Exam Countdowns")
        today = datetime.date.today()
        days_left = (exam_date - today).days
        
        st.metric("Days Remaining for Exam", f"{max(0, days_left)} days")
        st.progress(min(1.0, max(0.0, 1 - (days_left / 60.0))))
        
        total_needed_hours = days_left * hours
        st.info(f"💡 At {hours} hrs/day, you have approx **{total_needed_hours:.0f} hours** of prep time remaining.")
