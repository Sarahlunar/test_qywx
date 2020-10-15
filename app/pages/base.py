from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class Base:
    _black_list = [(MobileBy.XPATH, '//*[@text="确定"]'),
                   (MobileBy.XPATH, '//*[@text="下次再说"]'),
                   (MobileBy.XPATH, '//*[@text="好的"]')
    ]
    _max_try = 3
    _cur_try = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value:str = None):
        try:
            if isinstance(locator, tuple):
                el = self._driver.find_element(*locator)
            else:
                el = self._driver.find_element(locator, value)
            # 找到之后, _cur_try归0, 隐士等待时间恢复5
            self._cur_try = 0
            self._driver.implicitly_wait(1)
            return el
        except Exception as e:
            # 出现异常,隐士等待时间修改为1
            self._driver.implicitly_wait(1)
            # 如果重试次数超出了最大次数, 抛出异常
            if self._cur_try > self._max_try:
                raise e
            self._cur_try += 1
            # 判断黑名单
            for b in self._black_list:
                els = self._driver.find_elements(*b)
                # 如果存在弹窗, 点击并重新执行find方法
                if len(els) > 0:
                    els[0].click()
                    return self.find(locator, value)
            raise e


