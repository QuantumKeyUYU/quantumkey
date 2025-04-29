from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_threshold_split_and_combine():
    r1 = client.post("/threshold/split",   json={"shares":3})
    r2 = client.post("/threshold/combine", json={"shares":3})
    assert r1.status_code == 200 and r1.json()["status"] == "ok"
    assert r2.status_code == 200 and r2.json()["status"] == "ok"
