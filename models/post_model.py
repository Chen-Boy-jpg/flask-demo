import json
import os

DATA_FILE = "posts.json"


def load_posts():
    """Read the list of posts from disk.

    Returns:
        list: A list of dictionaries representing blog posts.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_posts(posts):
    """Write the list of posts back to disk.

    Args:
        posts (list): A list of dictionaries representing blog posts.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)
