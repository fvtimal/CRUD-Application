from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app


client = TestClient(app)


# def test_home():
#
#     response = client.get("/")
#
#     assert response.status_code == 200
#
#     assert response.json() == {
#         "message": "TODO API is running"
#     }


def test_register():

    response = client.post(
        "/users/register",
        json={
            "username": "testuser",
            "email": "testuser@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 201

    assert response.json() == {
        "message": "User Registered Successfully"
    }
