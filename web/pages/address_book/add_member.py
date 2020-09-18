from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.pages.base import Base


class AddMember(Base):
    def __init__(self, driver: WebDriver = None):
        super(AddMember, self).__init__()
        # 页面添加显示等待
        self.wait_to_click((By.CSS_SELECTOR, '.js_btn_save'))

    def add_member_save(self):
        # self.wait_to_click((By.CSS_SELECTOR, '#username'))
        self.find(By.CSS_SELECTOR, '#username').send_keys("sarah")
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys("sarah")
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys("11112222333")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        from web.pages.address_book.index import AddressBook
        return AddressBook(self._driver)
