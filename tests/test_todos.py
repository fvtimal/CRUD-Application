#
# from fastapi.testclient import TestClient
# # import sys, os
# # sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from main import app
#
#
# client = TestClient(app)
#
# def test_create_todo():
#
#     login = client.post(
#         "/users/login",
#         data={
#             "username": "test@test.com",
#             "password": "123456"
#         }
#     )
#
#     token = login.json()["access_token"]
#
#     response = client.post(
#         "/todos/",
#         headers={
#             "Authorization": f"Bearer {token}"
#         },
#         json={
#             "title": "Testing",
#             "completed": False
#         }
#     )
#
#     assert response.status_code == 201