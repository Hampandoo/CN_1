from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes import router
from app.config import settings

app = FastAPI(title="Gateway")

# Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Дозволяє всі джерела (налаштуй для безпеки)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення роутів
app.include_router(router)

# Глобальна обробка помилок
# @app.exception_handler(Exception)
# async def exception_handler(request, exc):
#     return await handle_error(exc)

# Запуск сервера
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.GATEWAY_PORT)