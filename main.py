from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# هذا السطر يبحث عن مجلد اسمه templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    # هذا السطر يفتح index.html الموجود داخل المجلد
    return templates.TemplateResponse("index.html", {"request": request})
