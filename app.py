import streamlit as st

# 🎀 Page Config
st.set_page_config(page_title="🌸 NLP Course Portfolio 🌸", layout="wide")

# 💖 Background color and style
st.markdown("""
    <style>
    body {
        background-color: #ffe6f2;
        font-family: 'Poppins', sans-serif;
        color: #4a004e;
    }
    h1, h2, h3 {
        text-align: center;
        color: #a60073;
    }
    .box {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 20px;
        margin: 10px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 🌼 Title and Info
st.markdown("<h1>🌸 NLP Course Portfolio 🌸</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Kavya Avula | Reg No: RA2211003010877 | Course Code: 21CSE356T</h4>", unsafe_allow_html=True)

# 🌷 Table of Contents
st.sidebar.title("📚 Table of Contents")
section = st.sidebar.radio("Go to", ["Introduction", "Learning Objectives", "Reflection", "Achievements"])

# 🪷 Section 1 — Introduction
if section == "Introduction":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("Introduction")
    st.write("""
    The Natural Language Processing (NLP) course explores how computers interpret and generate human language.
    I aimed to learn techniques like tokenization, stemming, embeddings, and transformers — building skills
    for applications such as chatbots, text classification, and summarization.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# 🌻 Section 2 — Learning Objectives
elif section == "Learning Objectives":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("Learning Objectives 🌻")
    with st.expander("Unit 1 — Overview and Word Level Analysis"):
        st.write("Introduction to NLP, text preprocessing, tokenization, stemming, and lemmatization.")
    with st.expander("Unit 2 — Syntax Analysis"):
        st.write("Parsing, POS tagging, syntax trees, and dependency grammar.")
    with st.expander("Unit 3 — Semantic and Discourse Analysis"):
        st.write("Word sense disambiguation, semantics, and discourse relationships.")
    with st.expander("Unit 4 — Language Models"):
        st.write("N-grams, neural language models, RNNs, LSTMs, and transformers.")
    with st.expander("Unit 5 — NLP Applications"):
        st.write("Chatbots, sentiment analysis, summarization, and question answering systems.")
    st.markdown("</div>", unsafe_allow_html=True)

# 🌸 Section 3 — Reflection
elif section == "Reflection":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("Reflection 🌸")
    st.write("""
    🪄 **New Skills:** Mastered NLP preprocessing, vectorization, and transformer model fine-tuning.  
    💡 **Challenge:** Understanding complex architectures like LSTMs and BERT.  
    🌱 **Growth:** Improved from learning tokenization to building complete NLP pipelines.  
    🚀 **Future Use:** Plan to use NLP for chatbots, summarization, and text analytics applications.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# 🌟 Section 4 — Achievements
elif section == "Achievements":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("Achievements 🌟")
    st.write("""
    • Built a mini NLP model for Fake news classification in various languages.  
    • Worked on a Chatbot prototype using Transformer models.  
    • made a case study report on "BioBERT: Revolutionizing Biomedical Text Mining using NLP" ”.  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# 💜 Footer
st.markdown("<h6 style='text-align:center; color:#a60073;'>© 2025 Kavya Avula </h6>", unsafe_allow_html=True)
