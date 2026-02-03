import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide", page_title="Monthly Market Update - December 2025")

html_path = Path(__file__).parent / "newsletter_2025_12_5y.html"
html_content = html_path.read_text()

st.components.v1.html(html_content, height=3000, scrolling=True)
