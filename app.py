from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    posts = [
        {"title": "第一篇文章", "content": "這是第一篇文章內容"},
        {"title": "第二篇文章", "content": "這是第二篇文章內容"},
        {"title": "第三篇文章", "content": "這是第三篇文章內容"},
    ]
    show_ads = True
    return render_template("index.html", posts=posts, show_ads=show_ads)

if __name__ == "__main__":
    app.run(debug=True)