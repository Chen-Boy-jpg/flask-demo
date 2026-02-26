# Flask 專案快速啟動

這份指南說明如何快速啟動本專案，包含建立 Conda 環境、安裝套件，以及啟動 Flask 伺服器。

---

## 步驟 1：建立 Conda 環境

在終端機或命令提示字元輸入以下指令，建立新的 Conda 環境（例如命名為 `flask_env`）：

```bash
conda create -n flask_env python=3.10 -y
```

## 步驟 2：安裝專案需求套件

確認專案資料夾內有 `requirements.txt`，然後在終端機或命令提示字元輸入：

```bash
pip install -r requirements.txt
```
## 步驟 3：啟動 Flask 專案

在專案根目錄打開終端機或命令提示字元，執行以下指令啟動 Flask 伺服器：

```bash
python app.py
```
## 步驟 4：開啟瀏覽器

啟動 Flask 伺服器後，打開瀏覽器並輸入以下網址：

```text
http://127.0.0.1:5000
```
