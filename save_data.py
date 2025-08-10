import pandas as pd

def save_earthquake_data(dataset, file_path = "earthquakes_all_month.csv"):
    dataset.to_csv(file_path, index=False)
    print(f"Saved {len(dataset)} records to {file_path}")