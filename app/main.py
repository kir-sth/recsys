from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.config import settings
from app.recommendations.router import router as recommendation_router


app = FastAPI()
app.include_router(recommendation_router)
add_pagination(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app=app,
        host=settings.FASTAPI_HOST,
        port=settings.FASTAPI_PORT,
        reload=True,
    )
