from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    prediction = random.uniform(50, 100)  # תחזית מספר אקראי בין 50 ל-100
    return jsonify({"prediction": prediction})

@app.route('/metrics', methods=['GET'])
def metrics():
    # פורמט Prometheus Metrics
    prediction = random.uniform(50, 100)
    metric_data = f"# HELP prediction_value Random prediction value\n# TYPE prediction_value gauge\nprediction_value {prediction}"
    return metric_data, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)