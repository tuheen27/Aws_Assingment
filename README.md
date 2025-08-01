# DevOps Assignment 2 - External Data Fetcher

## Overview
This is a Flask web application created for DevOps Assignment 2. The application fetches data from an external API and displays it through a web interface.

## Features
- Landing page with navigation
- External API data fetching from `http://13.232.73.138:5000/data`
- JSON and raw text response handling
- Error handling for network and API issues
- Responsive web interface

## Technology Stack
- **Backend:** Flask (Python)
- **HTTP Client:** requests library
- **Frontend:** HTML with CSS
- **Template Engine:** Jinja2

## Project Structure
```
├── app.py              # Main Flask application
└── templates/
    ├── index.html      # Landing page
    └── data.html       # Data display page
```

## How to Run
1. Install dependencies:
   ```bash
   pip install flask requests
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open browser and visit: `http://localhost:8000`

## Assignment Requirements
This application demonstrates:
- Flask web framework usage
- External API integration
- Error handling
- Template rendering
- Web application deployment concepts

## Author
Assignment completed for DevOps course 2025-2026
