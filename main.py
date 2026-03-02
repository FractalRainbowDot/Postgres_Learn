import uvicorn
from fastapi import FastAPI
from infrastructure.database.setup import engine
from infrastructure.database.models import create_tables
from presentation.routers import router

app = FastAPI(
    title="User Management API",
    description="API для управления пользователями с использованием Чистой Архитектуры",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """
    Событие, которое выполняется при запуске приложения.
    Здесь мы создаем таблицы в базе данных.
    """
    await create_tables(engine)

if __name__ == "__main__":
    # Запускаем сервер uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
