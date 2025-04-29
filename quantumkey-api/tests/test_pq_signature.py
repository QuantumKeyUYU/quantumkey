# quantumkey-api/tests/test_pq_signature.py
import pytest
from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_pq_sign_and_verify_stub():
    # stub-логика пока просто отдаёт заглушку подписи/доказательства
    message = "hello"
    r1 = client.post("/pq/sign", json={"message": message})
    assert r1.status_code == 200
    body1 = r1.json()
    assert "falcon_sig" in body1 and "phase_proof" in body1

    # проверка stub — любая подпись проходит
    r2 = client.post("/pq/verify", json={
        "message": message,
        "signature": body1["falcon_sig"],
        "phase_proof": body1["phase_proof"]
    })
    assert r2.status_code == 200
    assert r2.json().get("valid") is True
