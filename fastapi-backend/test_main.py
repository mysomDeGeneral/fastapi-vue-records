from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_create_record():
    response = client.post(
        "/records",
        headers={"X-Token": "coneofsilence"},
        json={
            "first_name": "nster",
            "last_name": "kofi",
            "phone": "054524989",
            "city": "sokpoe",
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": response.json()["id"],
        "first_name": "nster",
        "last_name": "kofi",
        "phone": "054524989",
        "city": "sokpoe"
    } 


def test_get_existing_record():
    response = client.get("/records/2", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": response.json()["id"],
        "first_name": "john",
        "last_name": "doe",
        "phone": "545148108",
        "city": "sokpoe"
    }


def test_get_nonexistent_record():
    response = client.get("/records/99", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Record not found!"}


def test_update_existing_record():
    response = client.put(
        "/records/5", 
        headers={"X-Token": "coneofsilence"},
        json={
            "city": "awusakpoe"
        }
        )
    assert response.status_code == 200
    assert response.json() == {
        "id": response.json()["id"],
        "first_name": "mysom",
        "last_name": "kofi",
        "phone": "054524989",
        "city": "awusakpoe"
    }


def test_update_nonexistent_record():
    response = client.put(
        "/records/99", 
        headers={"X-Token": "coneofsilence"},
        json={
            "city": "awusakpoe"
        }
        )   
    assert response.status_code == 404
    assert response.json() == {"detail": "Record not found!"} 


def test_delete_existing_record():
    response = client.delete("/records/6", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {"message": "Record deleted successfully"}


def test_delete_nonexistent_record():
    response = client.delete("/records/6", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Record not found!"}


