import allure
import pytest
from common.logger import logger
from api.user_api import UserApi
from common.mysql_util import query


@allure.title("用户注册")
@pytest.mark.parametrize(
    "username,password",
    [
        ("tom112", "111222"),
        ("abc", "123456"),
        ("addin", "111111"),
    ]
)
def test_register(username, password):

    with allure.step("调用注册接口"):
        logger.info("开始注册用户")
        r = UserApi.register(username, password)

        # 添加请求参数
        allure.attach(
            f"username={username}\npassword={password}",
            name="请求参数",
            attachment_type=allure.attachment_type.TEXT
        )

        # 添加响应结果
        allure.attach(
            r.text,
            name="接口响应",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("检查状态码"):
        assert r.status_code == 200

    with allure.step("数据库断言"):
        users = query(
            f"SELECT * FROM users WHERE username='{username}'"
        )

        allure.attach(
            str(users),
            name="数据库查询结果",
            attachment_type=allure.attachment_type.TEXT
        )

        assert len(users) == 1
