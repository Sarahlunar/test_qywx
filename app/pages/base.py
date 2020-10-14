from appium.webdriver.webdriver import WebDriver


class Base:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver
