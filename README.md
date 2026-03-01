# Flask Blog Demo (MVC)

This is a simple teaching project demonstrating a basic Flask application structured
following the **Model-View-Controller (MVC)** pattern. Posts are stored in a JSON file
and can be created, viewed, edited, and deleted through a web interface.

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/f45e3347-786c-451a-aa35-b8927be24a2a" />

## Structure

```
app.py                    # application factory
models/                   # data layer
  post_model.py           # file-based storage functions
controllers/              # controllers / view handlers
  post_controller.py      # blueprint with routes for posts
templates/                # Jinja2 templates (views)
static/                   # CSS and other static assets
posts.json                # data store
```

## Features

- List all posts
- Create new post (auto-increment ID)
- View a single post
- Edit existing post
- Delete post

## Requirements

The project uses Flask 3.x and standard Python libraries. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running

```bash
# from project root
python app.py
```

The app runs on `http://127.0.0.1:5000` by default. Use the web UI to manage posts.

## Notes

This is for educational use only. The JSON file storage is not suitable for
production use; you may replace it with a database or ORM later. The MVC layout
makes it easier to expand the app by adding new controllers or models.

## License

MIT-style educational sample. You’re free to copy and modify.
