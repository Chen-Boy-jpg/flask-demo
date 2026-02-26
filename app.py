from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "這是首頁"

@app.route("/about")
def about():
    return "這是關於頁面"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)