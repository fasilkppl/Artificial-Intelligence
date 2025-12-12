from flask import Flask, request, jsonify
import util

app = Flask(__name__)


print("Starting Python Flask Server For Home Price Prediction...")
util.load_saved_artifacts()

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    """Return all available locations"""
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    """Predict home price based on input parameters"""
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for container orchestration"""
    return jsonify({'status': 'healthy'})


