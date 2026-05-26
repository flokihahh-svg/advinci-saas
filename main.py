from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# تعريف مكان ملفات التصميم
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
