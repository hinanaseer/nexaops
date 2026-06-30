import os
from datetime import datetime

AI_MODE = os.getenv("AI_MODE", "mock")

def detect_drift(terraform_plan: str, resource_type: str, environment: str) -> dict:
    if AI_MODE == "mock":
        return mock_drift_detection(terraform_plan, resource_type, environment)
    else:
        return real_drift_detection(terraform_plan, resource_type, environment)

def mock_drift_detection(terraform_plan: str, resource_type: str, environment: str) -> dict:
    return {
        "environment": environment,
        "resource_type": resource_type,
        "analyzed_at": datetime.utcnow().isoformat(),
        "ai_engine": "Claude (Anthropic)",
        "drift_detected": True,
        "drift_count": 3,
        "severity": "high",
        "drifts": [
            {
                "resource": "aws_instance.web_server",
                "expected": "t3.medium",
                "actual": "t3.large",
                "risk": "Cost overrun — $40/month extra",
                "auto_fix": "terraform apply -target=aws_instance.web_server"
            },
            {
                "resource": "aws_security_group.app_sg",
                "expected": "port 443 only",
                "actual": "port 443, 8080, 22 open",
                "risk": "Security vulnerability — SSH exposed to internet",
                "auto_fix": "terraform apply -target=aws_security_group.app_sg"
            },
            {
                "resource": "aws_s3_bucket.assets",
                "expected": "private",
                "actual": "public-read",
                "risk": "Critical — sensitive data publicly accessible",
                "auto_fix": "terraform apply -target=aws_s3_bucket.assets"
            }
        ],
        "ai_summary": (
            f"Detected 3 infrastructure drifts in {environment} environment. "
            "Most critical: S3 bucket has been made public, exposing sensitive assets. "
            "Immediate remediation required before security audit."
        ),
        "compliance_status": "FAILED",
        "estimated_cost_impact": "+$40/month"
    }

def real_drift_detection(terraform_plan: str, resource_type: str, environment: str) -> dict:
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""You are a senior DevOps engineer. Analyze this Terraform plan output for infrastructure drift.

Environment: {environment}
Resource Type: {resource_type}
Terraform Plan:
{terraform_plan}

Identify all drifts, their severity, risk, and remediation commands. Respond in JSON."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "environment": environment,
        "resource_type": resource_type,
        "analyzed_at": datetime.utcnow().isoformat(),
        "ai_engine": "Claude (Anthropic)",
        "raw_analysis": message.content[0].text
    }
