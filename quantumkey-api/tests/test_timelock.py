from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_open_immediately_forbidden():
    r = client.post("/timelock/create", json={"message":"foo","unlock_in":2})
    assert r.status_code == 403
