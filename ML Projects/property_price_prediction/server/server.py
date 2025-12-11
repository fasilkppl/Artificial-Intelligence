from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
# returning a response containing all locations
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft']) # requesting and getting variable total_sqft
    location = request.form['location'] # requesting and getting variable location
    bhk = int(request.form['bhk']) # requesting and getting variable location
    bath = int(request.form['bath']) # requesting and getting variable location

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath) #prediction and hot one encoding
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()