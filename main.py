from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# المسار المطلق لضمان عمل المجلدات
BASE_DIR = os.path.dirname(os.path.abspath(file))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
