# quantumkey-api/tests/test_vdf.py
import pytest
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_vdf_default_delay_and_result():
    # без указания delay используется DEFAULT_DELAY=1
    r = client.get("/vdf/eval", params={"input_data": "abc"})
    assert r.status_code == 200
    data = r.json()
    assert "result" in data
    assert data["result"] == "proof_of_abc"

def test_vdf_custom_delay(monkeypatch):
    # ускоряем задержку, monkeypatch-им функцию time
    import app.vdf as vdf_mod

    called = []
    def fake_time(sec, *args, **kwargs):
        called.append(sec)

    monkeypatch.setattr(vdf_mod, "time", fake_time)
    r = client.get("/vdf/eval", params={"input_data": "xyz", "delay": "2"})
    assert r.status_code == 200
    assert called == [2]  # гарантируем, что наш fake_time получили правильный аргумент
    assert r.json()["result"] == "proof_of_xyz"

def test_vdf_missing_input_data():
    # если input_data пусто, возвращаем 400
    r = client.get("/vdf/eval", params={"input_data": ""})
    assert r.status_code == 400
