import pytest
from fastapi.testclient import TestClient
from app.main import app
import app.vdf as vdf_module

client = TestClient(app)

def test_vdf_default_delay():
    r = client.get("/vdf/eval", params={"input_data": "abc"})
    assert r.status_code == 200
    assert r.json() == {"result": "proof_of_abc"}

def test_vdf_custom_delay(monkeypatch):
    # тормозилку sleep тесты могут пробросить сюда как функцию
    monkeypatch.setattr(vdf_module, "time", lambda s: None)
    r = client.get("/vdf/eval", params={"input_data": "xyz", "delay": 2})
    assert r.status_code == 200
    assert r.json() == {"result": "proof_of_xyz"}

def test_vdf_missing_input():
    r = client.get("/vdf/eval", params={"input_data": ""})
    assert r.status_code == 400
    assert r.json()["detail"] == "input_data required"
