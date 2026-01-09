from fastapi.testclient import TestClient
from apps.api.main import app

def test_recommendations_endpoint():
    client = TestClient(app)
    resp = client.get("/recommendations")
    assert resp.status_code == 200
    data = resp.json()
    assert "recommendations" in data
    recs = data["recommendations"]
    assert isinstance(recs, list)
    assert len(recs) >= 3
    # Basic content sanity
    assert any("health" in r.lower() or "education" in r.lower() or "security" in r.lower() for r in recs)
