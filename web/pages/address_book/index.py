from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.pages.base import Base


class AddressBook(Base):
    def __init__(self, driver: WebDriver = None):
        super(AddressBook, self).__init__()
        # 页面添加显示等待
        self.wait_to_click((By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member'))

    # 添加成员
    def goto_add_member(self):
        self.find((By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member')).click()
        from web.pages.address_book.add_member import AddMember
        return AddMember(self._driver)

    # 通过搜索框查找成员
    def get_member_search(self, phone):
        self.find(By.CSS_SELECTOR, '#memberSearchInput').send_keys(phone)
        els = self.finds(By.CSS_SELECTOR, '#search_member_list, .ww_searchResult_title_peopleDepartment')
        if len(els) > 0:
            return True
        else:
            return False

    # 通过翻页查找成员
    def get_member_page(self, phone):
        pages: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        cur, totle = [int(n) for n in pages.split('/')]

        while cur <= totle:
            numbers = self.finds(By.CSS_SELECTOR, "#member_list>tr>td:nth-child(5)")
            nums = [n.get_attribute('title') for n in numbers]
            if phone in nums:
                return True
            self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
            cur += 1
        return False

    # 通过页面删除成员
    def delete_member_page(self, phone):
        pages: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        cur, totle = [int(n) for n in pages.split('/')]

        while cur <= totle:
            numbers = self.finds(By.CSS_SELECTOR, "#member_list>tr>td:nth-child(5)")
            nums = [n.get_attribute('title') for n in numbers]
            msg = ""
            if phone in nums:
                self.find(By.XPATH, f'//*[@title="{phone}"]/../td[1]').click()
                self.find(By.CSS_SELECTOR, '.js_delete').click()
                self.find(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue"]').click()
                msg = "删除成功"
                code = 1
                return msg, code
            self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
            cur += 1
        msg = "客户不存在"
        code = 0
        return msg, code

    # 通过查找删除成员
    def delete_member_search(self, phone):
        self.find(By.CSS_SELECTOR, '#memberSearchInput').send_keys(phone)
        els = self.finds(By.CSS_SELECTOR, '#search_member_list, .ww_searchResult_title_peopleDepartment')
        if len(els) > 0:
            self.find(By.CSS_SELECTOR, '#search_member_list, .ww_searchResult_title_peopleDepartment').click()
            self.find(By.CSS_SELECTOR, '.js_del_member').click()
            self.find(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue"]').click()
            msg = "删除成功"
            code = 1
            return msg, code
        else:
            msg = "客户不存在"
            code = 0
            return msg, code
