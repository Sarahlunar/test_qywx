from appium import webdriver

from app.pages.base import Base
from app.pages.home import Home


class App(Base):
    def start(self):
        if self._driver is None:
            des_caps = {
                'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': '127.0.0.1:7555',
                'appPackage': ' com.tencent.wework',
                'appActivity': '.launch.WwMainActivity',
                'unicodeKeyBoard': 'true',
                'resetKeyBoard': 'true',
                'noReset': 'true',
                'skipServerInstallation': 'true',
                'skipDeviceInitialization': 'true'
            }

            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self._driver.quit()

    def goto_home(self):
        return Home(self._driver)
