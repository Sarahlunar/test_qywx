from appium.webdriver.common.mobileby import MobileBy

from app.pages.address_book.member_invite_menu import MemberInvitemenu
from app.pages.base import Base


class AddressBook(Base):
    def goto_member_invite_menu(self):
        # 滚动查找元素
        # el = self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #
        #                                                         'scrollable(true).instance(0)).'
        #                                                         'scrollIntoView(new UiSelector().text("添加成员").instance(0));')
        # el.click()

        # 通过手势滑动查找
        els = []
        w = self._driver.get_window_size()['width']
        h = self._driver.get_window_size()['height']
        while len(els) <= 0:
            els = self.finds(MobileBy.XPATH, '//*[@text="添加成员"]')
            self._driver.swipe(int(w * 50 / 100), int(h * 80 / 100), int(int(w * 50 / 100)), int(h * 10 / 100))
        els[0].click()
        return MemberInvitemenu(self._driver)
