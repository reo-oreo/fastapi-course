from fastapi import FastAPI
from core.config import settings

#インスタンス化
app=FastAPI(title=settings.PROJECT_TITLE,varsion=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return {"detail":"hello world!"}
