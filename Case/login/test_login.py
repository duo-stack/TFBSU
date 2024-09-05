import unittest
from logging import getLogger
from sys import _getframe

# from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys

# from Base.get_driver import GetDriver
from Case import LOGIN
from Config.config import config_log
# from Flow.login.flow_login import FlowLogin


"""
没有目标页面，相关代码进行注释。
"""


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log_module = ".login"  # 日志模块名称
        cls.logger = getLogger(config_log["module"] + log_module)
        # cls.login = FlowLogin(GetDriver().get_driver())

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     GetDriver().quit_driver()

    @unittest.skip("跳过")
    def test_username_empty(self):
        """测试用户名为空。"""
        print(_getframe().f_code.co_name)
        result = True
        
        # 直接清空用户名，没有模拟键盘操作，不会触发change事件改变数据层的数据，
        # 依然可以触发验证图，因此需要模拟键盘退格键逐个删除内容。
        username = LOGIN["username"]
        password = LOGIN["password"]
        self.login.page_input_username(username)
        for _ in range(len(username)):
            self.login.page_input_username(Keys.BACKSPACE, clear=False)
        self.login.page_input_password(password)
        self.login.page_click_login()

        # 判断用户名输入框下方消息
        if self.login.page_exists_username_message():
            desired_message = LOGIN["username_empty_message"]
            message = self.login.page_get_username_message()
            if desired_message != message:
                self.logger.error(
                    f"用户名为：空，密码为：{password}，用户名输入框下方消息错误，"
                    f"期望消息为：{desired_message}，"
                    f"实际消息为：{message}。"
                )
                self.login.page_save_full_screenshot(
                    f"{_getframe().f_code.co_name}_{_getframe().f_lineno}.png"
                )
                result = False
        else:
            # 未找到消息元素，说明未显示
            self.logger.error(
                f"用户名为：空，密码为：{password}，用户名输入框下方未出现消息。"
            )
            self.login.page_save_full_screenshot(
                f"{_getframe().f_code.co_name}_{_getframe().f_lineno}.png"
            )
            result = False
        
        # 判断密码输入框下方消息
        if self.login.page_exists_password_message():
            self.logger.error(
                f"用户名为：空，密码为：{password}，密码输入框下方出现消息。"
            )
            self.login.page_save_full_screenshot(
                f"{_getframe().f_code.co_name}_{_getframe().f_lineno}.png"
            )
            result = False
        
        self.assertTrue(result)

    @unittest.skip("跳过")
    def test_password_empty(self):
        """测试密码为空。"""
        print(_getframe().f_code.co_name)
        result = True

        # 直接清空密码，没有模拟键盘操作，不会触发change事件改变数据层的数据，
        # 依然可以触发验证图，因此需要模拟键盘退格键逐个删除内容。
        username = LOGIN["username"]
        password = LOGIN["password"]
        self.login.page_input_username(username)
        self.login.page_input_password(password)
        for _ in range(len(password)):
            self.login.page_input_password(Keys.BACKSPACE, clear=False)
        self.login.page_click_login()

        # 判断用户名输入框下方消息
        if self.login.page_exists_username_message():
            self.logger.error(
                f"用户名为：{username}，密码为：空，用户名输入框下方出现消息。"
            )
            self.login.page_save_full_screenshot(
                f"{_getframe().f_code.co_name}_{_getframe().f_lineno}.png"
            )
            result = False

        # 判断密码输入框下方消息
        if self.login.page_exists_password_message():
            desired_message = LOGIN["password_empty_message"]
            message = self.login.page_get_password_message()
            if desired_message != message:
                self.logger.error(
                    f"用户名为：{username}，密码为：空，密码输入框下方消息错误，"
                    f"期望消息为：{desired_message}，"
                    f"实际消息为：{message}。"
                )
                self.login.page_save_full_screenshot(
                    f"{_getframe().f_code.co_name}_{_getframe().f_lineno}.png"
                )
                result = False
        else:
            # 未找到输入框下方消息元素，说明未显示
            self.logger.error(
                f"用户名为：{username}，密码为：空，密码输入框下方未出现消息。"
            )
            self.login.page_save_full_screenshot(
                f"{_getframe().f_code.co_name}_{_getframe().f_lineno}.png"
            )
            result = False

        self.assertTrue(result)
    
    def test_verify_code_empty(self):
        """测试验证码为空。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_all_empty(self):
        """测试全部输入框为空。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_username_not_exist(self):
        """测试用户名符合规则但不存在。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_username_not_rule(self):
        """测试用户名不符合规则，包含大写字母、符号等。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_username_short(self):
        """测试用户名不符合规则（太短）。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_password_short(self):
        """测试密码不符合规则（太短）。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_password_error(self):
        """测试密码错误。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_eye(self):
        """测试密码隐藏/显示功能。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_verify_code_error(self):
        """测试验证码错误。"""
        print(_getframe().f_code.co_name)
        result = True
        
        self.assertTrue(result)
    
    def test_login_success(self):
        """测试登录、登出。"""
        print(_getframe().f_code.co_name)
        result = False  # 刻意为之
        
        self.assertTrue(result)

# if __name__ == '__main__':
#     unittest.main()
