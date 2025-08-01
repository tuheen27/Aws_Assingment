from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    """Landing page with a link to fetch data."""
    return render_template('index.html')

@app.route('/fetch-data')
def fetch_data():
    """Fetch data from the external API and display it."""
    try:
        # Make request to the specified IP address
        response = requests.get('http://13.232.73.138:5000/data')
        
        # Check if the request was successful
        if response.status_code == 200:
            # Try to parse as JSON first
            try:
                data = response.json()
            except:
                # If not JSON, use text content
                data = {"raw_content": response.text}
                
            return render_template('data.html', data=data)
        else:
            error_message = f"Failed to fetch data. Status code: {response.status_code}"
            return render_template('data.html', error=error_message)
            
    except requests.RequestException as e:
        error_message = f"Error connecting to the server: {str(e)}"
        return render_template('data.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)