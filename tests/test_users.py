from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "TODO API is running"
    }

# # def test_register():
# #
# #     response = client.post(
# #         "/users/register",
# #         json={
# #             "username": "testuser",
# #             "email": "test@test.com",
# #             "password": "123456"
# #         }
# #     )
# #
# #     assert response.status_code == 201
#
#
# def test_login():
#
#     response = client.post(
#         "/users/login",
#         data={
#             "username": "test@test.com",
#             "password": "123456"
#         }
#     )
#
#     assert response.status_code == 200
#
#     body = response.json()
#
#     assert "access_token" in body
#
#     assert body["token_type"] == "bearer"
#
#
