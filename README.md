# Flask Web Application with Docker

A simple Flask web application that serves dynamic content with JavaScript interaction.

## Features

- Flask backend serving HTML templates
- Dynamic content updates with JavaScript
- Docker containerization for easy deployment

## Quick Start

### Running with Docker

1. Build the Docker image:
   ```
   docker build -t flask-app .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 flask-app
   ```

3. Access the application at http://localhost:5000

### Running Locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Access the application at http://localhost:5000

## Project Structure

- `app.py`: Main Flask application
- `templates/index.html`: HTML template
- `static/app.js`: JavaScript for dynamic content
- `Dockerfile`: Container configuration
- `requirements.txt`: Python dependencies
