from flask import Flask, render_template, jsonify

# Create Flask application
app = Flask(__name__)

# Home route - serves the index HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Data route - returns JSON data
@app.route('/data')
def get_data():
    sample_data = {
        "users": [
            {
                "id": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "age": 28,
                "city": "New York"
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "jane@example.com",
                "age": 25,
                "city": "Los Angeles"
            },
            {
                "id": 3,
                "name": "Mike Johnson",
                "email": "mike@example.com",
                "age": 32,
                "city": "Chicago"
            }
        ],
        "products": [
            {
                "id": 101,
                "name": "Laptop",
                "price": 999.99,
                "category": "Electronics"
            },
            {
                "id": 102,
                "name": "Phone",
                "price": 599.99,
                "category": "Electronics"
            },
            {
                "id": 103,
                "name": "Book",
                "price": 19.99,
                "category": "Education"
            }
        ],
        "status": "success",
        "message": "Data retrieved successfully"
    }
    
    return jsonify(sample_data)

if __name__ == '__main__':
    print("Starting Simple Flask Application...")
    print("Home page: http://localhost:5000")
    print("Data API: http://localhost:5000/data")
    app.run(debug=True, host='localhost', port=5000)
