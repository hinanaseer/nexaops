from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.diagnosis import router as diagnosis_router
from app.api.drift import router as drift_router
import os

load_dotenv()

app = FastAPI(
    title="NexaOps API",
    description="AI-Powered DevOps Command Center",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(diagnosis_router)
app.include_router(drift_router)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "development")
    }

@app.get("/")
async def root():
    return {
        "project": "NexaOps",
        "description": "AI-Powered DevOps Command Center",
        "docs": "/docs"
    }
