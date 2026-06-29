import os
from datetime import datetime

AI_MODE = os.getenv("AI_MODE", "mock")

def analyze_failure(logs: str, pod_name: str, namespace: str) -> dict:
    if AI_MODE == "mock":
        return mock_diagnosis(logs, pod_name, namespace)
    else:
        return real_diagnosis(logs, pod_name, namespace)

def mock_diagnosis(logs: str, pod_name: str, namespace: str) -> dict:
    return {
        "pod_name": pod_name,
        "namespace": namespace,
        "analyzed_at": datetime.utcnow().isoformat(),
        "ai_engine": "Claude (Anthropic)",
        "root_cause": "OOMKilled - Container exceeded memory limit of 512Mi",
        "severity": "critical",
        "confidence": "94%",
        "explanation": (
            f"Pod '{pod_name}' in namespace '{namespace}' was killed by the "
            "kernel due to out-of-memory condition. The container attempted to "
            "allocate more memory than the configured limit."
        ),
        "remediation_steps": [
            "Increase memory limit in deployment manifest to 1Gi",
            "Add memory request of 256Mi for proper scheduling",
            "Investigate application memory leak using heap profiler",
            "Consider horizontal scaling instead of vertical scaling",
            "Add memory usage alert at 80% threshold in Prometheus"
        ],
        "affected_resources": {
            "deployment": pod_name.rsplit("-", 2)[0],
            "namespace": namespace,
            "node": "ip-10-0-1-45.eu-west-1.compute.internal"
        },
        "estimated_resolution_time": "15 minutes"
    }

def real_diagnosis(logs: str, pod_name: str, namespace: str) -> dict:
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    prompt = f"""You are an expert DevOps engineer. Analyze these Kubernetes pod logs and provide diagnosis.

Pod: {pod_name}
Namespace: {namespace}
Logs:
{logs}

Respond with JSON containing: root_cause, severity, explanation, remediation_steps (list), estimated_resolution_time."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return {
        "pod_name": pod_name,
        "namespace": namespace,
        "analyzed_at": datetime.utcnow().isoformat(),
        "ai_engine": "Claude (Anthropic)",
        "raw_analysis": message.content[0].text
    }
