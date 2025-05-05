# main.py
from data_loader import load_data
from layout import DashboardLayout
import streamlit as st

# Load dataset
df = load_data("social_media_data.csv")

# Set page config
st.set_page_config(page_title="Social Media Dashboard", layout="wide")

# Render dashboard
layout = DashboardLayout(df)
layout.render()
