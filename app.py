from flask import Flask, render_template, jsonify
import json
import os

# Create Flask application
app = Flask(__name__)

# Home route - serves your HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to serve data from JSON file
@app.route('/api/data')
def get_data():
    try:
        # Load data from data.json file
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({'error': 'Data file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get users only
@app.route('/api/users')
def get_users():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data.get('users', []))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get products only
@app.route('/api/products')
def get_products():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data.get('products', []))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# About route
@app.route('/about')
def about():
    return """
    <html>
    <head>
        <title>About</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
                color: #333;
                text-align: center;
                padding: 50px;
            }
        </style>
    </head>
    <body>
        <h1>About This Application</h1>
        <p>This is a simple Flask web application that serves HTML pages and JSON data.</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """

# Health check route
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Flask application is running',
        'version': '1.0.0'
    })

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return """
    <html>
    <head>
        <title>404 - Not Found</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
                color: #333;
                text-align: center;
                padding: 50px;
            }
        </style>
    </head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The page you are looking for does not exist.</p>
        <a href="/">Go to Home</a>
    </body>
    </html>
    """, 404

if __name__ == '__main__':
    print("=" * 50)
    print(" Starting Flask Application")
    print(" Home page: http://localhost:5000")
    print(" API data: http://localhost:5000/api/data")
    print(" Users API: http://localhost:5000/api/users")
    print(" Products API: http://localhost:5000/api/products")
    print("ℹ  About page: http://localhost:5000/about")
    print("=" * 50)
    
    app.run(debug=True, host='localhost', port=5000)