import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controller import root_controller

app = FastAPI()


# 配置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源，或者指定具体的源，如 ["https://example.com"]
    allow_credentials=True,  # 允许携带凭证（如 cookies）
    allow_methods=["*"],  # 允许所有方法，或者指定具体的方法，如 ["GET", "POST"]
    allow_headers=["*"],  # 允许所有头，或者指定具体的头
)

# 加载路由
app.include_router(root_controller.router)

HOST = "127.0.0.1"
PORT = 8000

if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)
