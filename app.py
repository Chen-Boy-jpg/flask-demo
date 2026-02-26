from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "posts.json"


# ----------------------------
# 工具函式：讀取資料
# ----------------------------
def load_posts():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# ----------------------------
# 工具函式：儲存資料
# ----------------------------
def save_posts(posts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)


# ----------------------------
# 首頁 - 文章列表
# ----------------------------
@app.route("/")
def index():
    posts = load_posts()
    return render_template("index.html", posts=posts)


# ----------------------------
# 新增文章
# ----------------------------
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        posts = load_posts()

        # 自動產生 id
        new_id = 1
        if posts:
            new_id = max(post["id"] for post in posts) + 1

        new_post = {
            "id": new_id,
            "title": title,
            "content": content
        }

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for("index"))

    return render_template("create.html")


# ----------------------------
# 查看文章
# ----------------------------
@app.route("/post/<int:post_id>")
def view(post_id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "找不到文章", 404

    return render_template("view.html", post=post)


# ----------------------------
# 編輯文章
# ----------------------------
@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "找不到文章", 404

    if request.method == "POST":
        post["title"] = request.form["title"]
        post["content"] = request.form["content"]

        save_posts(posts)
        return redirect(url_for("index"))

    return render_template("edit.html", post=post)


# ----------------------------
# 刪除文章
# ----------------------------
@app.route("/delete/<int:post_id>")
def delete(post_id):
    posts = load_posts()
    posts = [p for p in posts if p["id"] != post_id]

    save_posts(posts)
    return redirect(url_for("index"))


# ----------------------------
# 主程式
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)