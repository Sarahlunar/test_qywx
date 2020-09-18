from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if self._driver is None:
            # 浏览器复用
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

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

    # 显示等待
    def wait_to_click(self, locater):
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locater))
