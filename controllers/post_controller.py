from flask import Blueprint, render_template, request, redirect, url_for

from models.post_model import load_posts, save_posts

posts_bp = Blueprint("posts", __name__)


@posts_bp.route("/")
def index():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@posts_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        posts = load_posts()

        # generate a new id automatically
        new_id = 1
        if posts:
            new_id = max(post["id"] for post in posts) + 1

        new_post = {"id": new_id, "title": title, "content": content}

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for("posts.index"))

    return render_template("create.html")


@posts_bp.route("/post/<int:post_id>")
def view(post_id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found", 404

    return render_template("view.html", post=post)


@posts_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        post["title"] = request.form["title"]
        post["content"] = request.form["content"]

        save_posts(posts)
        return redirect(url_for("posts.index"))

    return render_template("edit.html", post=post)


@posts_bp.route("/delete/<int:post_id>")
def delete(post_id):
    posts = load_posts()
    posts = [p for p in posts if p["id"] != post_id]

    save_posts(posts)
    return redirect(url_for("posts.index"))
