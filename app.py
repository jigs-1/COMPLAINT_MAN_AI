import streamlit as st

from preprocessing.text_cleaning import clean_text
from utils.predict import predict_category
from routing.category_mapping import get_authority
from routing.escalation_rules import get_escalation_time
from routing.authority_emails import authority_emails

from utils.email_service import send_email
from utils.otp_service import generate_otp, send_otp

from database.db import insert_complaint, get_all_complaints, create_table

from utils.sentiment import get_sentiment, get_priority_from_sentiment
from utils.summarizer import summarize_complaint
from utils.similarity import check_duplicate


# --------------------------------
# Ensure database table exists
# --------------------------------

create_table()


# --------------------------------
# Streamlit Title
# --------------------------------

st.title("AI Complaint Management System")


# --------------------------------
# Session State Initialization
# --------------------------------

if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

if "otp" not in st.session_state:
    st.session_state.otp = None

if "verified" not in st.session_state:
    st.session_state.verified = False


# --------------------------------
# Email Verification
# --------------------------------

st.header("User Verification")

user_email = st.text_input("Enter your email")


if st.button("Send OTP"):

    otp = generate_otp()

    send_otp(user_email, otp)

    st.session_state.otp = otp
    st.session_state.otp_sent = True

    st.success("OTP sent to your email")


if st.session_state.otp_sent:

    user_otp = st.text_input("Enter OTP")

    if st.button("Verify OTP"):

        if user_otp == st.session_state.otp:

            st.session_state.verified = True

            st.success("Email verified successfully")

        else:

            st.error("Invalid OTP")


# --------------------------------
# Complaint Submission
# --------------------------------

if st.session_state.verified:

    st.header("Submit a Complaint")

    name = st.text_input("Name")

    complaint = st.text_area("Enter your complaint")


    if st.button("Submit Complaint"):

        cleaned = clean_text(complaint)


        # -------------------------------
        # Duplicate Detection
        # -------------------------------

        duplicate = check_duplicate(complaint)

        if duplicate:

            st.warning("Similar complaint already exists! Complaint not submitted.")
            st.stop()


        # -------------------------------
        # NLP Pipeline
        # -------------------------------

        category, confidence, predictions = predict_category(cleaned)

        authority = get_authority(category)

        sentiment = get_sentiment(complaint)

        priority = get_priority_from_sentiment(sentiment)

        escalation = get_escalation_time(priority)

        summary = summarize_complaint(complaint)


        # -------------------------------
        # Store in Database
        # -------------------------------

        insert_complaint(
            name,
            user_email,
            complaint,
            category,
            priority
        )


        # -------------------------------
        # Send Email Notification
        # -------------------------------

        authority_email = authority_emails.get(authority)

        send_email(
            authority_email,
            "New Complaint Assigned",
            summary,
            category,
            priority,
            complaint,
            user_email
        )


        # -------------------------------
        # Display Results
        # -------------------------------

        st.subheader("Complaint Analysis")

        st.write("Complaint Summary:", summary)

        st.write("Predicted Category:", category)

        st.write("Model Confidence:", round(confidence, 2))

        if confidence < 0.5:
         st.warning("This complaint may contain multiple issues.")

        st.subheader("Top 3 Predictions")

        for label, score in predictions:
         st.write(label, "→", round(score, 2))
         
        st.write("Assigned Authority:", authority)

        st.write("Sentiment:", sentiment)

        st.write("Priority:", priority)

        st.write("Escalation Time:", escalation)

        st.success("Complaint Submitted Successfully")


# --------------------------------
# Dashboard
# --------------------------------

st.header("Complaint Dashboard")

complaints_df = get_all_complaints()

st.dataframe(complaints_df)