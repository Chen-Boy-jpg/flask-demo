# 04-jinja2 - Jinja2 語法教學

## 步驟 1：建立專案檔案
1. 建立資料夾 `04-jinja2`
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
    posts = [
        {"title": "第一篇文章", "content": "這是第一篇文章內容"},
        {"title": "第二篇文章", "content": "這是第二篇文章內容"},
        {"title": "第三篇文章", "content": "這是第三篇文章內容"},
    ]
    show_ads = True
    return render_template("index.html", posts=posts, show_ads=show_ads)

if __name__ == "__main__":
    app.run(debug=True)
```

## 說明
- `render_template("index.html", posts=posts, show_ads=show_ads)`  
  → 將 Python 變數傳給 HTML 模板
- `posts` 是文章列表
- `show_ads` 控制是否顯示廣告區塊

---

## 步驟 3：templates/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask + Jinja2 教學</title>
</head>
<body>
    <h1>文章列表</h1>

    <!-- if 條件判斷 -->
    {% if show_ads %}
        <div style="color: red;">這裡可以放廣告區塊</div>
    {% endif %}

    <ul>
        <!-- for 迴圈 -->
        {% for post in posts %}
            <li>
                <h3>{{ post.title }}</h3>
                <p>{{ post.content }}</p>
            </li>
        {% endfor %}
    </ul>

    <!-- if else 範例 -->
    {% if posts|length == 0 %}
        <p>目前沒有文章 😢</p>
    {% else %}
        <p>總共有 {{ posts|length }} 篇文章 📝</p>
    {% endif %}
</body>
</html>
```


## 步驟 4：Jinja2 語法說明表

| 語法       | 範例                                           | 功能                                      |
|-----------|----------------------------------------------|-----------------------------------------|
| 變數輸出    | `{{ variable }}`                               | 顯示 Python 傳入模板的變數                 |
| if 條件    | `{% if condition %} ... {% endif %}`          | 判斷條件，執行區塊內容                     |
| if else   | `{% if condition %} ... {% else %} ... {% endif %}` | 條件分支，二選一執行                        |
| for 迴圈   | `{% for item in list %} ... {% endfor %}`     | 遍歷列表、字典等                            |
| filter    | `{{ list|length }}`                           | 運用 filter 處理資料，例如計算列表長度       |
| 註解       | `{# 這是註解 #}`                              | 模板內部註解，不會出現在 HTML               |

---

## 步驟 5：執行專案

1. 在專案資料夾打開終端機 / 命令提示字元  
2. 執行：

```bash
python app.py

