# quantumkey-api/tests/test_pq_signature.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pq_sign_and_verify_stub():
    # 1) вызываем /pq/sign
    r1 = client.post("/pq/sign", json={"message": "hello"})
    assert r1.status_code == 200
    body1 = r1.json()
    assert body1["signature"]    == "falcon_sig_hello"
    assert body1["phase_proof"]  == "proof_of_hello"

    # 2) вызываем /pq/verify
    payload = {
        "message":     "hello",
        "signature":   body1["signature"],
        "phase_proof": body1["phase_proof"],
    }
    r2 = client.post("/pq/verify", json=payload)
    assert r2.status_code == 200
    body2 = r2.json()
    assert body2["valid"] is True
