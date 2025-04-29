# quantumkey-api/tests/test_timelock.py
import time
import pytest
from starlette.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_and_open_immediately_forbidden(client):
    # создаём таймлок на 2 секунды
    r1 = client.post("/timelock/create", json={"message": "foo", "unlock_in": 2})
    assert r1.status_code == 200
    lock_id = r1.json()["id"]

    # сразу открыть нельзя → 403
    r2 = client.get(f"/timelock/open/{lock_id}")
    assert r2.status_code == 403

def test_open_after_delay(client):
    # создаём таймлок на 1 секунду
    r1 = client.post("/timelock/create", json={"message": "bar", "unlock_in": 1})
    assert r1.status_code == 200
    lock_id = r1.json()["id"]

    # ждём чуть больше секунды
    time.sleep(1.1)

    # теперь открывается успешно
    r2 = client.get(f"/timelock/open/{lock_id}")
    assert r2.status_code == 200
    assert r2.json()["message"] == "bar"
