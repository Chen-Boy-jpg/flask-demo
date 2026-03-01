# 03-render-template - Basic render_template Tutorial

## Step 1: Create Project Files

1. Create a folder named `templates`
2. Inside the `templates` folder, create a file named `index.html`

---

## Step 2: app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Pass data to the template
    name = "Daniel"
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Step 3: index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My First Flask Page</title>
  </head>
  <body>
    <h1>Hello {{ name }}</h1>
  </body>
</html>
```
