from Api.apiFactory import ApiFactory

# 调用轮播图api
# print("轮播图：{}".format(ApiFactory.get_home_api().banner_api().json()))
# 调用专题栏
# print("专题栏：{}".format(ApiFactory.get_home_api().theme_api().json()))
# 调用最近新品
# print("最近新品：{}".format(ApiFactory.get_home_api().recent_product_api().json()))
# 调用商品分类
# print("商品分类：{}".format(ApiFactory.product_api().product_classify_api().json()))
# 调用分类下商品
# print("分类下商品：{}".format(ApiFactory.product_api().classify_product_api().json()))
# 调用获取商品信息
# print("商品信息：{}".format(ApiFactory.product_api().product_detail_api().json()))
# 调用获取用户token
print("返回值：{}".format(ApiFactory.user_api().get_token_api().json()))
# 调用验证token
# print("返回值：{}".format(ApiFactory.user_api().get_verify_api().json()))
# 查看订单
# print("查看订单：{}".format(ApiFactory.order_api().order_list_api().json()))
# # 创建订单
# print("创建订单：{}".format(ApiFactory.order_api().create_order_api(12, 7).json()))
# # 查看订单详情
# print("订单详情：{}".format(ApiFactory.order_api().query_order_api(100).json))
