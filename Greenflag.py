import streamlit as st
import pandas as pd
import os
import time

# -------------------------------
# LOGIN DETAILS
# -------------------------------
USERNAME = "SraAyu"
PASSWORD = "24022908"
DATA_FILE = "wanaparthy_secrets.csv"

# -------------------------------
# SESSION STATE
# -------------------------------
if "slide" not in st.session_state:
    st.session_state.slide = 1
if "history_unlock" not in st.session_state:
    st.session_state.history_unlock = False
if "form_data" not in st.session_state:
    st.session_state.form_data = {}

# -------------------------------
# THEME (PINK + GREEN)
# -------------------------------
st.markdown("""
<style>
body{background-color:#ffc0cb;color:#006400;}
.stApp{background-color:#ffc0cb;}
h1,h2,h3,h4,h5,p,label,div{color:#006400;font-weight:bold;}
.stButton>button{background-color:#ff1493;color:#006400;border-radius:10px;height:40px;font-weight:bold;}
textarea,input{background-color:#ffe4e1 !important;color:#006400 !important;}
</style>
""",unsafe_allow_html=True)

# -------------------------------
# CREATE CSV IF NOT EXISTS
# -------------------------------
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=[
        "Title", "Grievance", "Mood", "Severity", "Her Reply",
        "Day", "Remembered", "Need", "MessageToAyush", "LambadiWord"
    ]).to_csv(DATA_FILE,index=False)

# -------------------------------
# SLIDE 1 LOGIN
# -------------------------------
if st.session_state.slide == 1:
    st.title("💗 SraAyu Secret Portal")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == USERNAME and pwd == PASSWORD:
            st.session_state.slide = 2
            st.rerun()
        else:
            st.error("Wrong credentials")

# -------------------------------
# SLIDE 2 INTRO
# -------------------------------
elif st.session_state.slide == 2:
    st.markdown("<h1 style='text-align:center;color:white;border:5px solid blue;padding:40px;'>WELCOME TO WANAPARTHY SECRETS</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.slide = 1
            st.rerun()
    with col2:
        if st.button("Next"):
            st.session_state.slide = 3
            st.rerun()

# -------------------------------
# SLIDE 3 MESSAGE FROM AYUSH
# -------------------------------
elif st.session_state.slide == 3:
    st.markdown("<h2 style='text-align:center;'>Message from Ayush to SraAyu 💌</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Every word you write here matters to me, because you matter to me.</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.slide = 2
            st.rerun()
    with col2:
        if st.button("Next"):
            time.sleep(6)  # 6 seconds display
            st.session_state.slide = 4
            st.rerun()

# -------------------------------
# SLIDE 4 PERSONAL QUESTIONS
# -------------------------------
elif st.session_state.slide == 4:
    st.title("Just Curious About You 💗")
    q1 = st.text_area("1️⃣ How was your day? 😊")
    q2 = st.text_area("2️⃣ Have you remembered me today? 😉")
    q3 = st.text_area("3️⃣ Anything you need from me? 😏")
    q4 = st.text_area("4️⃣ Your message of the day to Ayush and any question for Ayush 💌")
    q5 = st.text_area("5️⃣ Lambadi word and its meaning of the day 💌")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.slide = 3
            st.rerun()
    with col2:
        if st.button("Next"):
            st.session_state.form_data.update({
                "Day": q1,
                "Remembered": q2,
                "Need": q3,
                "MessageToAyush": q4,
                "LambadiWord": q5
            })
            st.session_state.slide = 5
            st.rerun()

# -------------------------------
# SLIDE 5 GRIEVANCE FORM
# -------------------------------
elif st.session_state.slide == 5:
    st.title("Submit Your Grievance")
    title = st.text_input("Title")
    grievance = st.text_area("What is bothering you?")
    mood = st.selectbox("Mood", ["Angry","Sad","Neutral","Happy"])
    severity = st.slider("Severity",1,10,5)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.slide = 4
            st.rerun()
    with col2:
        if st.button("Next"):
            st.session_state.form_data.update({
                "Title": title,
                "Grievance": grievance,
                "Mood": mood,
                "Severity": severity
            })
            st.session_state.slide = 6
            st.rerun()

# -------------------------------
# SLIDE 6 WHY YOU BLOCKED ME
# -------------------------------
elif st.session_state.slide == 6:
    st.title("Why did you block me?")
    reply = st.text_area("Your reply (optional)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.slide = 5
            st.rerun()
    with col2:
        if st.button("Submit"):
            data = st.session_state.form_data
            new_row = pd.DataFrame([{
                "Title": data.get("Title",""),
                "Grievance": data.get("Grievance",""),
                "Mood": data.get("Mood",""),
                "Severity": data.get("Severity",""),
                "Her Reply": reply,
                "Day": data.get("Day",""),
                "Remembered": data.get("Remembered",""),
                "Need": data.get("Need",""),
                "MessageToAyush": data.get("MessageToAyush",""),
                "LambadiWord": data.get("LambadiWord","")
            }])
            old = pd.read_csv(DATA_FILE)
            updated = pd.concat([old,new_row],ignore_index=True)
            updated.to_csv(DATA_FILE,index=False)
            st.session_state.slide = 7
            st.rerun()

# -------------------------------
# SLIDE 7 CONFIRMATION
# -------------------------------
elif st.session_state.slide == 7:
    st.title("💖 Thank You")
    st.write("Your intimate conversation has been safely delivered to Ayush 💌, my dear SraAyu.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.slide = 6
            st.rerun()
    with col2:
        if st.button("Next"):
            st.session_state.slide = 8
            st.rerun()

# -------------------------------
# SLIDE 8 ABOUT
# -------------------------------
elif st.session_state.slide == 8:
    st.title("About This Portal")
    st.write("This playful grievance portal was created specially for My SraAyu 💗")
    st.write("If any other girl use or saw this My SraAyu will scratch her face.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.slide = 7
            st.rerun()
    with col2:
        if st.button("View History"):
            st.session_state.slide = 9
            st.rerun()

# -------------------------------
# SLIDE 9 HISTORY
# -------------------------------
elif st.session_state.slide == 9:
    st.title("Conversation History")
    if not st.session_state.history_unlock:
        pwd = st.text_input("Enter password to view history", type="password")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back"):
                st.session_state.slide = 8
                st.rerun()
        with col2:
            if st.button("Unlock"):
                if pwd == PASSWORD:
                    st.session_state.history_unlock = True
                    st.rerun()
                else:
                    st.error("Wrong password")
    else:
        if st.button("Back"):
            st.session_state.slide = 8
            st.rerun()
        df = pd.read_csv(DATA_FILE)
        st.dataframe(df)