from appium.webdriver.common.mobileby import MobileBy

from app.pages.address_book.address_book import AddressBook
from app.pages.base import Base
from app.pages.message.message import Message
from app.pages.profile.profile import Profile
from app.pages.work_bench.work_bench import WorkBench


class Home(Base):
    def goto_message(self):
        return Message()

    def goto_address_book(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/drb" and @text="通讯录"]').click()
        return AddressBook(self._driver)

    def goto_work_bench(self):
        return WorkBench()

    def goto_profile(self):
        return Profile()
