from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes import router
from app.config import settings

app = FastAPI(title="Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# @app.exception_handler(Exception)
# async def exception_handler(request, exc):
#     return await handle_error(exc)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.GATEWAY_PORT)
