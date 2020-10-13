import logging

import utils
from Api.apiFactory import ApiFactory


class TestOrderApi:
    def test_order_list(self):
        res = ApiFactory.order_api().order_list_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert False not in [i in res.text for i in ["current_page", "data"]]

    def test_create_order(self):
        product_id = 12
        count = 7
        res = ApiFactory.order_api().create_order_api(product_id, count)
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
        assert res.json().get("pass") is True
        assert False not in [i in res.text for i in ["order_no", "order_id", "create_time", "pass"]]

    def test_query_order(self):
        order_id = 107
        res = ApiFactory.order_api().query_order_api(order_id)
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        utils.common_assert_code(res)
