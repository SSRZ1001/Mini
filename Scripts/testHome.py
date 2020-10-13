import utils, logging
from Api.apiFactory import ApiFactory


class TestHomeApi:
    def test_home_api(self):
        res = ApiFactory.get_home_api().banner_api()
        # 打印请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)

        # 断言id=1 name=首页置顶
        assert res.json().get("id") == 1 and res.json().get("name") == "首页置顶"
        # 断言返回结果大于0
        assert len(res.json().get("items")) > 0

    def test_theme_api(self):
        res = ApiFactory.get_home_api().theme_api()
        # 打印请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)

        # 断言id=1,2,3
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        # 断言返回结果中包含name，description，topic_img，head_img
        assert False not in [i in res.text for i in ["name", "description", "topic_img", "head_img"]]

    def test_recent_product(self):
        res = ApiFactory.get_home_api().recent_product_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)

        # 断言返回结果大于0
        assert len(res.json()) > 0
        # 断言id，name，price在返回结果中
        assert "id" in res.text and "name" in res.text and "price" in res.text
