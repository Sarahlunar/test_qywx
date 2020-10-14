from appium.webdriver.common.mobileby import MobileBy

from app.pages.address_book.member_invite_menu import MemberInvitemenu
from app.pages.base import Base


class AddressBook(Base):
    def goto_member_invite_menu(self):
        el = self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                                'scrollable(true).instance(0)).'
                                                                'scrollIntoView(new UiSelector().text("添加成员").instance(0));')
        el.click()
        return MemberInvitemenu(self._driver)
