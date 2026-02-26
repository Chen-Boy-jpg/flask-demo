# 03-render-template - render_template 基礎教學

## 步驟 1：建立專案檔案

1. 建立 `templates` 資料夾
2. 在 `templates` 裡建立 `index.html`

---

## 步驟 2：app.py 

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # 將資料傳到模板
    name = "Daniel"
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
```
## 步驟 3：index.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>我的第一個 Flask 頁面</title>
</head>
<body>
    <h1>Hello {{ name }}</h1>
</body>
</html>
```
