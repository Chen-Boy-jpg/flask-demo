# Introduction to Jinja2 Templates in Flask

Jinja2 is a **templating engine** for Python web frameworks like Flask.  
It allows you to **generate HTML dynamically** by embedding Python-like expressions and logic directly in your HTML files.

With Jinja2, you can:

- Insert dynamic content (variables) into HTML
- Use conditional statements (`if`, `else`) to control output
- Loop over data structures (`for`) to generate repeated HTML elements
- Apply **filters** to format or transform data

---

# 1️ Jinja2 Syntax Basics

## Variables

Use double curly braces `{{ }}` to insert the value of a variable.

Example:

```
{{ name }}
```

- Displays the value of the variable `name` passed from Flask.

---

## Conditional Statements

Use `{% if %}`, `{% elif %}`, `{% else %}` to control what is rendered based on conditions.

Example:

```
{% if age >= 18 %}
    Adult
{% else %}
    Minor
{% endif %}
```

- If `age` is 18 or older, displays "Adult"; otherwise, displays "Minor".

---

## Loops

Use `{% for item in list %} ... {% endfor %}` to iterate over a list or collection.

Example:

```
{% for hobby in hobbies %}
    {{ hobby }}
{% endfor %}
```

- Displays each hobby in the `hobbies` list.

---

## Accessing Dictionary or Object Properties

If you pass a dictionary or object, you can access keys or attributes:

Example:

```
{{ student.name }}
{{ student.score }}
```

- `student` could be `{"name": "Alice", "score": 85}`

---

# 2️ Putting it Together in Flask

After learning Jinja2 syntax, you can use it in your Flask app:

1. Pass data from Flask to the template using `render_template()`.
2. Use Jinja2 syntax in the HTML file to display dynamic content.

---

# 3️ Flask app.py Example

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Pass data to the template
    name = "Daniel"
    age = 20
    hobbies = ["Basketball", "Coding", "Music"]
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 50},
        {"name": "Charlie", "score": 70}
    ]

    return render_template(
        "index.html",
        name=name,
        age=age,
        hobbies=hobbies,
        students=students
    )

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 4️ index.html Example (Jinja2 Template)

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Flask Page</title>
</head>
<body>

    <!-- Basic Variable -->
    <h1>Hello {{ name }}</h1>

    <hr>

    <!-- Display a Number -->
    <h2>Age: {{ age }}</h2>

    <hr>

    <!-- Conditional Statement (if) -->
    {% if age >= 18 %}
        <p>You are an adult.</p>
    {% else %}
        <p>You are under 18.</p>
    {% endif %}

    <hr>

    <!-- Loop (for) -->
    <h2>Hobbies:</h2>
    <ul>
        {% for hobby in hobbies %}
            <li>{{ hobby }}</li>
        {% endfor %}
    </ul>

    <hr>

    <!-- Loop + Condition -->
    <h2>Students:</h2>
    <ul>
        {% for student in students %}
            <li>
                {{ student.name }} - 
                {% if student.score >= 60 %}
                    Pass
                {% else %}
                    Fail
                {% endif %}
            </li>
        {% endfor %}
    </ul>

    <hr>


</body>
</html>
```

---

