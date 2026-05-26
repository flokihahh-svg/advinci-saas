from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# هذا السطر يحدد أن تصاميمك موجودة في مجلد اسمه templates
templates = Jinja2Templates(directory="templates")

# هذا السطر يخبر السيرفر أين يجد ملفاتك (مثل الصور أو الـ CSS إذا كان عندك)
# إذا لم يكن عندك ملفات CSS، يمكنك حذف هذا السطر
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request: Request):
    # هنا نقول للسيرفر: عندما يفتح المستخدم الصفحة الرئيسية، اعرض له ملف index.html
    return templates.TemplateResponse("index.html", {"request": request})