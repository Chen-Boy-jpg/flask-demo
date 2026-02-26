# 03-render-template - render_template 基礎教學

## 步驟 1：建立專案檔案
1. 建立資料夾 `03-render-template`
2. 在資料夾內建立 `app.py`
3. 建立 `templates` 資料夾
4. 在 `templates` 裡建立 `index.html`

---

## 步驟 2：app.py 範例程式

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
