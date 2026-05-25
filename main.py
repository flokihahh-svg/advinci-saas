from fastapi import FastAPI

# نقوم بإنشاء تطبيق FastAPI
app = FastAPI()

# هذا الجزء هو المسؤول عن الواجهة الرئيسية
@app.get("/")
def read_root():
    return {
        "message": "أهلاً بك في موقع Lutam الاحترافي",
        "status": "الموقع يعمل بنجاح",
        "description": "هذا هو مشروعي الأول المرفوع على سيرفر Render"
    }

# صفحة معلومات إضافية
@app.get("/info")
def get_info():
    return {
        "user": "Lutam",
        "location": "Iraq",
        "message": "أنا الآن مبرمج رسمي على الإنترنت!"
    }