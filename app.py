from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

# Load the K-means model
model_path = os.path.join(os.path.dirname(__file__), 'model', 'Kmeans.pkl')

with open(model_path, 'rb') as f:
    kmeans_model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features from the request
        # Using only amount as the model expects 1 feature
        features = [float(data.get('amount', 0))]
        
        # Convert to numpy array and reshape
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction using K-means
        cluster = kmeans_model.predict(features_array)[0]
        distance = kmeans_model.transform(features_array)[0].min()
        
        return jsonify({
            'success': True,
            'cluster': int(cluster),
            'distance': float(distance),
            'message': f'Transaction classified as Cluster {cluster}'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/model-info', methods=['GET'])
def model_info():
    try:
        info = {
            'n_clusters': int(kmeans_model.n_clusters),
            'n_features': int(kmeans_model.n_features_in_),
            'inertia': float(kmeans_model.inertia_),
            'model_loaded': True
        }
        return jsonify(info)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)