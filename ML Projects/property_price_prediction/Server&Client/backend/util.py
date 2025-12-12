import os
import pickle
import json
import numpy as np
from flask import Flask

app = Flask(__name__)

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    """Run predict method on saved model"""
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

#to handle cases where artifacts might not exist
def load_saved_artifacts():
    """Load JSON file and saved model"""
    print("loading saved artifacts...start")
    
    global __data_columns, __locations, __model
    
    base = os.path.dirname(os.path.abspath(__file__))
    columns_path = os.path.join(base, "artifacts", "columns.json")
    model_path = os.path.join(base, "artifacts", "home_prices_model.pickle")

    # Check if files exist
    if not os.path.exists(columns_path):
        raise FileNotFoundError(f"columns.json not found at {columns_path}")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open(model_path, "rb") as f:
        __model = pickle.load(f)

    print(f"Loaded {len(__locations)} locations")
    print("loading saved artifacts...done")


def get_location_names():
    """Return all locations (skips first 3 columns)"""
    return __locations


def get_data_columns():
    """Return all data columns including first 3"""
    return __data_columns


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(host='0.0.0.0', port=5000)