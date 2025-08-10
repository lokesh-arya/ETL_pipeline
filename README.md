# ETL_pipeline

## Real-Time Earthquake Dashboard

A real-time, interactive dashboard that monitors global earthquakes using the USGS GeoJSON API. Built with **Python**, **Streamlit**, **Requests**, and **Plotly**, this project fetches up-to-date earthquake data and visualizes it on an interactive map.

---

## 📌 Features

- **Live earthquake data** from the USGS (updated hourly)
- **Magnitude filtering** using interactive slider
- **Interactive world map** of earthquake locations
- **Data table** with sortable earthquake details

---

## 🔗 Data Source

- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/)
- API Endpoint: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson`

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/lokesh-arya/ETL_pipeline.git
cd ETL_pipeline
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit App (Dashboard)

```bash
streamlit run app.py
```