import streamlit as st
import os

os.environ.setdefault("API_BASE_URL", "http://localhost:8000")

home_page = st.Page("st_home.py", title="Trang chủ", icon="🏠")
gen_test_page = st.Page("st_gentest_app.py", title="Kiểm tra", icon="📝")

pg = st.navigation([home_page, gen_test_page])

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

input, textarea {
    -webkit-user-select: none !important;
    -ms-user-select: none !important;
    user-select: none !important;
}

pre, code {
    -webkit-user-select: none !important;
    -ms-user-select: none !important;
    user-select: none !important;
}
</style>

<script>
document.addEventListener("contextmenu", function(e) {
    e.preventDefault();
});

document.addEventListener("copy", function(e) {
    e.preventDefault();
});

document.addEventListener("cut", function(e) {
    e.preventDefault();
});

document.addEventListener("keydown", function(e) {
    if ((e.ctrlKey || e.metaKey) && ['c', 'x', 'a'].includes(e.key.toLowerCase())) {
        e.preventDefault();
    }
});
</script>
""", unsafe_allow_html=True)


st.markdown("""
<style>
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] strong,
[data-testid="stText"] {
    font-size: 1.15rem !important;
}

[data-testid="stRadio"] label {
    font-size: 1.1rem !important;
}

[data-testid="stCode"] code,
[data-testid="stCode"] pre {
    font-size: 1.05rem !important;
    line-height: 1.6 !important;
}
</style>
""", unsafe_allow_html=True)

pg.run()