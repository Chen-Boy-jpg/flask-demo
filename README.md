# 02-flask-route - Flask Route 教學

## 新增多個路由

```python
from flask import Flask

app = Flask(__name__)

# 首頁
@app.route("/")
def home():
    return "這是首頁"

# 關於頁
@app.route("/about")
def about():
    return "這是關於頁面"

# 動態路由
@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)

