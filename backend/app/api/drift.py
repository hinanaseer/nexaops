from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.drift_service import detect_drift

router = APIRouter(prefix="/api/v1", tags=["Drift Detection"])

class DriftRequest(BaseModel):
    terraform_plan: str
    resource_type: str
    environment: str

@router.post("/drift/detect")
async def detect_infrastructure_drift(request: DriftRequest):
    if not request.terraform_plan.strip():
        raise HTTPException(status_code=400, detail="Terraform plan cannot be empty")
    
    result = detect_drift(
        terraform_plan=request.terraform_plan,
        resource_type=request.resource_type,
        environment=request.environment
    )
    return result
