from flask import Flask, render_template

"""
This script demonstrates a basic Flask web application with the use of HTML templates.
Flask is a lightweight WSGI (Web Server Gateway Interface) web framework for building web applications.
"""

# Create an instance of the Flask class, which represents our web application.
app = Flask(__name__)

@app.route("/")
def welcome():
    """
    The root route of the application.
    Displays a welcome message directly in the browser as raw HTML.

    Returns:
        str: A simple HTML welcome message.
    """
    return "<html><h1>Welcome to the Flask Framework!</h1></html>"

@app.route("/index")
def index():
    """
    The Index route of the application.
    Renders the `index.html` template.

    Returns:
        str: Rendered HTML content of the `index.html` file.
    """
    return render_template('index.html')

@app.route("/about")
def about():
    """
    The About route of the application.
    Renders the `about.html` template.

    Returns:
        str: Rendered HTML content of the `about.html` file.
    """
    return render_template('about.html')

if __name__ == "__main__":
    """
    The entry point of the Python script.
    Starts the Flask development server in debug mode, which allows for real-time error feedback and auto-reloading.
    """
    app.run(debug=True)
