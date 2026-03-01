from flask import Flask

from controllers.post_controller import posts_bp


def create_app():
    """Application factory for the Flask blog demo."""

    app = Flask(__name__)
    app.register_blueprint(posts_bp)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
