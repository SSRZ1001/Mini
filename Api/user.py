import logging

import app, requests


class UserApi:
    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + "/token/user"
        # token验证码
        self.get_verify_url = app.base_url + "/token/verify"
        # 用户地址信息
        self.get_addr_url = app.base_url + "/address"

    def get_token_api(self):
        """获取token"""
        logging.info("用户-获取token")
        # 请求体
        data = {"code": app.code}
        logging.info("请求参数：{}".format(data))
        # 返回请求数据
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def get_verify_api(self):
        logging.info("用户-验证token")
        data = {"token": app.headers.get("token")}
        logging.info("请求参数：{}".format(data))
        return requests.post(self.get_verify_url, json=data, headers=app.headers)

    def get_address_api(self):
        logging.info("用户-获取地址")
        return requests.get(self.get_addr_url, headers=app.headers)
