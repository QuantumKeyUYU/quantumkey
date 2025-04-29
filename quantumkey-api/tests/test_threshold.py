from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_threshold_split_and_combine():
    r = client.post("/threshold/split", json={"message": "hello", "n": 5, "k": 3})
    assert r.status_code == 200
    data = r.json()
    assert "shares" in data

    r = client.post("/threshold/combine", json={"shares": data["shares"]})
    assert r.status_code == 200
    data = r.json()
    assert "combined_message" in data
