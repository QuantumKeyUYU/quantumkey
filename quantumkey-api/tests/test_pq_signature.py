from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pq_sign_and_verify_stub():
    r = client.post("/pq/sign", json={"message":"hello"})
    assert r.status_code == 200
    body = r.json()
    assert "falcon_sig_stub" in body["signature"]
    assert "falcon_sig_stub" in body["phase_proof"]
