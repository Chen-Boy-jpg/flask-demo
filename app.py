from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Daniel",
        age=20,
        hobbies=["Basketball", "Coding", "Music"],
        students=[
            {"name": "Alice", "score": 85},
            {"name": "Bob", "score": 50},
            {"name": "Charlie", "score": 70}
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)