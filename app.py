# app.py - Flask application to serve the Market Analysis Dashboard

# Import Flask and jsonify for creating the API
from flask import Flask, render_template, jsonify

# Initialize Flask application
app = Flask(__name__)

# --- Routes for serving the dashboard and API endpoints ---

# Route to serve the main dashboard page (index.html) at the root URL ("/")
@app.route("/")
def index():
    """
    Route for the main dashboard page.
    Renders the index.html template from the /templates folder.
    """
    return render_template('index.html')

# API endpoint for market share data (/api/marketShare)
@app.route("/api/marketShare")
def get_market_share():
    """
    API endpoint to serve market share data.
    Reads data from data/marketShare.json and returns it as JSON.
    """
    try:
        with open('data/marketShare.json', 'r') as f:
            market_share_data = f.read()
            import json
            return jsonify(json.loads(market_share_data)) # Use jsonify to properly format JSON response
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # Return error if file is not found

# API endpoint for revenue trends data (/api/revenueTrends)
@app.route("/api/revenueTrends")
def get_revenue_trends():
    """
    API endpoint to serve revenue trends data.
    Reads data from data/revenueTrends.json and returns it as JSON.
    """
    try:
        with open('data/revenueTrends.json', 'r') as f:
            revenue_trends_data = f.read()
            import json
            return jsonify(json.loads(revenue_trends_data)) # Use jsonify to properly format JSON response
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # Return error if file is not found

# API endpoint for market segmentation data (/api/marketSegmentation)
@app.route("/api/marketSegmentation")
def get_market_segmentation():
    """
    API endpoint to serve market segmentation data.
    Reads data from data/marketSegmentation.json and returns it as JSON.
    """
    try:
        with open('data/marketSegmentation.json', 'r') as f:
            market_segmentation_data = f.read()
            import json
            return jsonify(json.loads(market_segmentation_data)) # Use jsonify to properly format JSON response
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404 # Return error if file is not found

# --- Serving static files (if needed) ---
# In this case, static files like CSS, images, or additional JavaScript files
# would be placed in the 'static' folder. Flask automatically serves files
# from the 'static' folder at the '/static' URL path.
# Example: To access a file named 'styles.css' in the 'static' folder,
# you would use '/static/styles.css' in your HTML.
# No explicit route configuration is needed for serving static files from 'static' folder.

# --- Run the Flask application ---
if __name__ == '__main__':
    app.run(debug=True) # Set debug=True for development to enable auto-reloading

# --- Recommended Repository Structure ---
'''
Recommended Repository Structure for the Market Analysis Dashboard project:

market-analysis-dashboard/  (Root directory of the repository)
├── app.py                  (Flask application file)
├── templates/              (Folder for HTML templates)
│   └── index.html          (Main dashboard HTML file)
├── data/                   (Folder for JSON data files)
│   ├── marketShare.json
│   ├── revenueTrends.json
│   └── marketSegmentation.json
├── static/                 (Folder for static assets - CSS, images, etc. - currently empty)
├── README.md               (Optional: Project description and setup instructions)
└── requirements.txt        (Optional: List of Python dependencies if any - for this project, it would be Flask)

This structure keeps the project organized with clear separation of concerns:
- app.py: Contains the backend Flask application logic.
- templates: Holds the frontend HTML templates.
- data: Stores the data used by the application.
- static: For any static files needed by the frontend.
- README.md & requirements.txt: Standard files for project documentation and dependency management.

This structure is well-suited for a single GitHub repository as it is clean, maintainable, and follows common web application project conventions.
'''
