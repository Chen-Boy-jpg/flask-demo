from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/")
def home():
    return render_template("index.html", name="Daniel")

if __name__ == "__main__":
    app.run(debug=True)