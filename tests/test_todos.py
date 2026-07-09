import pytest
from httpx import AsyncClient, ASGITransport
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

#
# @pytest.mark.asyncio
# async def test_create_todo():
#
#     async with AsyncClient(
#         transport=ASGITransport(app=app),
#         base_url="http://test"
#     ) as client:
#
#
#         login = await client.post(
#             "/users/login",
#             data={
#                 "username": "ft@gmail.com",
#                 "password": "string"
#             }
#         )
#
#
#         token = login.json()["access_token"]
#
#
#         response = await client.post(
#             "/todos/",
#             headers={
#                 "Authorization": f"Bearer {token}"
#             },
#             json={
#                 "title": "Testing",
#                 "completed": False
#             }
#         )
#
#
#         assert response.status_code == 201
#


@pytest.mark.asyncio
async def test_get_todos():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        login = await client.post(
            "/users/login",
            data={
                "username": "ft@gmail.com",
                "password": "string"
            }
        )

        token = login.json()["access_token"]

        response = await client.get(
            "/todos/",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        assert response.status_code == 200
        assert isinstance(response.json(), list)