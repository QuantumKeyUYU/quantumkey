from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_threshold_create():
    r = client.post("/threshold/create", json={})
    assert r.status_code == 200
    assert r.json() == {"vault_id": "threshold_vault_stub"}
