import time
from fetch_data import fetch_earthquake_data
from parse_data import parse_earthquake_data
from save_data import save_earthquake_data

URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

def run_pipeline():
    data = fetch_earthquake_data(URL)
    df = parse_earthquake_data(data)
    save_earthquake_data(df)
    

if __name__ == "__main__":
    while True:
        run_pipeline()
        print("Waiting for next run...")
        time.sleep(3600)