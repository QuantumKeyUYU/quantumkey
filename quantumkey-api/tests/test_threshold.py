from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_threshold_split_and_combine():
    r = client.post("/threshold/split", json={"message":"hello","n":3,"k":2})
    assert r.status_code == 200
    shares = r.json()["shares"]
    assert isinstance(shares, list) and len(shares)==3

    r2 = client.post("/threshold/combine", json={"shares": shares[:2]})
    assert r2.status_code == 200
    assert r2.json()["message"] == "hello"
