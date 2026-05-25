from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    # هذا الكود سيقرأ ملف index.html من مجلد templates ويظهره
    file_path = "templates/index.html"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "<h1>ملف index.html غير موجود، تأكد من رفعه داخل مجلد templates</h1>"