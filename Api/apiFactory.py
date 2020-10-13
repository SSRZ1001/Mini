from Api.home import HomeApi
from Api.product import ProductApi
from Api.user import UserApi
from Api.order import OrderApi


class ApiFactory:
    @classmethod
    def get_home_api(cls):
        """返回首页API"""
        return HomeApi()

    @classmethod
    def product_api(cls):
        """返回商品分类API"""
        return ProductApi()

    @classmethod
    def user_api(cls):
        """返回用户API"""
        return UserApi()

    @classmethod
    def order_api(cls):
        return OrderApi()
