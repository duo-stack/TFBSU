from os import remove

import ddddocr

import Page.login as pl
from Base.base import Base


class PageLogin(Base):
    def page_input_username(self, username: str,
                            clear: bool=True, js: bool=True):
        """
        输入用户名。
        :param username: 用户名。
        :param clear: 输入前是否要清空输入框
        :param js: 若为 True，则使用 js 模拟鼠标键盘操作，否则使用 Selenium 原生方法操作
        """
        self.base_input(pl.username, username, clear, js)

    def page_get_username_message(self) -> str:
        """
        获得用户名输入框下面的错误提示。
        :return: 错误提示
        """
        return self.base_get_text(pl.username_message)

    def page_exists_username_message(self) -> bool:
        """获得用户名输入框下面的消息元素是否存在。"""
        return self.base_exists_element(pl.username_message)

    def page_input_password(self, password: str,
                            clear: bool=True, js: bool=True):
        """
        输入密码。
        :param password: 密码。
        :param clear: 输入前是否要清空输入框
        :param js: 若为 True，则使用 js 模拟鼠标键盘操作，否则使用 Selenium 原生方法操作
        """
        self.base_input(pl.password, password, clear, js)

    def page_get_password_message(self) -> str:
        """
        获得密码输入框下面的错误提示。
        :return: 错误提示
        """
        return self.base_get_text(pl.password_message)

    def page_exists_password_message(self) -> bool:
        """获得密码输入框下面的消息元素是否存在。"""
        return self.base_exists_element(pl.password_message)

    def page_ocr_verify_code(self) -> str:
        """
        识别验证图，并返回验证码。仅适用于图片中识别字符的验证码。
        :return: 验证码。
        """
        # 存储验证码图片
        verify_code = self.base_find_element(pl.verify_image)
        verify_code.screenshot(pl.verify_image_path)
        
        # 实例化 OCR，并传参不显示广告
        ocr = ddddocr.DdddOcr(show_ad=False)
        
        # 读取验证码图片，识别验证码
        with open(pl.verify_image_path, "rb") as f:
            verify_code = f.read()
        verify_code = ocr.classification(verify_code)
        
        # 删除验证码图片
        remove(pl.verify_image_path)
        
        return verify_code

    def page_input_verify_code(self, verify_code: str):
        """
        输入验证码。
        :param verify_code: 验证码。
        """
        self.base_input(pl.verify_code, verify_code)

    def page_click_verify_image(self):
        """点击验证图。"""
        self.base_click(pl.verify_image)

    def page_click_login(self):
        """点击登录按钮。"""
        self.base_click(pl.login)

    def page_save_full_screenshot(self, image_filename):
        """
        保存全屏截图。
        :param image_filename: 截图文件名。
        """
        self.base_save_full_screenshot(pl.image_path, image_filename)
