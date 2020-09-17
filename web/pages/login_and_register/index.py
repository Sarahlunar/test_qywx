from selenium.webdriver.common.by import By

from web.pages.base import Base
from web.pages.login_and_register.login import Login
from web.pages.login_and_register.resgister import Register


class Index(Base):
    _base_url = "https://work.weixin.qq.com/"

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)
