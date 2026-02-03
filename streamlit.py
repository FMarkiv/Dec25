import streamlit as st
   from pathlib import Path

   st.set_page_config(layout="wide")
   html_content = Path("your_file.html").read_text()
   st.components.v1.html(html_content, height=800, scrolling=True)