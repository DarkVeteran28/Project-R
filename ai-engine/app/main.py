from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Project R AI Engine",
    version="1.0.0"
)


app.include_router(router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "service": "Project R AI Engine",
        "status": "running"
    }