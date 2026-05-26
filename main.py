from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# المجلد هنا اسمه "templates" (حروف صغيرة)
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    # الملف هنا اسمه "index.html" (حروف صغيرة)
    return templates.TemplateResponse("index.html", {"request": request})
