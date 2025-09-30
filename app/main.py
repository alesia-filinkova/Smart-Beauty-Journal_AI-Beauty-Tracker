from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Skin & Health Tracker API")

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
# app.include_router(health.router)
# app.include_router(stats.router, prefix="/stats", tags=["stats"])
# app.include_router(progress.router, prefix="/progress", tags=["progress"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Skin & Health Tracker API"}
