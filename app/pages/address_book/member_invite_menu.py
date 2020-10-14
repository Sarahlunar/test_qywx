from appium.webdriver.common.mobileby import MobileBy

from app.pages.base import Base


class MemberInvitemenu(Base):
    def goto_contact_add(self):
        from app.pages.address_book.contact_add import ContactAdd
        self._driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/cjv"]').click()
        return ContactAdd(self._driver)