from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  # 추가
from app.api.routes import router
import os

app = FastAPI()

# 라우터 연결
app.include_router(router, prefix="/api")

# static 폴더 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

# 메인 페이지
@app.get("/", response_class=HTMLResponse)
def home():
    html_path = os.path.join("templates", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()