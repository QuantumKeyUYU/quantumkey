from fastapi.testclient import TestClient
from app.main import app
import app.vdf as vdf

client = TestClient(app)

def test_vdf_default_delay():
    r = client.get("/vdf/eval", params={"input_data":"abc"})
    assert r.status_code == 200
    assert r.json()["result"] == "proof_of_abc"

def test_vdf_custom_delay(monkeypatch):
    # подменяем asyncio.sleep, чтобы тест шёл мгновенно
    monkeypatch.setattr(vdf, "asyncio", type("X",(object,),{"sleep": lambda _,__: None}))
    r = client.get("/vdf/eval", params={"input_data":"xyz","delay":1})
    assert r.status_code == 200
    assert r.json()["result"] == "proof_of_xyz"
