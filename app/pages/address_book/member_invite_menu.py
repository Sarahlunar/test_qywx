from appium.webdriver.common.mobileby import MobileBy

from app.pages.base import Base


class MemberInvitemenu(Base):
    def goto_contact_add(self):
        from app.pages.address_book.contact_add import ContactAdd
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/cjv"]').click()
        return ContactAdd(self._driver)

    def get_toast(self):
        # 添加成员成功会有toast,获取toast做断言
        return self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
