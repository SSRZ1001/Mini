import app, utils, pytest,logging
from Api.apiFactory import ApiFactory


@pytest.mark.run(order=0)
class TestUserApi:
    def test_get_token(self):
        """获取 token"""
        # 响应对象
        res = ApiFactory.user_api().get_token_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言 token存在
        assert len(res.json().get("token")) > 0
        # 保存 token 到 app配置文件
        app.headers["token"] = res.json().get("token")
        # print("app.headers:{}".format(app.headers))

    def test_verify_api(self):
        """验证token"""
        # 响应对象
        res = ApiFactory.user_api().get_verify_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言有效
        assert res.json().get("isValid") is True

    def test_user_address(self):
        res = ApiFactory.user_api().get_address_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert False not in [i in res.text for i in ["SSR", "16666666666", "上海市", "浦东新区"]]
