import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_vdf_default_delay():
    resp = client.get("/vdf/eval", params={"input_data": "abc"})
    assert resp.status_code == 200
    assert resp.json()["result"] == "proof_of_abc"

def test_vdf_custom_delay(monkeypatch):
    import app.vdf as vdf
    # заменяем sleep, чтобы тест шёл быстро
    monkeypatch.setattr(vdf, "time", type("T", (), {"sleep": lambda x: None}))
    resp = client.get("/vdf/eval", params={"input_data": "xyz", "delay": 10})
    assert resp.json()["result"] == "proof_of_xyz"
