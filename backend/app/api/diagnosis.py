from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.diagnosis_service import analyze_failure

router = APIRouter(prefix="/api/v1", tags=["AI Diagnosis"])

class DiagnosisRequest(BaseModel):
    pod_name: str
    namespace: str
    logs: str

class DiagnosisResponse(BaseModel):
    pod_name: str
    namespace: str
    analyzed_at: str
    ai_engine: str
    root_cause: str
    severity: str
    confidence: str
    explanation: str
    remediation_steps: list
    estimated_resolution_time: str

@router.post("/diagnose", response_model=DiagnosisResponse)
async def diagnose_failure(request: DiagnosisRequest):
    if not request.logs.strip():
        raise HTTPException(status_code=400, detail="Logs cannot be empty")
    
    if not request.pod_name.strip():
        raise HTTPException(status_code=400, detail="Pod name is required")
    
    result = analyze_failure(
        logs=request.logs,
        pod_name=request.pod_name,
        namespace=request.namespace
    )
    return result
