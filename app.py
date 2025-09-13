from fetch_data import fetch_earthquake_data
from parse_data import parse_earthquake_data

import streamlit as st
import plotly.express as px

URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

# Fetch data
data = fetch_earthquake_data(URL)
df = parse_earthquake_data(data)

# Dashboard UI
st.title("🌍 Real-Time Earthquake Dashboard")
st.markdown("Data from [USGS](https://earthquake.usgs.gov/) | Updated hourly")

# Filters
min_mag = st.slider("Minimum Magnitude", 0.0, 10.0, 2.5, step=0.1)
df_filtered = df[df["magnitude"] >= min_mag]

# Map
st.subheader(f"🗺️ Earthquake Map (Magnitude ≥ {min_mag})")
fig = px.scatter_geo(df_filtered,
                     lat="latitude",
                     lon="longitude",
                     hover_name="place",
                     size="magnitude",
                     color="magnitude",
                     projection="natural earth",
                     title="Earthquake Locations")
st.plotly_chart(fig)

# Table
st.subheader("📋 Earthquake Details")
st.dataframe(df_filtered.sort_values("time", ascending=False).reset_index(drop=True))
