from fastapi import FastAPI
from routes.users_routes import router as users_router

app = FastAPI(title="MC - Mi Comunidad (Simple)")

app.include_router(users_router, prefix="/usuarios", tags=["usuarios"])

@app.get("/health")
def health():
    return {"status": "ok"}
