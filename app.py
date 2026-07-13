import streamlit as st
import requests

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */
.stApp{
    background:linear-gradient(135deg,#F8FAFC,#EEF4FF,#FFFFFF);
}

/* Hide Streamlit Menu */
#MainMenu{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
header{
    visibility:hidden;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0F172A;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Hero Banner */
.hero{
    background:
    linear-gradient(rgba(15,23,42,.72),
    rgba(15,23,42,.72)),
    url("https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1600");

    background-size:cover;
    background-position:center;

    border-radius:25px;

    padding:70px;

    color:white;

    text-align:center;

    box-shadow:0 15px 35px rgba(0,0,0,.25);

    margin-bottom:35px;
}

.hero h1{
    font-size:52px;
    font-weight:700;
    margin-bottom:15px;
}

.hero p{
    font-size:19px;
    line-height:1.8;
}

/* Glass Card */

.card{

    background:rgba(255,255,255,.92);

    border-radius:20px;

    padding:25px;

    box-shadow:0 10px 30px rgba(0,0,0,.08);

    border:1px solid #E5E7EB;

    margin-top:20px;

}

/* Result Card */

.result{

    background:linear-gradient(135deg,#10B981,#059669);

    color:white;

    padding:35px;

    border-radius:20px;

    text-align:center;

    box-shadow:0 15px 35px rgba(16,185,129,.35);

}

/* Button */

.stButton>button{

    width:100%;

    height:55px;

    border:none;

    border-radius:12px;

    background:linear-gradient(135deg,#2563EB,#1D4ED8);

    color:white;

    font-size:18px;

    font-weight:600;

    transition:.3s;
}

.stButton>button:hover{

    transform:translateY(-3px);

    box-shadow:0 10px 25px rgba(37,99,235,.35);

}

/* Input */

div[data-baseweb="input"]{

    border-radius:12px;

}

/* Footer */

.footer{

    text-align:center;

    color:#64748B;

    margin-top:50px;

    font-size:15px;

}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/home.png",
        width=80
    )

    st.title("House Price AI")

    st.markdown("---")

    st.markdown("### 📌 About Project")

    st.write("""
This application predicts the estimated
price of a house using a Machine Learning
model deployed with FastAPI.

### 🛠 Technologies

✔ Python

✔ Streamlit

✔ FastAPI

✔ Scikit-Learn

✔ Pandas

✔ Machine Learning
""")

    st.markdown("---")

    st.success("🟢 API Ready")

    st.info("🏡 Professional ML Project")

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div class="hero">

<h1>🏡 House Price Prediction System</h1>

<p>

Estimate the value of your dream home
using Artificial Intelligence and Machine Learning.

Fast • Accurate • Professional

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# INFORMATION CARDS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="card">

<center>

<h2>🤖</h2>

<h3>Machine Learning</h3>

<p>
Linear Regression Model
</p>

</center>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="card">

<center>

<h2>⚡</h2>

<h3>FastAPI</h3>

<p>
High Performance API
</p>

</center>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="card">

<center>

<h2>🎨</h2>

<h3>Streamlit UI</h3>

<p>
Modern Dashboard
</p>

</center>

</div>
""", unsafe_allow_html=True)

st.write("")
st.divider()

# ==========================================================
# INPUT SECTION
# ==========================================================

st.markdown("## 📏 Enter House Details")

st.markdown("""
<div class="card">
""", unsafe_allow_html=True)

area = st.number_input(

    "House Area (Square Feet)",

    min_value=100.0,

    max_value=10000.0,

    value=1500.0,

    step=50.0

)

predict = st.button(

    "🚀 Predict House Price",

    use_container_width=True

)

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    with st.spinner("🔄 AI is predicting the house price..."):

        try:

            response = requests.post(

                "http://127.0.0.1:8000/predict",

                json={"area": area},

                timeout=10

            )

            if response.status_code == 200:

                result = response.json()

                predicted_price = result["predicted_price"]

                st.balloons()

            else:

                st.error("Prediction Failed!")

        except:

            st.error("⚠️ FastAPI Server is not running.")
            # ==========================================================
# PREDICTION RESULT
# ==========================================================

if predict and "predicted_price" in locals():

    st.write("")

    st.markdown(
        f"""
        <div class="result">

        <h4>✅ Prediction Completed Successfully</h4>

        <h1>💰 Estimated House Price</h1>

        <h1>Rs. {predicted_price:,.0f}</h1>

        <p>
        This prediction was generated using a trained
        Machine Learning Linear Regression model.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("🎉 Prediction generated successfully!")

# ==========================================================
# PROJECT FEATURES
# ==========================================================

st.write("")
st.divider()

st.markdown("## ✨ Project Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Model",
        "Linear Regression"
    )

with col2:

    st.metric(
        "Backend",
        "FastAPI"
    )

with col3:

    st.metric(
        "Frontend",
        "Streamlit"
    )

st.write("")

feature1, feature2 = st.columns(2)

with feature1:

    st.info("""
### 🤖 AI Features

- House Price Prediction
- Machine Learning Model
- Fast Response
- Real-Time Prediction
- Professional Dashboard
""")

with feature2:

    st.info("""
### 🛠 Technology Stack

- Python
- Pandas
- Scikit-Learn
- FastAPI
- Streamlit
""")

# ==========================================================
# ABOUT PROJECT
# ==========================================================

st.write("")
st.divider()

st.markdown("## 📖 About This Project")

st.markdown("""

This project predicts the estimated market value of a house
based on its area using a Machine Learning model.

The application combines a FastAPI backend with a modern
Streamlit frontend to provide fast, accurate and interactive
predictions.

""")

# ==========================================================
# DEVELOPER SECTION
# ==========================================================

st.write("")
st.divider()

st.markdown("## 👩‍💻 Developer")

developer_col1, developer_col2 = st.columns([1,2])

with developer_col1:

    st.image(
        "https://img.icons8.com/color/240/female-student.png",
        width=180
    )

with developer_col2:

    st.markdown("""
### Hania Eman

**AI & Data Science Student**

Passionate about Machine Learning,
Artificial Intelligence and Data Science.

This project demonstrates a complete
Machine Learning deployment using:

- ✅ Python
- ✅ FastAPI
- ✅ Streamlit
- ✅ Scikit-Learn

""")

st.write("")

github, linkedin = st.columns(2)

with github:

    st.link_button(
        "🌐 GitHub",
        "https://github.com/haniaeman2026-pixel"
    )

with linkedin:

    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/"
    )

# ==========================================================
# FOOTER
# ==========================================================

st.write("")
st.divider()

st.markdown(
"""
<div class="footer">

🏡 House Price Prediction System

Built with ❤️ using Python • FastAPI • Streamlit • Scikit-Learn

<br><br>

© 2026 Hania Eman | All Rights Reserved

</div>
""",
unsafe_allow_html=True
)