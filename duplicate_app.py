import streamlit as st
import helper
import pickle
import os
import gdown

# Streamlit Page Setup
st.set_page_config(
    page_title="Duplicate Question Detector",
    page_icon="❓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Step 1: Download model from Google Drive if not present
file_id = "1LXM99sCtAn3puBvi8mMv1_m5-PMuEDM7"
model_path = "model.pkl"

if not os.path.exists(model_path):
    with st.spinner("Downloading model..."):
        gdown.download("https://drive.google.com/uc?export=download&id=1LXM99sCtAn3puBvi8mMv1_m5-PMuEDM7", model_path, quiet=False)

# Step 2: Load the model
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error("Failed to load the model.")
    st.stop()

# UI Components
st.title('Duplicate Question Detector 🧠')
st.markdown("<p style='text-align: center; font-size: 18px;'>Check if two questions are semantically identical</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    q1 = st.text_area('Question 1', height=100)
with col2:
    q2 = st.text_area('Question 2', height=100)

if st.button('Check for Duplicate', use_container_width=True):
    if q1.strip() == "" or q2.strip() == "":
        st.warning("Please enter both questions.")
    else:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.success("✅ These questions are duplicates!")
        else:
            st.error("❌ These questions are NOT duplicates.")

# Sidebar Info
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e6/Quora_logo_2015.svg", width=150)
    st.markdown("### About")
    st.info("This app uses an ML model to detect if two Quora questions are duplicates.")

# Footer
st.markdown("""
    <hr>
    <p style="text-align: center;">Made with ❤️ by Bhaskar Ranjan Karn</p>
    """, unsafe_allow_html=True)
