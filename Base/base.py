from os import makedirs
from os.path import join, abspath, dirname, exists
from time import strftime, time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import config_log, config_screen
from Common.log import delete_old_folders


class Base:
    def __init__(self, driver):
        self.driver = driver
        # self.driver.set_page_load_timeout(10)

    def base_find_element(self, locator, timeout=10, poll=0.5):
        """
        定位元素，0.5秒一次，10秒超时。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param timeout: 超时时间，可选参数，默认10秒。
        :param poll: 每隔poll秒定位一次，可选参数，默认为0.5。
        :return: element
        """
        return WebDriverWait(
            self.driver, timeout=timeout, poll_frequency=poll
        ).until(lambda dr: dr.find_element(*locator))

    def base_click(self, locator, js: bool=True):
        """
        模拟js进行点击操作，可以触发浮窗类内容。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param js: 若为 True，则使用 js 模拟鼠标点击操作，否则使用 Selenium 原生方法操作
        """
        element = self.base_find_element(locator)
        if js:
            ActionChains(self.driver).move_to_element(
                element).click(element).perform()
        else:
            element.click()

    def base_input(self, locator, value: str, clear: bool=True, js: bool=True):
        """
        在元素中输入内容。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param value: 要输入的内容。
        :param clear: 输入前是否要清空输入框
        :param js: 若为 True，则使用 js 模拟鼠标键盘操作，否则使用 Selenium 原生方法操作
        """
        element = self.base_find_element(locator)
        if clear:
            element.clear()
        if js:
            ActionChains(self.driver).move_to_element(
                element).click(element).send_keys(value).perform()
        else:
            element.send_keys(value)

    def base_drag(self, locator, distance: tuple):
        """
        使用 js 模拟拖拽操作。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param distance: 要拖拽的距离，横向距离和纵向距离。
        """
        element = self.base_find_element(locator)
        ActionChains(self.driver).move_to_element(
            element).click_and_hold(element).perform()
        ActionChains(self.driver).move_by_offset(*distance).perform()
        ActionChains(self.driver).release().perform()

    def base_get_text(self, locator) -> str:
        """
        获得元素的文本，即标签语言中间夹着的内容。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        return self.base_find_element(locator).text.strip()

    def base_get_attribute(self, locator, attribute: str) -> str:
        """
        功能存疑，可能包含base_get_text方法功能。
        获得元素的title属性。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        :param attribute: 需要获得的属性名。
        """
        element = self.base_find_element(locator)
        return element.get_attribute(attribute).strip()

    def base_save_full_screenshot(self, folder: str, name: str):
        """
        浏览器窗口内全屏截图并保存。
        :param folder: 保存截图文件的目录。
        :param name: 保存截图文件的文件名，.png格式。
        """
        home = abspath(dirname(dirname(__file__)))
        today = strftime("%Y%m%d")
        screen_path = join(home, config_log["folder"],
                           config_screen["folder"], today, folder)
        if not exists(screen_path):
            makedirs(screen_path)
            delete_old_folders()
        name = join(screen_path, name)
        if not name.endswith(".png"):
            name = name + str(round(time() * 1000)) + ".png"
        else:
            name = name[:-4] + str(round(time() * 1000)) + ".png"
        self.driver.save_screenshot(name)

    def base_exists_element(self, locator) -> bool:
        """
        元素是否存在。使用find_elements定位元素，长度为0则认为元素不存在。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        elements = self.driver.find_elements(*locator)
        if len(elements):
            return True
        else:
            return False

    def base_get_element_count(self, locator) -> int:
        """
        获得指定locator的元素的个数。
        :param locator: eg. (By.CSS_SELECTOR, "#username").
        """
        return len(self.driver.find_elements(*locator))
