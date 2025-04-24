import streamlit as st
import streamlit_analytics2 as streamlit_analytics

with streamlit_analytics.track():
   st.write("Hello, World!")
   st.button("Click me")