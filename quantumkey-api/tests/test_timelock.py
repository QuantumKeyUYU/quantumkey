from fastapi.testclient import TestClient
from app.main import app
import app.timelock as tm

client = TestClient(app)

def test_create_and_forbidden():
    r = client.post("/timelock/create", json={"message":"foo","unlock_in":5})
    assert r.status_code == 200
    lock_id = r.json()["id"]
    r2 = client.get(f"/timelock/open/{lock_id}")
    assert r2.status_code == 403

def test_create_and_open_after(monkeypatch):
    # принудительно откроем сразу
    monkeypatch.setattr(tm, "time", lambda: 0)
    r = client.post("/timelock/create", json={"message":"bar","unlock_in":0})
    lock_id = r.json()["id"]
    r2 = client.get(f"/timelock/open/{lock_id}")
    assert r2.status_code == 200
    assert r2.json()["message"] == "bar"
