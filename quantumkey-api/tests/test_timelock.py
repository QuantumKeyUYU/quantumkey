import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_open_immediately_forbidden():
    r = client.post("/timelock/create", json={"message": "foo", "unlock_in": 1})
    assert r.status_code == 200
    id_ = r.json()["id"]

    r2 = client.get(f"/timelock/open/{id_}")
    assert r2.status_code == 403

def test_open_after_delay_zero_unlock():
    # если unlock_in=0 — сразу открываем
    r = client.post("/timelock/create", json={"message": "bar", "unlock_in": 0})
    assert r.status_code == 200
    id_ = r.json()["id"]

    r2 = client.get(f"/timelock/open/{id_}")
    assert r2.status_code == 200
    assert r2.json() == {"message": "bar", "unlock_in": 0}
