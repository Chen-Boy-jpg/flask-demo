from flask import Flask # Import the Flask class from the flask package

app = Flask(**name**) # Create a Flask application instance, **name** represents the current module name

# Define the home route

@app.route("/") # When a user visits "/" (the home page), the function below will be called
def home():  
 return "Hello Flask!" # Return text to the browser

# Start the server

if **name** == "**main**": # Only run the server when this file is executed directly
app.run(debug=True) # Start the Flask server, debug=True enables auto-reload and shows error messages
