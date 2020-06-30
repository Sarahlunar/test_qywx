from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    _driver = None
    def __init__(self, driver: WebDriver = None):
        if not self._driver:
            self._driver = webdriver.Chrome()
            self._driver.get("https://work.weixin.qq.com/")
            self._driver.implicitly_wait(3)
    # 封装find函数
    def find(self, locater, content: str = None):
        if isinstance(locater, tuple):
            el = self._driver.find_element(*locater)
        else:
            el = self._driver.find_element(locater, content)
        return el