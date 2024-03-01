import streamlit as st
import csv
from send_email import send_email
from topicreader import topics


st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss?", topics())
    raw_message = st.text_area("Your Message")
    message = f'''\
Subject: Email from {user_email} about {topic}

From: {user_email}
Topic: {topic}
{raw_message}
'''
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")