import requests
import streamlit as st

@st.cache_data(ttl=3600)
def fetch_earthquake_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()