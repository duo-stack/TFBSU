from time import sleep

from Page.login.page_login import PageLogin


class FlowLogin(PageLogin):
    def flow_login(self, username: str, password: str, verify_code: str=None):
        """
        执行完整的登录操作。
        :param username: 用户名。
        :param password: 密码。
        :param verify_code: 验证码，默认为None，如果为None，则自动识别验证码。
        """
        self.page_click_verify_image()
        sleep(1)
        self.page_input_username(username)
        self.page_input_password(password)
        if verify_code is None:
            verify_code = self.page_ocr_verify_code()
            while len(verify_code) != 4:
                self.page_click_verify_image()
                sleep(1)
                verify_code = self.page_ocr_verify_code()
        self.page_input_verify_code(verify_code)
        self.page_click_login()
