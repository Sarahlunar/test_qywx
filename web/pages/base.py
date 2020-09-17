from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if not self._driver:
            # 浏览器复用
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options = options)
            self._driver.get(self._base_url)
            self._driver.implicitly_wait(3)

    # 封装find函数
    def find(self, locater, content: str = None):
        if isinstance(locater, tuple):
            el = self._driver.find_element(*locater)
        else:
            el = self._driver.find_element(locater, content)
        return el

    # 封装finds函数
    def finds(self, locater, content: str = None):
        if isinstance(locater, tuple):
            el = self._driver.find_elements(*locater)
        else:
            el = self._driver.find_elements(locater, content)
        return el
