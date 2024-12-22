from flask import Flask

"""
This script demonstrates a simple Flask web application. 
Flask is a lightweight WSGI (Web Server Gateway Interface) web application framework in Python. 
It allows developers to build web applications quickly and easily.
"""

# Create an instance of the Flask class.
# This instance will act as the central object of our Flask application.
app = Flask(__name__)

@app.route("/")
def welcome():
    """
    The root route of the application.
    This function handles requests to the root URL ("/").
    
    Returns:
        str: A welcome message for the Flask application.
    """
    return "Welcome to the Flask Framework!"

@app.route("/about")
def about():
    """
    A route for the About page.
    This function provides information about the application.

    Returns:
        str: Information about the purpose of the application.
    """
    return "This is a demo Flask application to understand routing and basic functionality."

@app.route("/services")
def services():
    """
    A route for the Services page.
    This function describes the services provided by the application.

    Returns:
        str: A list of services or features of the application.
    """
    return "I work on web development, data analysis, and machine learning solutions."

@app.route("/contact")
def contact():
    """
    A route for the Contact page.
    This function provides contact information for the application.

    Returns:
        str: A message with contact details.
    """
    return "Contact me at ravirohith135@gmail.com or call us at +123-456-7890."

@app.route("/index")
def index():
    """
    A route for the Index page.
    This function acts as a landing page for additional content.

    Returns:
        str: A welcome message for the Index page.
    """
    return "Welcome to the Index Page! Navigate through the other pages to learn more."

if __name__ == "__main__":
    """
    The entry point of the application.
    When this script is executed, the Flask application will start a development server.
    
    Debug mode is enabled to allow real-time feedback during development.
    """
    app.run(debug=True)
