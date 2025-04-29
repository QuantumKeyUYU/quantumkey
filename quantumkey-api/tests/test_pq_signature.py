from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pq_sign_and_verify_stub():
    message = "hello"
    # sign
    r1 = client.post("/pq/sign", json={"message": message})
    assert r1.status_code == 200
    body1 = r1.json()
    assert "falcon_sig_stub" in body1["signature"]
    assert "phase_proof_stub" in body1["phase_proof"]

    # verify
    r2 = client.post("/pq/verify", json={
        "message": message,
        "signature": body1["signature"]
    })
    assert r2.status_code == 200
    assert r2.json() == {"valid": True}
