from appium.webdriver.common.mobileby import MobileBy

from app.pages.base import Base


class ContactAdd(Base):
    def contact_add(self):
        from app.pages.address_book.member_invite_menu import MemberInvitemenu

        # 成员姓名
        self.find(MobileBy.XPATH,
                                  '//*[contains(@text, "姓名")]/..//*[@class="android.widget.EditText"]').send_keys("王一")
        # 成员性别
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[@class="android.widget.ImageView"]').click()
        self.find(MobileBy.XPATH, f'//*[@text="女"]').click()
        # 成员手机号
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/eqx"]').send_keys("14700000001")
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gvk"]').click()
        return MemberInvitemenu(self._driver)
