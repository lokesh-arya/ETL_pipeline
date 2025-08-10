import pandas as pd

def parse_earthquake_data(data):
    features = data['features']
    
    records = []
    for item in features:
        props = item['properties']
        coords = item['geometry']['coordinates']
        records.append({
            'time': pd.to_datetime(props['time'], unit='ms'),
            'place': props['place'],
            'magnitude': props['mag'],
            'longitude': coords[0],
            'latitude': coords[1],
            'depth': coords[2],
            'url': props['url']
        })
    
    df = pd.DataFrame(records)
    return df
