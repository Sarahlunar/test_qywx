from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.pages.wrapper import handle_black


class Base:

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value: str = None):
        if isinstance(locator, tuple):
            el = self._driver.find_element(*locator)
        else:
            el = self._driver.find_element(locator, value)
            # 找到之后, _cur_try归0, 隐士等待时间恢复5
        return el

    @handle_black
    def finds(self, locator, value: str = None):
        els: list
        if isinstance(locator, tuple):
            els = self._driver.find_elements(*locator)
        else:
            els = self._driver.find_elements(locator, value)
        # 找到之后, _cur_try归0, 隐士等待时间恢复5
        return els

    def wait(self, locator, value="click"):
        if value == "visable":
            WebDriverWait(self._driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        elif value == "selected":
            WebDriverWait(self._driver, 5).until(expected_conditions.element_selection_state_to_be(locator))
        else:
            WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable(locator))


