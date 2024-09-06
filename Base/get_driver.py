from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver

from Config.config import config_info


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        """
        driver不存在则创建一个driver，driver存在则返回现有的driver。
        :return: driver
        """
        if cls.driver is None:
            cls.driver = webdriver.Edge()
            cls.driver.maximize_window()
            cls.driver.get(config_info["url"])
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """销毁现有driver。"""
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None
