# quantumkey-api/tests/test_threshold.py
from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_threshold_split_and_recover():
    # разделяем секрет "s3cr3t" на 5 частей, порог 3
    r1 = client.post("/threshold/split", json={
        "secret": "s3cr3t",
        "n": 5,
        "k": 3
    })
    assert r1.status_code == 200
    shares = r1.json()["shares"]
    assert isinstance(shares, list)
    assert len(shares) == 5
    # каждый шар равен исходному секрету (по заглушке)
    assert all(s == "s3cr3t" for s in shares)

    # восстанавливаем секрет из первых трёх шаров
    r2 = client.post("/threshold/recover", json={
        "shares": shares[:3]
    })
    assert r2.status_code == 200
    assert r2.json()["secret"] == "s3cr3t"
