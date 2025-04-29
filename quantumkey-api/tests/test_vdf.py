import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_vdf_default_delay():
    r = client.get("/vdf/eval", params={"input_data": "abc"})
    assert r.status_code == 200
    assert r.json()["result"] == "proof_of_abc"

def test_vdf_custom_delay(monkeypatch):
    import app.vdf as vdf
    calls = []
    monkeypatch.setattr(vdf, "time", type("T", (), {"sleep": lambda _ : calls.append(True)}))
    r = client.get("/vdf/eval", params={"input_data": "xyz", "delay": 5})
    assert r.status_code == 200
    assert calls, "sleep не был вызван"
    assert r.json()["result"] == "proof_of_xyz"
