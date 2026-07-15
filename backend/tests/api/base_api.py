import requests
import time

from common.config import BASE_URL
from common.logger import logger


class BaseApi:

    @staticmethod
    def get(url, headers=None):

        logger.info(f"GET {BASE_URL + url}")

        start = time.time()

        response = requests.get(
            BASE_URL + url,
            headers=headers
        )

        cost = round(time.time() - start, 3)

        logger.info(f"状态码：{response.status_code}")
        logger.info(f"耗时：{cost}s")
        logger.info(f"响应：{response.text}")

        return response

    @staticmethod
    def post(url, json=None, headers=None):

        logger.info(f"POST {BASE_URL + url}")

        if json:
            logger.info(f"请求参数：{json}")

        start = time.time()

        response = requests.post(
            BASE_URL + url,
            json=json,
            headers=headers
        )

        cost = round(time.time() - start, 3)

        logger.info(f"状态码：{response.status_code}")
        logger.info(f"耗时：{cost}s")
        logger.info(f"响应：{response.text}")

        return response