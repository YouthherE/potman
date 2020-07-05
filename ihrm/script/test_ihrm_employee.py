# 导包
import unittest, logging
from ihrm import app
from ihrm.api.login_api import LoginApi
from ihrm.api.employee import EmployeeApi


# 创建测试类
from ihrm.utils import assert_common


class TestIHRMEmployee(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化员工
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        # 打印登录接口
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))

    def test02_add_emp(self):
        logging.info("app.HEADERS的值是：{}".format(app.HEADERS))
        # 发送添加员工的接口请求
        response = self.emp_api.add_emp("祖冲鸟", "13986150828", app.HEADERS)
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)
        # 打印添加员工的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        # 提取员工中的令牌并把员工令牌保存到全局变量中
        app.EMP_ID = response.json().get("data").get("id")
        # 打印保存的员工ID
        logging.info("保存到全局变量的员工的ID为：{}".format(app.EMP_ID))

    def test03_query_emp(self):
        # 发送查询员工的接口请求:
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)
        # 打印查询员工的数据
        logging.info("查询员工的结果为：{}".format(response.json()))

    def test04_modify_emp(self):
        # 发送修改员工的接口请求
        response = self.emp_api.modify_emp(app.EMP_ID, {'tom': '杨辉'},app.HEADERS)
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)
        # 打印修改员工的结果
        logging.info("查询修改员工的结果为：{}".format(response.json()))

    def test05_delete_emp(self):
        # 发送修改员工的接口请求
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)
        # 打印修改的结果
        logging.info("查询修改的结果为：{}".format(response.json()))
