from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sayhello():
    response = client.get("/hello/abdul")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello abdul"}

def test_rolldice():
    response = client.get('/rolldice')
    res_j = response.json()
    dice_val = int(res_j['dice_val'])
    if 0 <= dice_val <= 6:
        val_correct = True
    else:
        val_correct = False

    assert response.status_code == 200
    assert val_correct == True
