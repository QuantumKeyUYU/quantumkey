import pytest
from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)

def test_create_and_open_immediately_forbidden():
    r = client.post("/timelock/create", json={"message":"foo","unlock_in":2})
    assert r.status_code == 200
    data = r.json()
    # попытка сразу открыть
    r2 = client.get(f"/timelock/open/{data['id']}")
    assert r2.status_code == 403

def test_open_after_delay():
    r = client.post("/timelock/create", json={"message":"bar","unlock_in":1})
    id_ = r.json()["id"]
    time.sleep(1.1)
    r2 = client.get(f"/timelock/open/{id_}")
    assert r2.status_code == 200
    assert r2.json()["message"] == "bar"
