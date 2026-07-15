
from api.user_api import UserApi


def test_me(token):

    r = UserApi.me(token)

    assert r.status_code == 200

    assert r.json()["username"] == "tom112"