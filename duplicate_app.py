import streamlit as st
import helper
import pickle

# 1. Page configuration
st.set_page_config(
    page_title="Duplicate Question Detector",
    page_icon="❓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Load model
model = pickle.load(open('model.pkl', 'rb'))

# 3. Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e6/Quora_logo_2015.svg", width=150)
    st.markdown("### About")
    st.info("This app uses an ML model to detect if two Quora questions are duplicates.")

# 4. Main Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Duplicate Question Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Check if two questions are semantically identical</p>", unsafe_allow_html=True)
st.markdown("---")

# 5. Input section
col1, col2 = st.columns(2)
with col1:
    q1 = st.text_area('Question 1', height=100)
with col2:
    q2 = st.text_area('Question 2', height=100)

# 6. Prediction
if st.button('Check for Duplicate', use_container_width=True):
    if q1.strip() == "" or q2.strip() == "":
        st.warning("⚠️ Please enter both questions.")
    else:
        with st.spinner("Analyzing..."):
            query = helper.query_point_creator(q1, q2)
            result = model.predict(query)[0]

        if result:
            st.success("✅ These questions are duplicates!")
        else:
            st.error("❌ These questions are NOT duplicates.")

# 7. Footer
st.markdown("""
    <hr>
    <p style="text-align: center;">Made with ❤️ by Bhaskar Ranjan Karn</p>
    """, unsafe_allow_html=True)
