from appium.webdriver.common.mobileby import MobileBy

from app.pages.base import Base


class ContactAdd(Base):
    def contact_add(self, name, sex, mobile):
        from app.pages.address_book.member_invite_menu import MemberInvitemenu

        # 成员姓名
        self.find(MobileBy.XPATH,
                                  f'//*[contains(@text, "姓名")]/..//*[@class="android.widget.EditText"]').send_keys(name)
        # 成员性别
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[@class="android.widget.ImageView"]').click()
        # 添加多个用户时, 会出现选择不到性别的情况, 添加显示等待
        self.wait((MobileBy.XPATH, f'//*[@text="{sex}"]'))
        self.find(MobileBy.XPATH, f'//*[@text="{sex}"]').click()
        # 成员手机号
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/eqx"]').send_keys(mobile)
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gvk"]').click()
        return MemberInvitemenu(self._driver)
