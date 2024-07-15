from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow requests from your frontend

@app.route('/')
def home():
    return "Myntra Model API"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    category = data['category']
    budget = data['budget']
    # Add your filtering and model prediction logic here
    recommendations = get_recommendations(category, budget)
    return jsonify(recommendations)

def get_recommendations(category, budget):
    # Placeholder for filtering logic
    # Example:
    # filtered_products = [product for product in all_products if product['category'] == category and product['price'] <= budget]
    # recommendations = model.predict(filtered_products)  # Replace with actual prediction logic
    return [
        {'name': 'Sample Product 1', 'price': 1999, 'rating': 4.5, 'brand': 'Brand A', 'image': 'https://via.placeholder.com/150'},
        {'name': 'Sample Product 2', 'price': 2999, 'rating': 4.6, 'brand': 'Brand B', 'image': 'https://via.placeholder.com/150'},
        {'name': 'Sample Product 3', 'price': 3999, 'rating': 4.7, 'brand': 'Brand C', 'image': 'https://via.placeholder.com/150'},
        {'name': 'Sample Product 4', 'price': 4999, 'rating': 4.8, 'brand': 'Brand D', 'image': 'https://via.placeholder.com/150'}
    ]

if __name__ == '__main__':
    app.run(debug=True)