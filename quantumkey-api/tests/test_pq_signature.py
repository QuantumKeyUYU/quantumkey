from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pq_sign_and_verify_stub():
    r1 = client.post("/pq/sign", json={"message":"hello"})
    assert r1.status_code == 200
    body = r1.json()
    assert body["signature"]   == "falcon_sig_hello"
    assert body["phase_proof"] == "phase_proof_hello"

    r2 = client.post("/pq/verify", json={
        "signature":   body["signature"],
        "phase_proof": body["phase_proof"],
        "message":     "hello"
    })
    assert r2.status_code == 200
    assert r2.json()["valid"] is True
