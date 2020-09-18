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
    def delete_member_page(self):
        pass

    # 通过查找删除成员
    def delete_member_search(self):
        pass
