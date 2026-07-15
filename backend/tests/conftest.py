import pytest

from api.user_api import UserApi

import pytest

from api.user_api import UserApi



@pytest.fixture(scope="session", autouse=True)
def create_test_user():

    UserApi.register(
        "tom112",
        "111222"
    )


@pytest.fixture(scope="session")
def token():

    r = UserApi.login(
        "tom112",
        "111222"
    )

    return r.json()["access_token"]