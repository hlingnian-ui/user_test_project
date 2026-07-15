import requests
from common.logger import logger

from common.config import BASE_URL
from api.base_api import BaseApi


class UserApi(BaseApi):

    @staticmethod
    def register(username, password):
        
        return BaseApi.post(
            "/users/register",
            json={
                "username": username,
                "password": password
            }
        )
        

    @staticmethod
    def login(username, password):
        return BaseApi.post(
            "/users/login",
            json={
                "username": username,
                "password": password
            }
        )

    @staticmethod
    def me(token):
        return BaseApi.get(
            "/users/me",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

