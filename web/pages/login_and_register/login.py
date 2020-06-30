from selenium.webdriver.common.by import By

from web.pages.base import Base
from web.pages.login_and_register.resgister import Register


class Login(Base):
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link")
        return Register(self._driver)