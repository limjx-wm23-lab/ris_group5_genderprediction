import streamlit as st

# Page config
st.set_page_config(
    page_title="My Beautiful App",
    page_icon="✨",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}

h1 {
    text-align: center;
    font-size: 45px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    background: white;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.stButton button {
    border-radius: 20px;
    height: 45px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    "<h1>✨ My Streamlit App</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>A modern and clean dashboard</p>",
    unsafe_allow_html=True
)

st.write("")


# Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📊 Analytics</h3>
    <p>View your data insights here.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🤖 AI Tool</h3>
    <p>Smart processing system.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>⚡ Performance</h3>
    <p>Fast and efficient.</p>
    </div>
    """, unsafe_allow_html=True)


# Input section
st.markdown("### 🚀 Try it")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success(f"Welcome, {name}! 🎉")
    else:
        st.warning("Please enter your name")


# Footer
st.markdown("""
<hr>
<p style='text-align:center;color:gray;'>
Made with ❤️ using Streamlit
</p>
""", unsafe_allow_html=True)
