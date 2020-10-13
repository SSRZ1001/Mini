import utils,logging
from Api.apiFactory import ApiFactory


class TestProductApi:
    def test_product_classify(self):
        res = ApiFactory.product_api().product_classify_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)
        assert len(res.json()) > 0
        assert "果味" in res.text

    def test_classify_product(self):
        res = ApiFactory.product_api().classify_product_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)

        assert len(res.json()) > 0
        assert False not in [i in res.text for i in ["name", "main_img_url", "price", "img_id"]]

    def test_product_detail(self):
        res = ApiFactory.product_api().product_detail_api()
        logging.info("请求地址：{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)

        assert res.json().get("id") == 2
        assert res.json().get("price") == "0.01"
        assert False not in [i in res.text for i in ["id", "name", "price", "stock"]]
