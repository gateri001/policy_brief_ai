import os
import pandas as pd
from fastapi.testclient import TestClient
from apps.api.main import app

def setup_module(module):
    # Ensure synthetic data exists for the API
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(
        [
            {"feedback": "Citizens demand better healthcare access", "theme": "health"},
            {"feedback": "Youth unemployment is rising", "theme": "jobs"},
            {"feedback": "Security concerns in rural areas", "theme": "security"},
            {"feedback": "Education reforms are welcomed", "theme": "education"},
        ]
    )
    df.to_csv("data/synthetic_feedback.csv", index=False)

def test_health_endpoint():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_brief_endpoint_returns_list():
    client = TestClient(app)
    resp = client.get("/brief")
    assert resp.status_code == 200
    data = resp.json()
    assert "brief" in data
    assert isinstance(data["brief"], list)
    assert len(data["brief"]) >= 1
    # Check formatting: bullet and theme capitalization present
    assert any(item.startswith("- Theme: ") for item in data["brief"])
