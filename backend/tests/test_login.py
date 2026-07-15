import pytest

from api.user_api import UserApi


@pytest.mark.parametrize(
    "username,password",
    [
        ("tom112", "111222"),
        ("abc", "123456"),
        ("admin", "111111"),
        ("jack", "123456"),
        ("rose", "123456"),
        ("mike", "111222"),
        ("lily", "password123"),
    ]
)
def test_login(username, password):

    r = UserApi.login(
        username,
        password
    )

    print(r.status_code)